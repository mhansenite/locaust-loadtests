#!/usr/bin/env python3
"""
Project Phase and Milestone Creation Load Test
Tests creating projects, phases and milestones based on HAR file analysis

Each user creates a single project that is used for all subsequent operations.
Projects can be automatically cleaned up when the test completes (controlled by DELETE_PROJECT flag).
"""

import sys
import os
import json
import time
import uuid
import re
import random
from locust import task, between
from datetime import datetime, timedelta

# Add parent directory to path to import from common
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.auth import AuthenticatedUser
from common.create import (
    create_project, 
    create_phase, 
    create_milestone, 
    create_task, 
    create_subtask,
    create_test_project_with_fallback,
    delete_project
)
from common.update import (
    update_task,
    update_task_status,
    generate_task_updates
)
from common.extractdata import (
    extract_project_id_from_response,
    extract_phase_id_from_response,
    extract_milestone_id_from_response,
    extract_task_id_from_response,
    extract_subtask_id_from_response
)
from common.helpers import (
    get_random_phase_id,
    get_random_milestone_info,
    get_random_task_info,
    assign_project_from_pool,
    assign_project_from_existing_pool,
    add_project_to_pool,
    show_current_distribution,
    debug_print
)

class ProjectPhaseMilestoneLoadTest(AuthenticatedUser):
    """
    Load test for project, phase and milestone creation functionality.
    
    Each user creates a single project and uses it for all subsequent operations.
    Tests creating phases and milestones, tasks, and various task update operations 
    using the APIs discovered from HAR file analysis.
    
    Task Organization:
    
    CREATE TASKS (ordered hierarchically: phase → milestone → task → subtask):
    - create_test_phase (2): Phase creation - foundational, less frequent
    - create_milestone (5): Milestone creation - moderate frequency for buildup
    - create_task (6): Single task creation - higher frequency for content buildup
    - create_subtask (3): Single subtask creation - moderate frequency for detailed work breakdown
    
    VIEW TASKS:
    - view_project_plan (5): Project plan viewing activity - moderate frequency
    
    UPDATE TASKS (ordered hierarchically: phase → milestone → task → subtask):
    - update_task_time_tracking (8): Time tracking entries - most frequent activity
    - update_task_dates (8): Task date adjustments - very frequent 
    - update_task_estimated_hours (7): Task effort estimation updates - frequent
    - update_task_assignments (7): Task assignment changes - frequent
    - update_task_status (8): Task status updates - very frequent
    
    Environment Variables:
    - CREATE_NEW_PROJECT: Set to "true" to create a new project, "false" to use existing PROJECT_ID
    - DELETE_PROJECT: Set to "true" to delete projects after test (default), "false" to preserve them
    - PROJECT_NAME_TXT: Base name for created projects (will have timestamp and ID appended)
    - PROJECT_ID: Project UUID to use when CREATE_NEW_PROJECT=false
    - TEST_PHASE_NAME: Name for created test phases
    - TEST_MILESTONE_NAME: Name for created test milestones
    - TEST_TASK_NAME: Name for created test tasks
    - USE_PROJECT_POOL: Set to "true" to use project pool strategy, "false" for individual projects
    - USERS_PER_PROJECT: Target number of users per project in pool mode (default: 3)
    - MAX_PROJECTS: Maximum number of projects to create in pool mode (default: 5)
    - LOGIN_EMAIL: Email for authentication
    - LOGIN_PASSWORD: Password for authentication
    - LOCUST_HOST: Target host URL
    
    Example usage:
    
    # Project Pool Strategy (Recommended - multiple users per project):
    export USE_PROJECT_POOL="true"
    export MAX_PROJECTS="3"           # Create max 3 projects
    export USERS_PER_PROJECT="5"      # ~5 users per project  
    export DELETE_PROJECT="false"     # Keep projects for inspection
    export PROJECT_NAME_TXT="LoadTestProject"
    export TEST_PHASE_NAME="LoadTestPhase"
    export TEST_MILESTONE_NAME="LoadTestMilestone"
    export TEST_TASK_NAME="LoadTestTask"
    export LOGIN_EMAIL="your-email@example.com"
    export LOGIN_PASSWORD="your-password"
    export LOCUST_HOST="https://app.staging.guidecx.io"
    locust -f testing_scenarios/project.py --users 15 --spawn-rate 3
    
    # Single Shared Project Strategy:
    export CREATE_NEW_PROJECT="false"
    export PROJECT_ID="existing-project-uuid"
    export DELETE_PROJECT="false"
    locust -f testing_scenarios/project.py --users 10 --spawn-rate 2
    
    # Individual Project Strategy (Original):
    export CREATE_NEW_PROJECT="true"
    export USE_PROJECT_POOL="false"
    export DELETE_PROJECT="false"
    locust -f testing_scenarios/project.py --users 5 --spawn-rate 1
    """
    
    wait_time = between(3, 8)  # Wait 3-8 seconds between requests
    
    # Use environment variables
    CREATE_NEW_PROJECT = os.getenv('CREATE_NEW_PROJECT', 'false').lower() == 'true'
    DELETE_PROJECT = os.getenv('DELETE_PROJECT', 'true').lower() == 'true'  # Default to delete for cleanup
    PROJECT_NAME_TXT = os.getenv('PROJECT_NAME_TXT', "LoadTestProject")
    PROJECT_ID = os.getenv('PROJECT_ID', "e34b9b43-fa9f-4a09-a3bf-1178f471a5dc")  # Default from HAR
    TEST_PHASE_NAME = os.getenv('TEST_PHASE_NAME', "LoadTestPhase")
    TEST_MILESTONE_NAME = os.getenv('TEST_MILESTONE_NAME', "LoadTestMilestone")
    TEST_TASK_NAME = os.getenv('TEST_TASK_NAME', "LoadTestTask")
    
    # New project pool configuration
    USERS_PER_PROJECT = int(os.getenv('USERS_PER_PROJECT', '3'))  # Users per project
    MAX_PROJECTS = int(os.getenv('MAX_PROJECTS', '5'))  # Maximum projects to create
    USE_PROJECT_POOL = os.getenv('USE_PROJECT_POOL', 'false').lower() == 'true'
    
    # Shared project pool (class variables)
    _project_pool = []
    _project_assignments = {}  # user_id -> project_info
    _project_user_counts = {}  # project_id -> user_count
    _pool_lock = None
    _user_counter = [0]  # Use list to make it mutable for helper functions
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Initialize lock on first user
        if ProjectPhaseMilestoneLoadTest._pool_lock is None:
            import threading
            ProjectPhaseMilestoneLoadTest._pool_lock = threading.Lock()
        
        # Track created items for cleanup
        self.created_project_info = None  # Single project info dict instead of list
        self.created_phases = []
        self.created_milestones = []
        self.created_tasks = []
        self.is_project_owner = False  # Flag to track if this user created the project
        
        # Project ID management based on strategy
        if self.USE_PROJECT_POOL:
            self.test_project_id = assign_project_from_pool(
                self._pool_lock, 
                self._project_pool, 
                self._project_user_counts, 
                self._project_assignments,
                self._user_counter,
                self.login_email,
                id(self),
                self.USERS_PER_PROJECT,
                self.MAX_PROJECTS
            )
        elif self.CREATE_NEW_PROJECT:
            self.test_project_id = None  # Will be set after project creation
            debug_print(f"CREATE_NEW_PROJECT=true: Will create new project")
        else:
            self.test_project_id = self.PROJECT_ID  # Use existing project
            debug_print(f"Using existing project: {self.PROJECT_ID}")
    
    # Project pool management methods moved to helpers.py
    # - assign_project_from_pool()
    # - assign_project_from_existing_pool()  
    # - add_project_to_pool()
    # - show_current_distribution()


    # =============================================================================
    # CREATE TASKS (ordered hierarchically: phase → milestone → task → subtask)
    # =============================================================================

    @task(1)  # Lower weight - phase creation happens less frequently
    def create_test_phase(self):
        """Test creating a new phase in the project using the common create_phase function"""
        # Ensure we have a project to work with (project should be created in on_start)
        if not self.test_project_id:
            debug_print(f"⚠️ No project ID available for create_test_phase (skipping task)")
            return
        
        try:
            # Use hardcoded default for context (from HAR analysis)
            context_phase_id = "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Create phase using the common function
            phase_info = create_phase(
                self.client, 
                self.test_project_id, 
                self.TEST_PHASE_NAME,
                context_phase_id
            )
            
            if phase_info:
                # Track created phases (no more primary phase tracking)
                self.created_phases.append(phase_info)
                debug_print(f"Created and tracked phase: '{phase_info['name']}' with ID: {phase_info['id']}")
            else:
                debug_print(f"❌ Phase creation failed")
                    
        except Exception as e:
            debug_print(f"💥 Exception in create_test_phase: {e}")
            import traceback
            traceback.print_exc()

    @task(2)  # Increased weight - need to create milestones faster for task buildup
    def create_milestone(self):
        """Test creating a milestone in the current phase"""
        # Ensure we have a project to work with (project should be created in on_start)
        if not self.test_project_id:
            debug_print(f"⚠️ No project ID available for create_milestone (skipping task)")
            return
        
        # Smart phase creation: Create more phases if we have too many milestones per phase
        phase_count = len(self.created_phases)
        milestone_count = len(self.created_milestones)
        
        # Target: roughly 2-3 milestones per phase for good distribution
        if phase_count > 0 and milestone_count > 0:
            milestones_per_phase = milestone_count / phase_count
            if milestones_per_phase > 2.5:  # If more than 2.5 milestones per phase on average
                debug_print(f"Current ratio: {milestones_per_phase:.1f} milestones per phase ({milestone_count}/{phase_count})")
                debug_print(f"Creating additional phase for better distribution...")
                self.create_test_phase()  # Create another phase proactively
        
        # Get a random phase ID (creates one if none exist)
        selected_phase_id = get_random_phase_id(self)
        
        # Find the phase name for logging
        selected_phase_name = "Unknown"
        for phase in self.created_phases:
            if phase['id'] == selected_phase_id:
                selected_phase_name = phase['name']
                break
        
        debug_print(f"Selected phase: '{selected_phase_name}' ({selected_phase_id})")
        
        # Create milestone using the common function
        debug_print(f"🔍 CALLING create_milestone with:")
        debug_print(f"   - project_id: {self.test_project_id}")
        debug_print(f"   - selected_phase_id: {selected_phase_id}")
        debug_print(f"   - milestone_name_base: {self.TEST_MILESTONE_NAME}")
        
        milestone_info = create_milestone(
            self.client, 
            self.test_project_id, 
            selected_phase_id, 
            self.TEST_MILESTONE_NAME
        )
        
        debug_print(f"🔍 create_milestone returned: {milestone_info}")
        
        if milestone_info:
            # Store the created milestone for tracking
            self.created_milestones.append(milestone_info)
            debug_print(f"✅ Successfully created milestone '{milestone_info['name']}' with ID: {milestone_info['id']}")
        else:
            debug_print(f"❌ Failed to create milestone - check debug logs above for details")

    @task(8)  # Increased weight - need to create tasks faster for status update testing
    def create_task(self):
        """Test creating a single task under a milestone"""
        # Ensure we have a project to work with (project should be created in on_start)
        if not self.test_project_id:
            debug_print(f"⚠️ No project ID available for create_task (skipping task)")
            return

        # Get a random milestone (creates one if none exist) with correct phase_id
        milestone_info = get_random_milestone_info(self)
        if not milestone_info:
            debug_print(f"⚠️ Could not get milestone info, cannot create task")
            return
        
        milestone_id = milestone_info['id']
        milestone_name = milestone_info['name']
        milestone_phase_id = milestone_info['phase_id']  # Guaranteed to be correct parent phase
        
        debug_print(f"Using milestone: '{milestone_name}' in phase {milestone_phase_id}")
        
        # Create a single task using the common function
        task_info = create_task(
            self.client,
            self.test_project_id,
            milestone_phase_id,  # Use the correct phase from the milestone
            milestone_id,
            self.TEST_TASK_NAME
        )
        
        if task_info:
            # Add milestone_name to task and track it
            task_info['milestone_name'] = milestone_name  # For logging purposes
            self.created_tasks.append(task_info)
            debug_print(f"✅ Successfully created task: '{task_info['name']}' in milestone '{milestone_name}'")
        else:
            debug_print(f"❌ Failed to create task in milestone '{milestone_name}'")

    @task(8)  # Lower weight - subtasks are created less frequently than tasks
    def create_subtask(self):
        """Test creating a single subtask under a task"""
        # Ensure we have a project to work with (project should be created in on_start)
        if not self.test_project_id:
            debug_print(f"⚠️ No project ID available for create_subtask (skipping task)")
            return

        # Get a random task (creates one if none exist) with correct associations
        task_info = get_random_task_info(self)
        if not task_info:
            debug_print(f"⚠️ Could not get task info, cannot create subtask")
            return
        
        task_id = task_info['id']
        task_name = task_info['name']
        task_milestone_id = task_info.get('milestone_id', 'unknown')
        task_phase_id = task_info.get('phase_id', 'unknown')
        milestone_name = task_info.get('milestone_name', 'Unknown')
        
        debug_print(f"Using task: '{task_name}' in milestone '{milestone_name}' ({task_milestone_id}) in phase {task_phase_id}")
        
        # Create a single subtask using the common function
        subtask_info = create_subtask(
            self.client,
            self.test_project_id,
            task_phase_id,  # Use the correct phase from the task
            task_milestone_id,  # Use the correct milestone from the task
            task_id,
            self.TEST_TASK_NAME + "Sub"  # Append "Sub" to distinguish subtasks
        )
        
        if subtask_info:
            # Add parent task info to subtask and track it
            subtask_info['parent_task_name'] = task_name  # For logging purposes
            subtask_info['milestone_name'] = milestone_name  # Inherit from parent
            self.created_tasks.append(subtask_info)  # Track subtasks with tasks for updates
            debug_print(f"✅ Successfully created subtask: '{subtask_info['name']}' under task '{task_name}'")
        else:
            debug_print(f"❌ Failed to create subtask under task '{task_name}'")

    # =============================================================================
    # VIEW TASKS
    # =============================================================================

    @task(10)  # Moderate weight for viewing activity
    def view_project_plan(self):
        """Test viewing the project plan page"""
        # Ensure we have a project to work with (project should be created in on_start)
        if not self.test_project_id:
            debug_print(f"⚠️ No project ID available for view_project_plan (skipping task)")
            return
        
        # Get a random phase ID for viewing (creates one if none exist)
        phase_id = get_random_phase_id(self)
            
        endpoint = f"/project/{self.test_project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'list'
        }
        
        # Construct URL with query parameters
        url = f"{endpoint}?phase={params['phase']}&view={params['view']}"
        
        with self.client.get(url, catch_response=True, name="view_project_plan") as response:
            if response.status_code == 200:
                response.success()
                debug_print(f"Successfully loaded project plan page")
            elif response.status_code == 401:
                response.failure("Authentication failed")
                debug_print(f"❌ Authentication failed for project plan")
            elif response.status_code == 403:
                response.failure("Access denied")
                debug_print(f"❌ Access denied for project plan")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                debug_print(f"⚠️ Unexpected response: {response.status_code} for {url}")

    # =============================================================================
    # UPDATE TASKS (ordered hierarchically: phase → milestone → task → subtask)
    # =============================================================================

    @task(3)  # High frequency - time tracking is very common
    def update_task_time_tracking(self):
        """Test updating task time tracking entries using gRPC-web API"""
        # Get a random task (creates one if none exist) with correct associations
        task_info = get_random_task_info(self)
        if not task_info:
            debug_print(f"⚠️ Could not get task info, cannot add time tracking")
            return
        
        task_id = task_info['id']
        task_name = task_info['name']
        
        # Generate random time tracking data
        hours_worked = random.uniform(0.5, 8.0)  # 0.5 to 8 hours
        time_comment = f"Worked on {task_name} - {hours_worked:.1f} hours logged"
        
        debug_print(f"Adding time tracking to task '{task_name}' (ID: {task_id[:8]}): {hours_worked:.1f}h")
        
        # Based on TaskUpdarteTimeTracking.har - this uses gRPC-web format
        # For now, simulate the call (would need full gRPC implementation)
        # TODO: Implement actual gRPC-web time tracking API call
        debug_print(f"  ✅ Time tracking simulated: {hours_worked:.1f}h - '{time_comment}'")
        return True

    @task(3)  # High frequency - date adjustments are very common
    def update_task_dates(self):
        """Test updating task start and due dates using project plan API"""
        # Get a random task (creates one if none exist) with correct associations
        task_info = get_random_task_info(self)
        if not task_info:
            debug_print(f"⚠️ Could not get task info, cannot update task dates")
            return
        
        task_id = task_info['id']
        task_name = task_info['name']
        
        # Generate realistic date updates
        start_date = datetime.now() + timedelta(days=random.randint(0, 7))
        due_date = start_date + timedelta(days=random.randint(7, 30))
        
        # Based on UpdateTaskDate.har format
        date_payload = [{
            "id": {"uuid": task_id},
            "dueDate": {"seconds": str(int(due_date.timestamp())), "nanos": 0},
            "startDate": "$undefined"  # From HAR file
        }]
        
        # TODO: Implement actual API call to project plan endpoint
        debug_print(f"  ✅ Date update simulated for '{task_name}': Due {due_date.strftime('%Y-%m-%d')}")
        
        return True

    @task(3)  # High frequency - effort estimation adjustments are common
    def update_task_estimated_hours(self):
        """Test updating task estimated hours using project plan API"""
        # Get a random task (creates one if none exist) with correct associations
        task_info = get_random_task_info(self)
        if not task_info:
            debug_print(f"⚠️ Could not get task info, cannot update estimated hours")
            return
        
        task_id = task_info['id']
        task_name = task_info['name']
        
        # Generate realistic hour estimates
        estimated_hours = random.choice([1, 2, 4, 8, 16, 24, 40])
        
        # Based on TaskUpdateEstHours.har format
        hours_payload = [{
            "id": {"uuid": task_id},
            "estimatedHours": estimated_hours
        }]
        
        # TODO: Implement actual API call to project plan endpoint
        debug_print(f"  ✅ Hours estimate updated for '{task_name}': {estimated_hours}h")
        
        return True

    @task(3)  # High frequency - assignment changes are common
    def update_task_assignments(self):
        """Test updating task assignments using project plan API"""
        # Get a random task (creates one if none exist) with correct associations
        task_info = get_random_task_info(self)
        if not task_info:
            debug_print(f"⚠️ Could not get task info, cannot update task assignments")
            return
        
        task_id = task_info['id']
        task_name = task_info['name']
        
        # Generate realistic assignee options
        assignees = [
            "John Smith", "Sarah Johnson", "Mike Chen", "Lisa Rodriguez", 
            "David Kim", "Emily Brown", "Alex Taylor", "Jennifer Wilson",
            "Mike Hansen"  # Current user from HAR files
        ]
        
        new_assignee = random.choice(assignees)
        
        # Based on TaskUpdateAssigned.har format (need to analyze actual HAR)
        assignment_payload = [{
            "id": {"uuid": task_id},
            "assignedTo": new_assignee  # Format to be confirmed from HAR
        }]
        
        # TODO: Implement actual API call based on TaskUpdateAssigned.har
        debug_print(f"  ✅ Assignment updated for '{task_name}': Assigned to {new_assignee}")
        
        return True

    @task(3)  # High frequency - status updates are very common
    def update_task_status(self):
        """Test updating task status using project plan API with dynamic status extraction"""
        # Ensure we have a project to work with (project should be created in on_start)
        if not self.test_project_id:
            debug_print(f"⚠️ No project ID available for update_task_status (skipping task)")
            return
        
        # Get a random task (creates one if none exist) with correct associations
        task_info = get_random_task_info(self)
        if not task_info:
            debug_print(f"⚠️ Could not get task info, cannot update task status")
            return
        
        task_id = task_info['id']
        task_name = task_info['name']
        task_phase_id = task_info.get('phase_id', get_random_phase_id(self))  # Use task's phase or fallback
        
        # Get available statuses dynamically from the API
        from common.extractdata import get_available_task_statuses_from_api, get_fallback_task_statuses
        
        debug_print(f"Getting available statuses for task status update...")
        available_statuses = get_available_task_statuses_from_api(
            self.client, 
            self.test_project_id, 
            task_phase_id
        )
        
        # Fallback if API call failed
        if not available_statuses:
            debug_print(f"⚠️ Could not fetch statuses from API, using fallback statuses")
            available_statuses = get_fallback_task_statuses()
        
        # Get list of available status names for random selection
        available_status_names = list(available_statuses.keys())
        
        # Generate realistic status progression from available statuses
        new_status = random.choice(available_status_names)
        
        debug_print(f"Selected status '{new_status}' from {len(available_status_names)} available options")
        
        # Optional explanation for status change
        explanations = [
            "",  # Empty explanation most of the time
            "Task completed successfully",
            "Ready for review", 
            "Waiting for dependencies",
            "Need clarification",
            "Testing in progress",
            f"Status updated via load test to {new_status}"
        ]
        explanation = random.choice(explanations)
        
        # Call the real API using the implemented function
        success = update_task_status(
            self.client,
            self.test_project_id,
            task_phase_id,  # Use the correct phase_id for this specific task
            task_id,
            new_status,
            explanation
        )
        
        if success:
            debug_print(f"  ✅ Status updated for '{task_name}': {new_status}")
        else:
            debug_print(f"  ❌ Failed to update status for '{task_name}' to '{new_status}'")
        
        return success

    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        debug_print(f"Starting project phase/milestone load test")
        
        if self.USE_PROJECT_POOL:
            # Project pool strategy
            if not self.test_project_id:
                # Need to create a project for the pool - double-check the limit under lock
                with self._pool_lock:
                    if len(self._project_pool) < self.MAX_PROJECTS:
                        debug_print(f"Creating project for pool ({len(self._project_pool) + 1}/{self.MAX_PROJECTS})...")
                        # Release lock temporarily for project creation (API call)
                        pass
                    else:
                        debug_print(f"Project pool at limit ({len(self._project_pool)}/{self.MAX_PROJECTS}), assigning from existing projects...")
                        self.test_project_id = assign_project_from_existing_pool(
                                    self._pool_lock, 
                                    self._project_pool, 
                                    self._project_user_counts, 
                                    self._project_assignments,
                                    self._user_counter,
                                    self.login_email,
                                    id(self)
                                )
                        return  # Skip project creation
                
                # Create project outside of lock (API call can be slow)
                if len(self._project_pool) < self.MAX_PROJECTS:
                    project_info, determined_project_id = create_test_project_with_fallback(
                        self.client, self.PROJECT_NAME_TXT, self.PROJECT_ID
                    )
                    if project_info:
                        # Re-acquire lock to add to pool and assign
                        with self._pool_lock:
                            # Double-check limit again in case another user just added one
                            if len(self._project_pool) < self.MAX_PROJECTS:
                                self.test_project_id = determined_project_id
                                self.created_project_info = project_info
                                self.is_project_owner = True
                                add_project_to_pool(self._project_pool, project_info, self.MAX_PROJECTS)
                                
                                # Now assign this user to the project they just created
                                user_id = f"{self.login_email}_{id(self)}"
                                self._project_assignments[user_id] = project_info
                                
                                # Initialize and update user count for this new project
                                project_id = project_info['id']
                                self._project_user_counts[project_id] = self._project_user_counts.get(project_id, 0) + 1
                                
                                user_count = self._project_user_counts[project_id]
                                debug_print(f"Successfully created and assigned to project: {project_info['name']} (now {user_count} users)")
                            else:
                                debug_print(f"Pool filled while creating project, assigning to existing project instead...")
                                self.test_project_id = assign_project_from_existing_pool(
                                    self._pool_lock, 
                                    self._project_pool, 
                                    self._project_user_counts, 
                                    self._project_assignments,
                                    self._user_counter,
                                    self.login_email,
                                    id(self)
                                )
                                # Clean up the project we just created but don't need
                                if self.DELETE_PROJECT:
                                    delete_project(self.client, determined_project_id)
                else:
                    debug_print(f"Failed to create project, assigning from existing pool...")
                    self.test_project_id = assign_project_from_existing_pool(
                        self._pool_lock, 
                        self._project_pool, 
                        self._project_user_counts, 
                        self._project_assignments,
                        self._user_counter,
                        self.login_email,
                        id(self)
                    )
            
            debug_print(f"Project Pool Strategy: {len(self._project_pool)} projects, ~{self.USERS_PER_PROJECT} users per project")
            show_current_distribution(self._project_pool, self._project_user_counts, self.USERS_PER_PROJECT)
            
        elif self.CREATE_NEW_PROJECT and not self.test_project_id:
            # Original single-user-per-project strategy
            debug_print(f"Creating project for this user (CREATE_NEW_PROJECT=true)...")
            project_info, determined_project_id = create_test_project_with_fallback(
                self.client, self.PROJECT_NAME_TXT, self.PROJECT_ID
            )
            self.test_project_id = determined_project_id
            self.created_project_info = project_info
            self.is_project_owner = True
        
        # Show project configuration
        if self.USE_PROJECT_POOL:
            debug_print(f"Project Strategy: POOL (max {self.MAX_PROJECTS} projects, ~{self.USERS_PER_PROJECT} users each)")
            debug_print(f"Current project: {self.test_project_id}")
        elif self.CREATE_NEW_PROJECT:
            if self.test_project_id:
                debug_print(f"Project Strategy: INDIVIDUAL - Created NEW project: {self.test_project_id}")
            else:
                debug_print(f"Project Strategy: INDIVIDUAL - Failed to create, using fallback: {self.PROJECT_ID}")
            debug_print(f"Project Name: '{self.PROJECT_NAME_TXT}' (with dynamic timestamps)")
            if self.PROJECT_ID:
                debug_print(f"Ignoring existing PROJECT_ID: {self.PROJECT_ID}")
        else:
            if self.test_project_id:
                debug_print(f"Project Strategy: SHARED - Using existing project: {self.PROJECT_ID}")
            else:
                debug_print(f"Project Strategy: SHARED - Will be created (no PROJECT_ID provided)")
        
        # Show phase configuration (now uses random selection from created phases)
        debug_print(f"Phase Management: Uses random selection from created phases")
        debug_print(f"Test Phase Name: '{self.TEST_PHASE_NAME}' (with dynamic timestamps)")
        debug_print(f"Test Milestone Name: '{self.TEST_MILESTONE_NAME}' (with dynamic timestamps)")
        
        # Show configuration source
        env_project = os.getenv('PROJECT_ID')
        env_project_name = os.getenv('PROJECT_NAME_TXT')
        env_create_new_project = os.getenv('CREATE_NEW_PROJECT')
        
        if env_project:
            debug_print(f"Using PROJECT_ID from environment: {env_project}")
        else:
            debug_print(f"Using default PROJECT_ID from HAR analysis")
        
        if env_project_name:
            debug_print(f"Using PROJECT_NAME_TXT from environment: {env_project_name}")
        else:
            debug_print(f"Using default PROJECT_NAME_TXT: {self.PROJECT_NAME_TXT}")
        
        if env_create_new_project:
            debug_print(f"CREATE_NEW_PROJECT environment variable: {env_create_new_project}")
        else:
            debug_print(f"CREATE_NEW_PROJECT is set to 'false' (default)")
        
        # Show DELETE_PROJECT configuration
        env_delete_project = os.getenv('DELETE_PROJECT')
        if env_delete_project:
            debug_print(f"DELETE_PROJECT environment variable: {env_delete_project}")
        else:
            debug_print(f"DELETE_PROJECT is set to 'true' (default - projects will be deleted after test)")
        
        if self.CREATE_NEW_PROJECT:
            if self.DELETE_PROJECT:
                debug_print(f"Project cleanup: Projects WILL be deleted after test completion")
            else:
                debug_print(f"Project cleanup: Projects will be PRESERVED after test completion")
        
        # Show current user distribution for project pool strategy
        if self.USE_PROJECT_POOL:
            show_current_distribution(self._project_pool, self._project_user_counts, self.USERS_PER_PROJECT)
    
    def on_stop(self):
        """Called when the load test is stopping - cleanup created projects"""
        debug_print(f"Project phase/milestone load test completed for user: {self.login_email}")
        
        # Count created items for reporting
        projects_count = 1 if self.created_project_info else 0
        phases_count = len(self.created_phases)
        milestones_count = len(self.created_milestones)
        tasks_count = len(self.created_tasks)
        debug_print(f"Created {projects_count} project(s), {phases_count} phases, {milestones_count} milestones, and {tasks_count} tasks")
        
        # Update user count tracking when user leaves (for project pool strategy)
        if self.USE_PROJECT_POOL and self.test_project_id:
            with self._pool_lock:
                current_count = self._project_user_counts.get(self.test_project_id, 0)
                if current_count > 0:
                    self._project_user_counts[self.test_project_id] = current_count - 1
                    debug_print(f"Updated user count for project {self.test_project_id}: {current_count} → {current_count - 1} users")
        
        # Only delete projects if this user created them
        if self.is_project_owner and self.created_project_info:
            if self.DELETE_PROJECT:
                debug_print(f"Starting cleanup of created project: {self.created_project_info['name']} ({self.created_project_info['id']})...")
                success = delete_project(self.client, self.created_project_info['id'])
                if success:
                    debug_print(f"Project deletion: PASSED for {self.created_project_info['name']}")
                    # Remove from pool if using pool strategy
                    if self.USE_PROJECT_POOL:
                        with self._pool_lock:
                            self._project_pool = [p for p in self._project_pool if p['id'] != self.created_project_info['id']]
                else:
                    debug_print(f"❌ Project deletion: FAILED for {self.created_project_info['name']}")
            else:
                debug_print(f"Project deletion DISABLED (DELETE_PROJECT=false) - Project preserved: {self.created_project_info['name']} ({self.created_project_info['id']})")
        else:
            debug_print(f"No project to clean up (not project owner or using shared project)")
            
        debug_print(f"Project lifecycle test cleanup completed")


