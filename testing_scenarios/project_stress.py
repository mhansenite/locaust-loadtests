#!/usr/bin/env python3
"""
Project Stress Testing
Rapid creation stress testing for projects, phases, milestones, and tasks.
Uses environment variables for project lifecycle management.
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
    create_stress_project,
    create_stress_phase,
    create_stress_milestone,
    create_stress_task
)

# Additional test class for rapid creation stress testing
class ProjectStressTest(AuthenticatedUser):
    """
    Stress test for rapid project, phase and milestone creation.
    Uses environment variables for project lifecycle management.
    """
    
    wait_time = between(1, 3)  # Faster pace for stress testing
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Environment variables
        self.CREATE_NEW_PROJECT = os.getenv('CREATE_NEW_PROJECT', 'false').lower() == 'true'
        self.PROJECT_NAME_TXT = os.getenv('PROJECT_NAME_TXT', "StressProject")
        self.PROJECT_ID = os.getenv('PROJECT_ID', "e34b9b43-fa9f-4a09-a3bf-1178f471a5dc")
        self.PHASE_ID = os.getenv('PHASE_ID', None)
        self.CREATE_NEW_PHASE = os.getenv('CREATE_NEW_PHASE', 'false').lower() == 'true'
        self.TEST_PHASE_NAME = os.getenv('TEST_PHASE_NAME', "StressPhase")
        self.TEST_MILESTONE_NAME = os.getenv('TEST_MILESTONE_NAME', "StressMilestone")
        self.TEST_TASK_NAME = os.getenv('TEST_TASK_NAME', "StressTask")
        
        # Track created items
        self.created_projects = []
        self.created_phases = []
        self.created_milestones = []  
        self.created_tasks = []
        self.created_items = []  # For general tracking
        
        # Project ID management based on CREATE_NEW_PROJECT flag
        if self.CREATE_NEW_PROJECT:
            self.test_project_id = None  # Will be set after project creation
            print(f"Stress: CREATE_NEW_PROJECT=true: Will create new project")
        else:
            self.test_project_id = self.PROJECT_ID  # Use existing project
            print(f"Stress: Using existing project: {self.PROJECT_ID}")
        
        # Phase ID management based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            self.test_phase_id = None  # Force creation of new phase
            print(f"Stress: CREATE_NEW_PHASE=true: Will create new phase (ignoring PHASE_ID)")
        else:
            self.test_phase_id = self.PHASE_ID  # Use existing phase if provided
        
        print(f"Starting stress test")
    
    def create_stress_test_project(self):
        """Create a test project for stress testing using the common function"""
        try:
            project_info = create_stress_project(self.client, self.PROJECT_NAME_TXT)
            
            if project_info:
                self.test_project_id = project_info['id']
                print(f"Stress: Set test_project_id to: {project_info['id']}")
                
                # Track created project for cleanup
                self.created_projects.append(project_info)
                print(f"Stress: Tracked project for cleanup: {project_info['id']} ({project_info['name']})")
            else:
                print(f"⚠️ Stress: Project creation failed, using fallback")
                self.test_project_id = self.PROJECT_ID  # Fallback
                
        except Exception as e:
            print(f"💥 Stress: Exception in create_stress_test_project: {e}")
            self.test_project_id = self.PROJECT_ID  # Fallback
    
    def create_stress_test_phase(self):
        """Create a test phase for stress testing using the common function"""
        try:
            # Use the existing phase from environment or default for context
            context_phase_id = self.PHASE_ID or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Create phase using the common function
            phase_info = create_stress_phase(
                self.client, 
                self.test_project_id, 
                self.TEST_PHASE_NAME,
                context_phase_id
            )
            
            if phase_info:
                if not self.test_phase_id:
                    self.test_phase_id = phase_info['id']
                    print(f"Stress: Set test_phase_id to: {phase_info['id']}")
                
                # Always track created phases
                self.created_phases.append(phase_info)
                print(f"Stress: Tracked phase ID: {phase_info['id']}")
            else:
                print(f"❌ Stress: Phase creation failed")
                
        except Exception as e:
            print(f"💥 Stress: Exception in create_stress_test_phase: {e}")
    
    @task(8)  # Highest frequency for stress task creation
    def create_stress_task(self):
        """Stress test creating tasks under milestones"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"Stress: No project ID available, creating project first...")
                self.create_stress_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Stress: Project creation failed, cannot create task")
                    return
            else:
                print(f"⚠️ Stress: No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            print(f"Stress: No phase ID available, creating phase first...")
            self.create_stress_test_phase()
            if not self.test_phase_id:
                print(f"⚠️ Stress: Phase creation failed, cannot create task")
                return
        
        # Ensure we have a milestone to attach the task to
        if not self.created_milestones:
            print(f"Stress: No milestones available, creating milestone first...")
            self.create_stress_milestone()
            if not self.created_milestones:
                print(f"⚠️ Stress: Milestone creation failed, cannot create task")
                return
        
        # Use the most recent milestone as the parent
        milestone_info = self.created_milestones[-1]
        milestone_id = milestone_info['id']
        milestone_name = milestone_info['name']
        
        # Create task using the common stress function
        task_info = create_stress_task(
            self.client, 
            self.test_project_id, 
            self.test_phase_id, 
            milestone_id, 
            self.TEST_TASK_NAME
        )
        
        if task_info:
            print(f"Stress: Successfully created task '{task_info['name']}' with ID: {task_info['id']}")
            
            # Add milestone name and track the task
            task_info['milestone_name'] = milestone_name
            self.created_tasks.append(task_info)
            self.created_items.append(f"task:{task_info['id']}")
        else:
            print(f"❌ Stress: Failed to create task")

    @task(5)  # Stress milestone creation
    def create_stress_milestone(self):
        """Create milestones rapidly for stress testing"""
        # Ensure we have a project
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                self.create_stress_test_project()
                if not self.test_project_id:
                    return
            else:
                return
        
        if not self.test_phase_id:
            self.create_stress_test_phase()
            return
            
        try:
            # Create milestone using the common stress function
            milestone_info = create_stress_milestone(
                self.client, 
                self.test_project_id, 
                self.test_phase_id, 
                self.TEST_MILESTONE_NAME
            )
            
            if milestone_info:
                print(f"Stress test milestone created: {milestone_info['name']}")
                self.created_milestones.append(milestone_info)
                self.created_items.append(f"milestone:{milestone_info['name']}")
            else:
                print(f"⚠️ Stress test milestone failed")
                
        except Exception as e:
            print(f"❌ Stress test milestone error: {e}")
    
    @task(1)
    def create_stress_phase_task(self):
        """Create phases rapidly for stress testing"""
        # Ensure we have a project
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                self.create_stress_test_project()
                if not self.test_project_id:
                    return
            else:
                return
        
        try:
            # Use existing phase context or default
            context_phase_id = self.PHASE_ID or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Create phase using the common stress function
            phase_info = create_stress_phase(
                self.client,
                self.test_project_id,
                self.TEST_PHASE_NAME,
                context_phase_id
            )
            
            if phase_info:
                print(f"Stress test phase created: {phase_info['name']}")
                self.created_phases.append(phase_info)
                self.created_items.append(f"phase:{phase_info['name']}")
                
                # Set phase ID for milestone creation if not already set
                if not self.test_phase_id:
                    self.test_phase_id = phase_info['id']
                    print(f"Set stress test phase ID: {phase_info['id']}")
            else:
                print(f"⚠️ Stress test phase failed")
                
        except Exception as e:
            print(f"❌ Stress test phase error: {e}")


# Test runner for development
if __name__ == "__main__":
    print("Testing Project Stress Test...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectStressTest
        env = Environment(user_classes=[ProjectStressTest])
        user = ProjectStressTest(env)
        
        if user.is_authenticated:
            print("Stress Test Authentication successful - ready for stress tests")
            
            # Test project creation if CREATE_NEW_PROJECT=true
            if user.CREATE_NEW_PROJECT:
                try:
                    user.create_stress_test_project()
                    if user.test_project_id:
                        print("Stress Test project creation: PASSED")
                        print(f"Created stress project ID: {user.test_project_id}")
                    else:
                        print("❌ Stress Test project creation: FAILED")
                except Exception as e:
                    print(f"❌ Stress Test project creation: {e}")
            
            # Test milestone creation
            try:
                user.create_stress_milestone()
                print("Stress Test milestone creation: PASSED")
                print("Check your project plan - you should see a new milestone!")
            except Exception as e:
                print(f"❌ Stress Test milestone creation: {e}")
                
        else:
            print("❌ Stress Test Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Stress Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST") 