#!/usr/bin/env python3
"""
Common data extraction functions for load testing.
Contains reusable functions for extracting IDs and data from API responses.
All header functionality has been moved to hardcoded headers in create.py.
"""

import json
import re


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
                            print(f"Extracted project ID from response: {project_id}")
                            return project_id
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"⚠️ Could not parse project response line: {e}")
                    continue
        
        # Fallback: try to find any UUID pattern in the response that looks like a project ID
        # Look for the specific pattern from the HAR: "projectId":{"uuid":"..."} 
        project_id_pattern = r'"projectId":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(project_id_pattern, response_text)
        
        if matches:
            project_id = matches[0]
            print(f"Extracted project ID via regex: {project_id}")
            return project_id
                    
    except Exception as e:
        print(f"⚠️ Error extracting project ID: {e}")
        
    return None


def extract_phase_id_from_response(response_text):
    """Extract phase ID from the Next.js server action response"""
    print(f"PHASE EXTRACT DEBUG: Attempting to extract phase ID from response")
    print(f"PHASE EXTRACT DEBUG: Response length: {len(response_text)} characters")
    
    try:
        # Handle Next.js server action response format
        # Expected format: 0:["$@1",["Po1Suoqh66pXLW-Zjo28k",null]]
        # 1:{"response":{"phase":{"id":{"uuid":"e3bbffa4-e67d-4bf4-9c87-be182ed596a9"},...}}}
        # OR: 1:{"response":{"templates":[...]}} for phase creation API
        
        # Look for the JSON part with the phase data
        lines = response_text.strip().split('\n')
        print(f"PHASE EXTRACT DEBUG: Response has {len(lines)} lines")
        
        for i, line in enumerate(lines):
            print(f"PHASE EXTRACT DEBUG: Line {i}: {line[:100]}..." if len(line) > 100 else f"PHASE EXTRACT DEBUG: Line {i}: {line}")
            
            if line.startswith('1:'):
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    print(f"PHASE EXTRACT DEBUG: Parsed JSON data: {data}")
                    
                    # Primary logic for direct phase creation response (correct format)
                    if 'response' in data and 'phase' in data['response']:
                        phase_data = data['response']['phase']
                        if 'id' in phase_data and 'uuid' in phase_data['id']:
                            phase_id = phase_data['id']['uuid']
                            print(f"Found direct phase ID: {phase_id}")
                            return phase_id
                    
                    # Fallback: Check if this is a templates response (old behavior)
                    elif 'response' in data and 'templates' in data['response']:
                        templates = data['response']['templates']
                        print(f"⚠️ PHASE EXTRACT DEBUG: Got templates response instead of phase creation - this suggests wrong API or headers")
                        print(f"PHASE EXTRACT DEBUG: Found {len(templates)} templates in response")
                        
                        # Look for the most recently created template (our new phase)
                        # The newest phase should be the one with our naming pattern
                        for template in templates:
                            template_name = template.get('name', '')
                            template_id = template.get('id', {}).get('uuid')
                            print(f"PHASE EXTRACT DEBUG: Template: '{template_name}' -> {template_id}")
                            
                            # Check if this template matches our naming pattern (LoadTestPhase-timestamp-id)
                            if 'LoadTestPhase-' in template_name and template_id:
                                print(f"⚠️ Using matching phase template as fallback: '{template_name}' with ID: {template_id}")
                                return template_id
                        
                        # If no exact match, return the last template ID as fallback
                        if templates and 'id' in templates[-1] and 'uuid' in templates[-1]['id']:
                            fallback_id = templates[-1]['id']['uuid']
                            fallback_name = templates[-1].get('name', 'Unknown')
                            print(f"⚠️ Using fallback (last template): '{fallback_name}' -> {fallback_id}")
                            return fallback_id
                    else:
                        print(f"PHASE EXTRACT DEBUG: No phase or templates found in response")
                        
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"⚠️ Could not parse phase response line: {e}")
                    continue
        
        # Fallback: try to find any UUID pattern in the response
        print(f"PHASE EXTRACT DEBUG: Primary extraction failed, trying regex fallback")
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        matches = re.findall(uuid_pattern, response_text.lower())
        
        if matches:
            # Return the last UUID found (likely the newly created phase)
            fallback_id = matches[-1]
            print(f"⚠️ Using regex fallback (last UUID): {fallback_id}")
            return fallback_id
        else:
            print(f"PHASE EXTRACT DEBUG: No UUIDs found in response")
            
    except Exception as e:
        print(f"❌ Error extracting phase ID: {e}")
    
    print(f"❌ PHASE EXTRACT DEBUG: No phase ID could be extracted")
    return None


