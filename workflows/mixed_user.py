from locust import task
from auth.base_user import AuthenticatedUser
from utils.graphql_queries import (
    COUNT_NOTIFICATIONS_QUERY, GET_PROJECT_LIST_QUERY, 
    GET_GLOBAL_TASKS_QUERY, get_project_list_variables, 
    get_global_tasks_variables
)
from utils.api_helpers import make_graphql_request, TaskStatusGenerator
from auth.config import DEBUG, PROJECT_DOMAIN, PROJECT_URL


class MixedWorkflowUser(AuthenticatedUser):
    """
    User that performs a mix of project and global task activities.
    Simulates realistic user behavior switching between different features.
    """
    
    # Higher weight since this represents the most common user behavior
    weight = 3

    @task(weight=2)
    def browse_projects(self):
        """
        Browse project list (inherited behavior from ProjectUser)
        """
        variables = get_project_list_variables(
            page=1, 
            per_page=10, 
            sort_by="NAME", 
            sort_direction="ASC"
        )
        
        make_graphql_request(
            client=self.client,
            operation_name="GetProjectList",
            query=GET_PROJECT_LIST_QUERY,
            variables=variables,
            auth_token=self.get_auth_header(),
            referer_path="/projects",
            expected_data_key="projects",
            request_name="Browse Project List"
        )

    @task(weight=3)
    def check_global_tasks(self):
        """
        Check global tasks (inherited behavior from GlobalTasksUser)
        """
        # Use random status filters to simulate different user interests
        status_filter = TaskStatusGenerator.get_random_status_filter()
        
        variables = get_global_tasks_variables(
            page=1,
            per_page=20,
            statuses=status_filter
        )
        
        make_graphql_request(
            client=self.client,
            operation_name="GetGlobalTasks",
            query=GET_GLOBAL_TASKS_QUERY,
            variables=variables,
            auth_token=self.get_auth_header(),
            referer_path="/tasks",
            expected_data_key="tasks",
            request_name=f"View Global Tasks: {','.join(status_filter)}"
        )

    @task(weight=1)
    def verify_notifications(self):
        """
        Check notifications (common activity across all user types)
        """
        make_graphql_request(
            client=self.client,
            operation_name="CountNotifications",
            query=COUNT_NOTIFICATIONS_QUERY,
            variables={},
            auth_token=self.get_auth_header(),
            referer_path="/",
            request_name="Check Notifications"
        )

    @task(weight=1)
    def project_to_tasks_workflow(self):
        """
        Realistic workflow: Browse projects, then check related tasks
        Simulates a user going from project view to task management
        """
        # Step 1: Browse projects
        if DEBUG:
            print("🔄 Starting project-to-tasks workflow...")
        
        project_variables = get_project_list_variables(page=1, per_page=5)
        project_data = make_graphql_request(
            client=self.client,
            operation_name="GetProjectList",
            query=GET_PROJECT_LIST_QUERY,
            variables=project_variables,
            auth_token=self.get_auth_header(),
            referer_path="/projects",
            expected_data_key="projects",
            request_name="Workflow: Browse Projects"
        )
        
        # Step 2: Check tasks (simulating user clicking to tasks after seeing projects)
        if project_data:  # Only proceed if project call was successful
            task_variables = get_global_tasks_variables(
                page=1,
                per_page=15,
                statuses=["OPEN", "IN_PROGRESS"]
            )
            
            make_graphql_request(
                client=self.client,
                operation_name="GetGlobalTasks",
                query=GET_GLOBAL_TASKS_QUERY,
                variables=task_variables,
                auth_token=self.get_auth_header(),
                referer_path="/tasks",
                expected_data_key="tasks",
                request_name="Workflow: Check Related Tasks"
            )
            
            if DEBUG:
                print("✅ Completed project-to-tasks workflow")

    @task(weight=1)
    def filtered_project_search(self):
        """
        Search/filter projects with different criteria
        Simulates user trying different filters and sorting
        """
        from utils.api_helpers import ProjectFilterGenerator
        
        # Get random sorting options
        sort_by, sort_direction = ProjectFilterGenerator.get_random_sort()
        
        variables = get_project_list_variables(
            page=1,
            per_page=15,  # Slightly larger page for filtering
            sort_by=sort_by,
            sort_direction=sort_direction
        )
        
        make_graphql_request(
            client=self.client,
            operation_name="GetProjectList",
            query=GET_PROJECT_LIST_QUERY,
            variables=variables,
            auth_token=self.get_auth_header(),
            referer_path="/projects",
            expected_data_key="projects",
            request_name=f"Filter Projects: {sort_by} {sort_direction}"
        )

    @task(weight=1)
    def multi_page_browsing(self):
        """
        Browse multiple pages of content (simulates pagination usage)
        """
        import random
        
        # Randomly browse page 1, 2, or 3 (most users don't go beyond page 3)
        page_num = random.choice([1, 2, 3])
        
        # Alternate between projects and tasks
        if random.choice([True, False]):
            # Browse projects
            variables = get_project_list_variables(page=page_num, per_page=10)
            make_graphql_request(
                client=self.client,
                operation_name="GetProjectList",
                query=GET_PROJECT_LIST_QUERY,
                variables=variables,
                auth_token=self.get_auth_header(),
                referer_path="/projects",
                expected_data_key="projects",
                request_name=f"Browse Projects Page {page_num}"
            )
        else:
            # Browse tasks
            variables = get_global_tasks_variables(page=page_num, per_page=20)
            make_graphql_request(
                client=self.client,
                operation_name="GetGlobalTasks",
                query=GET_GLOBAL_TASKS_QUERY,
                variables=variables,
                auth_token=self.get_auth_header(),
                referer_path="/tasks",
                expected_data_key="tasks",
                request_name=f"Browse Tasks Page {page_num}"
            ) 

    @task(weight=1)
    def visit_global_projects(self):
        """
        Occasionally visit the global projects page (like GlobalProjectsUser)
        This adds more realistic navigation patterns
        """
        if DEBUG:
            print("🌐 Mixed User: Checking global projects...")
            
        # Navigate to global projects page (simplified version of GlobalProjectsUser)
        with self.client.get(
            "/v2/projects?_rsc=d8sqm", 
            headers={
                "Accept": "*/*",
                "Host": PROJECT_DOMAIN,
                "Priority": "u=4",
                "RSC": "1",
                "Referer": f"{PROJECT_URL}/tasks",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
            name="Mixed - Global Projects View"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Mixed User: Global projects loaded")
            else:
                if DEBUG:
                    print(f"❌ Mixed User: Global projects failed: {resp.status_code}") 