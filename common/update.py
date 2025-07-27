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
    
    debug_print(f"[UPDATE] Found status UUID: {status_id[:8]}... for '{status_name}'")
    debug_print(f"🔍 Using status UUID: {status_id} for '{status_name}'")
    
    try:
        debug_print(f"[UPDATE] Importing update_task_status_api from view module...")
        
        # Import view function (avoiding circular imports)
        from .view import update_task_status_api
        
        debug_print(f"[UPDATE] Calling update_task_status_api...")
        debug_print(f"CALLING update_task_status_api...")
        
        # Use view.py function to make the API call
        success, response_text, status_code = update_task_status_api(
            client, project_id, phase_id, task_id, status_id, explanation
        )
        
        debug_print(f"[UPDATE] API call completed - Success: {success}, Status: {status_code}")
        debug_print(f"[UPDATE] Response preview: {response_text[:500] if response_text else 'NO_RESPONSE'}...")
        
        debug_print(f"🔍 API call returned:")
        debug_print(f"   - Success: {success}")
        debug_print(f"   - Status Code: {status_code}")
        debug_print(f"   - Response Length: {len(response_text) if response_text else 0} characters")
        debug_print(f"   - Response Preview: {response_text[:300] if response_text else 'NO_RESPONSE'}")
        
        if success:
            debug_print(f"[UPDATE] ✅ Successfully updated task status to '{status_name}'")
            
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
                            
                            # Check response status - handle null response field
                            response_data = parsed_data.get('response')
                            if response_data is None:
                                debug_print(f"⚠️ Response field is null, treating as error")
                                return False
                            
                            response_info = response_data.get('info', {})
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
        debug_print(f"[UPDATE] Completed update_task_status for task: {task_id[:8]}...")
        debug_print(f"🔍 TASK STATUS UPDATE DEBUG END")
        debug_print(f"")  # Add blank line for readability


