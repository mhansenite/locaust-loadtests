"""
Automatic Workflow Discovery System

This module automatically discovers and imports all workflow classes
from the workflows directory, eliminating the need to manually update
imports when adding new workflows.
"""

import os
import importlib
import inspect
from typing import Dict, Type, List


def discover_workflow_classes() -> Dict[str, Type]:
    """
    Automatically discover all workflow classes in the workflows directory.
    
    Returns:
        Dict mapping class names to class objects for all classes that:
        - Are in *_user.py files
        - Inherit from AuthenticatedUser (indirectly via inspection)
        - Have a 'weight' attribute
    """
    workflow_classes = {}
    workflows_dir = os.path.dirname(__file__)
    
    # Find all Python files ending with '_user.py'
    for filename in os.listdir(workflows_dir):
        if filename.endswith('_user.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py extension
            
            try:
                # Import the module dynamically
                module = importlib.import_module(f'workflows.{module_name}')
                
                # Find all classes in the module
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    # Check if it's a workflow class by looking for:
                    # 1. 'weight' attribute (all workflow classes have this)
                    # 2. Class is defined in this module (not imported)
                    # 3. Has 'task' methods (characteristic of Locust users)
                    if (hasattr(obj, 'weight') and 
                        obj.__module__ == module.__name__ and
                        _has_task_methods(obj)):
                        
                        workflow_classes[name] = obj
                        
            except ImportError as e:
                print(f"⚠️  Could not import workflow module {module_name}: {e}")
                continue
    
    return workflow_classes


def _has_task_methods(cls) -> bool:
    """Check if a class has methods decorated with @task"""
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if hasattr(method, 'locust_task_weight'):  # Locust task attribute
            return True
    return False


def get_workflow_info() -> List[Dict]:
    """
    Get formatted information about all discovered workflows
    """
    workflows = discover_workflow_classes()
    workflow_info = []
    
    for name, cls in workflows.items():
        # Extract docstring description
        doc = cls.__doc__ or "No description available"
        description = doc.split('\n')[1].strip() if '\n' in doc else doc.strip()
        
        workflow_info.append({
            'name': name,
            'class': cls,
            'weight': getattr(cls, 'weight', 1),
            'description': description
        })
    
    # Sort by weight (higher weight first, then alphabetically)
    workflow_info.sort(key=lambda x: (-x['weight'], x['name']))
    
    return workflow_info


# Auto-discover and expose all workflow classes
_discovered_workflows = discover_workflow_classes()

# Create __all__ dynamically
__all__ = list(_discovered_workflows.keys())

# Make all discovered classes available at package level
locals().update(_discovered_workflows)

# For debugging
if __name__ == "__main__":
    print("🔍 Discovered Workflows:")
    for name, cls in _discovered_workflows.items():
        print(f"  • {name} (weight: {getattr(cls, 'weight', 1)})") 