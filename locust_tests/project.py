#!/usr/bin/env python3
"""
Project Plan Load Test
Tests the project plan endpoint with specific project and phase IDs

Environment Variables:
- PROJECT_ID: Specific project ID to test with (required for your environment)
- PHASE_ID: Specific phase ID to test with (required for your environment)  
- VIEW_TYPE: View type to test with (default: "board", options: "board", "list")

For MultiProjectLoadTest, additional scenarios can be added:
- PROJECT_ID_2, PHASE_ID_2, VIEW_TYPE_2: Second test scenario
- PROJECT_ID_3, PHASE_ID_3, VIEW_TYPE_3: Third test scenario
- etc.
"""

import sys
import os
from locust import task, between

# Add parent directory to path to import from common
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.auth import AuthenticatedUser

class ProjectPlanLoadTest(AuthenticatedUser):
    """
    Load test for project plan endpoints.
    
    Tests the specific project plan view with phase parameters.
    Inherits authentication from AuthenticatedUser.
    """
    
    wait_time = between(2, 5)  # Wait 2-5 seconds between requests
    
    # Test data - configurable via environment variables
    PROJECT_ID = os.getenv('PROJECT_ID', "7c235b03-d4ea-4d0d-a499-a466b43a3c83")  # Default from original test
    PHASE_ID = os.getenv('PHASE_ID', "6ee9e420-f690-45ff-b5cd-860f15423a3e")     # Default from original test  
    VIEW_TYPE = os.getenv('VIEW_TYPE', "board")                                   # Default view type
    
    @task(5)  # Primary task - weight 5
    def view_project_plan_board(self):
        """Test viewing the project plan in board view with specific phase"""
        endpoint = f"/project/{self.PROJECT_ID}/plan"
        params = {
            'phase': self.PHASE_ID,
            'view': self.VIEW_TYPE
        }
        
        # Construct full URL with parameters
        url = f"{endpoint}?phase={params['phase']}&view={params['view']}"
        
        with self.client.get(url, catch_response=True, name="project_plan_board") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Successfully loaded project plan board view")
            elif response.status_code == 404:
                response.failure("Project or phase not found")
                print(f"❌ Project or phase not found: {url}")
            elif response.status_code == 403:
                response.failure("Access denied to project")
                print(f"❌ Access denied to project: {url}")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                print(f"⚠️ Unexpected response: {response.status_code} for {url}")
    
    @task(3)  # Secondary task - weight 3
    def view_project_plan_without_phase(self):
        """Test viewing the project plan without specific phase"""
        endpoint = f"/project/{self.PROJECT_ID}/plan"
        
        with self.client.get(endpoint, catch_response=True, name="project_plan_default") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Successfully loaded project plan default view")
            elif response.status_code == 404:
                response.failure("Project not found")
                print(f"❌ Project not found: {endpoint}")
            elif response.status_code == 403:
                response.failure("Access denied to project")
                print(f"❌ Access denied to project: {endpoint}")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                print(f"⚠️ Unexpected response: {response.status_code} for {endpoint}")
    
    @task(2)  # Lower frequency task - weight 2
    def view_project_plan_list_view(self):
        """Test viewing the project plan in list view"""
        endpoint = f"/project/{self.PROJECT_ID}/plan"
        params = {
            'phase': self.PHASE_ID,
            'view': 'list'  # Test different view type
        }
        
        url = f"{endpoint}?phase={params['phase']}&view={params['view']}"
        
        with self.client.get(url, catch_response=True, name="project_plan_list") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Successfully loaded project plan list view")
            elif response.status_code == 404:
                response.failure("Project or phase not found")
                print(f"❌ Project or phase not found: {url}")
            elif response.status_code == 403:
                response.failure("Access denied to project")
                print(f"❌ Access denied to project: {url}")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                print(f"⚠️ Unexpected response: {response.status_code} for {url}")
    

    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting project plan load test for project: {self.PROJECT_ID}")
        print(f"📋 Testing phase: {self.PHASE_ID}")
        print(f"👁️ Primary view: {self.VIEW_TYPE}")
        
        # Show configuration source
        env_project = os.getenv('PROJECT_ID')
        env_phase = os.getenv('PHASE_ID')
        env_view = os.getenv('VIEW_TYPE')
        if env_project:
            print(f"📋 Using PROJECT_ID from environment: {env_project}")
        else:
            print(f"📋 Using default PROJECT_ID from original test")
        if env_phase:
            print(f"📋 Using PHASE_ID from environment: {env_phase}")
        else:
            print(f"📋 Using default PHASE_ID from original test")
        if env_view:
            print(f"📋 Using VIEW_TYPE from environment: {env_view}")
        else:
            print(f"📋 Using default VIEW_TYPE: board")
    
    def on_stop(self):
        """Called when user stops"""
        print(f"🛑 Project plan load test completed for user: {self.login_email}")

