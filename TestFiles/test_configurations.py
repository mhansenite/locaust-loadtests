#!/usr/bin/env python3
"""
Test Configuration Manager
Predefined test scenarios with all environment variables organized by test number

Usage:
    python TestFiles/test_configurations.py --test 1
    python TestFiles/test_configurations.py --list
    source TestFiles/test_configurations.sh 3
"""

import os
import sys
import argparse
from typing import Dict, Any

# =============================================================================
# 🔧 SHARED VARIABLES - UPDATE THESE FOR YOUR ENVIRONMENT
# =============================================================================

# Common Project/Phase IDs (UPDATE THESE FOR YOUR ENVIRONMENT)
DEFAULT_PROJECT_ID = "e34b9b43-fa9f-4a09-a3bf-1178f471a5dc"
DEFAULT_PHASE_ID = "e34bcc9e-18b2-44f7-9384-d1d8af35de78"

# Note: Authentication variables (LOGIN_EMAIL, LOGIN_PASSWORD, LOCUST_HOST) 
# should be set in your .env file and will be loaded automatically

# =============================================================================
# 🔧 TEST CONFIGURATIONS
# =============================================================================

TEST_CONFIGURATIONS = {
    
    # === BASIC CONFIGURATIONS ===
    
    1: {
        "name": "🆕 Full New Project Creation",
        "description": "Creates everything from scratch - project, phases, milestones, tasks",
        "use_case": "Testing complete project lifecycle from start to finish",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "FullLifecycleTest",
            "PROJECT_ID": "",  # Not used when CREATE_NEW_PROJECT=true
            
            # Phase Settings
            "CREATE_NEW_PHASE": "true", 
            "PHASE_ID": "",  # Not used when CREATE_NEW_PHASE=true
            "TEST_PHASE_NAME": "FullTestPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "FullTestMilestone",
            "TEST_TASK_NAME": "FullTestTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects,phases,milestones,tasks",
            "TEST_SCENARIO": "balanced",
            "COORDINATION_MODE": "smart"
        }
    },
    
    2: {
        "name": "📂 Use Existing Project - Task Focus",
        "description": "Uses existing project/phase, focuses on task creation and management", 
        "use_case": "Testing task operations without creating new projects",
        "env_vars": {
            # Project Settings (Use existing)
            "CREATE_NEW_PROJECT": "false",
            "PROJECT_NAME_TXT": "ExistingProject",
            "PROJECT_ID": DEFAULT_PROJECT_ID,
            
            # Phase Settings (Use existing)
            "CREATE_NEW_PHASE": "false",
            "PHASE_ID": DEFAULT_PHASE_ID,
            "TEST_PHASE_NAME": "ExistingPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "TaskFocusedMilestone", 
            "TEST_TASK_NAME": "TaskFocusedTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "milestones,tasks",
            "TEST_SCENARIO": "task_focused",
            "COORDINATION_MODE": "smart"
        }
    },
    
    # === LOAD TESTING SCENARIOS ===
    
    3: {
        "name": "🔥 Creation Heavy Load Test",
        "description": "Heavy focus on creation operations - stress test creation APIs",
        "use_case": "Testing system under heavy creation load, database write performance",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "CreationLoadTest",
            "PROJECT_ID": "",
            
            # Phase Settings
            "CREATE_NEW_PHASE": "true",
            "PHASE_ID": "",
            "TEST_PHASE_NAME": "CreationPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "CreationMilestone",
            "TEST_TASK_NAME": "CreationTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects,phases,milestones,tasks",
            "TEST_SCENARIO": "creation_heavy",
            "COORDINATION_MODE": "parallel"
        }
    },
    
    4: {
        "name": "👁️ View Heavy Load Test", 
        "description": "Heavy focus on viewing operations - test read performance",
        "use_case": "Testing system under heavy read load, caching performance, page load times",
        "env_vars": {
            # Project Settings (Use existing for viewing)
            "CREATE_NEW_PROJECT": "false",
            "PROJECT_NAME_TXT": "ViewLoadTest",
            "PROJECT_ID": DEFAULT_PROJECT_ID,
            
            # Phase Settings (Use existing)
            "CREATE_NEW_PHASE": "false", 
            "PHASE_ID": DEFAULT_PHASE_ID,
            "TEST_PHASE_NAME": "ViewPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "ViewMilestone",
            "TEST_TASK_NAME": "ViewTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects,phases,tasks",
            "TEST_SCENARIO": "view_heavy", 
            "COORDINATION_MODE": "parallel"
        }
    },
    
    5: {
        "name": "📝 Task Management Focus",
        "description": "Concentrated testing on task creation, updates, and management",
        "use_case": "Testing task-specific features and performance",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "TaskManagementTest", 
            "PROJECT_ID": "",
            
            # Phase Settings
            "CREATE_NEW_PHASE": "true",
            "PHASE_ID": "",
            "TEST_PHASE_NAME": "TaskPhase",
            
            # Test Item Names  
            "TEST_MILESTONE_NAME": "TaskMilestone",
            "TEST_TASK_NAME": "TaskManagementTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "phases,milestones,tasks,subtasks",
            "TEST_SCENARIO": "task_focused",
            "COORDINATION_MODE": "smart"
        }
    },
    
    # === DEVELOPMENT & DEBUGGING ===
    
    6: {
        "name": "🐛 Debug/Development Mode",
        "description": "Sequential operations for debugging, predictable behavior",
        "use_case": "Debugging test issues, development testing, step-by-step validation",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "DebugTest",
            "PROJECT_ID": "",
            
            # Phase Settings
            "CREATE_NEW_PHASE": "true", 
            "PHASE_ID": "",
            "TEST_PHASE_NAME": "DebugPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "DebugMilestone", 
            "TEST_TASK_NAME": "DebugTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects,phases,milestones,tasks",
            "TEST_SCENARIO": "balanced",
            "COORDINATION_MODE": "sequential"
        }
    },
    
    7: {
        "name": "🏗️ Project Creation Only",
        "description": "Focus only on project creation and management",
        "use_case": "Testing project-specific APIs and functionality",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "ProjectOnlyTest",
            "PROJECT_ID": "",
            
            # Phase Settings (minimal)
            "CREATE_NEW_PHASE": "false",
            "PHASE_ID": "",
            "TEST_PHASE_NAME": "ProjectPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "ProjectMilestone",
            "TEST_TASK_NAME": "ProjectTask", 
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects",
            "TEST_SCENARIO": "creation_heavy",
            "COORDINATION_MODE": "smart"
        }
    },
    
    # === ADVANCED SCENARIOS ===
    
    8: {
        "name": "⚡ High Performance Test",
        "description": "Maximum load testing with high concurrency",
        "use_case": "Stress testing system limits, performance benchmarking",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "PerformanceTest",
            "PROJECT_ID": "",
            
            # Phase Settings
            "CREATE_NEW_PHASE": "true",
            "PHASE_ID": "",
            "TEST_PHASE_NAME": "PerfPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "PerfMilestone",
            "TEST_TASK_NAME": "PerfTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects,phases,milestones,tasks",
            "TEST_SCENARIO": "creation_heavy", 
            "COORDINATION_MODE": "parallel"
        }
    },
    
    9: {
        "name": "🔄 Mixed Operations Test",
        "description": "Realistic mix of all operations with balanced load",
        "use_case": "Simulating real user behavior across all features",
        "env_vars": {
            # Project Settings
            "CREATE_NEW_PROJECT": "true", 
            "PROJECT_NAME_TXT": "MixedOpsTest",
            "PROJECT_ID": "",
            
            # Phase Settings
            "CREATE_NEW_PHASE": "true",
            "PHASE_ID": "",
            "TEST_PHASE_NAME": "MixedPhase",
            
            # Test Item Names
            "TEST_MILESTONE_NAME": "MixedMilestone",
            "TEST_TASK_NAME": "MixedTask",
            
            # Master Controller Settings
            "ENABLED_MODULES": "projects,phases,milestones,tasks,subtasks",
            "TEST_SCENARIO": "balanced",
            "COORDINATION_MODE": "smart"
        }
    },
    
    10: {
        "name": "🧪 Custom Template",
        "description": "Template for creating custom test configurations",
        "use_case": "Starting point for creating your own test scenarios",
        "env_vars": {
            # Project Settings (CUSTOMIZE THESE)
            "CREATE_NEW_PROJECT": "true",
            "PROJECT_NAME_TXT": "CustomTest",
            "PROJECT_ID": "your-project-id-if-using-existing",
            
            # Phase Settings (CUSTOMIZE THESE)
            "CREATE_NEW_PHASE": "true",
            "PHASE_ID": "your-phase-id-if-using-existing", 
            "TEST_PHASE_NAME": "CustomPhase",
            
            # Test Item Names (CUSTOMIZE THESE)
            "TEST_MILESTONE_NAME": "CustomMilestone",
            "TEST_TASK_NAME": "CustomTask",
            
            # Master Controller Settings (CUSTOMIZE THESE)
            "ENABLED_MODULES": "projects,phases,milestones,tasks",
            "TEST_SCENARIO": "balanced",  # balanced|creation_heavy|view_heavy|task_focused
            "COORDINATION_MODE": "smart"   # sequential|parallel|smart
        }
    }
}

