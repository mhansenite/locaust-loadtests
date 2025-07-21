#!/usr/bin/env python3
"""
Test script for the HAR to Workflow converter
Demonstrates the capabilities of the automated conversion
"""

import os
import sys
from har_to_workflow import HARWorkflowGenerator


def test_converter():
    """Test the converter with the existing GlobalProjects files"""
    
    # Test file paths - check both HAR and Python files
    test_har_file = "HARFiles/RAW_HAR/GlobalProjects.har"
    test_python_file = "HARFiles/RAW_PY/GlobalProjects.py"
    
    print("🧪 Testing HAR to Workflow Converter")
    print("=" * 50)
    
    # Test with HAR file if available
    if os.path.exists(test_har_file):
        print(f"✅ Found HAR file: {test_har_file}")
        print("🔄 Testing HAR file conversion...")
        generator = HARWorkflowGenerator(test_har_file, "TestGlobalProjectsHAR")
        workflow_code = generator.generate()
        
        if workflow_code:
            print("✅ HAR file conversion successful!")
            return True
    
    # Fallback to Python file if HAR not available
    elif os.path.exists(test_python_file):
        print(f"✅ Found Python file: {test_python_file}")
        print("🔄 Testing Python file conversion...")
        generator = HARWorkflowGenerator(test_python_file, "TestGlobalProjectsPython")
        workflow_code = generator.generate()
        
        if workflow_code:
            print("✅ Python file conversion successful!")
            return True
    
    else:
        print(f"❌ No test files found:")
        print(f"   HAR file: {test_har_file}")
        print(f"   Python file: {test_python_file}")
        print("Please ensure you have captured HAR files in the HARFiles directory")
        return False
        
    print("❌ Converter test failed!")
    return False


def show_usage_examples():
    """Show usage examples for the converter"""
    print("\n" + "=" * 60)
    print("🎯 HAR to Workflow Converter Usage Examples")
    print("=" * 60)
    
    examples = [
        {
            "description": "Convert HAR file directly (recommended)",
            "command": "python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/GlobalProjects.har GlobalProjects",
            "output": "workflows/global_projects_user.py"
        },
        {
            "description": "Convert a user management HAR file",
            "command": "python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/UserManagement.har UserManagement", 
            "output": "workflows/user_management_user.py"
        },
        {
            "description": "Convert from existing Python file",
            "command": "python3 HARFiles/har_to_workflow.py HARFiles/RAW_PY/Reports.py Reports",
            "output": "workflows/reports_user.py"
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['description']}:")
        print(f"   Command: {example['command']}")
        print(f"   Output:  {example['output']}")
        
    print(f"\n" + "=" * 60)
    print("🔧 Integration Steps:")
    print("=" * 60)
    
    integration_steps = [
        "1. Run the converter to generate your workflow file",
        "2. Review and adjust the generated code if needed",
        "3. Add import to guidex_loadtest.py:",
        "   from workflows.your_workflow_user import YourWorkflowUser",
        "4. Add to __all__ list:",
        "   __all__ = [..., 'YourWorkflowUser']",
        "5. Test the new workflow:",
        "   locust -f guidex_loadtest.py YourWorkflowUser --headless --users=5 --spawn-rate=1 --run-time=30s"
    ]
    
    for step in integration_steps:
        print(f"   {step}")


if __name__ == "__main__":
    print("🚀 HAR to Workflow Converter Test Suite")
    
    # Run the test
    success = test_converter()
    
    # Show usage examples
    show_usage_examples()
    
    if success:
        print(f"\n🎉 All tests passed! The converter is ready to use.")
        print(f"📖 Run with: python3 HARFiles/har_to_workflow.py <har_file.py> <WorkflowName>")
    else:
        print(f"\n❌ Tests failed. Check the converter implementation.")
        sys.exit(1) 