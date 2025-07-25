#!/usr/bin/env python3
"""
Project Phase and Milestone Creation Load Test
Tests creating projects, phases and milestones based on HAR file analysis

🚨 TEMPORARY: Project deletion is currently DISABLED for inspection purposes
   Projects will be created but NOT deleted automatically at test end.
   To re-enable deletion, uncomment the deletion calls in on_stop() methods.
"""

import sys
import os
import json
import time
import uuid
import re
import random
from locust import task, between

# Add parent directory to path to import from common
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.auth import AuthenticatedUser
from common.create import (
    create_project, 
    create_phase, 
    create_milestone, 
    create_task, 
    create_subtask,
    create_multiple_tasks,
    create_multiple_subtasks,
    delete_project,
    update_task,
    generate_task_updates
)
from common.extractdata import (
    extract_project_id_from_response,
    extract_phase_id_from_response,
    extract_milestone_id_from_response,
    extract_task_id_from_response,
    extract_subtask_id_from_response
)

class ProjectPhaseMilestoneLoadTest(AuthenticatedUser):
    """
    Load test for project, phase and milestone creation functionality.
    
    Tests creating projects (optionally), phases and milestones using the APIs
    discovered from HAR file analysis.
    
    Environment Variables:
    - CREATE_NEW_PROJECT: Set to "true" to create a new project, "false" to use existing PROJECT_ID
    - PROJECT_NAME_TXT: Base name for created projects (will have timestamp and ID appended)
    - PROJECT_ID: Project UUID to use when CREATE_NEW_PROJECT=false
    - CREATE_NEW_PHASE: Set to "true" to create a new phase, "false" to use existing PHASE_ID  
    - PHASE_ID: Phase UUID to use when CREATE_NEW_PHASE=false
    - TEST_PHASE_NAME: Name for created test phases
    - TEST_MILESTONE_NAME: Name for created test milestones
    - TEST_TASK_NAME: Name for created test tasks
    - LOGIN_EMAIL: Email for authentication
    - LOGIN_PASSWORD: Password for authentication
    - LOCUST_HOST: Target host URL
    
    Example usage:
    export CREATE_NEW_PROJECT="true"
    export PROJECT_NAME_TXT="LoadTestProject"
    export CREATE_NEW_PHASE="true"
    export TEST_PHASE_NAME="LoadTestPhase"
    export TEST_MILESTONE_NAME="LoadTestMilestone"
    export TEST_TASK_NAME="LoadTestTask"
    export LOGIN_EMAIL="your-email@example.com"
    export LOGIN_PASSWORD="your-password"
    export LOCUST_HOST="https://app.staging.guidecx.io"
    
    locust -f testing_scenarios/project.py --users 5 --spawn-rate 1
    """
    
    wait_time = between(3, 8)  # Wait 3-8 seconds between requests
    
    # Use environment variables
    CREATE_NEW_PROJECT = os.getenv('CREATE_NEW_PROJECT', 'false').lower() == 'true'
    PROJECT_NAME_TXT = os.getenv('PROJECT_NAME_TXT', "LoadTestProject")
    PROJECT_ID = os.getenv('PROJECT_ID', "e34b9b43-fa9f-4a09-a3bf-1178f471a5dc")  # Default from HAR
    PHASE_ID = os.getenv('PHASE_ID', None)  # Will be generated if not provided or CREATE_NEW_PHASE=true
    CREATE_NEW_PHASE = os.getenv('CREATE_NEW_PHASE', 'false').lower() == 'true'  # Flag to force new phase creation
    TEST_PHASE_NAME = os.getenv('TEST_PHASE_NAME', "LoadTestPhase")
    TEST_MILESTONE_NAME = os.getenv('TEST_MILESTONE_NAME', "LoadTestMilestone")
    TEST_TASK_NAME = os.getenv('TEST_TASK_NAME', "LoadTestTask")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track created items for cleanup
        self.created_projects = []
        self.created_phases = []
        self.created_milestones = []
        self.created_tasks = []
        
        # Project ID management based on CREATE_NEW_PROJECT flag
        if self.CREATE_NEW_PROJECT:
            self.test_project_id = None  # Will be set after project creation
            print(f"CREATE_NEW_PROJECT=true: Will create new project")
        else:
            self.test_project_id = self.PROJECT_ID  # Use existing project
            print(f"Using existing project: {self.PROJECT_ID}")
        
        # Phase ID management based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            self.test_phase_id = None  # Force creation of new phase
            print(f"CREATE_NEW_PHASE=true: Will create new phase (ignoring PHASE_ID)")
        else:
            self.test_phase_id = self.PHASE_ID  # Use existing phase if provided
    
    def create_test_project(self):
        """Create a new test project using the common create_project function"""
        try:
            project_info = create_project(self.client, self.PROJECT_NAME_TXT)
            
            if project_info:
                # Set the project ID for future operations
                self.test_project_id = project_info['id']
                print(f"Set test_project_id to: {project_info['id']}")
                
                # Track created project for cleanup
                self.created_projects.append(project_info)
                print(f"Tracked project for cleanup: {project_info['id']} ({project_info['name']})")
            else:
                print(f"⚠️ Project creation failed, using fallback project ID")
                self.test_project_id = self.PROJECT_ID  # Fallback
                    
        except Exception as e:
            print(f"💥 Exception in create_test_project: {e}")
            self.test_project_id = self.PROJECT_ID  # Fallback
            import traceback
            traceback.print_exc()
    
    def delete_test_project(self, project_id):
        """Delete a test project using the common delete_project function"""
        return delete_project(self.client, project_id)
    
    def _create_single_task(self, milestone_id, milestone_name, task_suffix=""):
        """Helper method to create a single task under a milestone"""
        task_info = create_task(
            self.client, 
            self.test_project_id, 
            self.test_phase_id, 
            milestone_id, 
            self.TEST_TASK_NAME, 
            task_suffix
        )
        
        if task_info:
            # Store the created task for tracking
            task_info['milestone_name'] = milestone_name
            self.created_tasks.append(task_info)
            return task_info['id'], task_info['name']
            
        return None, None

    @task(6)  # Primary task - increased weight for more viewing activity
    def view_project_plan(self):
        """Test viewing the project plan page"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot view project plan")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            # If no phase ID, create one first
            self.create_test_phase()
            return
            
        endpoint = f"/project/{self.test_project_id}/plan"
        params = {
            'phase': self.test_phase_id,
            'view': 'list'
        }
        
        # Construct URL with query parameters
        url = f"{endpoint}?phase={params['phase']}&view={params['view']}"
        
        with self.client.get(url, catch_response=True, name="view_project_plan") as response:
            if response.status_code == 200:
                response.success()
                print(f"Successfully loaded project plan page")
            elif response.status_code == 401:
                response.failure("Authentication failed")
                print(f"❌ Authentication failed for project plan")
            elif response.status_code == 403:
                response.failure("Access denied")
                print(f"❌ Access denied for project plan")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                print(f"⚠️ Unexpected response: {response.status_code} for {url}")
    
    @task(4)  # Adjusted weight for milestone creation (creates 1-10 tasks each)
    def create_milestone(self):
        """Test creating a milestone in the current phase"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot create milestone")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        # Ensure we have at least one phase available
        if not self.test_phase_id and not self.created_phases:
            # If no phase ID, create one first
            print(f"No phase ID available, creating phase first...")
            self.create_test_phase()
            
            # Check if phase creation succeeded
            if not self.test_phase_id and not self.created_phases:
                print(f"⚠️ Phase creation failed, cannot create milestone")
                return
            else:
                print(f"Phase created successfully, continuing with milestone creation")
        
        # Smart phase creation: Create more phases if we have too many milestones per phase
        phase_count = len(self.created_phases) + (1 if self.test_phase_id else 0)
        milestone_count = len(self.created_milestones)
        
        # Target: roughly 2-3 milestones per phase for good distribution
        if phase_count > 0 and milestone_count > 0:
            milestones_per_phase = milestone_count / phase_count
            if milestones_per_phase > 2.5:  # If more than 2.5 milestones per phase on average
                print(f"Current ratio: {milestones_per_phase:.1f} milestones per phase ({milestone_count}/{phase_count})")
                print(f"Creating additional phase for better distribution...")
                self.create_test_phase()  # Create another phase proactively
        
        # Select a random phase from available phases for realistic distribution
        if self.created_phases:
            selected_phase = random.choice(self.created_phases)
            selected_phase_id = selected_phase['id']
            selected_phase_name = selected_phase['name']
            print(f"Randomly selected phase: '{selected_phase_name}' ({selected_phase_id})")
        elif self.test_phase_id:
            selected_phase_id = self.test_phase_id
            print(f"Using primary phase: {selected_phase_id}")
        else:
            print(f"⚠️ No phases available for milestone creation")
            return
        
        # Create milestone using the common function
        milestone_info = create_milestone(
            self.client, 
            self.test_project_id, 
            selected_phase_id, 
            self.TEST_MILESTONE_NAME
        )
        
        if milestone_info:
            # Store the created milestone for tracking
            self.created_milestones.append(milestone_info)
            print(f"Successfully created milestone '{milestone_info['name']}' with ID: {milestone_info['id']}")
        else:
            print(f"❌ Failed to create milestone")
    
    @task(5)  # Balanced weight for task creation (each call creates 1-10 tasks)
    def create_task(self):
        """Test creating 1-10 random tasks under a milestone"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot create task")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            # If no phase ID, create one first
            print(f"No phase ID available, creating phase first...")
            self.create_test_phase()
            
            # Check if phase creation succeeded
            if not self.test_phase_id:
                print(f"⚠️ Phase creation failed, cannot create task")
                return
            else:
                print(f"Phase created successfully, continuing with task creation")
        
        # Ensure we have a milestone to attach the task to
        if not self.created_milestones:
            print(f"No milestones available, creating milestone first...")
            self.create_milestone()
            
            # Check if we have milestones after creation attempt
            if not self.created_milestones:
                print(f"⚠️ Milestone creation failed, cannot create task")
                return
        
        # Randomly select a milestone for realistic distribution across phases
        selected_milestone = random.choice(self.created_milestones)
        milestone_id = selected_milestone['id']
        milestone_name = selected_milestone['name']
        milestone_phase_id = selected_milestone['phase_id']
        
        print(f"Randomly selected milestone: '{milestone_name}' in phase {milestone_phase_id}")
        
        # Create multiple tasks using the common function
        created_tasks = create_multiple_tasks(
            self.client,
            self.test_project_id,
            milestone_phase_id,  # Use the phase from the milestone
            milestone_id,
            milestone_name,
            self.TEST_TASK_NAME,
            min_tasks=1,
            max_tasks=10
        )
        
        # Add milestone_name to each task and track them
        for task_info in created_tasks:
            task_info['milestone_name'] = milestone_name
            self.created_tasks.append(task_info)
        
        print(f"Task batch complete: Created {len(created_tasks)} tasks for milestone '{milestone_name}'")
    
    @task(3)  # Moderate frequency for realistic task management
    def update_existing_tasks(self):
        """Test updating existing tasks with assignments, dates, status, etc."""
        # Skip if no tasks exist yet
        if not self.created_tasks:
            return
        
        # Randomly select 1-3 tasks to update (or all if fewer)
        num_updates = min(random.randint(1, 3), len(self.created_tasks))
        tasks_to_update = random.sample(self.created_tasks, num_updates)
        
        print(f"Updating {num_updates} existing tasks...")
        
        for task_info in tasks_to_update:
            task_id = task_info['id']
            task_name = task_info['name']
            
            # Generate random updates
            updates = generate_task_updates()
            
            # Call task update API using common function
            success = update_task(self.client, self.test_project_id, task_id, updates)
            
            if success:
                print(f"  Successfully updated task '{task_name}' (ID: {task_id[:8]})")
            else:
                print(f"  ❌ Failed to update task '{task_name}' (ID: {task_id[:8]})")
      
    @task(6)  # Higher frequency to create more phases for distribution
    def create_test_phase(self):
        """Test creating a new phase in the project using the common create_phase function"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot create phase")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        try:
            # Use the existing phase from environment or default for context
            context_phase_id = self.PHASE_ID or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Create phase using the common function
            phase_info = create_phase(
                self.client, 
                self.test_project_id, 
                self.TEST_PHASE_NAME,
                context_phase_id
            )
            
            if phase_info:
                # Set the phase ID for future milestone creation
                if not self.test_phase_id:
                    self.test_phase_id = phase_info['id']
                    print(f"Set test_phase_id to: {phase_info['id']}")
                
                # Always track created phases
                self.created_phases.append(phase_info)
                print(f"Tracked phase ID: {phase_info['id']}")
            else:
                print(f"❌ Phase creation failed")
                    
        except Exception as e:
            print(f"💥 Exception in create_test_phase: {e}")
            import traceback
            traceback.print_exc()
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"Starting project phase/milestone load test")
        
        # Show project configuration based on CREATE_NEW_PROJECT flag
        if self.CREATE_NEW_PROJECT:
            print(f"Project ID: Will create NEW project (CREATE_NEW_PROJECT=true)")
            print(f"Project Name: '{self.PROJECT_NAME_TXT}' (with dynamic timestamps)")
            if self.PROJECT_ID:
                print(f"Ignoring existing PROJECT_ID: {self.PROJECT_ID}")
        else:
            if self.test_project_id:
                print(f"Project ID: Using existing project: {self.PROJECT_ID}")
            else:
                print(f"Project ID: Will be created (no PROJECT_ID provided)")
        
        # Show phase configuration based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            print(f"Phase ID: Will create NEW phase (CREATE_NEW_PHASE=true)")
            if self.PHASE_ID:
                print(f"Ignoring existing PHASE_ID: {self.PHASE_ID}")
        else:
            if self.test_phase_id:
                print(f"Phase ID: Using existing phase {self.test_phase_id}")
            else:
                print(f"Phase ID: Will be created (no PHASE_ID provided)")
        
        print(f"Test Phase Name: '{self.TEST_PHASE_NAME}' (with dynamic timestamps)")
        print(f"Test Milestone Name: '{self.TEST_MILESTONE_NAME}' (with dynamic timestamps)")
        
        # Show configuration source
        env_project = os.getenv('PROJECT_ID')
        env_project_name = os.getenv('PROJECT_NAME_TXT')
        env_phase = os.getenv('PHASE_ID')
        env_create_new_project = os.getenv('CREATE_NEW_PROJECT')
        env_create_new_phase = os.getenv('CREATE_NEW_PHASE')
        
        if env_project:
            print(f"Using PROJECT_ID from environment: {env_project}")
        else:
            print(f"Using default PROJECT_ID from HAR analysis")
        
        if env_project_name:
            print(f"Using PROJECT_NAME_TXT from environment: {env_project_name}")
        else:
            print(f"Using default PROJECT_NAME_TXT: {self.PROJECT_NAME_TXT}")
        
        if env_create_new_project:
            print(f"CREATE_NEW_PROJECT environment variable: {env_create_new_project}")
        else:
            print(f"CREATE_NEW_PROJECT is set to 'false' (default)")
        
        if env_create_new_phase:
            print(f"CREATE_NEW_PHASE environment variable: {env_create_new_phase}")
        else:
            print(f"CREATE_NEW_PHASE is set to 'false' (default)")
            
        if env_phase and not self.CREATE_NEW_PHASE:
            print(f"Using PHASE_ID from environment: {env_phase}")
        elif env_phase and self.CREATE_NEW_PHASE:
            print(f"PHASE_ID from environment ignored due to CREATE_NEW_PHASE=true")
        elif not env_phase:
            print(f"No PHASE_ID provided - will create new phase")
    
    def on_stop(self):
        """Called when the load test is stopping - cleanup created projects"""
        print(f"Project phase/milestone load test completed for user: {self.login_email}")
        
        # Count created items for reporting
        projects_count = len(self.created_projects)
        phases_count = len(self.created_phases)
        milestones_count = len(self.created_milestones)
        tasks_count = len(self.created_tasks)
        print(f"Created {projects_count} projects, {phases_count} phases, {milestones_count} milestones, and {tasks_count} tasks")
        
        if self.CREATE_NEW_PROJECT and self.created_projects:
            print(f"Starting cleanup of {len(self.created_projects)} created projects...")
            for project_info in self.created_projects:
                project_id = project_info['id']
                project_name = project_info['name']
                print(f"Attempting to delete project: {project_name} ({project_id})")
                
                # TEMPORARILY DISABLED - Comment out deletion for inspection
                # self.delete_test_project(project_id)
                print(f"⚠️ DELETION DISABLED - Project preserved for inspection: {project_name} ({project_id})")
            
            # print(f"Cleanup completed")
            print(f"Cleanup SKIPPED - Projects preserved for inspection")
        else:
            print(f"No projects to clean up (using existing project or no projects created)")
            
        print(f"Project lifecycle test cleanup completed")


