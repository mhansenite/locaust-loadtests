#!/usr/bin/env python3
"""
View/Get Functions for GuideCX Load Testing

This module contains functions for making API calls to view/get data from the application.
These functions return raw API responses, which are then processed by extraction functions
in extractdata.py to pull out the needed information.

Separation of concerns:
- view.py: Makes API calls, handles HTTP requests/responses
- extractdata.py: Processes raw response data, extracts structured information
"""

import json
from .helpers import debug_print


def view_task_details(client, project_id, task_id, phase_id=None):
    """
    Make API call to view task details including status information
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        task_id: UUID of the task to get details for
        phase_id: Optional phase ID for URL parameters
        
    Returns:
        tuple: (success: bool, response_text: str, status_code: int)
        
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
        
        # Add phase parameter if provided
        if phase_id:
            params['phase'] = phase_id
        
        # Construct URL with query parameters
        url_params = "&".join([f"{k}={v}" for k, v in params.items()])
        url = f"{endpoint}?{url_params}"
        
        # Request payload format from HAR
        payload = [{"taskId": task_id}]
        
        debug_print(f"Viewing task details: {task_id}")
        
        # Headers based on HAR analysis
        headers = {
            "Accept": "text/x-component",
            "Content-Type": "text/plain;charset=UTF-8",
            "Next-Action": "f4915f56dc7e1251c904d362345604917c93d6ba"  # From HAR file
        }
        
        with client.post(url, json=payload, headers=headers, catch_response=True, name="view_task_details") as response:
            debug_print(f"Task details API response: {response.status_code}")
            return (response.status_code == 200, response.text, response.status_code)
                
    except Exception as e:
        debug_print(f"💥 Exception viewing task details: {e}")
        return (False, str(e), 500)


def view_project_plan(client, project_id, phase_id, view_type="list"):
    """
    Make API call to view the project plan page
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        view_type: Type of view ("list", "board", etc.)
        
    Returns:
        tuple: (success: bool, response_text: str, status_code: int)
    """
    try:
        endpoint = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': view_type
        }
        
        # Construct URL with query parameters
        url_params = "&".join([f"{k}={v}" for k, v in params.items()])
        url = f"{endpoint}?{url_params}"
        
        debug_print(f"Viewing project plan: {project_id} (phase: {phase_id})")
        
        with client.get(url, catch_response=True, name="view_project_plan") as response:
            debug_print(f"Project plan API response: {response.status_code}")
            return (response.status_code == 200, response.text, response.status_code)
            
    except Exception as e:
        debug_print(f"💥 Exception viewing project plan: {e}")
        return (False, str(e), 500)


def view_task_with_drawer(client, project_id, phase_id, task_id, drawer_tab="details"):
    """
    Make API call to view a task with the task drawer open
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        task_id: UUID of the task
        drawer_tab: Which tab to open in the drawer ("details", "messages", etc.)
        
    Returns:
        tuple: (success: bool, response_text: str, status_code: int)
        
    This simulates opening a task in the task drawer, which may provide
    additional status information or dropdown options.
    """
    try:
        endpoint = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board',  # Default to board view for drawer
            'task-id': task_id,
            'task-drawer-tab': drawer_tab
        }
        
        # Construct URL with query parameters
        url_params = "&".join([f"{k}={v}" for k, v in params.items()])
        url = f"{endpoint}?{url_params}"
        
        debug_print(f"Opening task drawer: {task_id} (tab: {drawer_tab})")
        
        with client.get(url, catch_response=True, name="view_task_drawer") as response:
            debug_print(f"Task drawer API response: {response.status_code}")
            return (response.status_code == 200, response.text, response.status_code)
            
    except Exception as e:
        debug_print(f"💥 Exception viewing task drawer: {e}")
        return (False, str(e), 500)



def get_project_plan_status_options(client, project_id, phase_id):
    """
    Make API call to get status options from the project plan
    
    This makes the specific POST request that returns unitStatusOptions
    based on HAR file analysis.
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        
    Returns:
        tuple: (success: bool, response_text: str, status_code: int)
        
    Based on HAR file analysis:
    - URL: /project/{project_id}/plan
    - Method: POST
    - Payload: [{"projectId": {"uuid": project_id}, "phaseId": {"uuid": phase_id}, "filters": []}]
    - Response contains: unitStatusOptions array
    """
    try:
        # Build the request URL and payload based on HAR analysis
        endpoint = f"/project/{project_id}/plan"
        
        # Request payload format from HAR
        payload = [{"projectId": {"uuid": project_id}, "phaseId": {"uuid": phase_id}, "filters": []}]
        
        debug_print(f"Fetching project plan status options...")
        
        # Headers based on HAR analysis
        headers = {
            "Accept": "text/x-component",
            "Content-Type": "text/plain;charset=UTF-8",
            "Next-Action": "f0dcb167bb0486ad2aff91c85d8f91b40996dd37"  # From HAR file
        }
        
        with client.post(endpoint, json=payload, headers=headers, catch_response=True, name="get_project_plan_status_options") as response:
            debug_print(f"Project plan status options API response: {response.status_code}")
            return (response.status_code == 200, response.text, response.status_code)
                
    except Exception as e:
        debug_print(f"💥 Exception getting project plan status options: {e}")
        return (False, str(e), 500)


def update_task_status_api(client, project_id, phase_id, task_id, status_id, explanation=""):
    """
    Make API call to update a task's status
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase (for URL parameters)
        task_id: UUID of the task to update
        status_id: UUID of the status to set
        explanation: Optional explanation for status change
        
    Returns:
        tuple: (success: bool, response_text: str, status_code: int)
        
    Based on TaskUpdateStatus.har analysis:
    - URL: /project/{project_id}/plan?phase={phase_id}&view=board&task-id={task_id}&task-drawer-tab=details
    - Method: POST
    - Payload: [{"unitId": {"uuid": task_id}, "statusId": {"uuid": status_id}, "explanation": explanation}]
    """
    try:
        debug_print(f"🔍 UPDATE_TASK_STATUS_API DEBUG START")
        
        # Based on TaskUpdateStatus.har analysis
        update_url = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board',
            'task-id': task_id,
            'task-drawer-tab': 'details'
        }
        
        debug_print(f"🔍 Request URL: {update_url}")
        debug_print(f"🔍 Request Parameters: {params}")
        
        # Payload format from HAR file
        payload_data = [{
            "unitId": {"uuid": task_id},
            "statusId": {"uuid": status_id},
            "explanation": explanation
        }]
        status_payload = json.dumps(payload_data)
        
        debug_print(f"🔍 Request Payload Data: {payload_data}")
        debug_print(f"🔍 Request Payload JSON: {status_payload}")
        
        # Headers based on TaskUpdateStatus.har
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Accept': 'text/x-component',
            # 'Next-Action': '0ca3f6b0537f60187ded01a52a8a7942de8ab312',  # Removed - this was hardcoded from HAR
        }
        
        debug_print(f"🔍 Request Headers: {headers}")
        
        # Construct full URL for logging
        from urllib.parse import urlencode
        full_url = f"{update_url}?{urlencode(params)}"
        debug_print(f"🔍 Full Request URL: {full_url}")
        
        debug_print(f"🔍 Making POST request...")
        
        with client.post(
            update_url,
            params=params,
            data=status_payload,
            headers=headers,
            catch_response=True,
            name="update_task_status_api"
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
            
            # Log success/failure based on status code
            success = response.status_code == 200
            if success:
                debug_print(f"✅ HTTP request successful (200)")
            else:
                debug_print(f"❌ HTTP request failed ({response.status_code})")
                response.failure(f"Status update failed: {response.status_code}")
            
            debug_print(f"🔍 UPDATE_TASK_STATUS_API DEBUG END")
            return (success, response.text, response.status_code)
                
    except Exception as e:
        debug_print(f"💥 Exception updating task status: {e}")
        import traceback
        traceback.print_exc()
        return (False, str(e), 500)