# =============================================================================
# 🛠️ UTILITY FUNCTIONS
# =============================================================================

def list_all_configurations():
    """List all available test configurations"""
    print("🗂️ Available Test Configurations:\n")
    
    for test_num, config in TEST_CONFIGURATIONS.items():
        print(f"Test {test_num}: {config['name']}")
        print(f"   📄 {config['description']}")
        print(f"   🎯 Use case: {config['use_case']}")
        print(f"   📋 Modules: {config['env_vars']['ENABLED_MODULES']}")
        print(f"   🎭 Scenario: {config['env_vars']['TEST_SCENARIO']}")
        print(f"   🔗 Mode: {config['env_vars']['COORDINATION_MODE']}")
        print()

def show_configuration(test_num: int):
    """Show detailed configuration for a specific test"""
    if test_num not in TEST_CONFIGURATIONS:
        print(f"❌ Test {test_num} not found. Available tests: {list(TEST_CONFIGURATIONS.keys())}")
        return
    
    config = TEST_CONFIGURATIONS[test_num]
    print(f"🔧 Test {test_num}: {config['name']}\n")
    print(f"📄 Description: {config['description']}")
    print(f"🎯 Use case: {config['use_case']}\n")
    
    print("📋 Environment Variables:")
    print("=" * 50)
    
    # Group variables by category
    auth_vars = {}
    project_vars = {}
    phase_vars = {}
    naming_vars = {}
    controller_vars = {}
    
    for key, value in config['env_vars'].items():
        if key in ['LOGIN_EMAIL', 'LOGIN_PASSWORD', 'LOCUST_HOST']:
            auth_vars[key] = value
        elif 'PROJECT' in key:
            project_vars[key] = value
        elif 'PHASE' in key:
            phase_vars[key] = value
        elif key.startswith('TEST_'):
            naming_vars[key] = value
        else:
            controller_vars[key] = value
    
    print("\n🔐 Authentication:")
    for key, value in auth_vars.items():
        print(f"export {key}=\"{value}\"")
    
    print("\n🏗️ Project Settings:")
    for key, value in project_vars.items():
        print(f"export {key}=\"{value}\"")
    
    print("\n📋 Phase Settings:")
    for key, value in phase_vars.items():
        print(f"export {key}=\"{value}\"")
        
    print("\n🏷️ Test Item Names:")
    for key, value in naming_vars.items():
        print(f"export {key}=\"{value}\"")
        
    print("\n🎛️ Master Controller:")
    for key, value in controller_vars.items():
        print(f"export {key}=\"{value}\"")

