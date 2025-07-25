#!/usr/bin/env python3
"""
Project View Test Module
Extracted from project_cr_phase_milestone.py - Projects/View functionality

Can run standalone:
  locust -f TestFiles/Projects/View/project_view_test.py --users 5 --spawn-rate 1

Or imported by master controller
"""

import sys
import os
from locust import task, between

# Import base template
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from TestFiles.base_test_template import BaseTestTemplate

class ProjectViewTest(BaseTestTemplate):
    """
    Project viewing test module
    Extracted from original project_cr_phase_milestone.py
    """
    
    @task(6)  # Primary task - increased weight for more viewing activity
    def view_project_plan(self):
        """Test viewing the project plan page"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 No project ID available, creating project first...")
                # Note: In standalone mode, this would need to import project creation
                # In master controller mode, this will be handled by shared state
                print(f"⚠️ Project creation needed - run with master controller or set PROJECT_ID")
                return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            # If no phase ID, we need a phase first
            print(f"🔗 No phase ID available - need phase creation first")
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
                print(f"✅ Successfully loaded project plan page")
            elif response.status_code == 401:
                response.failure("Authentication failed")
                print(f"❌ Authentication failed for project plan")
            elif response.status_code == 403:
                response.failure("Access denied")
                print(f"❌ Access denied for project plan")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                print(f"⚠️ Unexpected response: {response.status_code} for {url}")
    
    @task(3)  # Additional view tasks for different perspectives
    def view_project_plan_board(self):
        """Test viewing the project plan in board view"""
        if not self.test_project_id or not self.test_phase_id:
            print(f"⚠️ Missing project or phase ID for board view")
            return
            
        endpoint = f"/project/{self.test_project_id}/plan"
        params = {
            'phase': self.test_phase_id,
            'view': 'board'  # Board view instead of list
        }
        
        url = f"{endpoint}?phase={params['phase']}&view={params['view']}"
        
        with self.client.get(url, catch_response=True, name="view_project_plan_board") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Successfully loaded project plan board view")
            else:
                response.failure(f"Board view failed: {response.status_code}")
                print(f"⚠️ Board view failed: {response.status_code}")
    
    @task(2)  # Lower weight for general project view without phase
    def view_project_overview(self):
        """Test viewing the project overview/general view"""
        if not self.test_project_id:
            print(f"⚠️ No project ID available for overview")
            return
            
        # Project overview without specific phase
        url = f"/project/{self.test_project_id}/plan"
        
        with self.client.get(url, catch_response=True, name="view_project_overview") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Successfully loaded project overview")
            else:
                response.failure(f"Project overview failed: {response.status_code}")
                print(f"⚠️ Project overview failed: {response.status_code}")


# Standalone execution capability
if __name__ == "__main__":
    print("🚀 Running Project View Tests independently...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectViewTest
        env = Environment(user_classes=[ProjectViewTest])
        user = ProjectViewTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for project view tests")
            
            # Check if we have required IDs
            if user.test_project_id:
                print(f"🔍 Using project ID: {user.test_project_id}")
                
                if user.test_phase_id:
                    print(f"🔍 Using phase ID: {user.test_phase_id}")
                    
                    # Test project plan viewing
                    try:
                        user.view_project_plan()
                        print("🎉 Project plan view test: PASSED")
                        
                        user.view_project_plan_board()
                        print("🎉 Project board view test: PASSED")
                        
                        user.view_project_overview()
                        print("🎉 Project overview test: PASSED")
                    except Exception as e:
                        print(f"❌ Project view tests: {e}")
                else:
                    print("⚠️ No phase ID available - limited testing")
                    try:
                        user.view_project_overview()
                        print("🎉 Project overview test: PASSED")
                    except Exception as e:
                        print(f"❌ Project overview test: {e}")
            else:
                print("⚠️ No project ID available - set PROJECT_ID environment variable")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        print("Set PROJECT_ID and PHASE_ID environment variables for full testing") 