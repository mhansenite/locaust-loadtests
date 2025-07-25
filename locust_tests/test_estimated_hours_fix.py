#!/usr/bin/env python3
"""
Simple test to verify estimated hours update fix
"""

import sys
import os
import json
import time

# Add parent directory to path to import from common
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.auth import AuthenticatedUser

class EstimatedHoursTest(AuthenticatedUser):
    """Simple test for estimated hours update functionality"""
    
    host = os.getenv('LOCUST_HOST', 'https://app.staging.guidecx.io')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_project_id = os.getenv('PROJECT_ID', "e34b9b43-fa9f-4a09-a3bf-1178f471a5dc")
        self.test_phase_id = os.getenv('PHASE_ID', "e3a7477d-a774-436f-9ae0-4a75d8ff6fe8")
        self.created_tasks = []
        self.created_milestones = []
        self.created_phases = []
    
    def test_estimated_hours_update(self):
        """Test the estimated hours update on an existing task"""
        
        # For this test, we'll use a known task ID from your project
        # You can get this from the UI or create a task first
        
        print("🧪 Testing Estimated Hours Update Fix")
        print(f"📂 Using Project: {self.test_project_id}")
        print(f"📁 Using Phase: {self.test_phase_id}")
        
        # First, let's create a task to test with
        task_id, task_name = self._create_test_task()
        
        if task_id:
            print(f"✅ Created test task: {task_name} (ID: {task_id})")
            
            # Test the estimated hours update
            success = self._update_task_estimated_hours(task_id, task_name)
            
            if success:
                print("🎉 Estimated hours update test: PASSED")
                print("🔍 Check the UI to verify the estimated hours are visible!")
            else:
                print("❌ Estimated hours update test: FAILED")
        else:
            print("❌ Could not create test task")
    
    def _create_test_task(self):
        """Create a simple test task"""
        import uuid
        
        try:
            # Create a unique task name
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            task_name = f"EstHoursTest-{timestamp}-{unique_id}"
            
            # First, we need a milestone to attach the task to
            milestone_id = self._create_test_milestone()
            if not milestone_id:
                print("❌ Could not create test milestone")
                return None, None
            
            # Create task payload
            task_payload = json.dumps([{
                "name": task_name,
                "parentId": {"uuid": milestone_id}
            }])
            
            task_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': self.test_phase_id,
                'view': 'board'
            }
            
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': '343a58a42088e8b2fca6b83aa952bd173682c1a1',
            }
            
            response = self.client.post(
                task_url,
                params=params,
                data=task_payload,
                headers=headers
            )
            
            if response.status_code == 200:
                # Extract task ID from response
                import re
                json_match = re.search(r'1:\{\"response\":\{\"task\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                if json_match:
                    task_id = json_match.group(1)
                    # Track the task
                    self.created_tasks.append({
                        'id': task_id,
                        'name': task_name,
                        'milestone_id': milestone_id,
                        'milestone_name': 'TestMilestone'
                    })
                    return task_id, task_name
                    
        except Exception as e:
            print(f"❌ Error creating test task: {e}")
            
        return None, None
    
    def _create_test_milestone(self):
        """Create a simple test milestone"""
        import uuid
        
        try:
            # Create unique milestone name
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            milestone_name = f"EstHoursTestMilestone-{timestamp}-{unique_id}"
            
            milestone_payload = json.dumps([{
                "name": milestone_name,
                "phaseId": {"uuid": self.test_phase_id}
            }])
            
            milestone_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': self.test_phase_id,
                'view': 'board'
            }
            
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5',
            }
            
            response = self.client.post(
                milestone_url,
                params=params,
                data=milestone_payload,
                headers=headers
            )
            
            if response.status_code == 200:
                # Extract milestone ID from response
                import re
                json_match = re.search(r'1:\{\"response\":\{\"milestone\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                if json_match:
                    milestone_id = json_match.group(1)
                    # Track the milestone
                    self.created_milestones.append({
                        'id': milestone_id,
                        'name': milestone_name,
                        'phase_id': self.test_phase_id
                    })
                    return milestone_id
                    
        except Exception as e:
            print(f"❌ Error creating test milestone: {e}")
            
        return None
    
    def _update_task_estimated_hours(self, task_id, task_name):
        """Update a task's estimated hours using the corrected API"""
        import json
        
        try:
            # Test with 8 hours
            estimated_hours = 8
            
            print(f"🔄 TESTING ESTIMATED HOURS UPDATE")
            print(f"🔄 Task: {task_name}")
            print(f"🔄 Setting estimated hours to: {estimated_hours}h")
            print(f"🔄 Task ID: {task_id}")
            
            # Get the correct phase for this task
            task_phase_id = self.test_phase_id  # default
            for task_info in self.created_tasks:
                if task_info['id'] == task_id:
                    milestone_id = task_info.get('milestone_id')
                    if milestone_id:
                        for milestone_info in self.created_milestones:
                            if milestone_info['id'] == milestone_id:
                                task_phase_id = milestone_info['phase_id']
                                print(f"🔍 Found task in phase: {task_phase_id}")
                                break
                    break
            
            # Use EXACT format from HAR
            update_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': task_phase_id,
                'view': 'board',
                'task-id': task_id,  # CRITICAL: Required for task context
                'task-drawer-tab': 'details'  # CRITICAL: Required for details context
            }
            
            update_payload = json.dumps([{
                "id": {"uuid": task_id},
                "estimatedHours": estimated_hours
            }])
            
            print(f"🔄 Request URL: {update_url}")
            print(f"🔄 Request params: {params}")
            print(f"🔄 Request payload: {update_payload}")
            
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': '5c0018c251e1f4df53ca01c659f4c781d2468788',  # From HAR
                'Next-Router-State-Tree': f'%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22{self.test_project_id}%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F{self.test_project_id}%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            response = self.client.post(
                update_url,
                params=params,
                data=update_payload,
                headers=headers
            )
            
            print(f"📝 RESPONSE STATUS: {response.status_code}")
            print(f"📝 RESPONSE BODY: {response.text[:500]}...")
            
            if response.status_code == 200:
                response_text = response.text
                
                # Check for successful update patterns from HAR
                if '"error":null' in response_text and '"status":0' in response_text:
                    if 'estimatedHours' in response_text or '"message":""' in response_text:
                        print(f"✅ Successfully updated estimated hours to {estimated_hours}h")
                        print(f"✅ Response matches successful HAR pattern")
                        return True
                    else:
                        print(f"⚠️ Update may have succeeded but response format unexpected")
                        print(f"⚠️ Expected estimatedHours or empty message, got: {response_text[:200]}")
                        return False
                else:
                    print(f"❌ Response indicates error: {response_text[:200]}")
                    return False
            else:
                print(f"❌ API call failed: {response.status_code}")
                print(f"❌ Error response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Exception updating estimated hours: {e}")
            import traceback
            traceback.print_exc()
            return False

# Test runner
if __name__ == "__main__":
    print("🧪 Testing Estimated Hours Update Fix...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        env = Environment(user_classes=[EstimatedHoursTest])
        user = EstimatedHoursTest(env)
        
        if user.is_authenticated:
            print("✅ Authentication successful")
            user.test_estimated_hours_update()
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc() 