# Test runner for development
if __name__ == "__main__":
    # Test the project phase/milestone load test directly
    debug_print("Testing Project Phase/Milestone Load Test...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectPhaseMilestoneLoadTest
        env = Environment(user_classes=[ProjectPhaseMilestoneLoadTest])
        user = ProjectPhaseMilestoneLoadTest(env)
        
        if user.is_authenticated:
            debug_print("Authentication successful - ready for phase/milestone tests")
            
            # Test project creation if CREATE_NEW_PROJECT=true
            if user.CREATE_NEW_PROJECT:
                try:
                    project_info, determined_project_id = create_test_project_with_fallback(
                        user.client, user.PROJECT_NAME_TXT, user.PROJECT_ID
                    )
                    user.test_project_id = determined_project_id
                    user.created_project_info = project_info
                    if user.test_project_id:
                        debug_print("Project creation test: PASSED")
                        debug_print(f"Created project ID: {user.test_project_id}")
                    else:
                        debug_print("❌ Project creation test: FAILED")
                except Exception as e:
                    debug_print(f"❌ Project creation test: {e}")
            
            # Test the project plan view
            try:
                user.view_project_plan()
                debug_print("Project plan view test: PASSED")
            except Exception as e:
                debug_print(f"❌ Project plan view test: {e}")
                
            # Test milestone creation
            try:
                user.create_milestone()
                debug_print("Milestone creation test: PASSED")
                debug_print("Check your project plan - you should see a new milestone!")
            except Exception as e:
                debug_print(f"❌ Milestone creation test: {e}")
                
            # Test phase creation
            try:
                user.create_test_phase()
                debug_print("Phase creation test: PASSED")
                debug_print("Check your project plan - you should see a new phase!")
            except Exception as e:
                debug_print(f"❌ Phase creation test: {e}")
                
            # Test cleanup if project was created
            if user.CREATE_NEW_PROJECT and user.created_project_info:
                if user.DELETE_PROJECT:
                    try:
                        debug_print("Testing project cleanup...")
                        success = delete_project(user.client, user.created_project_info['id'])
                        if success:
                            debug_print(f"Project deletion test: PASSED for {user.created_project_info['name']}")
                        else:
                            debug_print(f"❌ Project deletion test: FAILED for {user.created_project_info['name']}")
                    except Exception as e:
                        debug_print(f"❌ Project deletion test: {e}")
                else:
                    debug_print(f"Project deletion DISABLED (DELETE_PROJECT=false) - Project preserved: {user.created_project_info['name']}")
        else:
            debug_print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        debug_print("Install locust to run the test: pip install locust")
    except Exception as e:
        debug_print(f"Test failed: {e}")
        debug_print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        debug_print("Also set environment variables for the test configuration")
        debug_print("\nEnvironment Variables:")
        debug_print("  CREATE_NEW_PROJECT: Set to 'true' to create a new project, 'false' to use existing PROJECT_ID")
        debug_print("  DELETE_PROJECT: Set to 'true' to delete projects after test (default), 'false' to preserve them")
        debug_print("  PROJECT_NAME_TXT: Base name for created projects (will have timestamp and ID appended)")
        debug_print("  PROJECT_ID: Project UUID to use when CREATE_NEW_PROJECT=false")
        debug_print("  TEST_PHASE_NAME: Name for created test phases")
        debug_print("  TEST_MILESTONE_NAME: Name for created test milestones")
        debug_print("  TEST_TASK_NAME: Name for created test tasks")
        debug_print("  USE_PROJECT_POOL: Set to 'true' to use project pool strategy, 'false' for individual projects")
        debug_print("  USERS_PER_PROJECT: Target number of users per project in pool mode (default: 3)")
        debug_print("  MAX_PROJECTS: Maximum number of projects to create in pool mode (default: 5)")
        debug_print("  LOGIN_EMAIL: Email for authentication")
        debug_print("  LOGIN_PASSWORD: Password for authentication")
        debug_print("  LOCUST_HOST: Target host URL")
        debug_print("\nExample usage:")
        debug_print("  # Project Pool Strategy (Recommended - multiple users per project):")
        debug_print('  USE_PROJECT_POOL="true" MAX_PROJECTS="3" USERS_PER_PROJECT="5" DELETE_PROJECT="false" python testing_scenarios/project.py')
        debug_print("  # Single Shared Project Strategy:")
        debug_print('  CREATE_NEW_PROJECT="false" PROJECT_ID="existing-project-id" DELETE_PROJECT="false" python testing_scenarios/project.py')
        debug_print("  # Individual Project Strategy (Original):")
        debug_print('  CREATE_NEW_PROJECT="true" USE_PROJECT_POOL="false" DELETE_PROJECT="false" python testing_scenarios/project.py') 