#!/usr/bin/env python3
"""
Common data extraction functions for load testing.
Contains reusable functions for extracting IDs and data from API responses.
All header functionality has been moved to hardcoded headers in create.py.
"""

import json
import re
from .helpers import debug_print


def extract_project_id_from_response(response_text):
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
                            debug_print(f"Extracted project ID from response: {project_id}")
                            return project_id
                except (json.JSONDecodeError, KeyError) as e:
                    debug_print(f"⚠️ Could not parse project response line: {e}")
                    continue
        
        # Fallback: try to find any UUID pattern in the response that looks like a project ID
        # Look for the specific pattern from the HAR: "projectId":{"uuid":"..."} 
        project_id_pattern = r'"projectId":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(project_id_pattern, response_text)
        
        if matches:
            project_id = matches[0]
            debug_print(f"Extracted project ID via regex: {project_id}")
            return project_id
                    
    except Exception as e:
        debug_print(f"⚠️ Error extracting project ID: {e}")
        
    return None


def extract_phase_id_from_response(response_text):
    """Extract phase ID from the Next.js server action response"""
    debug_print(f"PHASE EXTRACT DEBUG: Attempting to extract phase ID from response")
    debug_print(f"PHASE EXTRACT DEBUG: Response length: {len(response_text)} characters")
    
    try:
        # Handle Next.js server action response format
        # Expected format: 0:["$@1",["Po1Suoqh66pXLW-Zjo28k",null]]
        # 1:{"response":{"phase":{"id":{"uuid":"e3bbffa4-e67d-4bf4-9c87-be182ed596a9"},...}}}
        # OR: 1:{"response":{"templates":[...]}} for phase creation API
        
        # Look for the JSON part with the phase data
        lines = response_text.strip().split('\n')
        debug_print(f"PHASE EXTRACT DEBUG: Response has {len(lines)} lines")
        
        for i, line in enumerate(lines):
            debug_print(f"PHASE EXTRACT DEBUG: Line {i}: {line[:100]}..." if len(line) > 100 else f"PHASE EXTRACT DEBUG: Line {i}: {line}")
            
            if line.startswith('1:'):
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    debug_print(f"PHASE EXTRACT DEBUG: Parsed JSON data: {data}")
                    
                    # Primary logic for direct phase creation response (correct format)
                    if 'response' in data and 'phase' in data['response']:
                        phase_data = data['response']['phase']
                        if 'id' in phase_data and 'uuid' in phase_data['id']:
                            phase_id = phase_data['id']['uuid']
                            debug_print(f"Found direct phase ID: {phase_id}")
                            return phase_id
                    
                    # Fallback: Check if this is a templates response (old behavior)
                    elif 'response' in data and 'templates' in data['response']:
                        templates = data['response']['templates']
                        debug_print(f"⚠️ PHASE EXTRACT DEBUG: Got templates response instead of phase creation - this suggests wrong API or headers")
                        debug_print(f"PHASE EXTRACT DEBUG: Found {len(templates)} templates in response")
                        
                        # Look for the most recently created template (our new phase)
                        # The newest phase should be the one with our naming pattern
                        for template in templates:
                            template_name = template.get('name', '')
                            template_id = template.get('id', {}).get('uuid')
                            debug_print(f"PHASE EXTRACT DEBUG: Template: '{template_name}' -> {template_id}")
                            
                            # Check if this template matches our naming pattern (LoadTestPhase-timestamp-id)
                            if 'LoadTestPhase-' in template_name and template_id:
                                debug_print(f"⚠️ Using matching phase template as fallback: '{template_name}' with ID: {template_id}")
                                return template_id
                        
                        # If no exact match, return the last template ID as fallback
                        if templates and 'id' in templates[-1] and 'uuid' in templates[-1]['id']:
                            fallback_id = templates[-1]['id']['uuid']
                            fallback_name = templates[-1].get('name', 'Unknown')
                            debug_print(f"⚠️ Using fallback (last template): '{fallback_name}' -> {fallback_id}")
                            return fallback_id
                    else:
                        debug_print(f"PHASE EXTRACT DEBUG: No phase or templates found in response")
                        
                except (json.JSONDecodeError, KeyError) as e:
                    debug_print(f"⚠️ Could not parse phase response line: {e}")
                    continue
        
        # Fallback: try to find any UUID pattern in the response
        debug_print(f"PHASE EXTRACT DEBUG: Primary extraction failed, trying regex fallback")
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        matches = re.findall(uuid_pattern, response_text.lower())
        
        if matches:
            # Return the last UUID found (likely the newly created phase)
            fallback_id = matches[-1]
            debug_print(f"⚠️ Using regex fallback (last UUID): {fallback_id}")
            return fallback_id
        else:
            debug_print(f"PHASE EXTRACT DEBUG: No UUIDs found in response")
            
    except Exception as e:
        debug_print(f"❌ Error extracting phase ID: {e}")
    
    debug_print(f"❌ PHASE EXTRACT DEBUG: No phase ID could be extracted")
    return None


