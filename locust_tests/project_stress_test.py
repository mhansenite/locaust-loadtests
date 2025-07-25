#!/usr/bin/env python3
"""
Project Stress Test
Rapid stress testing for project, phase and milestone creation

This is a separate stress test module that focuses on rapid creation
and high-frequency operations to test system limits and performance
under load.
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

class ProjectStressTest(AuthenticatedUser):
    """
    Stress test for rapid project, phase and milestone creation.
    Uses environment variables for project lifecycle management.
    
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
    export PROJECT_NAME_TXT="StressProject"
    export CREATE_NEW_PHASE="true"
    export TEST_PHASE_NAME="StressPhase"
    export TEST_MILESTONE_NAME="StressMilestone"
    export TEST_TASK_NAME="StressTask"
    export LOGIN_EMAIL="your-email@example.com"
    export LOGIN_PASSWORD="your-password"
    export LOCUST_HOST="https://app.staging.guidecx.io"
    
    locust -f locust_tests/project_stress_test.py --users 10 --spawn-rate 2
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
            print(f"🔄 Stress: CREATE_NEW_PROJECT=true: Will create new project")
        else:
            self.test_project_id = self.PROJECT_ID  # Use existing project
            print(f"📂 Stress: Using existing project: {self.PROJECT_ID}")
        
        # Phase ID management based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            self.test_phase_id = None  # Force creation of new phase
            print(f"🔄 Stress: CREATE_NEW_PHASE=true: Will create new phase (ignoring PHASE_ID)")
        else:
            self.test_phase_id = self.PHASE_ID  # Use existing phase if provided
        
        print(f"🚀 Starting stress test")
    
    def create_stress_test_project(self):
        """Create a test project for stress testing - simplified version"""
        try:
            # Create a unique project name for stress testing
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            project_name = f"{self.PROJECT_NAME_TXT}-stress-{timestamp}-{unique_id}"
            
            # Use same API as main test
            project_payload = json.dumps([{}])
            
            headers = {
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': '83cef14cae8a2ba4da184ad4fb26161dd04c149c',
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            create_url = "/v2/projects"
            
            print(f"🔧 Stress: Creating project using quick create API...")
            
            response = self.client.post(
                create_url,
                data=project_payload,
                headers=headers,
                name="create_stress_project"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress: Successfully called project creation API")
                
                # Try to extract project ID from response
                project_id = self._extract_project_id_from_response(response.text)
                if project_id:
                    self.test_project_id = project_id
                    print(f"🔗 Stress: Set test_project_id to: {project_id}")
                    
                    # Track created project for cleanup
                    self.created_projects.append({
                        'id': project_id,
                        'name': project_name
                    })
                    print(f"🗂️ Stress: Tracked project for cleanup: {project_id} ({project_name})")
                else:
                    print(f"⚠️ Stress: Could not extract project ID from response")
                    self.test_project_id = self.PROJECT_ID  # Fallback
            else:
                print(f"⚠️ Stress: Project creation failed: {response.status_code}")
                self.test_project_id = self.PROJECT_ID  # Fallback
                
        except Exception as e:
            print(f"💥 Stress: Exception in create_stress_test_project: {e}")
            self.test_project_id = self.PROJECT_ID  # Fallback
    
    def create_stress_test_phase(self):
        """Create a test phase for stress testing - simplified version"""
        try:
            # Create a unique phase name for stress testing
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            phase_name = f"{self.TEST_PHASE_NAME}-stress-{timestamp}-{unique_id}"
            
            # Use the existing phase from environment or default
            current_phase_id = self.PHASE_ID or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Construct the phase creation URL
            create_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': current_phase_id,
                'view': 'board'
            }
            
            # Create the payload - exact format from HAR
            phase_payload = json.dumps([{
                "projectId": {"uuid": self.test_project_id},
                "name": phase_name
            }])
            
            # Set up headers based on HAR analysis
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': '5955c4c2ae46e596cde573a76ce226e64e73fb9a',
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            print(f"🔧 Stress: Creating phase directly: '{phase_name}' in project: {self.test_project_id}")
            
            response = self.client.post(
                create_url,
                params=params,
                data=phase_payload,
                headers=headers,
                name="create_stress_phase"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress: Successfully created phase: '{phase_name}'")
                
                # Try to extract phase ID from response
                phase_id = self._extract_phase_id_from_response(response.text)
                if phase_id:
                    if not self.test_phase_id:
                        self.test_phase_id = phase_id
                        print(f"🔗 Stress: Set test_phase_id to: {phase_id}")
                    
                    # Always track created phases
                    self.created_phases.append({
                        'id': phase_id,
                        'name': phase_name,
                        'projectId': self.test_project_id
                    })
                    print(f"🗂️ Stress: Tracked phase ID: {phase_id}")
                else:
                    print(f"⚠️ Stress: Could not extract phase ID from response")
            else:
                print(f"❌ Stress: Phase creation failed: {response.status_code}")
                
        except Exception as e:
            print(f"💥 Stress: Exception in create_stress_test_phase: {e}")
    
    def _extract_project_id_from_response(self, response_text):
        """Extract project ID from response - same as main class"""
        try:
            lines = response_text.strip().split('\n')
            for line in lines:
                if line.startswith('1:') and 'projectId' in line and 'uuid' in line:
                    try:
                        json_part = line[2:]
                        data = json.loads(json_part)
                        
                        if 'response' in data and 'projectId' in data['response']:
                            project_data = data['response']['projectId']
                            if 'uuid' in project_data:
                                project_id = project_data['uuid']
                                print(f"🎯 Stress: Extracted project ID from response: {project_id}")
                                return project_id
                    except (json.JSONDecodeError, KeyError) as e:
                        continue
            
            # Fallback: try to find any UUID pattern
            project_id_pattern = r'"projectId":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
            matches = re.findall(project_id_pattern, response_text)
            
            if matches:
                project_id = matches[0]
                print(f"🎯 Stress: Extracted project ID via regex: {project_id}")
                return project_id
                        
        except Exception as e:
            print(f"⚠️ Stress: Error extracting project ID: {e}")
            
        return None
    
    def _extract_phase_id_from_response(self, response_text):
        """Extract phase ID from the Next.js server action response - same as main class"""
        try:
            lines = response_text.strip().split('\n')
            for line in lines:
                if line.startswith('1:') and 'phase' in line and 'uuid' in line:
                    try:
                        json_part = line[2:]
                        data = json.loads(json_part)
                        
                        if 'response' in data and 'phase' in data['response']:
                            phase_data = data['response']['phase']
                            if 'id' in phase_data and 'uuid' in phase_data['id']:
                                return phase_data['id']['uuid']
                    except (json.JSONDecodeError, KeyError) as e:
                        continue
            
            # Fallback: try to find any UUID pattern
            uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
            matches = re.findall(uuid_pattern, response_text.lower())
            
            if matches:
                return matches[-1]
                
        except Exception as e:
            print(f"⚠️ Stress: Error extracting phase ID: {e}")
            
        return None
    
    @task(8)  # Highest frequency for stress task creation
    def create_stress_task(self):
        """Stress test creating tasks under milestones"""
        # Import required modules at the start
        import json
        import re
        
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 Stress: No project ID available, creating project first...")
                self.create_stress_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Stress: Project creation failed, cannot create task")
                    return
            else:
                print(f"⚠️ Stress: No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            print(f"🔗 Stress: No phase ID available, creating phase first...")
            self.create_stress_test_phase()
            if not self.test_phase_id:
                print(f"⚠️ Stress: Phase creation failed, cannot create task")
                return
        
        # Ensure we have a milestone to attach the task to
        if not self.created_milestones:
            print(f"🔗 Stress: No milestones available, creating milestone first...")
            self.create_stress_milestone()
            if not self.created_milestones:
                print(f"⚠️ Stress: Milestone creation failed, cannot create task")
                return
        
        # Use the most recent milestone as the parent
        milestone_id = self.created_milestones[-1]['id']
        milestone_name = self.created_milestones[-1]['name']
        
        # Create a unique task name for stress testing
        timestamp = int(time.time() * 1000)  # More granular timestamp for stress testing
        random_id = uuid.uuid4().hex[:6]
        task_name = f"stress-{self.TEST_TASK_NAME}-{timestamp}-{random_id}"
        
        # Use the same API as the main test
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
            'Next-Action': '343a58a42088e8b2fca6b83aa952bd173682c1a1',  # From createingatask.har
            'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
        }
        
        print(f"📝 Stress: Creating task '{task_name}' under milestone '{milestone_name}' ({milestone_id})")
        
        with self.client.post(
            task_url,
            params=params,
            data=task_payload,
            headers=headers,
            catch_response=True,
            name="create_stress_task"
        ) as response:
            if response.status_code == 200:
                response.success()
                
                try:
                    if 'task' in response.text and 'response' in response.text:
                        json_match = re.search(r'1:\{\"response\":\{\"task\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                        if json_match:
                            task_id = json_match.group(1)
                            print(f"✅ Stress: Successfully created task '{task_name}' with ID: {task_id}")
                            
                            self.created_tasks.append({
                                'id': task_id,
                                'name': task_name,
                                'milestone_id': milestone_id,
                                'milestone_name': milestone_name
                            })
                            self.created_items.append(f"task:{task_id}")
                            
                        else:
                            print(f"⚠️ Stress: Task created but couldn't extract ID from response")
                    else:
                        print(f"⚠️ Stress: Unexpected task creation response: {response.text[:200]}")
                        
                except Exception as e:
                    print(f"⚠️ Stress: Error parsing task creation response: {e}")
                    
            else:
                response.failure(f"Stress task creation failed: {response.status_code} - {response.text[:200]}")
                print(f"❌ Stress: Failed to create task: {response.status_code} - {response.text[:200]}")

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
            # Generate unique test milestone
            timestamp = int(time.time() * 1000)  # More granular timestamp
            random_id = uuid.uuid4().hex[:6]
            milestone_name = f"stress-{self.TEST_MILESTONE_NAME}-{timestamp}-{random_id}"
            
            # Create milestone payload
            milestone_payload = json.dumps([{
                "name": milestone_name,
                "phaseId": {"uuid": self.test_phase_id}
            }])
            
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5',  # From CreateMilestone.har
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            milestone_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': self.test_phase_id,
                'view': 'board'
            }
            
            with self.client.post(
                milestone_url,
                params=params,
                data=milestone_payload,
                headers=headers,
                catch_response=True,
                name="create_stress_milestone"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    print(f"✅ Stress: Successfully created milestone '{milestone_name}'")
                    
                    # Parse the response to get the milestone ID
                    try:
                        if 'milestone' in response.text and 'response' in response.text:
                            json_match = re.search(r'1:\{\"response\":\{\"milestone\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                            if json_match:
                                milestone_id = json_match.group(1)
                                print(f"✅ Stress: Successfully created milestone '{milestone_name}' with ID: {milestone_id}")
                                
                                # Store the created milestone for tracking
                                self.created_milestones.append({
                                    'id': milestone_id,
                                    'name': milestone_name,
                                    'phase_id': self.test_phase_id
                                })
                                self.created_items.append(f"milestone:{milestone_id}")
                                
                            else:
                                print(f"⚠️ Stress: Milestone created but couldn't extract ID from response")
                        else:
                            print(f"⚠️ Stress: Unexpected milestone creation response: {response.text[:200]}")
                            
                    except Exception as e:
                        print(f"⚠️ Stress: Error parsing milestone creation response: {e}")
                        
                else:
                    response.failure(f"Stress milestone creation failed: {response.status_code} - {response.text[:200]}")
                    print(f"❌ Stress: Failed to create milestone: {response.status_code} - {response.text[:200]}")
                
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
            # Generate unique test phase
            timestamp = int(time.time() * 1000)
            random_id = uuid.uuid4().hex[:6]
            phase_name = f"stress-{self.TEST_PHASE_NAME}-{timestamp}-{random_id}"
            
            # Use the existing phase from environment or default for context
            current_phase_id = self.PHASE_ID or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Create phase payload
            phase_payload = json.dumps([{
                "projectId": {"uuid": self.test_project_id},
                "name": phase_name
            }])
            
            headers = {
                'Content-Type': 'text/plain;charset=UTF-8',
                'Accept': 'text/x-component',
                'Next-Action': '5955c4c2ae46e596cde573a76ce226e64e73fb9a',
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            create_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': current_phase_id,
                'view': 'board'
            }
            
            with self.client.post(
                create_url,
                params=params,
                data=phase_payload,
                headers=headers,
                catch_response=True,
                name="create_stress_phase_task"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    print(f"✅ Stress: Successfully created phase '{phase_name}'")
                    
                    # Try to extract phase ID for milestone creation
                    phase_id = self._extract_phase_id_from_response(response.text)
                    if phase_id:
                        if not self.test_phase_id:
                            self.test_phase_id = phase_id
                            print(f"🔗 Stress: Set test_phase_id to: {phase_id}")
                        
                        # Always track created phases
                        self.created_phases.append({
                            'id': phase_id,
                            'name': phase_name,
                            'projectId': self.test_project_id
                        })
                        self.created_items.append(f"phase:{phase_id}")
                        print(f"🗂️ Stress: Tracked phase ID: {phase_id}")
                    else:
                        print(f"⚠️ Stress: Could not extract phase ID from response")
                        
                else:
                    response.failure(f"Stress phase creation failed: {response.status_code} - {response.text[:200]}")
                    print(f"❌ Stress: Failed to create phase: {response.status_code} - {response.text[:200]}")
                
        except Exception as e:
            print(f"❌ Stress test phase error: {e}")
    
    def delete_stress_test_project(self, project_id):
        """Delete a stress test project using the pattern from DeleteProject.har"""
        try:
            # Project deletion payload based on DeleteProject.har analysis
            delete_payload = json.dumps([{
                "projectIds": [{"uuid": project_id}]
            }])
            
            # Headers from DeleteProject.har
            headers = {
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': '0a17c17cfd2792b0b228f1f194c95d78f6cb5330',  # From HAR
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            # Project deletion URL (from DeleteProject.har)
            delete_url = "/v2/projects"
            
            print(f"🗑️ Stress: Deleting project: {project_id}")
            
            with self.client.post(
                delete_url,
                data=delete_payload,
                headers=headers,
                catch_response=True,
                name="delete_stress_project"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    print(f"✅ Stress: Successfully deleted project: {project_id}")
                    return True
                else:
                    response.failure(f"Stress project deletion failed: {response.status_code}")
                    print(f"⚠️ Stress: Project deletion failed: {response.status_code}")
                    return False
                    
        except Exception as e:
            print(f"💥 Stress: Exception in delete_stress_test_project: {e}")
            return False
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting STRESS TEST for project phase/milestone creation")
        print(f"⚡ High-frequency, rapid creation patterns for load testing")
        
        # Show project configuration
        if self.CREATE_NEW_PROJECT:
            print(f"🔗 Stress Project: Will create NEW projects (CREATE_NEW_PROJECT=true)")
            print(f"📝 Stress Project Name: '{self.PROJECT_NAME_TXT}' (with stress timestamps)")
        else:
            print(f"🔗 Stress Project: Using existing project {self.test_project_id}")
        
        # Show phase configuration
        if self.CREATE_NEW_PHASE:
            print(f"🔗 Stress Phase: Will create NEW phases (CREATE_NEW_PHASE=true)")
        else:
            print(f"🔗 Stress Phase: Using existing phase {self.test_phase_id}")
        
        print(f"⚡ Stress Test Names: Phase='{self.TEST_PHASE_NAME}', Milestone='{self.TEST_MILESTONE_NAME}', Task='{self.TEST_TASK_NAME}'")
        print(f"🎯 Ready for high-frequency stress testing!")
    
    def on_stop(self):
        """Called when the stress test is stopping - cleanup created projects"""
        print(f"🛑 STRESS TEST completed for user: {self.login_email}")
        
        # Count created items for reporting
        projects_count = len(self.created_projects)
        phases_count = len(self.created_phases)
        milestones_count = len(self.created_milestones)
        tasks_count = len(self.created_tasks)
        total_items = len(self.created_items)
        
        print(f"📊 STRESS TEST RESULTS:")
        print(f"   🏗️ Created {projects_count} projects")
        print(f"   📋 Created {phases_count} phases")
        print(f"   🎯 Created {milestones_count} milestones")
        print(f"   📝 Created {tasks_count} tasks")
        print(f"   📦 Total items tracked: {total_items}")
        
        if self.CREATE_NEW_PROJECT and self.created_projects:
            print(f"🧹 Starting cleanup of {len(self.created_projects)} stress test projects...")
            for project_info in self.created_projects:
                project_id = project_info['id']
                project_name = project_info['name']
                print(f"🗑️ Attempting to delete stress project: {project_name} ({project_id})")
                
                # TEMPORARILY DISABLED - Comment out deletion for inspection
                # self.delete_stress_test_project(project_id)
                print(f"⚠️ DELETION DISABLED - Stress project preserved for inspection: {project_name} ({project_id})")
            
            print(f"🧹 Stress test cleanup SKIPPED - Projects preserved for inspection")
        else:
            print(f"📋 No stress projects to clean up (using existing project or no projects created)")
            
        print(f"🧹 Stress test lifecycle completed")


# Test runner for development
if __name__ == "__main__":
    # Test the stress test directly
    print("Testing Project Stress Test...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectStressTest
        env = Environment(user_classes=[ProjectStressTest])
        user = ProjectStressTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for stress tests")
            
            # Test project creation if CREATE_NEW_PROJECT=true
            if user.CREATE_NEW_PROJECT:
                try:
                    user.create_stress_test_project()
                    if user.test_project_id:
                        print("🎉 Stress project creation test: PASSED")
                        print(f"🔍 Created stress project ID: {user.test_project_id}")
                    else:
                        print("❌ Stress project creation test: FAILED")
                except Exception as e:
                    print(f"❌ Stress project creation test: {e}")
            
            # Test stress milestone creation
            try:
                user.create_stress_milestone()
                print("🎉 Stress milestone creation test: PASSED")
                print("🔍 Check your project plan - you should see a new stress milestone!")
            except Exception as e:
                print(f"❌ Stress milestone creation test: {e}")
                
            # Test stress task creation
            try:
                user.create_stress_task()
                print("🎉 Stress task creation test: PASSED")
                print("🔍 Check your project plan - you should see a new stress task!")
            except Exception as e:
                print(f"❌ Stress task creation test: {e}")
                
            # Test cleanup if project was created
            if user.CREATE_NEW_PROJECT and user.created_projects:
                try:
                    print("🧹 Testing stress project cleanup...")
                    for project in user.created_projects:
                        success = user.delete_stress_test_project(project['id'])
                        if success:
                            print(f"🎉 Stress project deletion test: PASSED for {project['name']}")
                        else:
                            print(f"❌ Stress project deletion test: FAILED for {project['name']}")
                except Exception as e:
                    print(f"❌ Stress project deletion test: {e}")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Stress test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        print("Also set environment variables for the stress test configuration")
        print("\nEnvironment Variables for Stress Testing:")
        print("  CREATE_NEW_PROJECT: Set to 'true' to create new projects, 'false' to use existing PROJECT_ID")
        print("  PROJECT_NAME_TXT: Base name for stress test projects (will have timestamps)")
        print("  PROJECT_ID: Project UUID to use when CREATE_NEW_PROJECT=false")
        print("  CREATE_NEW_PHASE: Set to 'true' to create new phases, 'false' to use existing PHASE_ID")
        print("  PHASE_ID: Phase UUID to use when CREATE_NEW_PHASE=false")
        print("  TEST_PHASE_NAME: Name for stress test phases")
        print("  TEST_MILESTONE_NAME: Name for stress test milestones")
        print("  TEST_TASK_NAME: Name for stress test tasks")
        print("  LOGIN_EMAIL: Email for authentication")
        print("  LOGIN_PASSWORD: Password for authentication")
        print("  LOCUST_HOST: Target host URL")
        print("\nExample stress test usage:")
        print("  # Stress test with new project creation:")
        print('  CREATE_NEW_PROJECT="true" PROJECT_NAME_TXT="StressProject" CREATE_NEW_PHASE="true" TEST_PHASE_NAME="StressPhase" TEST_MILESTONE_NAME="StressMilestone" TEST_TASK_NAME="StressTask" LOGIN_EMAIL="your-email@example.com" LOGIN_PASSWORD="your-password" LOCUST_HOST="https://app.staging.guidecx.io" locust -f locust_tests/project_stress_test.py --users 10 --spawn-rate 2')
        print("  # Stress test with existing project:")
        print('  CREATE_NEW_PROJECT="false" PROJECT_ID=existing-project-id CREATE_NEW_PHASE="false" PHASE_ID=existing-phase-id locust -f locust_tests/project_stress_test.py --users 5 --spawn-rate 1') 