# Test runner for development
if __name__ == "__main__":
    # Test the project phase/milestone load test directly
    print("Testing Project Phase/Milestone Load Test...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectPhaseMilestoneLoadTest
        env = Environment(user_classes=[ProjectPhaseMilestoneLoadTest])
        user = ProjectPhaseMilestoneLoadTest(env)
        
        if user.is_authenticated:
            print("Authentication successful - ready for phase/milestone tests")
            
            # Test project creation if CREATE_NEW_PROJECT=true
            if user.CREATE_NEW_PROJECT:
                try:
                    user.create_test_project()
                    if user.test_project_id:
                        print("Project creation test: PASSED")
                        print(f"Created project ID: {user.test_project_id}")
                    else:
                        print("❌ Project creation test: FAILED")
                except Exception as e:
                    print(f"❌ Project creation test: {e}")
            
            # Test the project plan view
            try:
                user.view_project_plan()
                print("Project plan view test: PASSED")
            except Exception as e:
                print(f"❌ Project plan view test: {e}")
                
            # Test milestone creation
            try:
                user.create_milestone()
                print("Milestone creation test: PASSED")
                print("Check your project plan - you should see a new milestone!")
            except Exception as e:
                print(f"❌ Milestone creation test: {e}")
                
            # Test phase creation
            try:
                user.create_test_phase()
                print("Phase creation test: PASSED")
                print("Check your project plan - you should see a new phase!")
            except Exception as e:
                print(f"❌ Phase creation test: {e}")
                
            # Test cleanup if project was created
            if user.CREATE_NEW_PROJECT and user.created_projects:
                try:
                    print("Testing project cleanup...")
                    for project in user.created_projects:
                        success = user.delete_test_project(project['id'])
                        if success:
                            print(f"Project deletion test: PASSED for {project['name']}")
                        else:
                            print(f"❌ Project deletion test: FAILED for {project['name']}")
                except Exception as e:
                    print(f"❌ Project deletion test: {e}")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        print("Also set environment variables for the test configuration")
        print("\nEnvironment Variables:")
        print("  CREATE_NEW_PROJECT: Set to 'true' to create a new project, 'false' to use existing PROJECT_ID")
        print("  PROJECT_NAME_TXT: Base name for created projects (will have timestamp and ID appended)")
        print("  PROJECT_ID: Project UUID to use when CREATE_NEW_PROJECT=false")
        print("  CREATE_NEW_PHASE: Set to 'true' to create a new phase, 'false' to use existing PHASE_ID")
        print("  PHASE_ID: Phase UUID to use when CREATE_NEW_PHASE=false")
        print("  TEST_PHASE_NAME: Name for created test phases")
        print("  TEST_MILESTONE_NAME: Name for created test milestones")
        print("  LOGIN_EMAIL: Email for authentication")
        print("  LOGIN_PASSWORD: Password for authentication")
        print("  LOCUST_HOST: Target host URL")
        print("\nExample usage:")
        print("  # Test with new project creation:")
        print('  CREATE_NEW_PROJECT="true" PROJECT_NAME_TXT="LoadTestProject" CREATE_NEW_PHASE="true" TEST_PHASE_NAME="LoadTestPhase" TEST_MILESTONE_NAME="LoadTestMilestone" TEST_TASK_NAME="LoadTestTask" LOGIN_EMAIL="your-email@example.com" LOGIN_PASSWORD="your-password" LOCUST_HOST="https://app.staging.guidecx.io" python testing_scenarios/project.py')
        print("  # Test with existing project:")
        print('  CREATE_NEW_PROJECT="false" PROJECT_ID=existing-project-id CREATE_NEW_PHASE="false" PHASE_ID=existing-phase-id python testing_scenarios/project.py') 