#!/usr/bin/env python3
"""
Common creation functions for load testing.
Contains reusable functions for creating projects, phases, milestones, and tasks.
"""

import json
import time
import uuid
import re
import random
from datetime import datetime, timedelta
from .extractdata import (
    extract_project_id_from_response,
    extract_phase_id_from_response,
    extract_milestone_id_from_response,
    extract_task_id_from_response,
    extract_subtask_id_from_response,
    get_dynamic_headers
)


def create_project(client, project_name_base="LoadTestProject"):
    """
    Create a new test project using the correct API from CreateProject.har
    
    Args:
        client: Locust HTTP client
        project_name_base: Base name for the project (will have timestamp and ID appended)
        
    Returns:
        dict: {'id': project_id, 'name': project_name} or None if creation failed
    """
    try:
        # Create a unique project name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        project_name = f"{project_name_base}-{timestamp}-{unique_id}"
        
        # Based on CreateProject.har analysis, the correct project creation API is:
        # POST /v2/projects with payload: [{}] for quick create
        # This creates a project with default name, then we can rename it
        
        # Project creation payload - exact format from HAR (quick create)
        project_payload = json.dumps([{}])
        
        # Get dynamic headers for project creation
        headers = get_dynamic_headers(client, "project_create")
        
        # Project creation URL (from CreateProject.har)
        create_url = "/v2/projects"
        
        print(f"Creating project using quick create API...")
        
        with client.post(
            create_url,
            data=project_payload,
            headers=headers,
            catch_response=True,
            name="create_project"
        ) as response:
            print(f"Project creation response status: {response.status_code}")
            print(f"Project creation response: {response.text[:500]}...")
            
            if response.status_code == 200:
                response.success()
                print(f"Successfully called project creation API")
                
                # Try to extract project ID from response
                project_id = extract_project_id_from_response(response.text)
                if project_id:
                    print(f"Created project with ID: {project_id}")
                    
                    # Now try to rename the project to our desired name
                    renamed_successfully = rename_project(client, project_id, project_name)
                    final_name = project_name if renamed_successfully else f"Quick Project {unique_id}"
                    
                    return {
                        'id': project_id,
                        'name': final_name
                    }
                else:
                    print(f"⚠️ Could not extract project ID from response")
                    return None
                    
            elif response.status_code == 401:
                response.failure("Authentication failed for project creation")
                print(f"❌ Authentication failed for project creation")
                return None
            elif response.status_code == 403:
                response.failure("Access denied for project creation")
                print(f"❌ Access denied for project creation") 
                return None
            else:
                response.failure(f"Project creation failed: {response.status_code}")
                print(f"⚠️ Project creation failed: {response.status_code}")
                return None
                
    except Exception as e:
        print(f"💥 Exception in create_project: {e}")
        import traceback
        traceback.print_exc()
        return None


def rename_project(client, project_id, new_name):
    """
    Rename a project using the correct API from project rename HAR
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project to rename
        new_name: New name for the project
        
    Returns:
        bool: True if successful, False otherwise
    """
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
        
        # Get dynamic headers for project rename
        headers = get_dynamic_headers(client, "project_rename")
        
        print(f"Attempting to rename project to: '{new_name}' using correct API")
        
        with client.post(
            rename_url,
            params=params,
            data=rename_payload,
            headers=headers,
            catch_response=True,
            name="rename_project"
        ) as response:
            print(f"Rename response status: {response.status_code}")
            print(f"Rename response: {response.text[:200]}...")
            
            if response.status_code == 200:
                # Check if the response indicates success
                if 'Project name updated' in response.text or '"name":"' in response.text:
                    print(f"Successfully renamed project to: '{new_name}'")
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


