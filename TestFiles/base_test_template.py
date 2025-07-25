#!/usr/bin/env python3
"""
Base Test Template
Common functionality for all test modules split from project_cr_phase_milestone.py
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
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from common.auth import AuthenticatedUser

class BaseTestTemplate(AuthenticatedUser):
    """
    Base template containing common functionality from project_cr_phase_milestone.py
    All split test classes inherit from this to maintain shared state and environment setup
    """
    abstract = True  # Mark as abstract - this class shouldn't be instantiated directly
    wait_time = between(3, 8)  # Wait 3-8 seconds between requests
    
    # Use environment variables (copied from original)
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
        
        # Initialize shared tracking - allows both standalone and coordinated execution
        if not hasattr(self, 'created_projects'):
            self.created_projects = []
        if not hasattr(self, 'created_phases'):
            self.created_phases = []
        if not hasattr(self, 'created_milestones'):
            self.created_milestones = []
        if not hasattr(self, 'created_tasks'):
            self.created_tasks = []
        if not hasattr(self, 'created_subtasks'):
            self.created_subtasks = []
        
        # Project ID management based on CREATE_NEW_PROJECT flag
        if self.CREATE_NEW_PROJECT:
            self.test_project_id = None  # Will be set after project creation
        else:
            self.test_project_id = self.PROJECT_ID  # Use existing project
        
        # Phase ID management based on CREATE_NEW_PHASE flag
        if self.CREATE_NEW_PHASE:
            self.test_phase_id = None  # Force creation of new phase
        else:
            self.test_phase_id = self.PHASE_ID  # Use existing phase if provided
    
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
    
    def _extract_phase_id_from_response(self, response_text):
        """Extract phase ID from phase creation response"""
        # Look for phase ID patterns in the response
        import re
        
        # Try multiple patterns for phase ID extraction
        patterns = [
            r'"phaseId":\s*"([^"]+)"',
            r'"id":\s*"([^"]+)"',
            r'phase[_-]?id["\s]*:\s*["\s]*([a-f0-9\-]{36})',
            r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})',  # UUID pattern
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, response_text, re.IGNORECASE)
            if matches:
                return matches[0]
        
        return None

    def _get_fresh_server_action_headers(self, project_id=None):
        """Get fresh Next-Action headers by loading the current page and extracting them"""
        try:
            # Load the project plan page to get fresh session data
            if not project_id:
                project_id = self.test_project_id or self.PROJECT_ID
            
            plan_url = f"/project/{project_id}/plan"
            response = self.client.get(plan_url, name="get_fresh_headers")
            
            if response.status_code == 200:
                # Extract Next-Action IDs from the page HTML
                import re
                
                # Look for Server Action patterns in the HTML
                action_patterns = [
                    r'action="([a-f0-9]{40})"',  # Server Action ID pattern
                    r'"([a-f0-9]{40})"',         # Generic 40-char hex pattern
                    r'Next-Action["\s]*:\s*["\s]*([a-f0-9]{40})',
                ]
                
                for pattern in action_patterns:
                    matches = re.findall(pattern, response.text)
                    if matches:
                        # Use the first valid action ID found
                        next_action = matches[0]
                        print(f"🔄 Found fresh Next-Action: {next_action[:16]}...")
                        
                        return {
                            'Accept': 'text/x-component',
                            'Content-Type': 'text/plain;charset=UTF-8',
                            'Next-Action': next_action,
                            'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22' + project_id + '%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F' + project_id + '%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
                        }
                
                print("⚠️ Could not extract fresh Next-Action from page")
            else:
                print(f"⚠️ Failed to load plan page: {response.status_code}")
                
        except Exception as e:
            print(f"⚠️ Error getting fresh headers: {e}")
        
        # Fallback to basic headers without Server Actions
        return {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
        } 