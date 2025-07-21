"""
Admin/Global Workflows
=====================

Administrative and global load testing workflows for testing 
system-wide functionality and admin operations.

Available User Classes:
- GlobalProjectsUser: Global projects management workflow
- GlobalTasksUser: Global tasks management workflow
"""

from .global_projects_user import GlobalProjectsUser
from .global_tasks_user import GlobalTasksUser

__all__ = [
    'GlobalProjectsUser',
    'GlobalTasksUser'
] 