def apply_configuration(test_num: int):
    """Apply configuration to current environment"""
    if test_num not in TEST_CONFIGURATIONS:
        print(f"❌ Test {test_num} not found")
        return False
    
    config = TEST_CONFIGURATIONS[test_num]
    print(f"🔧 Applying Test {test_num}: {config['name']}")
    
    for key, value in config['env_vars'].items():
        os.environ[key] = str(value)
        print(f"  ✅ {key}={value}")
    
    print(f"\n🎉 Configuration applied! You can now run:")
    print(f"locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2")
    return True

def generate_shell_script():
    """Generate shell script for easy configuration loading"""
    script_content = '''#!/bin/bash
# Test Configuration Shell Script
# Usage: source TestFiles/test_configurations.sh <test_number>

if [ $# -eq 0 ]; then
    echo "🗂️ Usage: source TestFiles/test_configurations.sh <test_number>"
    echo "📋 Available tests:"
'''
    
    for test_num, config in TEST_CONFIGURATIONS.items():
        script_content += f'    echo "  {test_num}: {config["name"]}"\n'
    
    script_content += '''    return 1
fi

TEST_NUM=$1

case $TEST_NUM in
'''
    
    for test_num, config in TEST_CONFIGURATIONS.items():
        script_content += f'    {test_num})\n'
        script_content += f'        echo "🔧 Loading Test {test_num}: {config["name"]}"\n'
        for key, value in config['env_vars'].items():
            script_content += f'        export {key}="{value}"\n'
        script_content += f'        echo "✅ Test {test_num} configuration loaded!"\n'
        script_content += f'        echo "🚀 Run: locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2"\n'
        script_content += '        ;;\n'
    
    script_content += '''    *)
        echo "❌ Invalid test number: $TEST_NUM"
        echo "📋 Available tests: 1-10"
        return 1
        ;;
esac
'''
    
    return script_content

# =============================================================================
# 🚀 MAIN EXECUTION
# =============================================================================

def main():
    """Main function for command line usage"""
    parser = argparse.ArgumentParser(description='Test Configuration Manager')
    parser.add_argument('--test', '-t', type=int, help='Apply specific test configuration')
    parser.add_argument('--show', '-s', type=int, help='Show specific test configuration')
    parser.add_argument('--list', '-l', action='store_true', help='List all configurations')
    parser.add_argument('--generate-shell', '-g', action='store_true', help='Generate shell script')
    
    args = parser.parse_args()
    
    if args.list:
        list_all_configurations()
    elif args.show:
        show_configuration(args.show)
    elif args.test:
        apply_configuration(args.test)
    elif args.generate_shell:
        script_content = generate_shell_script()
        script_path = 'test_configurations.sh' if os.path.basename(os.getcwd()) == 'TestFiles' else 'TestFiles/test_configurations.sh'
        with open(script_path, 'w') as f:
            f.write(script_content)
        os.chmod(script_path, 0o755)
        print(f"✅ Generated {script_path}")
        print(f"🚀 Usage: source {script_path} <test_number>")
    else:
        list_all_configurations()
        print("\n🔧 Usage Examples:")
        print("  python TestFiles/test_configurations.py --test 1")
        print("  python TestFiles/test_configurations.py --show 3") 
        print("  python TestFiles/test_configurations.py --list")
        print("  python TestFiles/test_configurations.py --generate-shell")

if __name__ == "__main__":
    main() 