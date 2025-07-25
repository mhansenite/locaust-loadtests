#!/usr/bin/env python3
"""
Task Creation Test Module
Extracted from project_cr_phase_milestone.py - Tasks/Create functionality

Can run standalone:
  locust -f TestFiles/Tasks/Create/task_create_test.py --users 5 --spawn-rate 1

Or imported by master controller
"""

import sys
import os
import json
import time
import uuid
import re
import random
from locust import task, between

# Import base template
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from TestFiles.base_test_template import BaseTestTemplate

class TaskCreateTest(BaseTestTemplate):
    """
    Task creation test module
    Extracted from original project_cr_phase_milestone.py
    """
    
    @task(5)  # Balanced weight for task creation (each call creates 1-10 tasks)
    def create_task(self):
        """Test creating 1-10 random tasks under a milestone"""
        # Import required modules at the start
        import json
        import re
        
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 No project ID available, creating project first...")
                # Note: In standalone mode, this would need coordination
                # In master controller mode, this will be handled by shared state
                print(f"⚠️ Project creation needed - run with master controller or set PROJECT_ID")
                return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            # If no phase ID, we need a phase first
            print(f"🔗 No phase ID available, need phase creation first")
            return
        
        # Ensure we have a milestone to attach the task to
        if not self.created_milestones:
            print(f"🔗 No milestones available, need milestone creation first")
            return
        
        # Randomly select a milestone for realistic distribution across phases
        selected_milestone = random.choice(self.created_milestones)
        milestone_id = selected_milestone['id']
        milestone_name = selected_milestone['name']
        milestone_phase_id = selected_milestone['phase_id']
        
        print(f"🎲 Randomly selected milestone: '{milestone_name}' in phase {milestone_phase_id}")
        
        # 🎯 Create random number of tasks (1-10) for this milestone
        num_tasks = random.randint(1, 10)
        print(f"📋 Creating {num_tasks} tasks for milestone '{milestone_name}'")
        
        tasks_created = 0
        for i in range(num_tasks):
            # Create a unique task name for each task
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            task_suffix = f"-{i+1}" if num_tasks > 1 else ""
            task_name = f"{self.TEST_TASK_NAME}-{timestamp}-{unique_id}{task_suffix}"
            
            # Based on createingatask.har analysis, the correct task creation API is:
            # POST /project/{projectId}/plan?phase={phaseId}&view=board
            # with payload: [{"name":"task_name","parentId":{"uuid":"milestone_id"}}]
            
            task_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': milestone_phase_id,
                'view': 'board'
            }
            
            # Create the task payload - exact format from createingatask.har
            task_payload = json.dumps([{
                "name": task_name,
                "parentId": {"uuid": milestone_id}
            }])
            
            # Set up headers based on createingatask.har analysis
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': '343a58a42088e8b2fca6b83aa952bd173682c1a1',  # From createingatask.har
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            print(f"📝 Creating task {i+1}/{num_tasks}: '{task_name}' under milestone '{milestone_name}' ({milestone_id})")
            
            with self.client.post(
                task_url,
                params=params,
                data=task_payload,
                headers=headers,
                catch_response=True,
                name="create_task_batch"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    
                    # Parse the response to get the task ID
                    try:
                        # Look for task creation confirmation in response
                        if 'task' in response.text and 'response' in response.text:
                            
                            # Extract task ID from response
                            json_match = re.search(r'1:\{\"response\":\{\"task\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                            if json_match:
                                task_id = json_match.group(1)
                                print(f"  ✅ Successfully created task {i+1}/{num_tasks}: '{task_name}' with ID: {task_id}")
                                
                                # Store the created task for tracking
                                self.created_tasks.append({
                                    'id': task_id,
                                    'name': task_name,
                                    'milestone_id': milestone_id,
                                    'milestone_name': milestone_name
                                })
                                
                                tasks_created += 1
                                
                            else:
                                print(f"  ⚠️ Task {i+1}/{num_tasks} created but couldn't extract ID from response")
                        else:
                            print(f"  ⚠️ Unexpected task creation response for task {i+1}/{num_tasks}: {response.text[:100]}")
                            
                    except Exception as e:
                        print(f"  ⚠️ Error parsing task creation response for task {i+1}/{num_tasks}: {e}")
                        
                else:
                    response.failure(f"Failed to create task {i+1}/{num_tasks}: {response.status_code} - {response.text[:200]}")
                    print(f"  ❌ Failed to create task {i+1}/{num_tasks}: {response.status_code} - {response.text[:100]}")
                    
                # Small delay between tasks to avoid overwhelming the server
                time.sleep(0.1)
        
        print(f"🎉 Task batch complete: Created {tasks_created}/{num_tasks} tasks for milestone '{milestone_name}'")
    
    def _create_single_task(self, milestone_id, milestone_name, task_suffix=""):
        """Helper method to create a single task under a milestone"""
        import json
        import re
        
        # Create a unique task name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        task_name = f"{self.TEST_TASK_NAME}-{timestamp}-{unique_id}{task_suffix}"
        
        # Based on createingatask.har analysis
        task_url = f"/project/{self.test_project_id}/plan"
        params = {
            'phase': self.test_phase_id,
            'view': 'board'
        }
        
        task_payload = json.dumps([{
            "name": task_name,
            "parentId": {"uuid": milestone_id}
        }])
        
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': 'text/x-component',
            'Next-Action': '343a58a42088e8b2fca6b83aa952bd173682c1a1',
            'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
        }
        
        with self.client.post(
            task_url,
            params=params,
            data=task_payload,
            headers=headers,
            catch_response=True,
            name="create_task_batch"
        ) as response:
            if response.status_code == 200:
                response.success()
                
                try:
                    if 'task' in response.text and 'response' in response.text:
                        json_match = re.search(r'1:\{\"response\":\{\"task\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                        if json_match:
                            task_id = json_match.group(1)
                            
                            # Store the created task for tracking
                            self.created_tasks.append({
                                'id': task_id,
                                'name': task_name,
                                'milestone_id': milestone_id,
                                'milestone_name': milestone_name
                            })
                            return task_id, task_name
                            
                except Exception as e:
                    print(f"⚠️ Error parsing task creation response: {e}")
            else:
                response.failure(f"Failed to create task: {response.status_code}")
                
        return None, None
    
    @task(3)  # Secondary task for single task creation
    def create_single_task_for_random_milestone(self):
        """Create a single task for a randomly selected milestone"""
        if not self.created_milestones:
            print(f"⚠️ No milestones available for single task creation")
            return
        
        # Randomly select a milestone
        selected_milestone = random.choice(self.created_milestones)
        milestone_id = selected_milestone['id']
        milestone_name = selected_milestone['name']
        
        print(f"📝 Creating single task for milestone: '{milestone_name}'")
        
        task_id, task_name = self._create_single_task(milestone_id, milestone_name, "-single")
        
        if task_id:
            print(f"✅ Successfully created single task: '{task_name}' ({task_id[:8]}...)")
        else:
            print(f"❌ Failed to create single task for milestone: '{milestone_name}'")


# Standalone execution capability
if __name__ == "__main__":
    print("🚀 Running Task Creation Tests independently...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test TaskCreateTest
        env = Environment(user_classes=[TaskCreateTest])
        user = TaskCreateTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for task creation tests")
            
            # Check if we have required IDs and milestones
            if user.test_project_id and user.test_phase_id:
                print(f"🔍 Using project ID: {user.test_project_id}")
                print(f"🔍 Using phase ID: {user.test_phase_id}")
                
                # For standalone testing, we need to manually add some milestones
                print("⚠️ For standalone testing, creating mock milestones...")
                user.created_milestones = [
                    {
                        'id': 'mock-milestone-1',
                        'name': 'Mock Milestone 1',
                        'phase_id': user.test_phase_id
                    },
                    {
                        'id': 'mock-milestone-2', 
                        'name': 'Mock Milestone 2',
                        'phase_id': user.test_phase_id
                    }
                ]
                
                # Test task creation
                try:
                    user.create_task()
                    if user.created_tasks:
                        print("🎉 Task creation test: PASSED")
                        print(f"🔍 Created tasks: {len(user.created_tasks)}")
                        for task in user.created_tasks[:3]:  # Show first 3
                            print(f"   • {task['name']} (ID: {task['id'][:8]}...)")
                    else:
                        print("❌ Task creation test: FAILED")
                        
                    # Test single task creation
                    user.create_single_task_for_random_milestone()
                    print(f"🎉 Single task creation test: PASSED")
                    print(f"🔍 Total created tasks: {len(user.created_tasks)}")
                except Exception as e:
                    print(f"❌ Task creation tests: {e}")
            else:
                print("⚠️ Missing project or phase ID - set PROJECT_ID and PHASE_ID environment variables")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        print("Set PROJECT_ID and PHASE_ID environment variables for testing") 