def update_task_estimated_hours(client, project_id, phase_id, task_id, estimated_hours):
    """
    Update task estimated hours using the project plan API
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase (for URL parameters)
        task_id: UUID of the task to update
        estimated_hours: Number of estimated hours to set
        
    Returns:
        bool: True if successful, False otherwise
        
    Based on TaskUpdateEstHours.har analysis:
    - URL: /project/{project_id}/plan?phase={phase_id}&view=board&task-id={task_id}&task-drawer-tab=details
    - Method: POST
    - Payload: [{"id": {"uuid": task_id}, "estimatedHours": estimated_hours}]
    """
    
    print(f"[UPDATE] Starting update_task_estimated_hours for task: {task_id[:8]}... -> {estimated_hours}h")
    
    debug_print(f"TASK ESTIMATED HOURS UPDATE DEBUG START")
    debug_print(f"   - Project ID: {project_id}")
    debug_print(f"   - Phase ID: {phase_id}")
    debug_print(f"   - Task ID: {task_id}")
    debug_print(f"   - Estimated Hours: {estimated_hours}")
    
    try:
        print(f"[UPDATE] Preparing API call...")
        
        # Based on TaskUpdateEstHours.har analysis
        update_url = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board',
            'task-id': task_id,
            'task-drawer-tab': 'details'
        }
        
        debug_print(f"🔍 Request URL: {update_url}")
        debug_print(f"🔍 Request Parameters: {params}")
        
        # Payload format from HAR file - EXACT match to working request
        payload_data = [{
            "id": {"uuid": task_id},
            "estimatedHours": estimated_hours
        }]
        hours_payload = json.dumps(payload_data)
        
        debug_print(f"🔍 Request Payload Data: {payload_data}")
        debug_print(f"🔍 Request Payload JSON: {hours_payload}")
        
        # Headers based on TaskUpdateEstHours.har - CRITICAL: Next-Action is required for Next.js Server Actions
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': 'text/x-component',
            'Next-Action': '5c0018c251e1f4df53ca01c659f4c781d2468788',  # From successful HAR - this is crucial!
            'Origin': 'https://app.staging.guidecx.io',
        }
        
        debug_print(f"🔍 Request Headers: {headers}")
        
        # Construct full URL for logging
        from urllib.parse import urlencode
        full_url = f"{update_url}?{urlencode(params)}"
        debug_print(f"🔍 Full Request URL: {full_url}")
        
        print(f"[UPDATE] Making POST request...")
        debug_print(f"🔍 Making POST request...")
        
        with client.post(
            update_url,
            params=params,
            data=hours_payload,
            headers=headers,
            catch_response=True,
            name="update_task_estimated_hours"
        ) as response:
            debug_print(f"🔍 HTTP Response Status: {response.status_code}")
            debug_print(f"🔍 Response Headers: {dict(response.headers)}")
            debug_print(f"🔍 Response Content-Type: {response.headers.get('content-type', 'NOT_SET')}")
            debug_print(f"🔍 Response Length: {len(response.text)} characters")
            
            if response.text:
                debug_print(f"🔍 Response Text (first 500 chars): {response.text[:500]}")
                if len(response.text) > 500:
                    debug_print(f"🔍 Response Text (last 200 chars): ...{response.text[-200:]}")
            else:
                debug_print(f"🔍 Response Text: EMPTY")
            
            print(f"[UPDATE] API call completed - Status: {response.status_code}")
            print(f"[UPDATE] Response preview: {response.text[:500] if response.text else 'NO_RESPONSE'}...")
            
            # Parse the response to determine actual success based on HAR analysis
            success = False
            if response.status_code == 200:
                try:
                    # From HAR: successful response contains: {"response":{"info":{"status":0,"message":""}},"error":null}
                    # Error response contains: {"response":null,"error":{"message":"Failed...","metadata":{...}}}
                    # The response is in a Next.js Server Action format: "1:{JSON_DATA}"
                    if response.text and ('"error"' in response.text or ('"response"' in response.text and '"info"' in response.text)):
                        # Extract JSON from Next.js Server Action format
                        import re
                        json_match = re.search(r'\d+:(\{.*\})', response.text)
                        if json_match:
                            json_str = json_match.group(1)
                            parsed_data = json.loads(json_str)
                            debug_print(f"🔍 Parsed response JSON: {json.dumps(parsed_data, indent=2)}")
                            
                            # Check for error in response
                            if parsed_data.get('error'):
                                debug_print(f"❌ API returned error: {parsed_data['error']}")
                                response.failure(f"API error: {parsed_data['error']}")
                                success = False
                            else:
                                # Check the response structure more thoroughly
                                response_data = parsed_data.get('response')
                                if response_data is None:
                                    debug_print(f"⚠️ Response field is null, treating as error")
                                    response.failure("Response field is null")
                                    success = False
                                else:
                                    info = response_data.get('info', {})
                                    info_status = info.get('status')
                                    info_message = info.get('message', '')
                                    
                                    debug_print(f"🔍 Response info.status: {info_status}")
                                    debug_print(f"🔍 Response info.message: '{info_message}'")
                                    
                                    # More robust success criteria for estimated hours:
                                    # 1. info.status must be 0 (no error code)
                                    # 2. info.message should be empty or not contain error keywords
                                    # 3. Check for common error patterns in message
                                    
                                    error_patterns = ['error', 'failed', 'invalid', 'unauthorized', 'forbidden', 'not found']
                                    message_has_error = any(pattern in info_message.lower() for pattern in error_patterns)
                                    
                                    if info_status == 0 and not message_has_error:
                                        debug_print(f"✅ Task estimated hours update successful!")
                                        response.success()
                                        success = True
                                    else:
                                        # Log why it failed
                                        reasons = []
                                        if info_status != 0:
                                            reasons.append(f"info.status={info_status}")
                                        if message_has_error:
                                            reasons.append(f"error in message: '{info_message}'")
                                            
                                        failure_reason = "; ".join(reasons)
                                        debug_print(f"❌ Task estimated hours update failed: {failure_reason}")
                                        debug_print(f"   info.message: '{info_message}'")
                                        response.failure(f"Estimated hours update failed: {failure_reason}")
                                        success = False
                        else:
                            debug_print(f"⚠️ Could not parse Next.js Server Action response format")
                            debug_print(f"🔍 Raw response: {response.text}")
                            response.failure("Could not parse response format")
                            success = False
                    else:
                        debug_print(f"⚠️ Response missing expected fields ('response' and 'info')")
                        debug_print(f"🔍 Raw response: {response.text}")
                        response.failure("Response missing expected fields")
                        success = False
                        
                except json.JSONDecodeError as je:
                    debug_print(f"❌ JSON decode error: {je}")
                    debug_print(f"🔍 Raw response: {response.text}")
                    response.failure(f"JSON decode error: {je}")
                    success = False
                except Exception as e:
                    debug_print(f"❌ Error parsing response: {e}")
                    debug_print(f"🔍 Raw response: {response.text}")
                    response.failure(f"Response parsing error: {e}")
                    success = False
            else:
                debug_print(f"❌ HTTP request failed with status {response.status_code}")
                response.failure(f"HTTP {response.status_code}")
                success = False
            
            if success:
                print(f"[UPDATE] ✅ Successfully updated task estimated hours to {estimated_hours}h")
                return True
            elif response.status_code == 401:
                print(f"[UPDATE] ❌ Authentication failed for estimated hours update")
                debug_print(f"❌ Authentication failed for estimated hours update")
                return False
            elif response.status_code == 403:
                print(f"[UPDATE] ❌ Access denied for estimated hours update")
                debug_print(f"❌ Access denied for estimated hours update")
                return False
            else:
                print(f"[UPDATE] ❌ Estimated hours update failed with status code: {response.status_code}")
                debug_print(f"❌ Estimated hours update failed with status code: {response.status_code}")
                debug_print(f"🔍 Error response: {response.text}")
                return False
                
    except Exception as e:
        print(f"[UPDATE] ❌ Exception in update_task_estimated_hours: {e}")
        debug_print(f"💥 Exception in update_task_estimated_hours: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        print(f"[UPDATE] Completed update_task_estimated_hours for task: {task_id[:8]}...")
        debug_print(f"🔍 TASK ESTIMATED HOURS UPDATE DEBUG END")
        debug_print(f"")  # Add blank line for readability


def update_task_dates(client, project_id, phase_id, task_id, start_date=None, due_date=None):
    """
    Update task start and due dates using the project plan API
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase (for URL parameters)
        task_id: UUID of the task to update
        start_date: datetime object for start date, or None to unset
        due_date: datetime object for due date, or None to unset
        
    Returns:
        bool: True if successful, False otherwise
        
    Based on UpdateTaskDate.har analysis:
    - URL: /project/{project_id}/plan?phase={phase_id}&view=board&task-id={task_id}&task-drawer-tab=details
    - Method: POST
    - Payload: [{"id": {"uuid": task_id}, "dueDate": {"seconds": "timestamp", "nanos": 0}, "startDate": "$undefined" or {"seconds": "timestamp", "nanos": 0}}]
    """
    
    print(f"[UPDATE] Starting update_task_dates for task: {task_id[:8]}...")
    
    debug_print(f"TASK DATES UPDATE DEBUG START")
    debug_print(f"   - Project ID: {project_id}")
    debug_print(f"   - Phase ID: {phase_id}")
    debug_print(f"   - Task ID: {task_id}")
    debug_print(f"   - Start Date: {start_date}")
    debug_print(f"   - Due Date: {due_date}")
    
    try:
        print(f"[UPDATE] Preparing API call...")
        
        # Based on UpdateTaskDate.har analysis
        update_url = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board',
            'task-id': task_id,
            'task-drawer-tab': 'details'
        }
        
        debug_print(f"🔍 Request URL: {update_url}")
        debug_print(f"🔍 Request Parameters: {params}")
        
        # Payload format from HAR file - EXACT match to working request
        payload_data = {
            "id": {"uuid": task_id}
        }
        
        # Handle due date - convert to seconds timestamp or set to "$undefined"
        if due_date:
            due_timestamp = str(int(due_date.timestamp()))
            payload_data["dueDate"] = {"seconds": due_timestamp, "nanos": 0}
            debug_print(f"🔍 Due date: {due_date} -> timestamp: {due_timestamp}")
        else:
            payload_data["dueDate"] = "$undefined"
            debug_print(f"🔍 Due date: unset (using $undefined)")
        
        # Handle start date - convert to seconds timestamp or set to "$undefined"
        if start_date:
            start_timestamp = str(int(start_date.timestamp()))
            payload_data["startDate"] = {"seconds": start_timestamp, "nanos": 0}
            debug_print(f"🔍 Start date: {start_date} -> timestamp: {start_timestamp}")
        else:
            payload_data["startDate"] = "$undefined"
            debug_print(f"🔍 Start date: unset (using $undefined)")
        
        # Wrap in array as shown in HAR
        dates_payload = json.dumps([payload_data])
        
        debug_print(f"🔍 Request Payload Data: {[payload_data]}")
        debug_print(f"🔍 Request Payload JSON: {dates_payload}")
        
        # Headers based on UpdateTaskDate.har - CRITICAL: Next-Action is required for Next.js Server Actions
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': 'text/x-component',
            'Next-Action': '5268054c851d66d770d67a03d9d7209b7afe9977',  # From UpdateTaskDate.har - different from estimated hours!
            'Origin': 'https://app.staging.guidecx.io',
        }
        
        debug_print(f"🔍 Request Headers: {headers}")
        
        # Construct full URL for logging
        from urllib.parse import urlencode
        full_url = f"{update_url}?{urlencode(params)}"
        debug_print(f"🔍 Full Request URL: {full_url}")
        
        print(f"[UPDATE] Making POST request...")
        debug_print(f"🔍 Making POST request...")
        
        with client.post(
            update_url,
            params=params,
            data=dates_payload,
            headers=headers,
            catch_response=True,
            name="update_task_dates"
        ) as response:
            debug_print(f"🔍 HTTP Response Status: {response.status_code}")
            debug_print(f"🔍 Response Headers: {dict(response.headers)}")
            debug_print(f"🔍 Response Content-Type: {response.headers.get('content-type', 'NOT_SET')}")
            debug_print(f"🔍 Response Length: {len(response.text)} characters")
            
            if response.text:
                debug_print(f"🔍 Response Text (first 500 chars): {response.text[:500]}")
                if len(response.text) > 500:
                    debug_print(f"🔍 Response Text (last 200 chars): ...{response.text[-200:]}")
            else:
                debug_print(f"🔍 Response Text: EMPTY")
            
            print(f"[UPDATE] API call completed - Status: {response.status_code}")
            print(f"[UPDATE] Response preview: {response.text[:500] if response.text else 'NO_RESPONSE'}...")
            
            # Parse the response to determine actual success based on HAR analysis
            success = False
            if response.status_code == 200:
                try:
                    # From HAR: successful response contains: {"response":{"info":{"status":0,"message":""}},"error":null}
                    # Error response contains: {"response":null,"error":{"message":"Failed...","metadata":{...}}}
                    # The response is in a Next.js Server Action format: "1:{JSON_DATA}"
                    if response.text and ('"error"' in response.text or ('"response"' in response.text and '"info"' in response.text)):
                        # Extract JSON from Next.js Server Action format
                        import re
                        json_match = re.search(r'\d+:(\{.*\})', response.text)
                        if json_match:
                            json_str = json_match.group(1)
                            parsed_data = json.loads(json_str)
                            debug_print(f"🔍 Parsed response JSON: {json.dumps(parsed_data, indent=2)}")
                            
                            # Check for error in response
                            if parsed_data.get('error'):
                                debug_print(f"❌ API returned error: {parsed_data['error']}")
                                response.failure(f"API error: {parsed_data['error']}")
                                success = False
                            else:
                                # Check the response structure more thoroughly
                                response_data = parsed_data.get('response')
                                if response_data is None:
                                    debug_print(f"⚠️ Response field is null, treating as error")
                                    response.failure("Response field is null")
                                    success = False
                                else:
                                    info = response_data.get('info', {})
                                    info_status = info.get('status')
                                    info_message = info.get('message', '')
                                    
                                    debug_print(f"🔍 Response info.status: {info_status}")
                                    debug_print(f"🔍 Response info.message: '{info_message}'")
                                    
                                    # More robust success criteria for date updates:
                                    # 1. info.status must be 0 (no error code)
                                    # 2. info.message should be empty or not contain error keywords
                                    # 3. Check for common error patterns in message
                                    
                                    error_patterns = ['error', 'failed', 'invalid', 'unauthorized', 'forbidden', 'not found']
                                    message_has_error = any(pattern in info_message.lower() for pattern in error_patterns)
                                    
                                    if info_status == 0 and not message_has_error:
                                        debug_print(f"✅ Task dates update successful!")
                                        response.success()
                                        success = True
                                    else:
                                        # Log why it failed
                                        reasons = []
                                        if info_status != 0:
                                            reasons.append(f"info.status={info_status}")
                                        if message_has_error:
                                            reasons.append(f"error in message: '{info_message}'")
                                            
                                        failure_reason = "; ".join(reasons)
                                        debug_print(f"❌ Task dates update failed: {failure_reason}")
                                        debug_print(f"   info.message: '{info_message}'")
                                        response.failure(f"Dates update failed: {failure_reason}")
                                        success = False
                        else:
                            debug_print(f"⚠️ Could not parse Next.js Server Action response format")
                            debug_print(f"🔍 Raw response: {response.text}")
                            response.failure("Could not parse response format")
                            success = False
                    else:
                        debug_print(f"⚠️ Response missing expected fields ('response' and 'info')")
                        debug_print(f"🔍 Raw response: {response.text}")
                        response.failure("Response missing expected fields")
                        success = False
                        
                except json.JSONDecodeError as je:
                    debug_print(f"❌ JSON decode error: {je}")
                    debug_print(f"🔍 Raw response: {response.text}")
                    response.failure(f"JSON decode error: {je}")
                    success = False
                except Exception as e:
                    debug_print(f"❌ Error parsing response: {e}")
                    debug_print(f"🔍 Raw response: {response.text}")
                    response.failure(f"Response parsing error: {e}")
                    success = False
            else:
                debug_print(f"❌ HTTP request failed with status {response.status_code}")
                response.failure(f"HTTP {response.status_code}")
                success = False
            
            if success:
                start_str = start_date.strftime('%Y-%m-%d') if start_date else 'unset'
                due_str = due_date.strftime('%Y-%m-%d') if due_date else 'unset'
                print(f"[UPDATE] ✅ Successfully updated task dates - Start: {start_str}, Due: {due_str}")
                return True
            elif response.status_code == 401:
                print(f"[UPDATE] ❌ Authentication failed for dates update")
                debug_print(f"❌ Authentication failed for dates update")
                return False
            elif response.status_code == 403:
                print(f"[UPDATE] ❌ Access denied for dates update")
                debug_print(f"❌ Access denied for dates update")
                return False
            else:
                print(f"[UPDATE] ❌ Dates update failed with status code: {response.status_code}")
                debug_print(f"❌ Dates update failed with status code: {response.status_code}")
                debug_print(f"🔍 Error response: {response.text}")
                return False
                
    except Exception as e:
        print(f"[UPDATE] ❌ Exception in update_task_dates: {e}")
        debug_print(f"💥 Exception in update_task_dates: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        print(f"[UPDATE] Completed update_task_dates for task: {task_id[:8]}...")
        debug_print(f"🔍 TASK DATES UPDATE DEBUG END")
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
