#!/usr/bin/env python3
"""
Example Load Test Script using auth.py Authentication
Demonstrates how to use the AuthenticatedUser class for load testing
"""

from locust import task, between
from common.auth import AuthenticatedUser

class ExampleLoadTest(AuthenticatedUser):
    """
    Example load test that extends the AuthenticatedUser class.
    
    This inherits all authentication functionality and automatically
    authenticates users when they start.
    """
    
    wait_time = between(2, 5)  # Wait 2-5 seconds between tasks
    
    @task(3)  # Weight of 3 - this task will run 3x more often
    def view_projects(self):
        """Test viewing the projects page"""
        with self.client.get("/projects", catch_response=True, name="view_projects") as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status {response.status_code}")
    
    @task(2)  # Weight of 2 
    def get_session_info(self):
        """Test getting session information via API"""
        response = self.make_authenticated_request('GET', '/auth/session')
        
        if response.status_code == 200:
            print("✅ Session API call successful")
        else:
            print(f"⚠️ Session API call failed: {response.status_code}")
    
    @task(1)  # Weight of 1 - least frequent
    def view_dashboard(self):
        """Test viewing dashboard if available"""
        with self.client.get("/dashboard", catch_response=True, name="view_dashboard") as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 404:
                response.success()  # Dashboard might not exist, that's OK
            else:
                response.failure(f"Unexpected status {response.status_code}")
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"User {self.login_email} is ready for testing")
    
    def on_stop(self):
        """Called when user stops"""
        print(f"User {self.login_email} finished testing")

# Additional example class for API-focused testing
class APILoadTest(AuthenticatedUser):
    """
    Example focused on API endpoint testing
    """
    
    wait_time = between(1, 3)
    
    @task
    def api_health_check(self):
        """Test API health endpoint"""
        response = self.make_authenticated_request('GET', '/api/health')
        
        if response.status_code == 200:
            print("✅ API health check passed")
        else:
            print(f"⚠️ API health check failed: {response.status_code}")
    
    @task  
    def test_session_endpoint(self):
        """Test the session endpoint specifically"""
        response = self.make_authenticated_request('GET', '/auth/session')
        
        # Verify we get JSON back
        try:
            if response.status_code == 200:
                import json
                session_data = json.loads(response.text)
                if 'user' in session_data or 'accessToken' in session_data:
                    print("✅ Session data looks valid")
                else:
                    print("⚠️ Session data missing expected fields")
        except json.JSONDecodeError:
            print("⚠️ Session response is not valid JSON")

if __name__ == "__main__":
    # Test the load test classes directly
    print("Testing authentication and basic functionality...")
    
    try:
        from locust.env import Environment
        
        # Test ExampleLoadTest
        env = Environment(user_classes=[ExampleLoadTest])
        user = ExampleLoadTest(env)
        
        if user.is_authenticated:
            print("🎉 ExampleLoadTest authentication: PASSED")
            
            # Test a few methods
            user.view_projects()
            user.get_session_info()
            
        else:
            print("❌ ExampleLoadTest authentication: FAILED")
            
    except Exception as e:
        print(f"Error testing: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST") 