def extract_milestone_id_from_response(response_text):
    """Extract milestone ID from the Next.js server action response"""
    debug_print(f"EXTRACT DEBUG: Attempting to extract milestone ID from response")
    debug_print(f"EXTRACT DEBUG: Response length: {len(response_text)} characters")
    
    try:
        # Expected format: 1:{"response":{"milestone":{"id":{"uuid":"milestone_id_here"},...}}}
        
        # Look for the JSON part with the milestone data
        lines = response_text.strip().split('\n')
        debug_print(f"EXTRACT DEBUG: Response has {len(lines)} lines")
        
        for i, line in enumerate(lines):
            debug_print(f"EXTRACT DEBUG: Line {i}: {line[:100]}..." if len(line) > 100 else f"EXTRACT DEBUG: Line {i}: {line}")
            
            if line.startswith('1:'):
                debug_print(f"EXTRACT DEBUG: Found line starting with '1:' - checking for milestone data")
                
                if 'milestone' in line and 'uuid' in line:
                    debug_print(f"EXTRACT DEBUG: Line contains 'milestone' and 'uuid' - attempting JSON parse")
                    try:
                        # Remove the "1:" prefix
                        json_part = line[2:]
                        data = json.loads(json_part)
                        debug_print(f"EXTRACT DEBUG: Successfully parsed JSON: {data}")
                        
                        # Navigate to the milestone UUID
                        if 'response' in data and 'milestone' in data['response']:
                            milestone_data = data['response']['milestone']
                            debug_print(f"EXTRACT DEBUG: Found milestone data: {milestone_data}")
                            
                            if 'id' in milestone_data and 'uuid' in milestone_data['id']:
                                milestone_id = milestone_data['id']['uuid']
                                debug_print(f"Extracted milestone ID from response: {milestone_id}")
                                return milestone_id
                            else:
                                debug_print(f"EXTRACT DEBUG: Milestone data missing 'id' or 'uuid' field")
                        elif 'response' in data:
                            debug_print(f"EXTRACT DEBUG: Response found but no milestone: {data['response']}")
                        else:
                            debug_print(f"EXTRACT DEBUG: No 'response' key in data")
                            
                    except (json.JSONDecodeError, KeyError) as e:
                        debug_print(f"⚠️ Could not parse milestone response line: {e}")
                        debug_print(f"EXTRACT DEBUG: Failed JSON part: {json_part[:200]}...")
                        continue
                else:
                    debug_print(f"EXTRACT DEBUG: Line with '1:' but missing 'milestone' or 'uuid'")
            else:
                debug_print(f"EXTRACT DEBUG: Line doesn't start with '1:' - skipping")
        
        # Fallback: try to find milestone ID pattern in the response
        debug_print(f"EXTRACT DEBUG: Primary extraction failed, trying regex fallback")
        milestone_id_pattern = r'"milestone":\s*\{\s*[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(milestone_id_pattern, response_text)
        
        if matches:
            milestone_id = matches[0]
            debug_print(f"Extracted milestone ID via regex: {milestone_id}")
            return milestone_id
        else:
            debug_print(f"EXTRACT DEBUG: Regex fallback also failed - no milestone UUID found")
                    
    except Exception as e:
        debug_print(f"❌ Error extracting milestone ID: {e}")
        
    debug_print(f"❌ EXTRACT DEBUG: No milestone ID could be extracted from response")
    return None