def delete_project(client, project_id):
    """
    Delete a test project using the pattern from DeleteProject.har
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project to delete
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Project deletion payload based on DeleteProject.har analysis
        delete_payload = json.dumps([{
            "projectIds": [{"uuid": project_id}]
        }])
        
        # Get dynamic headers for project deletion
        headers = get_dynamic_headers(client, "project_delete")
        
        # Project deletion URL (from DeleteProject.har)
        delete_url = "/v2/projects"
        
        print(f"Deleting project: {project_id}")
        
        with client.post(
            delete_url,
            data=delete_payload,
            headers=headers,
            catch_response=True,
            name="delete_project"
        ) as response:
            print(f"Project deletion response status: {response.status_code}")
            print(f"Project deletion response: {response.text[:200]}...")
            
            if response.status_code == 200:
                response.success()
                print(f"Successfully deleted project: {project_id}")
                return True
            else:
                response.failure(f"Project deletion failed: {response.status_code}")
                print(f"⚠️ Project deletion failed: {response.status_code}")
                return False
                
    except Exception as e:
        print(f"💥 Exception in delete_project: {e}")
        return False


def create_phase(client, project_id, phase_name_base="LoadTestPhase", context_phase_id=None):
    """
    Create a new phase in a project using the correct direct API
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project to create the phase in
        phase_name_base: Base name for the phase (will have timestamp and ID appended)
        context_phase_id: Existing phase ID for context (optional)
        
    Returns:
        dict: {'id': phase_id, 'name': phase_name, 'project_id': project_id} or None if creation failed
    """
    try:
        # Create a unique phase name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        phase_name = f"{phase_name_base}-{timestamp}-{unique_id}"
        
        # Based on HAR analysis, the correct phase creation API is:
        # POST /project/{projectId}/plan?phase={existingPhaseId}&view=board
        # with payload: [{"projectId":{"uuid":"..."},"name":"phase_name"}]
        
        # Use the provided context phase or a default
        current_phase_id = context_phase_id or "e34bcc9e-18b2-44f7-9384-d1d8af35de78"
        
        # Construct the phase creation URL
        create_url = f"/project/{project_id}/plan"
        params = {
            'phase': current_phase_id,
            'view': 'board'  # Can be 'board' or 'list'
        }
        
        # Create the payload - exact format from HAR
        phase_payload = json.dumps([{
            "projectId": {"uuid": project_id},
            "name": phase_name
        }])
        
        # Get dynamic headers for phase creation
        headers = get_dynamic_headers(client, "phase_create", project_id, current_phase_id)
        
        print(f"Creating phase directly: '{phase_name}' in project: {project_id}")
        print(f"Using direct phase creation API with existing phase context: {current_phase_id}")
        
        with client.post(
            create_url,
            params=params,
            data=phase_payload,
            headers=headers,
            catch_response=True,
            name="create_phase"
        ) as response:
            print(f"Phase creation response status: {response.status_code}")
            print(f"Phase creation response body: {response.text[:1000]}...")
            
            if response.status_code == 200:
                response.success()
                print(f"Successfully created phase: '{phase_name}'")
                
                # Try to extract phase ID from response
                phase_id = extract_phase_id_from_response(response.text)
                if phase_id:
                    print(f"Extracted phase ID: {phase_id}")
                    return {
                        'id': phase_id,
                        'name': phase_name,
                        'project_id': project_id
                    }
                else:
                    print(f"⚠️ Could not extract phase ID from response")
                    return {
                        'id': 'unknown',
                        'name': phase_name,
                        'project_id': project_id
                    }
            else:
                response.failure(f"Phase creation failed with status {response.status_code}: {response.text[:200]}")
                print(f"❌ Phase creation failed: {response.status_code} - {response.text[:200]}")
                return None
                
    except Exception as e:
        print(f"💥 Exception in create_phase: {e}")
        import traceback
        traceback.print_exc()
        return None


def create_milestone(client, project_id, phase_id, milestone_name_base="LoadTestMilestone"):
    """
    Create a milestone in a phase using the correct direct API
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project 
        phase_id: UUID of the phase to create the milestone in
        milestone_name_base: Base name for the milestone (will have timestamp and ID appended)
        
    Returns:
        dict: {'id': milestone_id, 'name': milestone_name, 'phase_id': phase_id} or None if creation failed
    """
    try:
        # Create a unique milestone name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        milestone_name = f"{milestone_name_base}-{timestamp}-{unique_id}"
        
        # Based on CreateMilestone.har analysis, milestone creation uses this format:
        # POST /project/{projectId}/plan?phase={phaseId}&view=board
        # with payload: [{"name":"milestone_name","phaseId":{"uuid":"phase_id"}}]
        
        milestone_url = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board'
        }
        
        # Correct milestone creation payload - exact format from CreateMilestone.har line 1359
        milestone_payload = json.dumps([{
            "name": milestone_name,
            "phaseId": {"uuid": phase_id}
        }])
        
        # Get dynamic headers for milestone creation
        headers = get_dynamic_headers(client, "milestone_create", project_id, phase_id)
        
        print(f"Creating milestone '{milestone_name}' directly in phase {phase_id}")
        
        with client.post(
            milestone_url,
            params=params,
            data=milestone_payload,
            headers=headers,
            catch_response=True,
            name="create_milestone"
        ) as response:
            print(f"Milestone creation response status: {response.status_code}")
            print(f"Milestone creation response: {response.text[:500]}...")
            
            if response.status_code == 200:
                response.success()
                
                # Check for successful milestone creation in response
                if 'milestone' in response.text and 'response' in response.text:
                    # Try to extract milestone ID from response
                    milestone_id = extract_milestone_id_from_response(response.text)
                    if milestone_id:
                        print(f"Created milestone: '{milestone_name}' with ID: {milestone_id}")
                        return {
                            'id': milestone_id,
                            'name': milestone_name,
                            'phase_id': phase_id
                        }
                    else:
                        print(f"⚠️ Milestone created but couldn't extract ID from response")
                        return {
                            'id': 'unknown',
                            'name': milestone_name,
                            'phase_id': phase_id
                        }
                else:
                    print(f"⚠️ Unexpected milestone creation response: {response.text[:200]}")
                    return None
            else:
                response.failure(f"Milestone creation failed: {response.status_code}")
                print(f"❌ Milestone creation failed: {response.status_code} - {response.text[:200]}")
                return None
                
    except Exception as e:
        print(f"💥 Exception in create_milestone: {e}")
        import traceback
        traceback.print_exc()
        return None


def create_task(client, project_id, phase_id, milestone_id, task_name_base="LoadTestTask", task_suffix=""):
    """
    Create a single task under a milestone
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        milestone_id: UUID of the milestone to create the task under
        task_name_base: Base name for the task (will have timestamp and ID appended)
        task_suffix: Optional suffix to add to the task name
        
    Returns:
        dict: {'id': task_id, 'name': task_name, 'milestone_id': milestone_id} or None if creation failed
    """
    try:
        # Create a unique task name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        task_name = f"{task_name_base}-{timestamp}-{unique_id}{task_suffix}"
        
        # Based on createingatask.har analysis
        task_url = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board'
        }
        
        task_payload = json.dumps([{
            "name": task_name,
            "parentId": {"uuid": milestone_id}
        }])
        
        # Get dynamic headers for task creation
        headers = get_dynamic_headers(client, "task_create", project_id, phase_id)
        
        print(f"Creating task '{task_name}' under milestone {milestone_id}")
        
        with client.post(
            task_url,
            params=params,
            data=task_payload,
            headers=headers,
            catch_response=True,
            name="create_task"
        ) as response:
            if response.status_code == 200:
                response.success()
                
                try:
                    if 'task' in response.text and 'response' in response.text:
                        
                        # Extract task ID from response using the helper function
                        task_id = extract_task_id_from_response(response.text)
                        if task_id:
                            print(f"Successfully created task '{task_name}' with ID: {task_id}")
                            
                            return {
                                'id': task_id,
                                'name': task_name,
                                'milestone_id': milestone_id
                            }
                        else:
                            print(f"⚠️ Task created but couldn't extract ID from response")
                            return {
                                'id': 'unknown',
                                'name': task_name,
                                'milestone_id': milestone_id
                            }
                    else:
                        print(f"⚠️ Unexpected task creation response: {response.text[:100]}")
                        return None
                        
                except Exception as e:
                    print(f"⚠️ Error parsing task creation response: {e}")
                    return None
                    
            else:
                response.failure(f"Failed to create task: {response.status_code} - {response.text[:200]}")
                print(f"❌ Failed to create task: {response.status_code} - {response.text[:100]}")
                return None
                
    except Exception as e:
        print(f"💥 Exception in create_task: {e}")
        import traceback
        traceback.print_exc()
        return None


def create_subtask(client, project_id, phase_id, parent_task_id, subtask_name_base="LoadTestSubtask", task_suffix=""):
    """
    Create a single subtask under a parent task
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        parent_task_id: UUID of the parent task to create the subtask under
        subtask_name_base: Base name for the subtask (will have timestamp and ID appended)
        task_suffix: Optional suffix to add to the subtask name
        
    Returns:
        dict: {'id': subtask_id, 'name': subtask_name, 'parent_task_id': parent_task_id} or None if creation failed
    """
    try:
        # Create a unique subtask name
        timestamp = int(time.time())
        unique_id = uuid.uuid4().hex[:8]
        subtask_name = f"{subtask_name_base}-{timestamp}-{unique_id}{task_suffix}"
        
        # Based on typical subtask creation patterns, this would likely be similar to task creation
        # but with a parentId pointing to a task instead of a milestone
        subtask_url = f"/project/{project_id}/plan"
        params = {
            'phase': phase_id,
            'view': 'board'
        }
        
        subtask_payload = json.dumps([{
            "name": subtask_name,
            "parentId": {"uuid": parent_task_id},
            "type": "subtask"  # Specify that this is a subtask
        }])
        
        # Get dynamic headers for subtask creation
        headers = get_dynamic_headers(client, "subtask_create", project_id, phase_id)
        
        print(f"Creating subtask '{subtask_name}' under parent task {parent_task_id}")
        
        with client.post(
            subtask_url,
            params=params,
            data=subtask_payload,
            headers=headers,
            catch_response=True,
            name="create_subtask"
        ) as response:
            if response.status_code == 200:
                response.success()
                
                try:
                    if ('subtask' in response.text or 'task' in response.text) and 'response' in response.text:
                        
                        # Extract subtask ID from response using the helper function
                        subtask_id = extract_subtask_id_from_response(response.text)
                        if subtask_id:
                            print(f"Successfully created subtask '{subtask_name}' with ID: {subtask_id}")
                            
                            return {
                                'id': subtask_id,
                                'name': subtask_name,
                                'parent_task_id': parent_task_id
                            }
                        else:
                            print(f"⚠️ Subtask created but couldn't extract ID from response")
                            return {
                                'id': 'unknown',
                                'name': subtask_name,
                                'parent_task_id': parent_task_id
                            }
                    else:
                        print(f"⚠️ Unexpected subtask creation response: {response.text[:100]}")
                        return None
                        
                except Exception as e:
                    print(f"⚠️ Error parsing subtask creation response: {e}")
                    return None
                    
            else:
                response.failure(f"Failed to create subtask: {response.status_code} - {response.text[:200]}")
                print(f"❌ Failed to create subtask: {response.status_code} - {response.text[:100]}")
                return None
                
    except Exception as e:
        print(f"💥 Exception in create_subtask: {e}")
        import traceback
        traceback.print_exc()
        return None


def create_multiple_tasks(client, project_id, phase_id, milestone_id, milestone_name, 
                         task_name_base="LoadTestTask", min_tasks=1, max_tasks=10):
    """
    Create multiple random tasks under a milestone
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        milestone_id: UUID of the milestone to create tasks under
        milestone_name: Name of the milestone (for logging)
        task_name_base: Base name for the tasks
        min_tasks: Minimum number of tasks to create
        max_tasks: Maximum number of tasks to create
        
    Returns:
        list: List of created task dictionaries
    """
    # Create random number of tasks
    num_tasks = random.randint(min_tasks, max_tasks)
    print(f"Creating {num_tasks} tasks for milestone '{milestone_name}'")
    
    created_tasks = []
    
    for i in range(num_tasks):
        task_suffix = f"-{i+1}" if num_tasks > 1 else ""
        
        task_info = create_task(
            client=client,
            project_id=project_id,
            phase_id=phase_id,
            milestone_id=milestone_id,
            task_name_base=task_name_base,
            task_suffix=task_suffix
        )
        
        if task_info:
            created_tasks.append(task_info)
            print(f"  Successfully created task {i+1}/{num_tasks}: '{task_info['name']}'")
        else:
            print(f"  ❌ Failed to create task {i+1}/{num_tasks}")
            
        # Small delay between tasks to avoid overwhelming the server
        time.sleep(0.1)
    
    print(f"Task batch complete: Created {len(created_tasks)}/{num_tasks} tasks for milestone '{milestone_name}'")
    return created_tasks


def create_multiple_subtasks(client, project_id, phase_id, parent_task_id, parent_task_name, 
                            subtask_name_base="LoadTestSubtask", min_subtasks=1, max_subtasks=5):
    """
    Create multiple random subtasks under a parent task
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        phase_id: UUID of the phase
        parent_task_id: UUID of the parent task to create subtasks under
        parent_task_name: Name of the parent task (for logging)
        subtask_name_base: Base name for the subtasks
        min_subtasks: Minimum number of subtasks to create
        max_subtasks: Maximum number of subtasks to create
        
    Returns:
        list: List of created subtask dictionaries
    """
    # Create random number of subtasks
    num_subtasks = random.randint(min_subtasks, max_subtasks)
    print(f"Creating {num_subtasks} subtasks for task '{parent_task_name}'")
    
    created_subtasks = []
    
    for i in range(num_subtasks):
        subtask_suffix = f"-{i+1}" if num_subtasks > 1 else ""
        
        subtask_info = create_subtask(
            client=client,
            project_id=project_id,
            phase_id=phase_id,
            parent_task_id=parent_task_id,
            subtask_name_base=subtask_name_base,
            task_suffix=subtask_suffix
        )
        
        if subtask_info:
            created_subtasks.append(subtask_info)
            print(f"  Successfully created subtask {i+1}/{num_subtasks}: '{subtask_info['name']}'")
        else:
            print(f"  ❌ Failed to create subtask {i+1}/{num_subtasks}")
            
        # Small delay between subtasks to avoid overwhelming the server
        time.sleep(0.1)
    
    print(f"Subtask batch complete: Created {len(created_subtasks)}/{num_subtasks} subtasks for task '{parent_task_name}'")
    return created_subtasks


# Stress testing variants (simplified versions for rapid creation)
def create_stress_project(client, project_name_base="StressProject"):
    """Simplified project creation for stress testing"""
    return create_project(client, project_name_base + "-stress")


def create_stress_phase(client, project_id, phase_name_base="StressPhase", context_phase_id=None):
    """Simplified phase creation for stress testing"""
    return create_phase(client, project_id, phase_name_base + "-stress", context_phase_id)


def create_stress_milestone(client, project_id, phase_id, milestone_name_base="StressMilestone"):
    """Simplified milestone creation for stress testing"""
    return create_milestone(client, project_id, phase_id, milestone_name_base + "-stress")


def create_stress_task(client, project_id, phase_id, milestone_id, task_name_base="StressTask"):
    """Simplified task creation for stress testing"""
    # Use more granular timestamp for stress testing
    timestamp = int(time.time() * 1000)
    random_id = uuid.uuid4().hex[:6]
    task_suffix = f"-stress-{timestamp}-{random_id}"
    
    return create_task(client, project_id, phase_id, milestone_id, task_name_base, task_suffix)


# Utility functions for task updates (placeholder - requires HAR analysis)
def update_task(client, project_id, task_id, updates):
    """
    Update an existing task with new properties
    
    Args:
        client: Locust HTTP client
        project_id: UUID of the project
        task_id: UUID of the task to update
        updates: Dictionary of updates to apply
        
    Returns:
        bool: True if successful, False otherwise
        
    Note: This is a placeholder - requires task update HAR file analysis for implementation
    """
    print(f"Updating task {task_id[:8]}...")
    
    # TODO: Implement with actual HAR file analysis
    # For now, this is a placeholder showing the structure
    
    if 'assignee' in updates:
        print(f"     • Assignee: {updates['assignee']}")
    if 'status' in updates:
        print(f"     • Status: {updates['status']}")
    if 'estimated_hours' in updates:
        print(f"     • Estimated: {updates['estimated_hours']}h")
    if 'due_date' in updates:
        print(f"     • Due: {updates['due_date']}")
    if 'priority' in updates:
        print(f"     • Priority: {updates['priority']}")
    
    print(f"     Task update simulated (need HAR file for real API)")
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
