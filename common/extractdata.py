#!/usr/bin/env python3
"""
Common data extraction functions for load testing.
Contains reusable functions for extracting IDs and data from API responses.
"""

import json
import re
import urllib.parse


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
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        matches = re.findall(uuid_pattern, response_text.lower())
        
        if matches:
            # Return the last UUID found (likely the newly created phase)
            return matches[-1]
            
    except Exception as e:
        print(f"⚠️ Error extracting phase ID: {e}")
        
    return None


def extract_milestone_id_from_response(response_text):
    """Extract milestone ID from the Next.js server action response"""
    try:
        # Expected format: 1:{"response":{"milestone":{"id":{"uuid":"milestone_id_here"},...}}}
        
        # Look for the JSON part with the milestone data
        lines = response_text.strip().split('\n')
        for line in lines:
            if line.startswith('1:') and 'milestone' in line and 'uuid' in line:
                try:
                    # Remove the "1:" prefix
                    json_part = line[2:]
                    data = json.loads(json_part)
                    
                    # Navigate to the milestone UUID
                    if 'response' in data and 'milestone' in data['response']:
                        milestone_data = data['response']['milestone']
                        if 'id' in milestone_data and 'uuid' in milestone_data['id']:
                            milestone_id = milestone_data['id']['uuid']
                            print(f"Extracted milestone ID from response: {milestone_id}")
                            return milestone_id
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"⚠️ Could not parse milestone response line: {e}")
                    continue
        
        # Fallback: try to find milestone ID pattern in the response
        milestone_id_pattern = r'"milestone":\s*\{\s*[^}]*"id":\s*\{\s*"uuid":\s*"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"\s*\}'
        matches = re.findall(milestone_id_pattern, response_text)
        
        if matches:
            milestone_id = matches[0]
            print(f"Extracted milestone ID via regex: {milestone_id}")
            return milestone_id
                    
    except Exception as e:
        print(f"⚠️ Error extracting milestone ID: {e}")
        
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


# ========== DYNAMIC HEADER EXTRACTION FUNCTIONS ==========

def extract_next_action_from_page(page_html):
    """
    Extract Next-Action header value from a page's HTML.
    Enhanced patterns to work with actual Next.js server-rendered content.
    
    Args:
        page_html: HTML content of the page
        
    Returns:
        str: Next-Action header value or None if not found
    """
    try:
        # Pattern 1: Look for form action attributes with various formats
        form_patterns = [
            r'<form[^>]*action="([a-f0-9]{40})"',
            r'action\s*=\s*["\']([a-f0-9]{40})["\']',
            r'formAction\s*[=:]\s*["\']([a-f0-9]{40})["\']'
        ]
        
        for pattern in form_patterns:
            matches = re.findall(pattern, page_html, re.IGNORECASE)
            if matches:
                print(f"Found action hash via form pattern: {matches[0][:8]}...")
                return matches[0]
        
        # Pattern 2: Look for data attributes
        data_patterns = [
            r'data-next-action="([a-f0-9]{40})"',
            r'data-action="([a-f0-9]{40})"',
            r'data-server-action="([a-f0-9]{40})"'
        ]
        
        for pattern in data_patterns:
            matches = re.findall(pattern, page_html, re.IGNORECASE)
            if matches:
                print(f"Found action hash via data attribute: {matches[0][:8]}...")
                return matches[0]
        
        # Pattern 3: Look for JavaScript/JSON objects containing action hashes
        js_patterns = [
            r'"action"\s*:\s*"([a-f0-9]{40})"',
            r'"serverAction"\s*:\s*"([a-f0-9]{40})"',
            r'"nextAction"\s*:\s*"([a-f0-9]{40})"',
            r'nextAction\s*:\s*["\']([a-f0-9]{40})["\']',
            r'action\s*:\s*["\']([a-f0-9]{40})["\']'
        ]
        
        for pattern in js_patterns:
            matches = re.findall(pattern, page_html, re.IGNORECASE)
            if matches:
                print(f"Found action hash via JS pattern: {matches[0][:8]}...")
                return matches[0]
        
        # Pattern 4: Look for webpack/module references
        module_patterns = [
            r'__webpack_require__[^"]*"([a-f0-9]{40})"',
            r'__webpack_exports__[^"]*"([a-f0-9]{40})"',
            r'module\.exports[^"]*"([a-f0-9]{40})"',
            r'function\(\)\s*\{\s*return\s*"([a-f0-9]{40})"\s*\}',
            r'exports[^"]*"([a-f0-9]{40})"',
            r'return\s*"([a-f0-9]{40})"'
        ]
        
        for pattern in module_patterns:
            matches = re.findall(pattern, page_html)
            if matches:
                print(f"Found action hash via module pattern: {matches[0][:8]}...")
                return matches[0]
        
        # Pattern 5: Look for any 40-character hex strings in context that might be action hashes
        # This is more aggressive but may find embedded hashes
        context_patterns = [
            r'(?:action|server|next).*?([a-f0-9]{40})',
            r'([a-f0-9]{40}).*?(?:action|server|next)',
            r'"([a-f0-9]{40})"[^"]*(?:action|server|component)'
        ]
        
        for pattern in context_patterns:
            matches = re.findall(pattern, page_html, re.IGNORECASE)
            if matches:
                # Validate that this looks like a real action hash (not just any hex string)
                for match in matches:
                    if len(match) == 40 and all(c in '0123456789abcdef' for c in match):
                        print(f"Found action hash via context pattern: {match[:8]}...")
                        return match
        
        print("⚠️ Could not find Next-Action in page HTML using any pattern")
        
        # Debug: Show a sample of the page content to help improve patterns
        if len(page_html) > 0:
            # Look for any 40-char hex strings at all
            all_hex_patterns = re.findall(r'[a-f0-9]{40}', page_html)
            if all_hex_patterns:
                print(f"⚠️ Found {len(all_hex_patterns)} potential action hashes in page, but none matched our patterns")
                print(f"⚠️ First few: {[h[:8] + '...' for h in all_hex_patterns[:3]]}")
            else:
                print(f"⚠️ No 40-character hex strings found in page (length: {len(page_html)})")
        
        return None
        
    except Exception as e:
        print(f"⚠️ Error extracting Next-Action from page: {e}")
        return None


