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
from locust import task, between

# Add parent directory to path to import from common
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.auth import AuthenticatedUser

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
    
    locust -f locust_tests/project_cr_phase_milestone.py --users 5 --spawn-rate 1
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
            print(f"🔄 CREATE_NEW_PROJECT=true: Will create new project")
        else:
            self.test_project_id = self.PROJECT_ID  # Use existing project
            print(f"📂 Using existing project: {self.PROJECT_ID}")
        
        # Phase ID management based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            self.test_phase_id = None  # Force creation of new phase
            print(f"🔄 CREATE_NEW_PHASE=true: Will create new phase (ignoring PHASE_ID)")
        else:
            self.test_phase_id = self.PHASE_ID  # Use existing phase if provided
    
    def create_test_project(self):
        """Create a new test project using the correct API from CreateProject.har"""
        try:
            # Create a unique project name
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            project_name = f"{self.PROJECT_NAME_TXT}-{timestamp}-{unique_id}"
            
            # Based on CreateProject.har analysis, the correct project creation API is:
            # POST /v2/projects with payload: [{}] for quick create
            # This creates a project with default name, then we can rename it
            
            # Project creation payload - exact format from HAR (quick create)
            project_payload = json.dumps([{}])
            
            # Headers from CreateProject.har - Next.js Server Actions pattern
            headers = {
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': '83cef14cae8a2ba4da184ad4fb26161dd04c149c',  # From CreateProject.har
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            # Project creation URL (from CreateProject.har)
            create_url = "/v2/projects"
            
            print(f"🔧 Creating project using quick create API...")
            
            with self.client.post(
                create_url,
                data=project_payload,
                headers=headers,
                catch_response=True,
                name="create_project"
            ) as response:
                print(f"🔍 Project creation response status: {response.status_code}")
                print(f"🔍 Project creation response: {response.text[:500]}...")
                
                if response.status_code == 200:
                    response.success()
                    print(f"✅ Successfully called project creation API")
                    
                    # Try to extract project ID from response
                    project_id = self._extract_project_id_from_response(response.text)
                    if project_id:
                        # Set the project ID for future operations
                        self.test_project_id = project_id
                        print(f"🔗 Set test_project_id to: {project_id}")
                        
                        # Now try to rename the project to our desired name
                        renamed_successfully = self._rename_project(project_id, project_name)
                        final_name = project_name if renamed_successfully else f"Quick Project {unique_id}"
                        
                        # Track created project for cleanup
                        self.created_projects.append({
                            'id': project_id,
                            'name': final_name
                        })
                        print(f"🗂️ Tracked project for cleanup: {project_id} ({final_name})")
                    else:
                        print(f"⚠️ Could not extract project ID from response")
                        # Use a fallback project ID if creation appeared successful
                        self.test_project_id = self.PROJECT_ID
                        
                elif response.status_code == 401:
                    response.failure("Authentication failed for project creation")
                    print(f"❌ Authentication failed for project creation")
                    self.test_project_id = self.PROJECT_ID  # Fallback
                elif response.status_code == 403:
                    response.failure("Access denied for project creation")
                    print(f"❌ Access denied for project creation")
                    self.test_project_id = self.PROJECT_ID  # Fallback
                else:
                    response.failure(f"Project creation failed: {response.status_code}")
                    print(f"⚠️ Project creation failed: {response.status_code}")
                    self.test_project_id = self.PROJECT_ID  # Fallback
                    
        except Exception as e:
            print(f"💥 Exception in create_test_project: {e}")
            self.test_project_id = self.PROJECT_ID  # Fallback
            import traceback
            traceback.print_exc()
    
    def _rename_project(self, project_id, new_name):
        """Rename the newly created project using the correct API from project rename HAR"""
        try:
            # Based on project rename.har, the correct API is:
            # POST /project/{projectId}/messages?messageKey=projectId&messageId={projectId}&channelId={channelId}
            # with payload: [{"projectId":{"uuid":"PROJECT_ID"},"name":"NEW_NAME"}]
            
            # For now, we'll use a placeholder channel ID (this might need to be dynamic)
            # In practice, this might need to be obtained from the project data
            placeholder_channel_id = "e3fb17d1-ece9-4e3f-90cb-23918b648ade"  # From HAR
            
            # Construct the rename URL with correct query parameters
            rename_url = f"/project/{project_id}/messages"
            params = {
                'messageKey': 'projectId',
                'messageId': project_id,
                'channelId': placeholder_channel_id
            }
            
            # Project rename payload - exact format from HAR
            rename_payload = json.dumps([{
                "projectId": {"uuid": project_id},
                "name": new_name
            }])
            
            # Headers from project rename.har
            headers = {
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': '75aaedb01b5c98f20a569b8a7a97ee1fa04c3acf'  # From rename HAR
            }
            
            print(f"🏷️ Attempting to rename project to: '{new_name}' using correct API")
            
            with self.client.post(
                rename_url,
                params=params,
                data=rename_payload,
                headers=headers,
                catch_response=True,
                name="rename_project"
            ) as response:
                print(f"🔍 Rename response status: {response.status_code}")
                print(f"🔍 Rename response: {response.text[:200]}...")
                
                if response.status_code == 200:
                    # Check if the response indicates success
                    if 'Project name updated' in response.text or '"name":"' in response.text:
                        print(f"✅ Successfully renamed project to: '{new_name}'")
                        return True
                    else:
                        print(f"⚠️ Rename API called but response unclear: {response.text[:100]}...")
                        return False
                else:
                    print(f"⚠️ Project rename failed: {response.status_code}")
                    return False
                    
        except Exception as e:
            print(f"⚠️ Project rename error: {e}")
            return False
    
    def delete_test_project(self, project_id):
        """Delete a test project using the pattern from DeleteProject.har"""
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
            
            print(f"🗑️ Deleting project: {project_id}")
            
            with self.client.post(
                delete_url,
                data=delete_payload,
                headers=headers,
                catch_response=True,
                name="delete_project"
            ) as response:
                print(f"🔍 Project deletion response status: {response.status_code}")
                print(f"🔍 Project deletion response: {response.text[:200]}...")
                
                if response.status_code == 200:
                    response.success()
                    print(f"✅ Successfully deleted project: {project_id}")
                    return True
                else:
                    response.failure(f"Project deletion failed: {response.status_code}")
                    print(f"⚠️ Project deletion failed: {response.status_code}")
                    return False
                    
        except Exception as e:
            print(f"💥 Exception in delete_test_project: {e}")
            return False
    
    def _extract_project_id_from_response(self, response_text):
        """Extract project ID from the Next.js server action response using CreateProject.har format"""
        try:
            # Based on CreateProject.har, the response format is:
            # 1:{"response":{"info":{"status":0,"message":"Project created successfully"},"projectId":{"uuid":"PROJECT_ID_HERE"}},"error":null}
            
            # Look for the JSON part with the project data
            lines = response_text.strip().split('\n')
            for line in lines:
                if line.startswith('1:') and 'projectId' in line and 'uuid' in line:
                    try:
                        # Remove the "1:" prefix
                        json_part = line[2:]
                        data = json.loads(json_part)
                        
                        # Navigate to the project UUID based on HAR format
                        if 'response' in data and 'projectId' in data['response']:
                            project_data = data['response']['projectId']
                            if 'uuid' in project_data:
                                project_id = project_data['uuid']
                                print(f"🎯 Extracted project ID from response: {project_id}")
                                return project_id
                    except (json.JSONDecodeError, KeyError) as e:
                        print(f"⚠️ Could not parse project response line: {e}")
                        continue
            
            # Fallback: try to find any UUID pattern in the response that looks like a project ID
            import re
            # Look for the specific pattern from the HAR: "projectId":{"uuid":"..."} 
            project_id_pattern = r'"projectId":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
            matches = re.findall(project_id_pattern, response_text)
            
            if matches:
                project_id = matches[0]
                print(f"🎯 Extracted project ID via regex: {project_id}")
                return project_id
                        
        except Exception as e:
            print(f"⚠️ Error extracting project ID: {e}")
            
        return None

    @task(3)  # Primary task - weight 3
    def view_project_plan(self):
        """Test viewing the project plan page"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 No project ID available, creating project first...")
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
    
    @task(5)  # Higher frequency for milestone creation - weight 5
    def create_milestone(self):
        """Test creating a milestone in the current phase"""
        # Import required modules at the start
        import json
        import re
        
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot create milestone")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            # If no phase ID, create one first
            print(f"🔗 No phase ID available, creating phase first...")
            self.create_test_phase()
            
            # Check if phase creation succeeded
            if not self.test_phase_id:
                print(f"⚠️ Phase creation failed, cannot create milestone")
                return
            else:
                print(f"✅ Phase created successfully, continuing with milestone creation in phase: {self.test_phase_id}")
        
        # Create a unique milestone name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        milestone_name = f"{self.TEST_MILESTONE_NAME}-{timestamp}-{unique_id}"
        
        # Based on CreateMilestone.har analysis, the correct milestone creation API is:
        # POST /project/{projectId}/plan?phase={phaseId}&view=board
        # with payload: [{"name":"milestone_name","phaseId":{"uuid":"phase_id"}}]
        
        milestone_url = f"/project/{self.test_project_id}/plan"
        params = {
            'phase': self.test_phase_id,
            'view': 'board'
        }
        
        # Create the milestone payload - exact format from CreateMilestone.har
        milestone_payload = json.dumps([{
            "name": milestone_name,
            "phaseId": {"uuid": self.test_phase_id}
        }])
        
        # Set up headers based on CreateMilestone.har analysis
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': 'text/x-component',
            'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5',  # From CreateMilestone.har
            'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
        }
        
        print(f"🎯 Creating milestone '{milestone_name}' in phase {self.test_phase_id}")
        
        with self.client.post(
            milestone_url,
            params=params,
            data=milestone_payload,
            headers=headers,
            catch_response=True,
            name="create_milestone"
        ) as response:
            if response.status_code == 200:
                response.success()
                
                # Parse the response to get the milestone ID
                try:
                    # Look for milestone creation confirmation in response
                    if 'milestone' in response.text and 'response' in response.text:
                        print(f"✅ Milestone creation response received")
                        
                        # Extract milestone ID from response
                        json_match = re.search(r'1:\{\"response\":\{\"milestone\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                        if json_match:
                            milestone_id = json_match.group(1)
                            print(f"✅ Successfully created milestone '{milestone_name}' with ID: {milestone_id}")
                            
                            # Store the created milestone for tracking
                            self.created_milestones.append({
                                'id': milestone_id,
                                'name': milestone_name,
                                'phase_id': self.test_phase_id
                            })
                            
                        else:
                            print(f"⚠️ Milestone created but couldn't extract ID from response")
                    else:
                        print(f"⚠️ Unexpected milestone creation response: {response.text[:200]}")
                        
                except Exception as e:
                    print(f"⚠️ Error parsing milestone creation response: {e}")
                    
            else:
                response.failure(f"Failed to create milestone: {response.status_code} - {response.text[:200]}")
                print(f"❌ Failed to create milestone: {response.status_code} - {response.text[:200]}")
    
    @task(7)  # Higher frequency for task creation - weight 7 
    def create_task(self):
        """Test creating a task under a milestone"""
        # Import required modules at the start
        import json
        import re
        
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot create task")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        if not self.test_phase_id:
            # If no phase ID, create one first
            print(f"🔗 No phase ID available, creating phase first...")
            self.create_test_phase()
            
            # Check if phase creation succeeded
            if not self.test_phase_id:
                print(f"⚠️ Phase creation failed, cannot create task")
                return
            else:
                print(f"✅ Phase created successfully, continuing with task creation")
        
        # Ensure we have a milestone to attach the task to
        if not self.created_milestones:
            print(f"🔗 No milestones available, creating milestone first...")
            self.create_milestone()
            
            # Check if we have milestones after creation attempt
            if not self.created_milestones:
                print(f"⚠️ Milestone creation failed, cannot create task")
                return
        
        # Use the most recent milestone as the parent
        milestone_id = self.created_milestones[-1]['id']
        milestone_name = self.created_milestones[-1]['name']
        
        # Create a unique task name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        task_name = f"{self.TEST_TASK_NAME}-{timestamp}-{unique_id}"
        
        # Based on createingatask.har analysis, the correct task creation API is:
        # POST /project/{projectId}/plan?phase={phaseId}&view=board
        # with payload: [{"name":"task_name","parentId":{"uuid":"milestone_id"}}]
        
        task_url = f"/project/{self.test_project_id}/plan"
        params = {
            'phase': self.test_phase_id,
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
        
        print(f"📝 Creating task '{task_name}' under milestone '{milestone_name}' ({milestone_id})")
        
        with self.client.post(
            task_url,
            params=params,
            data=task_payload,
            headers=headers,
            catch_response=True,
            name="create_task"
        ) as response:
            if response.status_code == 200:
                response.success()
                
                # Parse the response to get the task ID
                try:
                    # Look for task creation confirmation in response
                    if 'task' in response.text and 'response' in response.text:
                        print(f"✅ Task creation response received")
                        
                        # Extract task ID from response
                        json_match = re.search(r'1:\{\"response\":\{\"task\":\{[^}]*\"id\":\{\"uuid\":\"([^\"]+)\"', response.text)
                        if json_match:
                            task_id = json_match.group(1)
                            print(f"✅ Successfully created task '{task_name}' with ID: {task_id}")
                            
                            # Store the created task for tracking
                            self.created_tasks.append({
                                'id': task_id,
                                'name': task_name,
                                'milestone_id': milestone_id,
                                'milestone_name': milestone_name
                            })
                            
                        else:
                            print(f"⚠️ Task created but couldn't extract ID from response")
                    else:
                        print(f"⚠️ Unexpected task creation response: {response.text[:200]}")
                        
                except Exception as e:
                    print(f"⚠️ Error parsing task creation response: {e}")
                    
            else:
                response.failure(f"Failed to create task: {response.status_code} - {response.text[:200]}")
                print(f"❌ Failed to create task: {response.status_code} - {response.text[:200]}")
      
    @task(1)  # Lower frequency - weight 1 (reduced from 4)
    def create_test_phase(self):
        """Test creating a new phase in the project using the correct direct API"""
        # Ensure we have a project to work with
        if not self.test_project_id:
            if self.CREATE_NEW_PROJECT:
                print(f"🔗 No project ID available, creating project first...")
                self.create_test_project()
                if not self.test_project_id:
                    print(f"⚠️ Project creation failed, cannot create phase")
                    return
            else:
                print(f"⚠️ No project ID available and CREATE_NEW_PROJECT=false")
                return
        
        try:
            # Create a unique phase name
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            phase_name = f"{self.TEST_PHASE_NAME}-{timestamp}-{unique_id}"
            
            # Based on HAR analysis, the correct phase creation API is:
            # POST /project/{projectId}/plan?phase={existingPhaseId}&view=board
            # with payload: [{"projectId":{"uuid":"..."},"name":"phase_name"}]
            
            # Use the existing phase from environment or default
            current_phase_id = self.PHASE_ID or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
            
            # Construct the phase creation URL
            create_url = f"/project/{self.test_project_id}/plan"
            params = {
                'phase': current_phase_id,
                'view': 'board'  # Can be 'board' or 'list'
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
                'Next-Action': '5955c4c2ae46e596cde573a76ce226e64e73fb9a',  # From HAR
                'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + self.test_project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + self.test_project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            }
            
            print(f"🔧 Creating phase directly: '{phase_name}' in project: {self.test_project_id}")
            print(f"🔧 Using direct phase creation API with existing phase context: {current_phase_id}")
            
            with self.client.post(
                create_url,
                params=params,
                data=phase_payload,
                headers=headers,
                catch_response=True,
                name="create_phase"
            ) as response:
                print(f"🔍 Phase creation response status: {response.status_code}")
                print(f"🔍 Phase creation response headers: {dict(response.headers)}")
                print(f"🔍 Phase creation response body: {response.text[:1000]}...")
                
                if response.status_code == 200:
                    response.success()
                    print(f"✅ Successfully created phase: '{phase_name}'")
                    
                    # Try to extract phase ID from response
                    phase_id = self._extract_phase_id_from_response(response.text)
                    if phase_id:
                        # Set the phase ID for future milestone creation
                        if not self.test_phase_id:
                            self.test_phase_id = phase_id
                            print(f"🔗 Set test_phase_id to: {phase_id}")
                        
                        # Always track created phases
                        self.created_phases.append({
                            'id': phase_id,
                            'name': phase_name,
                            'projectId': self.test_project_id
                        })
                        print(f"🗂️ Tracked phase ID: {phase_id}")
                    else:
                        print(f"⚠️ Could not extract phase ID from response")
                        print(f"🔍 Response preview: {response.text[:200]}...")
                        
                        # Still track the attempt
                        self.created_phases.append({
                            'id': 'unknown',
                            'name': phase_name,
                            'projectId': self.test_project_id
                        })
                else:
                    response.failure(f"Phase creation failed with status {response.status_code}: {response.text[:200]}")
                    print(f"❌ Phase creation failed: {response.status_code} - {response.text[:200]}")
                    
        except Exception as e:
            print(f"💥 Exception in create_test_phase: {e}")
            import traceback
            traceback.print_exc()
    
    def _extract_phase_id_from_response(self, response_text):
        """Extract phase ID from the Next.js server action response"""
        try:
            # Handle Next.js server action response format
            # Expected format: 0:["$@1",["Po1Suoqh66pXLW-Zjo28k",null]]
            # 1:{"response":{"phase":{"id":{"uuid":"e3bbffa4-e67d-4bf4-9c87-be182ed596a9"},...}}}
            
            # Look for the JSON part with the phase data
            lines = response_text.strip().split('\n')
            for line in lines:
                if line.startswith('1:') and 'phase' in line and 'uuid' in line:
                    try:
                        # Remove the "1:" prefix
                        json_part = line[2:]
                        data = json.loads(json_part)
                        
                        # Navigate to the phase UUID
                        if 'response' in data and 'phase' in data['response']:
                            phase_data = data['response']['phase']
                            if 'id' in phase_data and 'uuid' in phase_data['id']:
                                return phase_data['id']['uuid']
                    except (json.JSONDecodeError, KeyError) as e:
                        print(f"⚠️ Could not parse phase response line: {e}")
                        continue
            
            # Fallback: try to find any UUID pattern in the response
            import re
            uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
            matches = re.findall(uuid_pattern, response_text.lower())
            
            if matches:
                # Return the last UUID found (likely the newly created phase)
                return matches[-1]
                
        except Exception as e:
            print(f"⚠️ Error extracting phase ID: {e}")
            
        return None
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting project phase/milestone load test")
        
        # Show project configuration based on CREATE_NEW_PROJECT flag
        if self.CREATE_NEW_PROJECT:
            print(f"🔗 Project ID: Will create NEW project (CREATE_NEW_PROJECT=true)")
            print(f"📝 Project Name: '{self.PROJECT_NAME_TXT}' (with dynamic timestamps)")
            if self.PROJECT_ID:
                print(f"📋 Ignoring existing PROJECT_ID: {self.PROJECT_ID}")
        else:
            if self.test_project_id:
                print(f"🔗 Project ID: Using existing project {self.test_project_id}")
            else:
                print(f"🔗 Project ID: Will be created (no PROJECT_ID provided)")
        
        # Show phase configuration based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            print(f"🔗 Phase ID: Will create NEW phase (CREATE_NEW_PHASE=true)")
            if self.PHASE_ID:
                print(f"📋 Ignoring existing PHASE_ID: {self.PHASE_ID}")
        else:
            if self.test_phase_id:
                print(f"🔗 Phase ID: Using existing phase {self.test_phase_id}")
            else:
                print(f"🔗 Phase ID: Will be created (no PHASE_ID provided)")
        
        print(f"📱 Test Phase Name: '{self.TEST_PHASE_NAME}' (with dynamic timestamps)")
        print(f"🎯 Test Milestone Name: '{self.TEST_MILESTONE_NAME}' (with dynamic timestamps)")
        
        # Show configuration source
        env_project = os.getenv('PROJECT_ID')
        env_project_name = os.getenv('PROJECT_NAME_TXT')
        env_phase = os.getenv('PHASE_ID')
        env_create_new_project = os.getenv('CREATE_NEW_PROJECT')
        env_create_new_phase = os.getenv('CREATE_NEW_PHASE')
        
        if env_project:
            print(f"📋 Using PROJECT_ID from environment: {env_project}")
        else:
            print(f"📋 Using default PROJECT_ID from HAR analysis")
        
        if env_project_name:
            print(f"📋 Using PROJECT_NAME_TXT from environment: {env_project_name}")
        else:
            print(f"📋 Using default PROJECT_NAME_TXT: {self.PROJECT_NAME_TXT}")
        
        if env_create_new_project:
            print(f"📋 CREATE_NEW_PROJECT environment variable: {env_create_new_project}")
        else:
            print(f"📋 CREATE_NEW_PROJECT is set to 'false' (default)")
        
        if env_create_new_phase:
            print(f"📋 CREATE_NEW_PHASE environment variable: {env_create_new_phase}")
        else:
            print(f"📋 CREATE_NEW_PHASE is set to 'false' (default)")
            
        if env_phase and not self.CREATE_NEW_PHASE:
            print(f"📋 Using PHASE_ID from environment: {env_phase}")
        elif env_phase and self.CREATE_NEW_PHASE:
            print(f"📋 PHASE_ID from environment ignored due to CREATE_NEW_PHASE=true")
        elif not env_phase:
            print(f"📋 No PHASE_ID provided - will create new phase")
    
    def on_stop(self):
        """Called when the load test is stopping - cleanup created projects"""
        print(f"🛑 Project phase/milestone load test completed for user: {self.login_email}")
        
        # Count created items for reporting
        projects_count = len(self.created_projects)
        phases_count = len(self.created_phases)
        milestones_count = len(self.created_milestones)
        tasks_count = len(self.created_tasks)
        print(f"📊 Created {projects_count} projects, {phases_count} phases, {milestones_count} milestones, and {tasks_count} tasks")
        
        if self.CREATE_NEW_PROJECT and self.created_projects:
            print(f"🧹 Starting cleanup of {len(self.created_projects)} created projects...")
            for project_info in self.created_projects:
                project_id = project_info['id']
                project_name = project_info['name']
                print(f"🗑️ Attempting to delete project: {project_name} ({project_id})")
                
                # TEMPORARILY DISABLED - Comment out deletion for inspection
                # self.delete_test_project(project_id)
                print(f"⚠️ DELETION DISABLED - Project preserved for inspection: {project_name} ({project_id})")
            
            # print(f"🧹 Cleanup completed")
            print(f"🧹 Cleanup SKIPPED - Projects preserved for inspection")
        else:
            print(f"📋 No projects to clean up (using existing project or no projects created)")
            
        print(f"🧹 Project lifecycle test cleanup completed")

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
        
        print(f"🚀 Starting stress test")
        print(f"🔗 Project ID: Will create NEW project (CREATE_NEW_PROJECT=true)") if self.CREATE_NEW_PROJECT else print(f"🔗 Project ID: Using existing {self.PROJECT_ID}")
    
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
            self.rapid_phase_creation()
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
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5'
            }
            
            create_url = f"/project/{self.test_project_id}/plan?phase={self.test_phase_id}&view=list"
            
            response = self.client.post(
                create_url,
                data=milestone_payload,
                headers=headers,
                name="stress_milestone_create"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress test milestone created: {milestone_name}")
                self.created_items.append(f"milestone:{milestone_name}")
            else:
                print(f"⚠️ Stress test milestone failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Stress test milestone error: {e}")
    
    @task(1)
    def rapid_phase_creation(self):
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
            
            # Create phase payload
            phase_payload = json.dumps([{
                "name": phase_name,
                "projectId": {"uuid": self.test_project_id}
            }])
            
            headers = {
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5'
            }
            
            create_url = f"/project/{self.test_project_id}/plan"
            
            response = self.client.post(
                create_url,
                data=phase_payload,
                headers=headers,
                name="stress_phase_create"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress test phase created: {phase_name}")
                self.created_items.append(f"phase:{phase_name}")
                
                # Try to extract phase ID for milestone creation
                if not self.test_phase_id:
                    phase_id = self._extract_phase_id_from_response(response.text)
                    if phase_id:
                        self.test_phase_id = phase_id
                        print(f"🔗 Set stress test phase ID: {phase_id}")
            else:
                print(f"⚠️ Stress test phase failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Stress test phase error: {e}")
    
    def _extract_phase_id_from_response(self, response_text):
        """Extract phase ID from response"""
        try:
            uuid_pattern = r'"uuid":"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"'
            matches = re.findall(uuid_pattern, response_text)
            
            if matches:
                for uuid_match in matches:
                    if uuid_match != self.test_project_id:
                        return uuid_match
        except Exception as e:
            print(f"⚠️ Could not extract phase ID: {e}")
        return None
    
    def on_start(self):
        """Called when stress test user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        self.created_projects = []
        self.created_phases = []
        self.created_milestones = []  
        self.created_tasks = []
        self.created_items = []  # For general tracking
        
        print(f"🚀 Starting stress test")
        print(f"🔗 Project ID: Will create NEW project (CREATE_NEW_PROJECT=true)") if self.CREATE_NEW_PROJECT else print(f"🔗 Project ID: Using existing {self.PROJECT_ID}")
    
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
            self.rapid_phase_creation()
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
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5'
            }
            
            create_url = f"/project/{self.test_project_id}/plan?phase={self.test_phase_id}&view=list"
            
            response = self.client.post(
                create_url,
                data=milestone_payload,
                headers=headers,
                name="stress_milestone_create"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress test milestone created: {milestone_name}")
                self.created_items.append(f"milestone:{milestone_name}")
            else:
                print(f"⚠️ Stress test milestone failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Stress test milestone error: {e}")
    
    @task(1)
    def rapid_phase_creation(self):
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
            
            # Create phase payload
            phase_payload = json.dumps([{
                "name": phase_name,
                "projectId": {"uuid": self.test_project_id}
            }])
            
            headers = {
                'Accept': 'text/x-component',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5'
            }
            
            create_url = f"/project/{self.test_project_id}/plan"
            
            response = self.client.post(
                create_url,
                data=phase_payload,
                headers=headers,
                name="stress_phase_create"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress test phase created: {phase_name}")
                self.created_items.append(f"phase:{phase_name}")
                
                # Try to extract phase ID for milestone creation
                if not self.test_phase_id:
                    phase_id = self._extract_phase_id_from_response(response.text)
                    if phase_id:
                        self.test_phase_id = phase_id
                        print(f"🔗 Set stress test phase ID: {phase_id}")
            else:
                print(f"⚠️ Stress test phase failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Stress test phase error: {e}")
    
    def _extract_phase_id_from_response(self, response_text):
        """Extract phase ID from response"""
        try:
            uuid_pattern = r'"uuid":"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"'
            matches = re.findall(uuid_pattern, response_text)
            
            if matches:
                for uuid_match in matches:
                    if uuid_match != self.test_project_id:
                        return uuid_match
        except Exception as e:
            print(f"⚠️ Could not extract phase ID: {e}")
        return None
    
    def on_stop(self):
        """Called when stress test user stops - cleanup projects if created"""
        print(f"🛑 Stress test completed for user: {self.login_email}")
        print(f"📊 Created {len(self.created_items)} items total")
        tasks_count = len(self.created_tasks)
        milestones_count = len(self.created_milestones)
        phases_count = len(self.created_phases)
        projects_count = len(self.created_projects)
        print(f"📊 Breakdown: {projects_count} projects, {phases_count} phases, {milestones_count} milestones, {tasks_count} tasks")
        
        if self.CREATE_NEW_PROJECT and self.created_projects:
            print(f"🧹 Starting stress test cleanup of {len(self.created_projects)} projects...")
            for project_info in self.created_projects:
                project_id = project_info['id']
                project_name = project_info['name']
                print(f"🗑️ Stress test: Attempting to delete project {project_name} ({project_id})")
                
                # TEMPORARILY DISABLED - Comment out deletion for inspection
                # success = self.delete_stress_test_project(project_id)
                # if success:
                #     print(f"✅ Stress test: Deleted project {project_name}")
                # else:
                #     print(f"⚠️ Stress test: Failed to delete project {project_name}")
                print(f"⚠️ DELETION DISABLED - Stress test project preserved: {project_name} ({project_id})")
            
            # print(f"🧹 Stress test cleanup completed")
            print(f"🧹 Stress test cleanup SKIPPED - Projects preserved for inspection")
        else:
            print(f"📋 No stress test projects to clean up")

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
            print("🎉 Authentication successful - ready for phase/milestone tests")
            
            # Test project creation if CREATE_NEW_PROJECT=true
            if user.CREATE_NEW_PROJECT:
                try:
                    user.create_test_project()
                    if user.test_project_id:
                        print("🎉 Project creation test: PASSED")
                        print(f"🔍 Created project ID: {user.test_project_id}")
                    else:
                        print("❌ Project creation test: FAILED")
                except Exception as e:
                    print(f"❌ Project creation test: {e}")
            
            # Test the project plan view
            try:
                user.view_project_plan()
                print("🎉 Project plan view test: PASSED")
            except Exception as e:
                print(f"❌ Project plan view test: {e}")
                
            # Test milestone creation
            try:
                user.create_milestone()
                print("🎉 Milestone creation test: PASSED")
                print("🔍 Check your project plan - you should see a new milestone!")
            except Exception as e:
                print(f"❌ Milestone creation test: {e}")
                
            # Test phase creation
            try:
                user.create_test_phase()
                print("🎉 Phase creation test: PASSED")
                print("🔍 Check your project plan - you should see a new phase!")
            except Exception as e:
                print(f"❌ Phase creation test: {e}")
                
            # Test cleanup if project was created
            if user.CREATE_NEW_PROJECT and user.created_projects:
                try:
                    print("🧹 Testing project cleanup...")
                    for project in user.created_projects:
                        success = user.delete_test_project(project['id'])
                        if success:
                            print(f"🎉 Project deletion test: PASSED for {project['name']}")
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
        print('  CREATE_NEW_PROJECT="true" PROJECT_NAME_TXT="LoadTestProject" CREATE_NEW_PHASE="true" TEST_PHASE_NAME="LoadTestPhase" TEST_MILESTONE_NAME="LoadTestMilestone" TEST_TASK_NAME="LoadTestTask" LOGIN_EMAIL="your-email@example.com" LOGIN_PASSWORD="your-password" LOCUST_HOST="https://app.staging.guidecx.io" python project_cr_phase_milestone.py')
        print("  # Test with existing project:")
        print('  CREATE_NEW_PROJECT="false" PROJECT_ID=existing-project-id CREATE_NEW_PHASE="false" PHASE_ID=existing-phase-id python project_cr_phase_milestone.py')