def extract_milestone_id_from_response(response_text):
    """Extract milestone ID from the Next.js server action response"""
    print(f"EXTRACT DEBUG: Attempting to extract milestone ID from response")
    print(f"EXTRACT DEBUG: Response length: {len(response_text)} characters")
    
    try:
        # Expected format: 1:{"response":{"milestone":{"id":{"uuid":"milestone_id_here"},...}}}
        
        # Look for the JSON part with the milestone data
        lines = response_text.strip().split('\n')
        print(f"EXTRACT DEBUG: Response has {len(lines)} lines")
        
        for i, line in enumerate(lines):
            print(f"EXTRACT DEBUG: Line {i}: {line[:100]}..." if len(line) > 100 else f"EXTRACT DEBUG: Line {i}: {line}")
            
            if line.startswith('1:'):
                print(f"EXTRACT DEBUG: Found line starting with '1:' - checking for milestone data")
                
                if 'milestone' in line and 'uuid' in line:
                    print(f"EXTRACT DEBUG: Line contains 'milestone' and 'uuid' - attempting JSON parse")
                    try:
                        # Remove the "1:" prefix
                        json_part = line[2:]
                        data = json.loads(json_part)
                        print(f"EXTRACT DEBUG: Successfully parsed JSON: {data}")
                        
                        # Navigate to the milestone UUID
                        if 'response' in data and 'milestone' in data['response']:
                            milestone_data = data['response']['milestone']
                            print(f"EXTRACT DEBUG: Found milestone data: {milestone_data}")
                            
                            if 'id' in milestone_data and 'uuid' in milestone_data['id']:
                                milestone_id = milestone_data['id']['uuid']
                                print(f"Extracted milestone ID from response: {milestone_id}")
                                return milestone_id
                            else:
                                print(f"EXTRACT DEBUG: Milestone data missing 'id' or 'uuid' field")
                        elif 'response' in data:
                            print(f"EXTRACT DEBUG: Response found but no milestone: {data['response']}")
                        else:
                            print(f"EXTRACT DEBUG: No 'response' key in data")
                            
                    except (json.JSONDecodeError, KeyError) as e:
                        print(f"⚠️ Could not parse milestone response line: {e}")
                        print(f"EXTRACT DEBUG: Failed JSON part: {json_part[:200]}...")
                        continue
                else:
                    print(f"EXTRACT DEBUG: Line with '1:' but missing 'milestone' or 'uuid'")
            else:
                print(f"EXTRACT DEBUG: Line doesn't start with '1:' - skipping")
        
        # Fallback: try to find milestone ID pattern in the response
        print(f"EXTRACT DEBUG: Primary extraction failed, trying regex fallback")
        milestone_id_pattern = r'"milestone":\s*\{\s*[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(milestone_id_pattern, response_text)
        
        if matches:
            milestone_id = matches[0]
            print(f"Extracted milestone ID via regex: {milestone_id}")
            return milestone_id
        else:
            print(f"EXTRACT DEBUG: Regex fallback also failed - no milestone UUID found")
                    
    except Exception as e:
        print(f"❌ Error extracting milestone ID: {e}")
        
    print(f"❌ EXTRACT DEBUG: No milestone ID could be extracted from response")
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
                            print(f"Extracted task ID from response: {task_id}")
                            return task_id
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"⚠️ Could not parse task response line: {e}")
                    continue
        
        # Fallback: try to find task ID pattern in the response using regex
        task_id_pattern = r'"task":\s*\{\s*[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(task_id_pattern, response_text)
        
        if matches:
            task_id = matches[0]
            print(f"Extracted task ID via regex: {task_id}")
            return task_id
                    
    except Exception as e:
        print(f"⚠️ Error extracting task ID: {e}")
        
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
                                print(f"Extracted subtask ID from response: {subtask_id}")
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
                                    print(f"Extracted subtask ID from task response: {subtask_id}")
                                    return subtask_id
                                    
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"⚠️ Could not parse subtask response line: {e}")
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
                print(f"Extracted subtask ID via regex: {subtask_id}")
                return subtask_id
                    
    except Exception as e:
        print(f"⚠️ Error extracting subtask ID: {e}")
        
    return None