def extract_task_id_from_response(response_text):
    """Extract task ID from the Next.js server action response"""
    try:
        # Expected format: 1:{"response":{"task":{"id":{"uuid":"task_id_here"},...}}}
        
        # Look for the JSON part with the task data
        lines = response_text.strip().split('\n')
        for line in lines:
            if line.startswith('1:') and 'task' in line and 'uuid' in line:
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    
                    # Navigate to the task UUID
                    if 'response' in data and 'task' in data['response']:
                        task_data = data['response']['task']
                        if 'id' in task_data and 'uuid' in task_data['id']:
                            task_id = task_data['id']['uuid']
                            debug_print(f"Extracted task ID from response: {task_id}")
                            return task_id
                except (json.JSONDecodeError, KeyError) as e:
                    debug_print(f"⚠️ Could not parse task response line: {e}")
                    continue
        
        # Fallback: try to find task ID pattern in the response using regex
        task_id_pattern = r'"task":\s*\{\s*[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(task_id_pattern, response_text)
        
        if matches:
            task_id = matches[0]
            debug_print(f"Extracted task ID via regex: {task_id}")
            return task_id
                    
    except Exception as e:
        debug_print(f"⚠️ Error extracting task ID: {e}")
        
    return None


def extract_subtask_id_from_response(response_text):
    """Extract subtask ID from the Next.js server action response"""
    try:
        # Expected format: 1:{"response":{"subtask":{"id":{"uuid":"subtask_id_here"},...}}}
        # or potentially: 1:{"response":{"task":{"id":{"uuid":"subtask_id_here"},"type":"subtask",...}}}
        
        # Look for the JSON part with the subtask data
        lines = response_text.strip().split('\n')
        for line in lines:
            if line.startswith('1:') and ('subtask' in line or ('task' in line and 'subtask' in line)) and 'uuid' in line:
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    
                    # Navigate to the subtask UUID
                    if 'response' in data:
                        # Try subtask key first
                        if 'subtask' in data['response']:
                            subtask_data = data['response']['subtask']
                            if 'id' in subtask_data and 'uuid' in subtask_data['id']:
                                subtask_id = subtask_data['id']['uuid']
                                debug_print(f"Extracted subtask ID from response: {subtask_id}")
                                return subtask_id
                        
                        # Try task key with subtask type
                        elif 'task' in data['response']:
                            task_data = data['response']['task']
                            if 'id' in task_data and 'uuid' in task_data['id']:
                                # Check if this is actually a subtask
                                if ('type' in task_data and task_data['type'] == 'subtask') or \
                                   ('parentId' in task_data) or \
                                   ('isSubtask' in task_data and task_data['isSubtask']):
                                    subtask_id = task_data['id']['uuid']
                                    debug_print(f"Extracted subtask ID from task response: {subtask_id}")
                                    return subtask_id
                                    
                except (json.JSONDecodeError, KeyError) as e:
                    debug_print(f"⚠️ Could not parse subtask response line: {e}")
                    continue
        
        # Fallback: try to find subtask ID patterns in the response
        subtask_patterns = [
            r'"subtask":\s*\{\s*[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}',
            r'"task":\s*\{[^}]*"type":\s*"subtask"[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}',
            r'"task":\s*\{[^}]*"parentId"[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        ]
        
        for pattern in subtask_patterns:
            matches = re.findall(pattern, response_text, re.DOTALL)
            if matches:
                subtask_id = matches[0]
                debug_print(f"Extracted subtask ID via regex: {subtask_id}")
                return subtask_id
                    
    except Exception as e:
        debug_print(f"⚠️ Error extracting subtask ID: {e}")
        
    return None


def get_task_details_with_status(client, project_id, task_id):
    """
    Get task details including current status information
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        task_id: UUID of the task to get details for
        
    Returns:
        dict: Task details including status information, or None if failed
        
    Based on TaskViewTask.har analysis:
    - URL: /project/{project_id}/plan?task-id={task_id}&task-drawer-tab=details
    - Method: POST
    - Payload: [{"taskId": "task_id"}]
    """
    try:
        # Build the request URL and payload based on HAR analysis
        endpoint = f"/project/{project_id}/plan"
        params = {
            'task-id': task_id,
            'task-drawer-tab': 'details'
        }
        
        # Construct URL with query parameters
        url = f"{endpoint}?task-id={params['task-id']}&task-drawer-tab={params['task-drawer-tab']}"
        
        # Request payload format from HAR
        payload = [{"taskId": task_id}]
        
        debug_print(f"Getting task details for: {task_id}")
        
        # Headers based on HAR analysis
        headers = {
            "Accept": "text/x-component",
            "Content-Type": "text/plain;charset=UTF-8",
            "Next-Action": "f4915f56dc7e1251c904d362345604917c93d6ba"  # From HAR file
        }
        
        with client.post(url, json=payload, headers=headers, catch_response=True, name="get_task_details") as response:
            if response.status_code == 200:
                task_details = extract_task_details_from_response(response.text)
                if task_details:
                    debug_print(f"Successfully extracted task details: {task_details['name']}")
                    debug_print(f"Current status: {task_details.get('status', {}).get('label', 'Unknown')}")
                    return task_details
                else:
                    debug_print(f"⚠️ Could not parse task details from response")
                    return None
            else:
                debug_print(f"❌ Failed to get task details: {response.status_code}")
                return None
                
    except Exception as e:
        debug_print(f"💥 Exception getting task details: {e}")
        return None


def extract_task_details_from_response(response_text):
    """
    Extract task details including status from task view API response
    
    Args:
        response_text: Response text from task view API
        
    Returns:
        dict: Parsed task details including status information
        
    Response format from TaskViewTask.har:
    1:{"response":{"task":{"name":"TaskName","status":{"label":"Not Started","statusCategory":0,"id":{"uuid":"status_uuid"}},...}}}
    """
    try:
        # Look for the JSON part with the task data (similar to other extract functions)
        lines = response_text.strip().split('\n')
        
        for line in lines:
            if line.startswith('1:') and 'task' in line and 'status' in line:
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    
                    # Navigate to task data
                    if 'response' in data and 'task' in data['response']:
                        task_data = data['response']['task']
                        
                        # Extract key task information
                        task_details = {
                            'id': task_data.get('id', {}).get('uuid', 'unknown'),
                            'name': task_data.get('name', 'Unknown Task'),
                            'description': task_data.get('description', ''),
                            'type': task_data.get('type', 1),
                            'priority': task_data.get('priority', 1),
                            'responsibility': task_data.get('responsibility', 0),
                            'visibility': task_data.get('visibility', 0),
                            'status': task_data.get('status', {}),
                            'assignees': task_data.get('assignees', []),
                            'watchers': task_data.get('watchers', []),
                            'parents': task_data.get('parents', []),
                            'children': task_data.get('children', []),
                            'tags': task_data.get('tags', []),
                            'createdAt': task_data.get('createdAt', {}),
                            'createdBy': task_data.get('createdBy', {})
                        }
                        
                        debug_print(f"Extracted task details for: {task_details['name']}")
                        if task_details['status']:
                            status_info = task_details['status']
                            debug_print(f"  Status: {status_info.get('label', 'Unknown')} (Category: {status_info.get('statusCategory', 'Unknown')})")
                            debug_print(f"  Status ID: {status_info.get('id', {}).get('uuid', 'Unknown')}")
                        
                        return task_details
                        
                except (json.JSONDecodeError, KeyError) as e:
                    debug_print(f"⚠️ Could not parse task details response: {e}")
                    continue
        
        debug_print(f"❌ No task details found in response")
        return None
        
    except Exception as e:
        debug_print(f"❌ Error extracting task details: {e}")
        return None


def get_available_task_statuses_from_api(client, project_id, phase_id):
    """
    Get available task statuses dynamically from the project plan API
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        
    Returns:
        dict: Mapping of status names to their UUIDs and categories, or None if failed
        
    Uses view.py functions following separation of concerns:
    - view.py: Makes API calls, handles HTTP requests/responses
    - extractdata.py: Processes raw response data, extracts structured information
    """
    try:
        # Import view function (avoiding circular imports)
        from .view import get_project_plan_status_options
        
        debug_print(f"Fetching available statuses from project plan API...")
        
        # Use view.py function to make the API call
        success, response_text, status_code = get_project_plan_status_options(client, project_id, phase_id)
        
        if success:
            statuses = extract_status_options_from_response(response_text)
            if statuses:
                debug_print(f"Successfully extracted {len(statuses)} available statuses from API")
                return statuses
            else:
                debug_print(f"⚠️ Could not parse status options from response")
                return get_fallback_task_statuses()
        else:
            debug_print(f"❌ Failed to get status options: {status_code}")
            return get_fallback_task_statuses()
                
    except Exception as e:
        debug_print(f"💥 Exception getting status options: {e}")
        return get_fallback_task_statuses()


def extract_status_options_from_response(response_text):
    """
    Extract available status options from project plan API response
    
    Args:
        response_text: Response text from project plan API
        
    Returns:
        dict: Mapping of status names to their UUIDs and categories
        
    Response format from HAR analysis:
    1:{"response":{"projectDetails":{...,"unitStatusOptions":[
        {"label":"Not Started","statusCategory":0,"id":{"uuid":"2d2216f3-8e1e-49e3-96ec-fa5205d7a543"}},
        {"label":"In Progress","statusCategory":1,"id":{"uuid":"2d224538-9890-435e-a2bc-bebe1d16a7a3"}},
        ...
    ]}}
    """
    try:
        # Look for the JSON part with the status options
        lines = response_text.strip().split('\n')
        
        for line in lines:
            if line.startswith('1:') and 'unitStatusOptions' in line:
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    
                    # Navigate to status options
                    if 'response' in data and 'projectDetails' in data['response']:
                        project_details = data['response']['projectDetails']
                        if 'unitStatusOptions' in project_details:
                            status_options = project_details['unitStatusOptions']
                            
                            # Convert to our status mapping format
                            status_mapping = {}
                            for status_option in status_options:
                                label = status_option.get('label', 'Unknown')
                                status_id = status_option.get('id', {}).get('uuid', 'unknown')
                                category = status_option.get('statusCategory', 0)
                                
                                status_mapping[label] = {
                                    "uuid": status_id,
                                    "category": category,
                                    "description": f"Status: {label} (Category: {category})"
                                }
                            
                            debug_print(f"Extracted status options from API response:")
                            for status_name, status_info in status_mapping.items():
                                debug_print(f"  - {status_name}: {status_info['uuid']} (Category: {status_info['category']})")
                            
                            return status_mapping
                        else:
                            debug_print(f"No unitStatusOptions found in projectDetails")
                    else:
                        debug_print(f"No projectDetails found in response")
                        
                except (json.JSONDecodeError, KeyError) as e:
                    debug_print(f"⚠️ Could not parse status options response: {e}")
                    continue
        
        debug_print(f"❌ No unitStatusOptions found in response")
        return None
        
    except Exception as e:
        debug_print(f"❌ Error extracting status options: {e}")
        return None


def get_fallback_task_statuses():
    """
    Get fallback task status mapping when API extraction fails
    
    Returns:
        dict: Mapping of status names to their UUIDs and categories
        
    This provides the basic status mapping discovered from HAR files
    as a fallback when dynamic extraction fails.
    """
    # Fallback status mapping from HAR file analysis
    # These are commonly used statuses that should work in most cases
    status_mapping = {
        "Not Started": {
            "uuid": "2d2216f3-8e1e-49e3-96ec-fa5205d7a543",
            "category": 0,
            "description": "Task has not been started yet"
        },
        "In Progress": {
            "uuid": "2d224538-9890-435e-a2bc-bebe1d16a7a3",
            "category": 1,
            "description": "Task is currently being worked on"
        },
        "Done": {
            "uuid": "2d22c720-251e-4be4-ad95-675e53c7efff",
            "category": 4,
            "description": "Task has been completed successfully"
        },
        "Stuck": {
            "uuid": "2d22256b-f2d1-4bba-baeb-99ba8f27ae41",
            "category": 2,
            "description": "Task is stuck and needs attention"
        },
        "Not Applicable": {
            "uuid": "2d228998-c417-444b-8a85-9d1ec1229857",
            "category": 3,
            "description": "Task is not applicable in current context"
        }
    }
    
    debug_print(f"⚠️ Using fallback task statuses:")
    for status_name, status_info in status_mapping.items():
        debug_print(f"  - {status_name}: {status_info['uuid']} (Category: {status_info['category']})")
    
    return status_mapping


def get_available_task_statuses():
    """
    DEPRECATED: Use get_available_task_statuses_from_api() instead
    
    This function was hardcoded and will not work reliably across environments.
    Use the dynamic API-based version instead.
    
    Returns:
        dict: Fallback status mapping
    """
    debug_print("⚠️ WARNING: get_available_task_statuses() is deprecated!")
    debug_print("⚠️ Use get_available_task_statuses_from_api(client, project_id, phase_id) instead")
    debug_print("⚠️ Returning fallback statuses only...")
    
    return get_fallback_task_statuses()


def extract_status_from_task_response(response_text):
    """
    Extract status information from any task-related API response
    
    Args:
        response_text: Response text from task API call
        
    Returns:
        dict: Status information with label, category, and UUID, or None if not found
    """
    try:
        # Look for status information in the response
        lines = response_text.strip().split('\n')
        
        for line in lines:
            if 'status' in line and ('label' in line or 'statusCategory' in line):
                try:
                    # Try to parse as JSON (for server action responses)
                    if line.startswith('1:'):
                        json_part = line[2:]
                        data = json.loads(json_part)
                        
                        # Look for status in different response structures
                        status_locations = [
                            data.get('response', {}).get('task', {}).get('status'),
                            data.get('response', {}).get('status'),
                            data.get('status')
                        ]
                        
                        for status_data in status_locations:
                            if status_data and isinstance(status_data, dict):
                                status_info = {
                                    'label': status_data.get('label', 'Unknown'),
                                    'category': status_data.get('statusCategory', 0),
                                    'uuid': status_data.get('id', {}).get('uuid', 'unknown'),
                                    'explanation': status_data.get('explanation', '')
                                }
                                debug_print(f"Extracted status: {status_info['label']} ({status_info['uuid']})")
                                return status_info
                                
                except (json.JSONDecodeError, KeyError) as e:
                    continue
        
        # Fallback: try regex pattern matching for status UUIDs
        status_uuid_patterns = [
            r'"status":\s*\{[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9-]+)"\s*\}[^}]*"label":\s*"([^"]+)"',
            r'"label":\s*"([^"]+)"[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9-]+)"\s*\}'
        ]
        
        for pattern in status_uuid_patterns:
            matches = re.findall(pattern, response_text)
            if matches:
                if len(matches[0]) == 2:
                    uuid_val, label = matches[0] if 'uuid' in pattern else (matches[0][1], matches[0][0])
                    status_info = {
                        'label': label,
                        'category': 0,  # Default category
                        'uuid': uuid_val,
                        'explanation': ''
                    }
                    debug_print(f"Extracted status via regex: {status_info['label']} ({status_info['uuid']})")
                    return status_info
        
        return None
        
    except Exception as e:
        debug_print(f"❌ Error extracting status from response: {e}")
        return None


def discover_statuses_from_html(html_content):
    """
    Discover available statuses from HTML dropdown or form elements
    
    Args:
        html_content: HTML content that might contain status options
        
    Returns:
        list: List of discovered status options
        
    This function looks for common HTML patterns that indicate status dropdowns:
    - Select option elements
    - Data attributes with status information
    - JavaScript variables containing status configuration
    """
    discovered_statuses = []
    
    try:
        # Common patterns for status dropdown options
        status_patterns = [
            r'<option[^>]*value=["\']([\w\s-]+)["\'][^>]*>([^<]+)</option>',
            r'data-status=["\']([\w\s-]+)["\']',
            r'"status":\s*"([^"]+)"',
            r'status-(\w+)',
            r'class="[^"]*status[^"]*"[^>]*>([^<]+)<'
        ]
        
        for pattern in status_patterns:
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    discovered_statuses.extend(match)
                else:
                    discovered_statuses.append(match)
        
        # Clean and deduplicate
        cleaned_statuses = []
        for status in discovered_statuses:
            cleaned = status.strip()
            if len(cleaned) > 0 and len(cleaned) < 50:  # Reasonable status name length
                cleaned_statuses.append(cleaned)
        
        unique_statuses = list(set(cleaned_statuses))
        
        if unique_statuses:
            debug_print(f"Discovered statuses from HTML: {unique_statuses}")
        
        return unique_statuses
        
    except Exception as e:
        debug_print(f"❌ Error discovering statuses from HTML: {e}")
        return []



