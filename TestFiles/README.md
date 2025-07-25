# 🗂️ TestFiles - Modular Load Testing Framework

Comprehensive modular load testing framework extracted from the original `project_cr_phase_milestone.py` file. Each test domain is organized into independent, runnable modules that can operate standalone or be coordinated by the master controller.

## 📁 **Directory Structure**

```
TestFiles/
├── 📄 README.md                           # This documentation
├── 🎛️ master_test_controller.py           # Master coordinator for all modules
├── 🧬 base_test_template.py               # Shared base functionality
├── 🏗️ Projects/
│   ├── Create/
│   │   └── project_create_test.py         # Project creation and deletion
│   ├── Update/                            # (Future: Project updates/renaming)
│   └── View/
│       └── project_view_test.py           # Project plan viewing
├── 📋 Phases/
│   ├── Create/
│   │   └── phase_create_test.py           # Phase creation
│   ├── Update/                            # (Future: Phase modifications)
│   └── View/                              # (Future: Phase viewing)
├── 🎯 Milestones/
│   ├── Create/                            # (Future: From original file)
│   ├── Update/                            # (Future: Milestone updates)
│   └── View/                              # (Future: Milestone viewing)
├── ✅ Tasks/
│   ├── Create/
│   │   └── task_create_test.py            # Task creation (1-10 per execution)
│   ├── Update/                            # (Future: Task updates from HAR files)
│   └── View/                              # (Future: Task viewing)
└── 🔗 SubTasks/
    ├── Create/                            # (Future: Subtask creation)
    ├── Update/                            # (Future: Subtask updates)
    └── View/                              # (Future: Subtask viewing)
```

## 🚀 **Quick Start**

### **Option 1: Master Controller (Recommended)**

Run coordinated tests with automatic dependency management:

```bash
# Run with default settings (balanced scenario, smart coordination)
locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2

# Run specific modules only
ENABLED_MODULES="projects,phases,tasks" locust -f TestFiles/master_test_controller.py

# Run task-focused testing
TEST_SCENARIO="task_focused" locust -f TestFiles/master_test_controller.py

# Run creation-heavy testing
TEST_SCENARIO="creation_heavy" ENABLED_MODULES="projects,phases,tasks" locust -f TestFiles/master_test_controller.py
```

### **Option 2: Standalone Module Testing**

Run individual modules independently:

```bash
# Test project creation only
locust -f TestFiles/Projects/Create/project_create_test.py --users 3 --spawn-rate 1

# Test project viewing only  
PROJECT_ID="your-project-id" PHASE_ID="your-phase-id" \
locust -f TestFiles/Projects/View/project_view_test.py --users 5 --spawn-rate 1

# Test phase creation only
PROJECT_ID="your-project-id" \
locust -f TestFiles/Phases/Create/phase_create_test.py --users 3 --spawn-rate 1

# Test task creation only
PROJECT_ID="your-project-id" PHASE_ID="your-phase-id" \
locust -f TestFiles/Tasks/Create/task_create_test.py --users 5 --spawn-rate 1
```

## ⚙️ **Configuration**

### **Environment Variables**

#### **Authentication (Required)**
```bash
LOGIN_EMAIL="your-email@example.com"
LOGIN_PASSWORD="your-password" 
LOCUST_HOST="https://app.staging.guidecx.io"
```

#### **Project & Phase Management**
```bash
# Project settings
CREATE_NEW_PROJECT="true"              # Create new project vs use existing
PROJECT_NAME_TXT="LoadTestProject"     # Base name for created projects
PROJECT_ID="uuid-of-existing-project"  # Use when CREATE_NEW_PROJECT=false

# Phase settings  
CREATE_NEW_PHASE="true"                # Create new phase vs use existing
PHASE_ID="uuid-of-existing-phase"     # Use when CREATE_NEW_PHASE=false
TEST_PHASE_NAME="LoadTestPhase"        # Base name for created phases

# Test item names
TEST_MILESTONE_NAME="LoadTestMilestone"
TEST_TASK_NAME="LoadTestTask"
```

#### **Master Controller Configuration**
```bash
# Module selection
ENABLED_MODULES="projects,phases,milestones,tasks,subtasks"  # Comma-separated

# Test scenarios
TEST_SCENARIO="balanced"               # balanced|creation_heavy|view_heavy|task_focused

# Coordination mode
COORDINATION_MODE="smart"              # sequential|parallel|smart
```

