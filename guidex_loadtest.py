#!/usr/bin/env python3
"""
GuideX Load Testing - Modular Architecture with Auto-Discovery

This is the main entry point for GuideX load testing. It automatically 
discovers and imports all workflow classes, so you never need to edit 
this file when adding new workflows!

ARCHITECTURE:
├── auth/
│   ├── config.py         # Environment variables & configuration
│   └── base_user.py      # Shared authentication logic
├── workflows/
│   ├── *_user.py         # All workflow files auto-discovered! 
│   └── __init__.py       # Auto-discovery magic happens here
└── utils/
    ├── graphql_queries.py # Reusable GraphQL queries
    └── api_helpers.py     # Common API patterns

🚀 AUTO-DISCOVERY: Just add any new *_user.py file to workflows/ and it's automatically available!

USAGE EXAMPLES:

1. Run with Mixed Workflows (if available):
   locust -f guidex_loadtest.py MixedWorkflowUser --headless --users=10 --spawn-rate=2 --run-time=60s

2. Run any specific workflow (auto-discovered):
   locust -f guidex_loadtest.py <WorkflowClassName> --headless --users=10 --spawn-rate=2 --run-time=60s

3. Run All User Types Together:
   locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s

4. Interactive Web UI (auto-populates with all discovered workflows):
   locust -f guidex_loadtest.py
   # Then open http://localhost:8089

5. Single User Debug Mode:
   python guidex_loadtest.py [WorkflowClassName]    # Run specific workflow
   python guidex_loadtest.py --list                 # List available workflows
   python guidex_loadtest.py                        # Show help and run default
"""

import sys
import argparse
from locust import run_single_user

# Import auto-discovery system and all workflow classes
from workflows import discover_workflow_classes, get_workflow_info

# Import configuration for display
from auth.config import (
    LOGIN_EMAIL, WAIT_TIME_BETWEEN_TASKS, DEFAULT_USERS, 
    DEFAULT_SPAWN_RATE, DEFAULT_RUN_TIME, DEBUG
)

# Auto-discover all workflow classes and make them available to locust
_workflow_classes = discover_workflow_classes()

# Export dynamically discovered classes so they can be found by locust
__all__ = list(_workflow_classes.keys())

# Make all workflow classes available at module level for locust discovery
locals().update(_workflow_classes)


def print_available_workflows():
    """Print all available workflows in a nice format"""
    workflow_info = get_workflow_info()
    
    print(f"""
🎯 AVAILABLE WORKFLOWS ({len(workflow_info)} discovered):
""")
    
    for i, info in enumerate(workflow_info, 1):
        print(f"""   {i}. {info['name']}
      • {info['description']}
      • Weight: {info['weight']}""")
    
    print()


def print_usage_examples(workflow_info):
    """Print usage examples with discovered workflows"""
    print(f"""
🚀 READY-TO-RUN COMMANDS:

# Single User Debug Mode (specify workflow):
python guidex_loadtest.py {workflow_info[0]['name'] if workflow_info else 'WorkflowName'}

# List all available workflows:
python guidex_loadtest.py --list

# Locust Load Testing:""")
    
    if workflow_info:
        # Show the highest weight workflow first
        top_workflow = workflow_info[0]
        print(f"""locust -f guidex_loadtest.py {top_workflow['name']} --headless --users=10 --spawn-rate=2 --run-time=60s""")
        
        # Show a couple more examples if available
        for info in workflow_info[1:2]:
            print(f"""locust -f guidex_loadtest.py {info['name']} --headless --users=10 --spawn-rate=2 --run-time=60s""")
    
    print(f"""
# All workflows together:
locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s

# Interactive Web UI:
locust -f guidex_loadtest.py
""")


def main():
    """
    Main function for single-user testing and information display
    """
    workflow_info = get_workflow_info()
    workflow_dict = {info['name']: info for info in workflow_info}
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='GuideX Load Testing with Auto-Discovery',
        add_help=False  # We'll handle help ourselves for better formatting
    )
    parser.add_argument('workflow', nargs='?', help='Workflow class name to run')
    parser.add_argument('--list', action='store_true', help='List all available workflows')
    parser.add_argument('--help', '-h', action='store_true', help='Show this help message')
    
    args = parser.parse_args()
    
    # Handle help
    if args.help:
        print(__doc__)
        print_available_workflows()
        print_usage_examples(workflow_info)
        return
    
    # Handle list workflows
    if args.list:
        print_available_workflows()
        return
    
    # Show configuration in debug mode
    if DEBUG and not args.workflow:
        print(f"""
🚀 GuideX Modular Load Testing Ready!

📊 Configuration:
   • Login Email: {LOGIN_EMAIL}
   • Wait Between Tasks: {WAIT_TIME_BETWEEN_TASKS}s per user
   • Default Users: {DEFAULT_USERS}
   • Default Spawn Rate: {DEFAULT_SPAWN_RATE}/sec
   • Default Run Time: {DEFAULT_RUN_TIME}
""")
        print_available_workflows()
        print_usage_examples(workflow_info)
    
    # Handle workflow execution
    if args.workflow:
        # Check if specified workflow exists
        if args.workflow not in workflow_dict:
            print(f"❌ Workflow '{args.workflow}' not found!")
            print_available_workflows()
            print(f"\n💡 Usage: python guidex_loadtest.py <WorkflowName>")
            return
        
        # Run the specified workflow
        selected_workflow = workflow_dict[args.workflow]
        print(f"🔍 Testing {selected_workflow['name']} (Weight: {selected_workflow['weight']})...")
        print(f"📝 Description: {selected_workflow['description']}")
        print(f"🚀 Starting single-user debug mode...\n")
        run_single_user(selected_workflow['class'])
        
    elif workflow_info:
        # No workflow specified, run default (highest weight)
        default_workflow = workflow_info[0]
        print(f"🔍 No workflow specified. Testing {default_workflow['name']} (highest weight: {default_workflow['weight']})...")
        print(f"💡 Tip: Use 'python guidex_loadtest.py {default_workflow['name']}' to be explicit")
        print(f"📝 Use 'python guidex_loadtest.py --list' to see all available workflows\n")
        run_single_user(default_workflow['class'])
        
    else:
        print("❌ No workflow classes discovered! Check your workflows directory.")


if __name__ == "__main__":
    main()
