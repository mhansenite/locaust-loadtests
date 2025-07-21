"""
GuideX Load Testing Workflows
=============================

Organized workflow collection for comprehensive load testing of GuideX platform.

Directory Structure:
- project/: Project management and planning workflows
- admin/: Administrative and global system workflows  
- testing/: Testing utilities and debugging workflows

Usage Examples:
    # Import specific workflow
    from workflows.project import ProjectPlanUser
    
    # Import all workflows from a category
    from workflows.project import *
    
    # Import everything
    from workflows import *
"""

# Import from subdirectories
from .project import (
    ProjectPlanUser,
    ProjectPlanFixedUser,
    ThundercatsProjectUser
)

from .admin import (
    GlobalProjectsUser,
    GlobalTasksUser
)

from .testing import (
    TestQuotesFixUser
)

# Export all user classes
__all__ = [
    # Project workflows
    'ProjectPlanUser',
    'ProjectPlanFixedUser', 
    'ThundercatsProjectUser',
    
    # Admin workflows
    'GlobalProjectsUser',
    'GlobalTasksUser',
    
    # Testing workflows
    'TestQuotesFixUser'
]

# Workflow categories for easy access
PROJECT_WORKFLOWS = [
    'ProjectPlanUser',
    'ProjectPlanFixedUser', 
    'ThundercatsProjectUser'
]

ADMIN_WORKFLOWS = [
    'GlobalProjectsUser',
    'GlobalTasksUser'
]

TESTING_WORKFLOWS = [
    'TestQuotesFixUser'
]

def list_workflows():
    """List all available workflow classes organized by category"""
    print("📊 Available Load Testing Workflows")
    print("=" * 50)
    
    print(f"\n🏗️  PROJECT WORKFLOWS ({len(PROJECT_WORKFLOWS)}):")
    for workflow in PROJECT_WORKFLOWS:
        print(f"   • {workflow}")
    
    print(f"\n⚙️  ADMIN WORKFLOWS ({len(ADMIN_WORKFLOWS)}):")
    for workflow in ADMIN_WORKFLOWS:
        print(f"   • {workflow}")
        
    print(f"\n🧪 TESTING WORKFLOWS ({len(TESTING_WORKFLOWS)}):")
    for workflow in TESTING_WORKFLOWS:
        print(f"   • {workflow}")
    
    print(f"\n📖 Usage:")
    print("   from workflows.project import ProjectPlanUser")
    print("   locust -f guidex_loadtest.py ProjectPlanUser --users=10")

def get_workflow_by_name(name):
    """Get workflow class by name"""
    return globals().get(name, None) 