### **Test Scenarios**

#### **🎯 Balanced (Default)**
Equal distribution across create/view operations
- Project Create: 3, View: 5
- Phase Create: 4
- Task Create: 6, View: 3

#### **🔧 Creation Heavy**
Focus on creation operations for load testing
- Project Create: 6, View: 2  
- Phase Create: 7
- Task Create: 8, View: 1

#### **👁️ View Heavy**  
Focus on viewing operations for read performance
- Project Create: 2, View: 8
- Phase Create: 2
- Task Create: 3, View: 7

#### **📝 Task Focused**
Concentrate on task management operations
- Project Create: 1, View: 2
- Phase Create: 2
- Task Create: 8, View: 5

## 🎛️ **Master Controller Features**

### **Smart Coordination**
- **Dependency Management**: Automatically creates projects before phases, phases before milestones, etc.
- **Ratio Analysis**: Maintains good distribution (2-3 milestones per phase, 3+ tasks per milestone)
- **State Sharing**: All modules share created items for realistic cross-module operations

### **Flexible Module Loading**
```bash
# Projects only
ENABLED_MODULES="projects"

# Projects and phases only  
ENABLED_MODULES="projects,phases"

# Full stack
ENABLED_MODULES="projects,phases,milestones,tasks,subtasks"
```

### **Real-time Coordination**
- **Sequential**: Create dependencies first, then run modules in order
- **Parallel**: Run modules simultaneously with dependency checking  
- **Smart**: Analyze ratios and make intelligent decisions about what to create next

## 📋 **Module Details**

### **Projects/Create (`project_create_test.py`)**
- **Primary Task**: `create_test_project()` - Creates projects using quick create API
- **Features**: 
  - Project creation with automatic naming (timestamp + UUID)
  - Project renaming to desired names
  - Project deletion for cleanup (currently disabled)
  - Fallback handling for creation failures

### **Projects/View (`project_view_test.py`)**  
- **Primary Task**: `view_project_plan()` - Views project plan pages
- **Additional Tasks**:
  - `view_project_plan_board()` - Board view testing
  - `view_project_overview()` - General project viewing
- **Dependencies**: Requires valid PROJECT_ID and PHASE_ID

### **Phases/Create (`phase_create_test.py`)**
- **Primary Task**: `create_test_phase()` - Creates phases within projects
- **Secondary Task**: `create_multiple_phases()` - Batch phase creation (2-3 at once)
- **Features**:
  - Phase creation with unique naming
  - Phase ID extraction and tracking
  - Multiple phase creation for distribution testing

### **Tasks/Create (`task_create_test.py`)**  
- **Primary Task**: `create_task()` - Creates 1-10 random tasks per milestone
- **Helper**: `_create_single_task()` - Creates individual tasks
- **Secondary Task**: `create_single_task_for_random_milestone()` - Focused task creation
- **Features**:
  - Batch task creation (1-10 tasks per execution)
  - Random milestone selection for distribution
  - Task ID extraction and tracking

## 🔧 **Development & Extension**

### **Adding New Modules**

1. **Create the module structure**:
```bash
mkdir -p TestFiles/NewDomain/{Create,Update,View}
```

2. **Create the test file**:
```python
# TestFiles/NewDomain/Create/new_domain_create_test.py
from TestFiles.base_test_template import BaseTestTemplate

class NewDomainCreateTest(BaseTestTemplate):
    @task(5)
    def create_new_domain_item(self):
        # Your implementation here
        pass
```

3. **Add to master controller**:
```python
# In master_test_controller.py
from NewDomain.Create.new_domain_create_test import NewDomainCreateTest

# Add to __init__
self.new_domain_creator = NewDomainCreateTest()

# Add orchestrated task
@task
def orchestrated_new_domain_creation(self):
    if 'newdomain' not in self.ENABLED_MODULES:
        return
    self.new_domain_creator.create_new_domain_item()
```

### **Adding HAR-Based Tasks**

For each HAR file in `/HARFIles/RAW_HAR/Tasks/`:

1. **Analyze the HAR file** for API patterns:
   - URL structure  
   - Payload format
   - Required headers (especially Next-Action)

