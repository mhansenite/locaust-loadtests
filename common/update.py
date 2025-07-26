#!/usr/bin/env python3
"""
Task Update Functions for GuideCX Load Testing

This module contains functions for updating existing tasks, including status updates,
assignment changes, date modifications, and other task property updates.
"""

import json
import random
from datetime import datetime, timedelta
from .helpers import debug_print


def update_task_status(client, project_id, phase_id, task_id, status_name, explanation=""):
    """
    Update task status using the project plan API
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase (for URL parameters)
        task_id: UUID of the task to update
        status_name: Name of the status to set (e.g., "Done", "In Progress", etc.)
        explanation: Optional explanation for status change
        
    Returns:
        bool: True if successful, False otherwise
    """
    
    print(f"[UPDATE] Starting update_task_status for task: {task_id[:8]}... -> '{status_name}'")
    
    debug_print(f"TASK STATUS UPDATE DEBUG START")
    debug_print(f"   - Project ID: {project_id}")
    debug_print(f"   - Phase ID: {phase_id}")
    debug_print(f"   - Task ID: {task_id}")
    debug_print(f"   - Target Status: '{status_name}'")
    debug_print(f"   - Explanation: '{explanation}'")
    
    # Import dynamic status extraction from extractdata
    from .extractdata import get_available_task_statuses_from_api, get_fallback_task_statuses
    
    print(f"[UPDATE] Fetching available statuses from API...")
    
    # Get the available statuses dynamically from the API
    debug_print(f"FETCHING available statuses for status update...")
    available_statuses = get_available_task_statuses_from_api(client, project_id, phase_id)
    
    print(f"[UPDATE] API returned {len(available_statuses) if available_statuses else 0} statuses")
    
    # Fallback if API call failed
    if not available_statuses:
        debug_print(f"⚠️ Could not fetch statuses from API, using fallback statuses")
        available_statuses = get_fallback_task_statuses()
        print(f"[UPDATE] Using fallback statuses: {len(available_statuses)} statuses")
    
    # Log all available statuses for debugging
    debug_print(f"AVAILABLE status options:")
    for status_name_key, status_info in available_statuses.items():
        status_uuid = status_info.get("uuid", "NO_UUID")
        debug_print(f"   - '{status_name_key}' -> {status_uuid}")
    
    # Convert to simple name -> UUID mapping for backward compatibility
    status_mapping = {
        status_name: status_info["uuid"] 
        for status_name, status_info in available_statuses.items()
    }
    
    print(f"[UPDATE] Looking for status '{status_name}' in available options...")
    
    # Get status ID
    status_id = status_mapping.get(status_name)
    if not status_id:
        print(f"[UPDATE] ❌ Unknown status: '{status_name}'. Available: {list(status_mapping.keys())}")
        debug_print(f"❌ Unknown status: '{status_name}'. Available: {list(status_mapping.keys())}")
        debug_print(f"🔍 Status mapping debug: {status_mapping}")
        return False
    
    print(f"[UPDATE] Found status UUID: {status_id[:8]}... for '{status_name}'")
    debug_print(f"🔍 Using status UUID: {status_id} for '{status_name}'")
    
    try:
        print(f"[UPDATE] Importing update_task_status_api from view module...")
        
        # Import view function (avoiding circular imports)
        from .view import update_task_status_api
        
        print(f"[UPDATE] Calling update_task_status_api...")
        debug_print(f"CALLING update_task_status_api...")
        
        # Use view.py function to make the API call
        success, response_text, status_code = update_task_status_api(
            client, project_id, phase_id, task_id, status_id, explanation
        )
        
        print(f"[UPDATE] API call completed - Success: {success}, Status: {status_code}")
        print(f"[UPDATE] Response preview: {response_text[:500] if response_text else 'NO_RESPONSE'}...")
        
        debug_print(f"🔍 API call returned:")
        debug_print(f"   - Success: {success}")
        debug_print(f"   - Status Code: {status_code}")
        debug_print(f"   - Response Length: {len(response_text) if response_text else 0} characters")
        debug_print(f"   - Response Preview: {response_text[:300] if response_text else 'NO_RESPONSE'}")
        
        if success:
            print(f"[UPDATE] ✅ Successfully updated task status to '{status_name}'")
            
            try:
                # Parse response for detailed analysis
                debug_print(f"🔍 Analyzing response content...")
                
                # Check if response contains success indicator
                if 'response' in response_text and 'status' in response_text:
                    debug_print(f"✅ Response contains expected 'response' and 'status' fields")
                    
                    # Try to parse JSON for more details
                    try:
                        import re
                        # Look for JSON in the response (similar to other extractors)
                        json_match = re.search(r'\d+:(\{.*\})', response_text)
                        if json_match:
                            json_str = json_match.group(1)
                            parsed_data = json.loads(json_str)
                            debug_print(f"🔍 Parsed response JSON: {json.dumps(parsed_data, indent=2)}")
                            
                            # Check for error indicators
                            if parsed_data.get('error'):
                                debug_print(f"❌ API returned error: {parsed_data['error']}")
                                return False
                            
                            # Check response status
                            response_info = parsed_data.get('response', {}).get('info', {})
                            response_status = response_info.get('status')
                            response_message = response_info.get('message', '')
                            
                            debug_print(f"🔍 Response status: {response_status}")
                            debug_print(f"🔍 Response message: '{response_message}'")
                            
                            if response_status == 0:  # Assuming 0 means success
                                debug_print(f"✅ Successfully updated task status to '{status_name}'")
                                return True
                            else:
                                debug_print(f"⚠️ Unexpected response status: {response_status}")
                                return False
                        else:
                            debug_print(f"⚠️ Could not find JSON in response")
                            return True  # Assume success if 200 OK
                            
                    except json.JSONDecodeError as je:
                        debug_print(f"⚠️ Could not parse response JSON: {je}")
                        return True  # Assume success if 200 OK
                    except Exception as pe:
                        debug_print(f"⚠️ Error parsing response: {pe}")
                        return True  # Assume success if 200 OK
                        
                else:
                    debug_print(f"⚠️ Status update response does not contain expected fields")
                    debug_print(f"🔍 Full response text: {response_text}")
                    return True  # Assume success if 200 OK
                    
            except Exception as e:
                debug_print(f"⚠️ Error parsing status update response: {e}")
                debug_print(f"🔍 Raw response for debugging: {response_text}")
                return True  # Assume success if 200 OK
                
        elif status_code == 401:
            print(f"[UPDATE] ❌ Authentication failed for status update")
            debug_print(f"❌ Authentication failed for status update")
            return False
        elif status_code == 403:
            print(f"[UPDATE] ❌ Access denied for status update")
            debug_print(f"❌ Access denied for status update")
            return False
        else:
            print(f"[UPDATE] ❌ Status update failed with status code: {status_code}")
            debug_print(f"❌ Status update failed with status code: {status_code}")
            debug_print(f"🔍 Error response: {response_text}")
            return False
                
    except Exception as e:
        print(f"[UPDATE] ❌ Exception in update_task_status: {e}")
        debug_print(f"💥 Exception in update_task_status: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        print(f"[UPDATE] Completed update_task_status for task: {task_id[:8]}...")
        debug_print(f"🔍 TASK STATUS UPDATE DEBUG END")
        debug_print(f"")  # Add blank line for readability


def update_task(client, project_id, task_id, updates):
    """
    Update an existing task with new properties (placeholder for future implementations)
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        task_id: UUID of the task to update
        updates: Dictionary of updates to apply
        
    Returns:
        bool: True if successful, False otherwise
        
    Note: This is a placeholder - requires task update HAR file analysis for implementation
    """
    debug_print(f"Updating task {task_id[:8]}...")
    
    # TODO: Implement specific update functions based on HAR file analysis
    # For now, this is a placeholder showing the structure
    
    if 'assignee' in updates:
        debug_print(f"     • Assignee: {updates['assignee']}")
    if 'status' in updates:
        debug_print(f"     • Status: {updates['status']}")
    if 'estimated_hours' in updates:
        debug_print(f"     • Estimated: {updates['estimated_hours']}h")
    if 'due_date' in updates:
        debug_print(f"     • Due: {updates['due_date']}")
    if 'priority' in updates:
        debug_print(f"     • Priority: {updates['priority']}")
    
    debug_print(f"     Task update simulated (need HAR file for real API)")
    return True  # Simulated success


def generate_task_updates():
    """Generate random task updates for testing"""
    assignees = [
        "John Smith", "Sarah Johnson", "Mike Chen", "Lisa Rodriguez", 
        "David Kim", "Emily Brown", "Alex Taylor", "Jennifer Wilson"
    ]
    
    statuses = ["To Do", "In Progress", "Review", "Done", "Blocked"]
    priorities = ["Low", "Medium", "High", "Critical"]
    
    return {
        "assignee": random.choice(assignees),
        "status": random.choice(statuses),
        "estimated_hours": random.randint(1, 40),
        "start_date": (datetime.now() + timedelta(days=random.randint(0, 14))).strftime("%Y-%m-%d"),
        "due_date": (datetime.now() + timedelta(days=random.randint(15, 45))).strftime("%Y-%m-%d"),
        "progress": random.randint(0, 100),
        "priority": random.choice(priorities)
    }