def build_router_state_tree(path, project_id=None, encoded=True):
    """
    Build Next-Router-State-Tree header value for a given path.
    
    Args:
        path: The page path (e.g., "/v2/projects", "/project/{id}/plan")
        project_id: Project UUID if needed for the path
        encoded: Whether to return URL-encoded version (default True)
        
    Returns:
        str: Next-Router-State-Tree header value
    """
    try:
        if path == "/v2/projects":
            # Projects list page structure
            state_tree = [
                "",
                {
                    "children": [
                        "(protected)",
                        {
                            "children": [
                                "v2",
                                {
                                    "children": [
                                        "projects",
                                        {
                                            "children": [
                                                "(list)",
                                                {
                                                    "children": [
                                                        "__PAGE__",
                                                        {},
                                                        "/v2/projects",
                                                        "refresh"
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "navigation": ["__DEFAULT__", {}]
                        }
                    ]
                },
                None,
                None,
                True
            ]
        elif path.startswith("/project/") and path.endswith("/plan"):
            # Project plan page structure
            if not project_id:
                raise ValueError("project_id required for project plan pages")
                
            state_tree = [
                "",
                {
                    "children": [
                        "(protected)",
                        {
                            "children": [
                                "project",
                                {
                                    "children": [
                                        ["projectId", project_id, "d"],
                                        {
                                            "children": [
                                                "plan",
                                                {
                                                    "children": [
                                                        "__PAGE__",
                                                        {},
                                                        f"/project/{project_id}/plan",
                                                        "refresh"
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "navigation": ["__DEFAULT__", {}]
                        }
                    ]
                },
                None,
                None,
                True
            ]
        else:
            print(f"⚠️ Unknown path pattern for router state: {path}")
            return None
        
        # Convert to JSON string
        state_json = json.dumps(state_tree, separators=(',', ':'))
        
        # URL encode if requested
        if encoded:
            return urllib.parse.quote(state_json)
        else:
            return state_json
            
    except Exception as e:
        print(f"⚠️ Error building router state tree: {e}")
        return None


def get_project_creation_headers(client):
    """
    Get dynamic headers for project creation by loading the projects page.
    
    Args:
        client: Locust HTTP client
        
    Returns:
        dict: Headers for project creation or None if failed
    """
    try:
        print("Loading projects page to get dynamic headers...")
        
        # Load the projects page to extract dynamic values
        with client.get("/v2/projects", catch_response=True, name="get_project_headers") as response:
            if response.status_code == 200:
                # Try to extract Next-Action from the page
                next_action = extract_next_action_from_page(response.text)
                
                # Build router state tree for projects page
                router_state = build_router_state_tree("/v2/projects")
                
                if next_action and router_state:
                    headers = {
                        'Accept': 'text/x-component',
                        'Content-Type': 'text/plain;charset=UTF-8',
                        'Next-Action': next_action,
                        'Next-Router-State-Tree': router_state
                    }
                    print(f"Successfully extracted project creation headers with action: {next_action[:8]}...")
                    return headers
                else:
                    print("⚠️ Could not extract dynamic values, falling back to verified headers")
                    return None
            else:
                print(f"⚠️ Failed to load projects page: {response.status_code}")
                return None
                
    except Exception as e:
        print(f"⚠️ Error getting project creation headers: {e}")
        return None


def get_project_plan_headers(client, project_id, phase_id=None):
    """
    Get dynamic headers for project plan operations (phases, milestones, tasks).
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase (optional, for URL params)
        
    Returns:
        dict: Headers for project plan operations or None if failed
    """
    try:
        print(f"Loading project plan page to get dynamic headers for project {project_id[:8]}...")
        
        # Build the plan page URL
        plan_url = f"/project/{project_id}/plan"
        params = {}
        if phase_id:
            params['phase'] = phase_id
            params['view'] = 'board'
        
        # Load the project plan page to extract dynamic values
        with client.get(plan_url, params=params, catch_response=True, name="get_plan_headers") as response:
            if response.status_code == 200:
                # Try to extract Next-Action from the page
                next_action = extract_next_action_from_page(response.text)
                
                # Build router state tree for project plan page
                router_state = build_router_state_tree(plan_url, project_id)
                
                if next_action and router_state:
                    headers = {
                        'Content-Type': 'text/plain;charset=UTF-8',
                        'Accept': 'text/x-component',
                        'Next-Action': next_action,
                        'Next-Router-State-Tree': router_state
                    }
                    print(f"Successfully extracted project plan headers with action: {next_action[:8]}...")
                    return headers
                else:
                    print("⚠️ Could not extract dynamic values, falling back to verified headers")
                    return None
            else:
                print(f"⚠️ Failed to load project plan page: {response.status_code}")
                return None
                
    except Exception as e:
        print(f"⚠️ Error getting project plan headers: {e}")
        return None


def get_fallback_headers(action_type="default"):
    """
    Get fallback static headers when dynamic extraction fails.
    Uses verified action hashes from HAR analysis.
    
    Args:
        action_type: Type of action (project_create, project_plan, etc.)
        
    Returns:
        dict: Fallback headers with verified action hashes
    """
    fallback_headers = {
        'Accept': 'text/x-component',
        'Content-Type': 'text/plain;charset=UTF-8'
    }
    
    # Add action-specific fallbacks using verified hashes from HAR analysis
    if action_type == "project_create":
        fallback_headers.update({
            'Next-Action': '83cef14cae8a2ba4da184ad4fb26161dd04c149c',  # Verified from CreateProject.har
            'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
        })
    elif action_type in ["phase_create", "milestone_create", "task_create", "subtask_create", "project_plan"]:
        # Different action hashes for different operations
        if action_type == "milestone_create":
            fallback_headers.update({
                'Next-Action': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5',  # Verified from CreateMilestone.har
            })
        else:
            # Phase, task, subtask creation use the same action hash
            fallback_headers.update({
                'Next-Action': '15d3270c2971f5e4e99b1316e5ea51e002989af7',  # Verified from create_phase.har, createingatask.har
            })
        
        # For milestone and task operations, add a generic router state tree for project plan pages
        # This will need to be built dynamically for the specific project, but use a generic structure
        if action_type in ["milestone_create", "task_create", "subtask_create"]:
            # Generic router state tree structure for project plan operations
            # Note: This is a simplified version that should work for most cases
            generic_router_state = '%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F%5BprojectId%5D%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
            fallback_headers['Next-Router-State-Tree'] = generic_router_state
            
    elif action_type == "project_rename":
        fallback_headers.update({
            'Next-Action': '75aaedb01b5c98f20a569b8a7a97ee1fa04c3acf'  # From original HAR analysis
        })
    elif action_type == "project_delete":
        fallback_headers.update({
            'Next-Action': '0a17c17cfd2792b0b228f1f194c95d78f6cb5330'  # From original HAR analysis
        })
    
    print(f"🔧 Using verified fallback headers for {action_type}")
    if 'Next-Action' in fallback_headers:
        print(f"🎯 Fallback Next-Action: {fallback_headers['Next-Action'][:8]}...")
    return fallback_headers


def get_dynamic_headers(client, action_type, project_id=None, phase_id=None):
    """
    Main function to get dynamic headers for any operation.
    
    Args:
        client: Locust HTTP client
        action_type: Type of action (project_create, project_plan, etc.)
        project_id: UUID of the project (if needed)
        phase_id: UUID of the phase (if needed)
        
    Returns:
        dict: Dynamic headers for the operation
    """
    # Define verified working hashes to validate against
    verified_hashes = {
        'project_create': '83cef14cae8a2ba4da184ad4fb26161dd04c149c',
        'phase_create': '15d3270c2971f5e4e99b1316e5ea51e002989af7',
        'milestone_create': 'fad80c9e91456a1347f0b756268242cbcb7d9cd5',  # Correct hash from CreateMilestone.har line 1236
        'task_create': '15d3270c2971f5e4e99b1316e5ea51e002989af7',
        'subtask_create': '15d3270c2971f5e4e99b1316e5ea51e002989af7',
        'project_plan': '15d3270c2971f5e4e99b1316e5ea51e002989af7',
        'project_rename': '75aaedb01b5c98f20a569b8a7a97ee1fa04c3acf',
        'project_delete': '0a17c17cfd2792b0b228f1f194c95d78f6cb5330'
    }
    
    print(f"🔍 Attempting dynamic header extraction for {action_type}")
    expected_hash = verified_hashes.get(action_type, "unknown")
    print(f"🎯 Expected hash for {action_type}: {expected_hash[:8]}...")
    
    try:
        extracted_headers = None
        
        if action_type == "project_create":
            extracted_headers = get_project_creation_headers(client)
        elif action_type in ["phase_create", "milestone_create", "task_create", "subtask_create", "project_plan"]:
            extracted_headers = get_project_plan_headers(client, project_id, phase_id)
        elif action_type in ["project_rename", "project_delete"]:
            extracted_headers = get_project_creation_headers(client)
        else:
            print(f"⚠️ Unknown action type: {action_type}")
            return get_fallback_headers(action_type)
        
        # Validate the extracted action hash
        if extracted_headers and 'Next-Action' in extracted_headers:
            extracted_hash = extracted_headers['Next-Action']
            expected_hash = verified_hashes.get(action_type)
            
            print(f"🔎 Extracted hash: {extracted_hash[:8]}...")
            print(f"🎯 Expected hash:  {expected_hash[:8]}...")
            
            if extracted_hash == expected_hash:
                print(f"✅ Dynamic extraction successful - hash matches verified!")
                return extracted_headers
            else:
                print(f"❌ Dynamic extraction found WRONG hash!")
                print(f"🔄 Using verified fallback headers instead of extracted headers")
                return get_fallback_headers(action_type)
        else:
            print(f"⚠️ Dynamic extraction failed - no Next-Action header found in extracted headers")
            if extracted_headers:
                print(f"📋 Available headers: {list(extracted_headers.keys())}")
            print(f"🔄 Using verified fallback headers")
            return get_fallback_headers(action_type)
        
    except Exception as e:
        print(f"❌ Error in dynamic header extraction for {action_type}: {e}")
        print(f"🔄 Using fallback headers due to exception")
        return get_fallback_headers(action_type)


# Legacy dynamic extraction functions (kept for future improvements)
def get_dynamic_headers_experimental(client, action_type, project_id=None, phase_id=None):
    """
    Experimental dynamic header extraction. Currently disabled in favor of verified headers.
    Can be re-enabled once we solve the action hash validation problem.
    """
    try:
        if action_type == "project_create":
            headers = get_project_creation_headers(client)
        elif action_type in ["phase_create", "milestone_create", "task_create", "subtask_create", "project_plan"]:
            headers = get_project_plan_headers(client, project_id, phase_id)
        elif action_type in ["project_rename", "project_delete"]:
            headers = get_project_creation_headers(client)  # Use project headers for project operations
        else:
            print(f"⚠️ Unknown action type: {action_type}")
            headers = get_fallback_headers(action_type)
        
        return headers if headers else get_fallback_headers(action_type)
        
    except Exception as e:
        print(f"⚠️ Error getting dynamic headers: {e}")
        return get_fallback_headers(action_type)