2. **Create the test method**:
```python
@task(3)
def har_based_task_operation(self):
    """Based on YourHARFile.har analysis"""
    
    # Extract API details from HAR
    url = f"/project/{self.test_project_id}/endpoint"
    payload = json.dumps([{"key": "value"}])
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept': 'text/x-component', 
        'Next-Action': 'action_id_from_har'
    }
    
    # Make the request with proper error handling
    with self.client.post(url, data=payload, headers=headers, catch_response=True) as response:
        if response.status_code == 200:
            response.success()
            # Parse response and update tracking
        else:
            response.failure(f"Failed: {response.status_code}")
```

## 🧪 **Testing & Validation**

### **Standalone Testing**
```bash
# Test individual modules
python TestFiles/Projects/Create/project_create_test.py
python TestFiles/Phases/Create/phase_create_test.py
python TestFiles/Tasks/Create/task_create_test.py
```

### **Master Controller Testing**  
```bash
# Test coordination
python TestFiles/master_test_controller.py

# Test with different scenarios
TEST_SCENARIO="creation_heavy" python TestFiles/master_test_controller.py
```

### **Load Testing**
```bash
# Light load testing
locust -f TestFiles/master_test_controller.py --users 5 --spawn-rate 1 --run-time 60s

# Heavy load testing
locust -f TestFiles/master_test_controller.py --users 20 --spawn-rate 2 --run-time 300s

# Task-focused load testing
TEST_SCENARIO="task_focused" ENABLED_MODULES="tasks" \
locust -f TestFiles/master_test_controller.py --users 15 --spawn-rate 3
```

## 🔍 **Monitoring & Debugging**

### **Logging**
All modules provide detailed console output:
- ✅ Success indicators
- ⚠️ Warning messages  
- ❌ Error indicators
- 🔍 Debug information
- 📊 Statistics and counts

### **State Tracking**  
Monitor created items:
```python
print(f"Created: {len(user.created_projects)} projects, {len(user.created_phases)} phases")
print(f"Tasks: {len(user.created_tasks)} across {len(user.created_milestones)} milestones")
```

### **Dependency Verification**
The master controller automatically checks and reports:
- Missing dependencies before operations
- Ratio analysis for optimal distribution
- Coordination decisions and reasoning

## 🚦 **Next Steps**

### **Immediate Priorities**

1. **Extract remaining functionality** from original file:
   - Milestone creation (`create_milestone()`)
   - Task updates (`update_existing_tasks()`, `_update_single_task()`) 
   - Stress testing classes (`ProjectStressTest`)

2. **Implement HAR-based updates**:
   - `TaskUpdateAssigned.har` → `TestFiles/Tasks/Update/task_update_assigned_test.py`
   - `TaskUpdateEstHours.har` → `TestFiles/Tasks/Update/task_update_hours_test.py`
   - `UpdateTaskDate.har` → `TestFiles/Tasks/Update/task_update_date_test.py`

3. **Add task messaging**:
   - `TaskSendAMessage.har` → `TestFiles/Tasks/Update/task_send_message_test.py`
   - `TaskDeleteMessage.har` → `TestFiles/Tasks/Update/task_delete_message_test.py`
   - `TaskViewMessages.har` → `TestFiles/Tasks/View/task_view_messages_test.py`

4. **Implement subtask operations**:
   - `TaskSubtaskUpdateStatus.har` → `TestFiles/SubTasks/Update/`
   - `TaskSubtaskUpdateAssigned.har` → `TestFiles/SubTasks/Update/`
   - `TaskViewSubTask.har` → `TestFiles/SubTasks/View/`

### **Advanced Features**

- **Dynamic HAR loading**: Load HAR files at runtime for flexible testing
- **Test data management**: CSV-based test data for realistic scenarios  
- **Performance metrics**: Detailed timing and throughput analysis
- **Failure recovery**: Automatic retry and fallback mechanisms
- **Report generation**: Comprehensive test result reporting

---

## 🎉 **Benefits of This Architecture**

✅ **Modularity**: Each domain can be developed and tested independently  
✅ **Reusability**: Modules can be combined in different test scenarios  
✅ **Maintainability**: Easy to update individual components without affecting others  
✅ **Scalability**: Simple to add new test modules as the application grows  
✅ **Flexibility**: Run standalone modules or coordinated suites  
✅ **Debugging**: Isolated testing makes issues easier to identify and fix  
✅ **Team Development**: Multiple developers can work on different modules simultaneously  

This modular approach transforms your large, monolithic test file into a flexible, maintainable testing framework that can grow with your application's complexity. 