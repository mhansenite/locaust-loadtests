#!/usr/bin/env python3
"""
Project Plan Load Test
Tests the project plan endpoint with specific project and phase IDs
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
    
    # Test data - these could be moved to environment variables if needed
    PROJECT_ID = "7c235b03-d4ea-4d0d-a499-a466b43a3c83"
    PHASE_ID = "6ee9e420-f690-45ff-b5cd-860f15423a3e"
    VIEW_TYPE = "board"
    
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
    
    @task(1)  # Least frequent - weight 1
    def test_project_api_call(self):
        """Test making an authenticated API call to project data"""
        try:
            # Use the authenticated request method for API calls
            api_endpoint = f"/api/projects/{self.PROJECT_ID}"
            response = self.make_authenticated_request('GET', api_endpoint)
            
            if response.status_code == 200:
                print(f"✅ Successfully retrieved project API data")
            elif response.status_code == 404:
                print(f"⚠️ Project API endpoint not found: {api_endpoint}")
            elif response.status_code == 403:
                print(f"❌ Access denied to project API: {api_endpoint}")
            else:
                print(f"⚠️ Project API response: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error making project API call: {e}")
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting project plan load test for project: {self.PROJECT_ID}")
        print(f"📋 Testing phase: {self.PHASE_ID}")
        print(f"👁️ Primary view: {self.VIEW_TYPE}")
    
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
    
    # Multiple test scenarios - add your own project/phase IDs here
    TEST_SCENARIOS = [
        {
            'project_id': '7c235b03-d4ea-4d0d-a499-a466b43a3c83',
            'phase_id': '6ee9e420-f690-45ff-b5cd-860f15423a3e',
            'view': 'board'
        },
        # Add more test scenarios here:
        # {
        #     'project_id': 'another-project-id',
        #     'phase_id': 'another-phase-id', 
        #     'view': 'list'
        # }
    ]
    
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