# Additional test class for different project scenarios
class MultiProjectLoadTest(AuthenticatedUser):
    """
    Load test for multiple project scenarios.
    Tests different projects and phases if you have access to them.
    """
    
    wait_time = between(1, 3)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Multiple test scenarios - configurable via environment variables
        # Use the same environment variables as the main test, plus additional ones for multi-scenario testing
        self.TEST_SCENARIOS = [
            {
                'project_id': os.getenv('PROJECT_ID', '7c235b03-d4ea-4d0d-a499-a466b43a3c83'),
                'phase_id': os.getenv('PHASE_ID', '6ee9e420-f690-45ff-b5cd-860f15423a3e'),
                'view': os.getenv('VIEW_TYPE', 'board')
            }
        ]
        
        # Add additional scenarios from environment if provided
        # PROJECT_ID_2, PHASE_ID_2, VIEW_TYPE_2, etc.
        scenario_count = 2
        while os.getenv(f'PROJECT_ID_{scenario_count}'):
            additional_scenario = {
                'project_id': os.getenv(f'PROJECT_ID_{scenario_count}'),
                'phase_id': os.getenv(f'PHASE_ID_{scenario_count}', os.getenv('PHASE_ID', '6ee9e420-f690-45ff-b5cd-860f15423a3e')),
                'view': os.getenv(f'VIEW_TYPE_{scenario_count}', os.getenv('VIEW_TYPE', 'board'))
            }
            self.TEST_SCENARIOS.append(additional_scenario)
            scenario_count += 1
    
    @task
    def test_random_project_scenario(self):
        """Test a random project scenario from the list"""
        import random
        scenario = random.choice(self.TEST_SCENARIOS)
        
        endpoint = f"/project/{scenario['project_id']}/plan"
        url = f"{endpoint}?phase={scenario['phase_id']}&view={scenario['view']}"
        
        with self.client.get(url, catch_response=True, name="random_project_scenario") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Random scenario success: {scenario['view']} view")
            else:
                response.failure(f"Status: {response.status_code}")
                print(f"⚠️ Random scenario failed: {response.status_code}")
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting multi-project load test with {len(self.TEST_SCENARIOS)} scenarios")
        for i, scenario in enumerate(self.TEST_SCENARIOS, 1):
            print(f"📋 Scenario {i}: Project {scenario['project_id']}, Phase {scenario['phase_id']}, View {scenario['view']}")
        
        # Show configuration source
        env_project = os.getenv('PROJECT_ID')
        if env_project:
            print(f"📋 Base configuration from environment variables")
        else:
            print(f"📋 Base configuration using defaults")
            
        # Show additional scenarios
        additional_count = len(self.TEST_SCENARIOS) - 1
        if additional_count > 0:
            print(f"📋 Found {additional_count} additional scenario(s) from environment variables (PROJECT_ID_2, etc.)")
    
    def on_stop(self):
        """Called when user stops"""
        print(f"🛑 Multi-project load test completed for user: {self.login_email}")

# Test runner for development
if __name__ == "__main__":
    # Test the project load test directly
    print("Testing Project Plan Load Test...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectPlanLoadTest
        env = Environment(user_classes=[ProjectPlanLoadTest])
        user = ProjectPlanLoadTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for load testing")
            
            # Test the main endpoint
            try:
                user.view_project_plan_board()
                print("🎉 Project plan board test: PASSED")
            except Exception as e:
                print(f"❌ Project plan board test: {e}")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
