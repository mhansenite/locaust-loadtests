#!/usr/bin/env python3
"""
Master Test Controller
Coordinates multiple independent test modules based on configuration

Usage Examples:
  # Run all modules with default weights
  locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2
  
  # Run specific modules only
  ENABLED_MODULES="projects,phases,tasks" locust -f TestFiles/master_test_controller.py
  
  # Run with specific test scenario
  TEST_SCENARIO="creation_heavy" locust -f TestFiles/master_test_controller.py
  
  # Run task-focused testing
  TEST_SCENARIO="task_focused" ENABLED_MODULES="tasks,milestones" locust -f TestFiles/master_test_controller.py
"""

import sys
import os
import random
from locust import task, between

# Add base path for imports
sys.path.append(os.path.dirname(__file__))

# Import all test modules
from Projects.Create.project_create_test import ProjectCreateTest
from Projects.View.project_view_test import ProjectViewTest
from Phases.Create.phase_create_test import PhaseCreateTest
from Tasks.Create.task_create_test import TaskCreateTest

# Import base template for shared functionality
from base_test_template import BaseTestTemplate

class MasterTestController(BaseTestTemplate):
    """
    Master test controller that coordinates multiple test modules.
    
    Environment Variables:
    - ENABLED_MODULES: Comma-separated list of modules to enable
                      Options: projects, phases, milestones, tasks, subtasks
                      Default: "projects,phases,tasks"
    
    - TEST_SCENARIO: Test scenario configuration
                    Options: balanced, creation_heavy, view_heavy, task_focused
                    Default: "balanced"
    
    - COORDINATION_MODE: How to coordinate between modules
                        Options: sequential, parallel, smart
                        Default: "smart"
    """
    
    wait_time = between(2, 8)  # Wait 2-8 seconds between requests
    
    # Configuration from environment
    ENABLED_MODULES = os.getenv('ENABLED_MODULES', 'projects,phases,tasks').lower().split(',')
    TEST_SCENARIO = os.getenv('TEST_SCENARIO', 'balanced').lower()
    COORDINATION_MODE = os.getenv('COORDINATION_MODE', 'smart').lower()
    
    # Test scenario configurations
    SCENARIO_WEIGHTS = {
        'balanced': {
            'create_project': 3, 'view_project': 5, 'create_phase': 4,
            'create_task': 6, 'view_task': 3
        },
        'creation_heavy': {
            'create_project': 6, 'view_project': 2, 'create_phase': 7,
            'create_task': 8, 'view_task': 1
        },
        'view_heavy': {
            'create_project': 2, 'view_project': 8, 'create_phase': 2,
            'create_task': 3, 'view_task': 7
        },
        'task_focused': {
            'create_project': 1, 'view_project': 2, 'create_phase': 2,
            'create_task': 8, 'view_task': 5
        }
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Initialize module instances for coordination - pass environment
        self.project_creator = ProjectCreateTest(self.environment)
        self.project_viewer = ProjectViewTest(self.environment)
        self.phase_creator = PhaseCreateTest(self.environment)
        self.task_creator = TaskCreateTest(self.environment)
        
        # Share state across all modules
        self._setup_shared_state()
        
        print(f"🎛️ Master Controller initialized")
        print(f"📋 Enabled modules: {self.ENABLED_MODULES}")
        print(f"🎯 Test scenario: {self.TEST_SCENARIO}")
        print(f"🔗 Coordination mode: {self.COORDINATION_MODE}")
    
    def _setup_shared_state(self):
        """Setup shared state across all test modules"""
        # All modules share the same tracking lists
        shared_state = {
            'created_projects': self.created_projects,
            'created_phases': self.created_phases,
            'created_milestones': self.created_milestones,
            'created_tasks': self.created_tasks,
            'created_subtasks': self.created_subtasks,
            'test_project_id': self.test_project_id,
            'test_phase_id': self.test_phase_id
        }
        
        # Share state with all module instances
        for attr_name, attr_value in shared_state.items():
            setattr(self.project_creator, attr_name, attr_value)
            setattr(self.project_viewer, attr_name, attr_value)
            setattr(self.phase_creator, attr_name, attr_value)
            setattr(self.task_creator, attr_name, attr_value)
        
        # Share client instances
        self.project_creator.client = self.client
        self.project_viewer.client = self.client
        self.phase_creator.client = self.client
        self.task_creator.client = self.client
    
    def _get_task_weight(self, task_name):
        """Get task weight based on current scenario"""
        current_weights = self.SCENARIO_WEIGHTS.get(self.TEST_SCENARIO, self.SCENARIO_WEIGHTS['balanced'])
        return current_weights.get(task_name, 1)
    
    # === PROJECT MANAGEMENT TASKS ===
    
    @task
    def orchestrated_project_creation(self):
        """Orchestrated project creation with smart coordination"""
        if 'projects' not in self.ENABLED_MODULES:
            return
            
        weight = self._get_task_weight('create_project')
        if random.randint(1, 10) > weight:
            return
        
        print(f"🎛️ Orchestrating project creation...")
        
        # Use project creator module
        project_result = self.project_creator.create_test_project()
        
        # Update shared state
        if project_result and project_result.get('id'):
            self.test_project_id = project_result['id']
            print(f"🔗 Master controller updated project ID: {self.test_project_id}")
        elif self.project_creator.test_project_id:
            self.test_project_id = self.project_creator.test_project_id
            print(f"🔗 Master controller got project ID from creator: {self.test_project_id}")
        else:
            print("⚠️ Project creation did not return a valid ID")
            # Try to use the default project for fallback
            if not self.CREATE_NEW_PROJECT and self.PROJECT_ID:
                self.test_project_id = self.PROJECT_ID
                print(f"🔄 Falling back to default project: {self.test_project_id}")
            
        self._update_shared_state()
        return project_result
    
    @task
    def orchestrated_project_viewing(self):
        """Orchestrated project viewing with dependency checking"""
        if 'projects' not in self.ENABLED_MODULES:
            return
            
        weight = self._get_task_weight('view_project')
        if random.randint(1, 10) > weight:
            return
        
        # Ensure we have a project to view
        if not self.test_project_id and not self.created_projects:
            print(f"🔗 No project available for viewing, creating one first...")
            result = self.orchestrated_project_creation()
            if not self.test_project_id:
                print("⚠️ Could not create project for viewing")
                return
        
        print(f"🎛️ Orchestrating project viewing...")
        self.project_viewer.view_project_plan()
    
    # === PHASE MANAGEMENT TASKS ===
    
    @task
    def orchestrated_phase_creation(self):
        """Orchestrated phase creation with project dependency"""
        if 'phases' not in self.ENABLED_MODULES:
            return
            
        weight = self._get_task_weight('create_phase')
        if random.randint(1, 10) > weight:
            return
        
        # Ensure we have a project - with better error handling
        if not self.test_project_id:
            print(f"🔗 No project available for phase creation, creating one first...")
            result = self.orchestrated_project_creation()
            if not self.test_project_id:
                print("⚠️ Could not create or find project for phase creation")
                return
        
        print(f"🎛️ Orchestrating phase creation...")
        phase_result = self.phase_creator.create_test_phase()
        
        # Update shared state
        if phase_result and phase_result.get('id'):
            if not hasattr(self, 'test_phase_id') or not self.test_phase_id:
                self.test_phase_id = phase_result['id']
                print(f"🔗 Master controller set phase ID: {self.test_phase_id}")
        
        self._update_shared_state()
        return phase_result
    
    # === MILESTONE MANAGEMENT TASKS ===
    
    @task
    def orchestrated_milestone_creation(self):
        """Orchestrated milestone creation with phase dependency"""
        if 'milestones' not in self.ENABLED_MODULES:
            return
            
        # Ensure we have project and phase
        if not self.test_project_id:
            self.orchestrated_project_creation()
            return
            
        if not self.test_phase_id and not self.created_phases:
            self.orchestrated_phase_creation()
            return
        
        print(f"🎛️ Orchestrating milestone creation...")
        # Note: This would call milestone creation module when created
        # For now, we'll create a mock milestone for task dependencies
        
        # Create mock milestone for task creation
        import time
        import uuid
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        
        # Select appropriate phase
        phase_id = self.test_phase_id if self.test_phase_id else self.created_phases[0]['id']
        
        mock_milestone = {
            'id': f"mock-milestone-{unique_id}",
            'name': f"Orchestrated-Milestone-{timestamp}",
            'phase_id': phase_id
        }
        
        self.created_milestones.append(mock_milestone)
        print(f"✅ Created mock milestone: {mock_milestone['name']}")
    
    # === TASK MANAGEMENT TASKS ===
    
    @task
    def orchestrated_task_creation(self):
        """Orchestrated task creation with milestone dependency"""
        if 'tasks' not in self.ENABLED_MODULES:
            return
            
        weight = self._get_task_weight('create_task')
        if random.randint(1, 10) > weight:
            return
        
        # Ensure we have all dependencies
        if not self.test_project_id:
            self.orchestrated_project_creation()
            return
            
        if not self.test_phase_id and not self.created_phases:
            self.orchestrated_phase_creation()
            return
            
        if not self.created_milestones:
            self.orchestrated_milestone_creation()
            return
        
        print(f"🎛️ Orchestrating task creation...")
        self.task_creator.create_task()
    
    @task  
    def orchestrated_single_task_creation(self):
        """Orchestrated single task creation for focused testing"""
        if 'tasks' not in self.ENABLED_MODULES:
            return
            
        # Check dependencies
        if not self.created_milestones:
            return
            
        print(f"🎛️ Orchestrating single task creation...")
        self.task_creator.create_single_task_for_random_milestone()
    
    # === COORDINATION HELPERS ===
    
    def _update_shared_state(self):
        """Update shared state across all modules"""
        # Update project ID
        if self.project_creator.test_project_id:
            self.test_project_id = self.project_creator.test_project_id
            
        # Update phase ID  
        if self.phase_creator.test_phase_id:
            self.test_phase_id = self.phase_creator.test_phase_id
        
        # Propagate to all modules
        for module in [self.project_creator, self.project_viewer, self.phase_creator, self.task_creator]:
            module.test_project_id = self.test_project_id
            module.test_phase_id = self.test_phase_id
    
    @task(1)  # Low weight coordination task
    def smart_coordination_check(self):
        """Smart coordination to ensure good test distribution"""
        if self.COORDINATION_MODE != 'smart':
            return
        
        # Analyze current state and make smart decisions
        project_count = len(self.created_projects)
        phase_count = len(self.created_phases)
        milestone_count = len(self.created_milestones)
        task_count = len(self.created_tasks)
        
        print(f"📊 Smart coordination check: P:{project_count} Ph:{phase_count} M:{milestone_count} T:{task_count}")
        
        # Smart decisions based on ratios
        if phase_count > 0 and milestone_count / max(phase_count, 1) < 2:
            print(f"🎯 Smart coordination: Need more milestones per phase")
            self.orchestrated_milestone_creation()
            
        elif milestone_count > 0 and task_count / max(milestone_count, 1) < 3:
            print(f"🎯 Smart coordination: Need more tasks per milestone")
            self.orchestrated_task_creation()
            
        elif project_count == 0 and self.CREATE_NEW_PROJECT:
            print(f"🎯 Smart coordination: Need initial project")
            self.orchestrated_project_creation()
    
    def on_start(self):
        """Initialize master controller"""
        super().on_start()
        print(f"🚀 Master Test Controller started")
        print(f"📋 Configuration:")
        print(f"   • Enabled modules: {', '.join(self.ENABLED_MODULES)}")
        print(f"   • Test scenario: {self.TEST_SCENARIO}")
        print(f"   • Coordination mode: {self.COORDINATION_MODE}")
        print(f"   • Create new project: {self.CREATE_NEW_PROJECT}")
        print(f"   • Create new phase: {self.CREATE_NEW_PHASE}")
    
    def on_stop(self):
        """Cleanup and reporting"""
        print(f"🛑 Master Test Controller stopping")
        
        # Summary reporting
        project_count = len(self.created_projects)
        phase_count = len(self.created_phases)
        milestone_count = len(self.created_milestones)
        task_count = len(self.created_tasks)
        
        print(f"📊 Final Summary:")
        print(f"   • Projects: {project_count}")
        print(f"   • Phases: {phase_count}")
        print(f"   • Milestones: {milestone_count}")
        print(f"   • Tasks: {task_count}")
        
        # Cleanup (currently disabled for inspection)
        if self.CREATE_NEW_PROJECT and self.created_projects:
            print(f"🧹 Cleanup would delete {len(self.created_projects)} projects")
            print(f"⚠️ CLEANUP DISABLED - Projects preserved for inspection")


# Standalone execution capability
if __name__ == "__main__":
    print("🎛️ Running Master Test Controller...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test MasterTestController
        env = Environment(user_classes=[MasterTestController])
        user = MasterTestController(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for coordinated testing")
            
            # Run a sample coordination sequence
            try:
                print("🔧 Testing coordination sequence...")
                
                # Test project creation
                user.orchestrated_project_creation()
                print(f"✅ Project creation coordinated")
                
                # Test phase creation  
                user.orchestrated_phase_creation()
                print(f"✅ Phase creation coordinated")
                
                # Test milestone creation
                user.orchestrated_milestone_creation()
                print(f"✅ Milestone creation coordinated")
                
                # Test task creation
                user.orchestrated_task_creation()
                print(f"✅ Task creation coordinated")
                
                # Smart coordination check
                user.smart_coordination_check()
                print(f"✅ Smart coordination check completed")
                
                print("🎉 Master controller coordination test: PASSED")
                
            except Exception as e:
                print(f"❌ Master controller test: {e}")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        print("\nEnvironment Variables:")
        print("  ENABLED_MODULES: Comma-separated list (projects,phases,tasks)")
        print("  TEST_SCENARIO: balanced|creation_heavy|view_heavy|task_focused")
        print("  COORDINATION_MODE: sequential|parallel|smart") 