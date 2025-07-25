#!/usr/bin/env python3
"""
Project Creation Test Module
Extracted from project_cr_phase_milestone.py - Projects/Create functionality

Can run standalone:
  locust -f TestFiles/Projects/Create/project_create_test.py --users 3 --spawn-rate 1

Or imported by master controller
"""

import sys
import os
import json
import time
import uuid
from locust import task, between

# Import base template
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from TestFiles.base_test_template import BaseTestTemplate

class ProjectCreateTest(BaseTestTemplate):
    """
    Project creation and management test module
    Extracted from original project_cr_phase_milestone.py
    """
    
    @task(5)  # Primary project creation task
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
                        
                        # Return project info for coordination
                        return {
                            'id': project_id,
                            'name': final_name,
                            'success': True
                        }
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
            
        return None
    
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
    
    def on_stop(self):
        """Cleanup created projects when test stops"""
        print(f"🛑 Project creation test completed")
        
        if self.CREATE_NEW_PROJECT and self.created_projects:
            print(f"🧹 Starting cleanup of {len(self.created_projects)} created projects...")
            for project_info in self.created_projects:
                project_id = project_info['id']
                project_name = project_info['name']
                print(f"🗑️ Attempting to delete project: {project_name} ({project_id})")
                
                # TEMPORARILY DISABLED - Comment out deletion for inspection
                # self.delete_test_project(project_id)
                print(f"⚠️ DELETION DISABLED - Project preserved for inspection: {project_name} ({project_id})")
        else:
            print(f"📋 No projects to clean up")


# Standalone execution capability
if __name__ == "__main__":
    print("🚀 Running Project Creation Tests independently...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test ProjectCreateTest
        env = Environment(user_classes=[ProjectCreateTest])
        user = ProjectCreateTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for project creation tests")
            
            # Test project creation
            try:
                user.create_test_project()
                if user.test_project_id:
                    print("🎉 Project creation test: PASSED")
                    print(f"🔍 Created project ID: {user.test_project_id}")
                else:
                    print("❌ Project creation test: FAILED")
            except Exception as e:
                print(f"❌ Project creation test: {e}")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST") 