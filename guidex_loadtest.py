#!/usr/bin/env python3
"""
GuideX Load Testing - Modular Architecture

This is the main entry point for GuideX load testing. It imports the modular 
user classes and provides various workflow options.

ARCHITECTURE:
├── auth/
│   ├── config.py         # Environment variables & configuration
│   └── base_user.py      # Shared authentication logic
├── workflows/
│   ├── project_user.py   # Project-focused activities
│   ├── global_tasks_user.py # Global task management
│   └── mixed_user.py     # Combined workflows (most realistic)
└── utils/
    ├── graphql_queries.py # Reusable GraphQL queries
    └── api_helpers.py     # Common API patterns

USAGE EXAMPLES:

1. Run with Mixed Workflows (Recommended):
   locust -f guidex_loadtest.py MixedWorkflowUser --headless --users=10 --spawn-rate=2 --run-time=60s

2. Run Project-Only Testing:
   locust -f guidex_loadtest.py ProjectUser --headless --users=10 --spawn-rate=2 --run-time=60s

3. Run Global Tasks Only:
   locust -f guidex_loadtest.py GlobalTasksUser --headless --users=10 --spawn-rate=2 --run-time=60s

4. Run Global Projects Only (HAR-based):
   locust -f guidex_loadtest.py GlobalProjectsUser --headless --users=10 --spawn-rate=2 --run-time=60s

5. Run All User Types Together:
   locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s

6. Interactive Web UI:
   locust -f guidex_loadtest.py
   # Then open http://localhost:8089
"""

from locust import run_single_user

# Import all user classes
from workflows.project_user import ProjectUser
from workflows.global_tasks_user import GlobalTasksUser
from workflows.global_projects_user import GlobalProjectsUser
from workflows.mixed_user import MixedWorkflowUser

# Import configuration for display
from auth.config import (
    LOGIN_EMAIL, WAIT_TIME_BETWEEN_TASKS, DEFAULT_USERS, 
    DEFAULT_SPAWN_RATE, DEFAULT_RUN_TIME, DEBUG
)

# Export user classes so they can be discovered by locust
__all__ = ['ProjectUser', 'GlobalTasksUser', 'GlobalProjectsUser', 'MixedWorkflowUser']


def main():
    """
    Main function for single-user testing and information display
    """
    if DEBUG:
        print(f"""
🚀 GuideX Modular Load Testing Ready!

📊 Configuration:
   • Login Email: {LOGIN_EMAIL}
   • Wait Between Tasks: {WAIT_TIME_BETWEEN_TASKS}s per user
   • Default Users: {DEFAULT_USERS}
   • Default Spawn Rate: {DEFAULT_SPAWN_RATE}/sec
   • Default Run Time: {DEFAULT_RUN_TIME}

🎯 USER TYPES AVAILABLE:

   1. MixedWorkflowUser (Recommended)
      • Combines project browsing + global tasks
      • Most realistic user behavior
      • Weight: 3 (most common)

   2. ProjectUser  
      • Focuses on project management
      • Browse projects, verify auth
      • Weight: 1

                  3. GlobalTasksUser
                  • Focuses on task management
                  • View/filter/update global tasks
                  • Weight: 1 (placeholder queries)

               4. GlobalProjectsUser (NEW!)
                  • HAR-based global projects workflow
                  • Real project management interactions
                  • Weight: 2 (production-ready)

🚀 READY-TO-RUN LOCUST COMMANDS:

# Mixed Workflow (Recommended)
locust -f guidex_loadtest.py MixedWorkflowUser --headless --users=10 --spawn-rate=2 --run-time=60s

# Project Focus
locust -f guidex_loadtest.py ProjectUser --headless --users=10 --spawn-rate=2 --run-time=60s

# Global Projects (HAR-based)
locust -f guidex_loadtest.py GlobalProjectsUser --headless --users=10 --spawn-rate=2 --run-time=60s

# All User Types (Distributed Load)
locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s

# Interactive Web UI (Choose user types in browser)
locust -f guidex_loadtest.py

📝 Single User Debug Mode Running Below...
    """)
    
    # Run single user for testing/debugging
    # Default to MixedWorkflowUser for testing since it's most comprehensive
    print("🔍 Testing MixedWorkflowUser (most comprehensive)...")
    run_single_user(MixedWorkflowUser)


if __name__ == "__main__":
    main()
