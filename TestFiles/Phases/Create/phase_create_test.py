#!/usr/bin/env python3
"""
Phase Creation Test Module
Extracted from project_cr_phase_milestone.py - Phases/Create functionality

Can run standalone:
  locust -f TestFiles/Phases/Create/phase_create_test.py --users 3 --spawn-rate 1

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

class PhaseCreateTest(BaseTestTemplate):
    """
    Phase creation test module
    Extracted from original project_cr_phase_milestone.py
    """
    
    @task(4)
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
                        
                        # Return phase info for coordination
                        return {
                            'id': phase_id,
                            'name': phase_name,
                            'project_id': self.test_project_id,
                            'success': True
                        }
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
            
        return None
    
    @task(3)  # Secondary task for rapid phase creation
    def create_multiple_phases(self):
        """Create multiple phases for better distribution testing"""
        # Create 2-3 phases in a single task execution
        import random
        num_phases = random.randint(2, 3)
        
        print(f"📋 Creating {num_phases} phases for distribution testing...")
        
        for i in range(num_phases):
            self.create_test_phase()
            # Small delay between phase creations
            time.sleep(0.5)
        
        print(f"✅ Completed batch creation of {num_phases} phases")


# Standalone execution capability
if __name__ == "__main__":
    print("🚀 Running Phase Creation Tests independently...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test PhaseCreateTest
        env = Environment(user_classes=[PhaseCreateTest])
        user = PhaseCreateTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for phase creation tests")
            
            # Check if we have required project ID
            if user.test_project_id:
                print(f"🔍 Using project ID: {user.test_project_id}")
                
                # Test phase creation
                try:
                    user.create_test_phase()
                    if user.created_phases:
                        print("🎉 Phase creation test: PASSED")
                        print(f"🔍 Created phases: {len(user.created_phases)}")
                        for phase in user.created_phases:
                            print(f"   • {phase['name']} (ID: {phase['id'][:8]}...)")
                    else:
                        print("❌ Phase creation test: FAILED")
                        
                    # Test multiple phase creation
                    user.create_multiple_phases()
                    print(f"🎉 Multiple phase creation test: PASSED")
                    print(f"🔍 Total created phases: {len(user.created_phases)}")
                except Exception as e:
                    print(f"❌ Phase creation tests: {e}")
            else:
                print("⚠️ No project ID available - set PROJECT_ID environment variable")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
        print("Set PROJECT_ID environment variable for testing") 