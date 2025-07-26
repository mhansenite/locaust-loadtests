import random
import os

# Debug mode - only print debug messages when enabled
DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

def debug_print(message):
    """Print debug message only when DEBUG is enabled"""
    if DEBUG:
        print(message)


def get_random_phase_id(user_instance):
    """Get a random phase ID, creating one if none exist"""
    if not user_instance.created_phases:
        # Bootstrap: create first phase
        debug_print(f"No phases available, creating bootstrap phase...")
        user_instance.create_test_phase()
    
    if user_instance.created_phases:
        selected_phase = random.choice(user_instance.created_phases)
        return selected_phase['id']
    
    # This should rarely happen - fallback to hardcoded phase ID
    print(f"❌ No phases available after creation attempt, using hardcoded fallback")
    return "e34bcc9e-18b2-44f7-9384-d1d8af35de78"  # From HAR analysis


def get_random_milestone_info(user_instance):
    """Get a random milestone info dict, creating one if none exist. Ensures correct phase_id association."""
    if not user_instance.created_milestones:
        # Bootstrap: create first milestone
        debug_print(f"No milestones available, creating bootstrap milestone...")
        user_instance.create_milestone()
    
    if user_instance.created_milestones:
        selected_milestone = random.choice(user_instance.created_milestones)
        debug_print(f"Selected milestone: '{selected_milestone['name']}' (ID: {selected_milestone['id']}) in phase {selected_milestone['phase_id']}")
        return selected_milestone
    
    # This should rarely happen - no fallback for milestones since they require valid phase
    print(f"❌ No milestones available after creation attempt")
    return None


def get_random_task_info(user_instance):
    """Get a random task info dict, creating one if none exist. Ensures correct milestone_id and phase_id association."""
    if not user_instance.created_tasks:
        # Bootstrap: create first task
        debug_print(f"No tasks available, creating bootstrap task...")
        user_instance.create_task()
    
    if user_instance.created_tasks:
        selected_task = random.choice(user_instance.created_tasks)
        task_id = selected_task['id']
        task_name = selected_task['name']
        task_milestone_id = selected_task.get('milestone_id', 'unknown')
        task_phase_id = selected_task.get('phase_id', 'unknown')
        milestone_name = selected_task.get('milestone_name', 'Unknown')
        
        debug_print(f"Selected task: '{task_name}' (ID: {task_id}) in milestone '{milestone_name}' ({task_milestone_id}) in phase {task_phase_id}")
        return selected_task
    
    # This should rarely happen - no fallback for tasks since they require valid milestone and phase
    print(f"❌ No tasks available after creation attempt")
    return None


# =============================================================================
# PROJECT POOL HELPERS
# =============================================================================

def assign_project_from_pool(pool_lock, project_pool, project_user_counts, project_assignments, 
                           user_counter_ref, login_email, user_instance_id, users_per_project, max_projects):
    """Assign a user to a project from the shared pool using load balancing"""
    with pool_lock:
        user_id = f"{login_email}_{user_instance_id}"
        user_counter_ref[0] += 1
        user_number = user_counter_ref[0]
        
        # If pool is empty, signal to create first project
        if len(project_pool) == 0:
            debug_print(f"Project pool empty, will create initial project...")
            return None  # Signal that this user should create a project
        
        # Find the project with the least users for load balancing
        min_users = float('inf')
        least_loaded_project = None
        project_loads = []
        
        for project in project_pool:
            project_id = project['id']
            current_users = project_user_counts.get(project_id, 0)
            project_loads.append(f"{project['name']}: {current_users} users")
            
            if current_users < min_users:
                min_users = current_users
                least_loaded_project = project
        
        debug_print(f"Current project loads: {', '.join(project_loads)}")
        
        # Check if we need a new project (all existing projects are at capacity)
        all_projects_at_capacity = min_users >= users_per_project
        can_create_more = len(project_pool) < max_projects
        
        if all_projects_at_capacity and can_create_more:
            debug_print(f"All {len(project_pool)} projects have {users_per_project}+ users, creating new project...")
            debug_print(f"Current pool: {len(project_pool)}/{max_projects} projects")
            return None  # Signal that this user should create a project
        
        # Assign to the least loaded project
        if least_loaded_project:
            project_id = least_loaded_project['id']
            
            # Update user count for this project
            project_user_counts[project_id] = project_user_counts.get(project_id, 0) + 1
            
            # Track this assignment
            project_assignments[user_id] = least_loaded_project
            
            new_count = project_user_counts[project_id]
            debug_print(f"User {user_number} assigned to least loaded project: {least_loaded_project['name']} (now {new_count} users)")
            debug_print(f"Project ID: {project_id}")
            
            return project_id
        
        print(f"❌ No available project found!")
        return None


def assign_project_from_existing_pool(pool_lock, project_pool, project_user_counts, project_assignments,
                                    user_counter_ref, login_email, user_instance_id):
    """Assign a user to an existing project from the pool using load balancing"""
    if len(project_pool) == 0:
        print("❌ Cannot assign from empty pool!")
        return None
        
    user_id = f"{login_email}_{user_instance_id}"
    user_number = user_counter_ref[0]
    
    # Find the project with the least users for load balancing
    min_users = float('inf')
    least_loaded_project = None
    
    for project in project_pool:
        project_id = project['id']
        current_users = project_user_counts.get(project_id, 0)
        
        if current_users < min_users:
            min_users = current_users
            least_loaded_project = project
    
    if least_loaded_project:
        project_id = least_loaded_project['id']
        
        # Update user count for this project
        project_user_counts[project_id] = project_user_counts.get(project_id, 0) + 1
        
        # Track this assignment
        project_assignments[user_id] = least_loaded_project
        
        new_count = project_user_counts[project_id]
        debug_print(f"User {user_number} assigned to least loaded existing project: {least_loaded_project['name']} (now {new_count} users)")
        return project_id
    
    print("❌ No suitable project found in pool!")
    return None


def add_project_to_pool(project_pool, project_info, max_projects):
    """Add a project to the shared pool"""
    if len(project_pool) < max_projects:
        project_pool.append(project_info)
        debug_print(f"Added project to pool: {project_info['name']} (Pool size: {len(project_pool)}/{max_projects})")
        return True
    print(f"❌ Cannot add project - pool at limit ({len(project_pool)}/{max_projects})")
    return False


def show_current_distribution(project_pool, project_user_counts, users_per_project):
    """Display current user distribution across all projects"""
    if len(project_pool) == 0:
        return
        
    debug_print("=" * 50)
    debug_print("CURRENT USER DISTRIBUTION:")
    total_users = 0
    for i, project in enumerate(project_pool):
        project_id = project['id']
        user_count = project_user_counts.get(project_id, 0)
        total_users += user_count
        debug_print(f"  Project {i+1}: {project['name']} = {user_count} users")
    
    debug_print(f"Total: {total_users} users across {len(project_pool)} projects")
    if len(project_pool) > 0:
        avg_users = total_users / len(project_pool)
        debug_print(f"Average: {avg_users:.1f} users per project (target: {users_per_project})")
    debug_print("=" * 50)
