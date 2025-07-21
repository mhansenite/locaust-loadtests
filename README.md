# GuideX Load Testing - Modular Architecture

A comprehensive, modular load testing framework for GuideX using Locust. Features environment-based configuration, multiple user workflows, and production-ready authentication flows.

> 🆕 **NEW AUTOMATION FEATURE!** 
> 
> 🤖 **HAR to Workflow Converter** - Automatically convert HAR files directly into load testing workflows! 
> 
> ```bash
> python3 HARFiles/har_to_workflow.py your_workflow.har WorkflowName
> ```
> 
> **Now supports direct HAR files!** No manual conversion needed.
> See [HAR Converter Guide](utils/README_HAR_CONVERTER.md) for details.

## 🏗️ Architecture Overview

```
locaust-loadtests/
├── HARFiles/
│   ├── har_to_workflow.py      # 🤖 HAR to workflow converter (automation!)
│   ├── README_HAR_CONVERTER.md # 📖 Converter documentation  
│   ├── test_converter.py       # 🧪 Test suite for converter
│   ├── RAW_HAR/                # Your original HAR captures
│   │   ├── GlobalProjects.har
│   │   └── YourWorkflow.har
│   └── RAW_PY/                 # HAR→Python conversions (auto-generated)
│       ├── GlobalProjects.py
│       └── YourWorkflow.py
├── auth/
│   ├── config.py               # Environment variables & configuration
│   └── base_user.py            # Shared authentication logic
├── workflows/
│   ├── project_user.py         # Project-focused activities  
│   ├── global_tasks_user.py    # Global task management
│   ├── global_projects_user.py # Global project management (HAR-based)
│   └── mixed_user.py           # Combined workflows (most realistic)
├── utils/
│   ├── graphql_queries.py      # Reusable GraphQL queries
│   └── api_helpers.py          # Common API patterns
├── guidex_loadtest.py          # Main entry point
├── requirements.txt            # Dependencies
└── .env                        # Environment configuration (create this)
```

## 🚀 Quick Start

### 1. Setup Environment

Create a `.env` file in the project root:

```env
# GuideX Load Testing Configuration

# URLs
BASE_URL_APP=https://app.staging.guidecx.io
PROJECT_URL=https://thundercats.staging.guidecx.io
BASE_URL_API=https://api.staging.guidecx.io

# Authentication
LOGIN_EMAIL=your-email@guidecx.com
LOGIN_PASSWORD=your-password

# Load Testing Parameters
DEFAULT_USERS=10
DEFAULT_SPAWN_RATE=2
DEFAULT_RUN_TIME=60s

# Debug Configuration
DEBUG=false

# Performance Configuration
WAIT_TIME_BETWEEN_TASKS=1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Load Tests

```bash
# Mixed workflow (recommended - most realistic)
locust -f guidex_loadtest.py MixedWorkflowUser --headless --users=10 --spawn-rate=2 --run-time=60s

# Project-focused testing
locust -f guidex_loadtest.py ProjectUser --headless --users=10 --spawn-rate=2 --run-time=60s

# Global tasks testing (requires real GraphQL queries)
locust -f guidex_loadtest.py GlobalTasksUser --headless --users=10 --spawn-rate=2 --run-time=60s

# Global projects testing (HAR-based workflow)
locust -f guidex_loadtest.py GlobalProjectsUser --headless --users=10 --spawn-rate=2 --run-time=60s

# All user types together (distributed load)
locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s

# Interactive web UI
locust -f guidex_loadtest.py
# Then open http://localhost:8089
```

### 🎯 User Types

#### 1. **MixedWorkflowUser** (Recommended)
- **Purpose**: Most realistic user behavior combining multiple features
- **Activities**: Project browsing + global tasks + notifications
- **Weight**: 3 (most common in load tests)
- **Status**: ✅ Production ready

#### 2. **ProjectUser**
- **Purpose**: Traditional project management workflows
- **Activities**: Browse projects, verify authentication, project lists
- **Weight**: 1
- **Status**: ✅ Production ready

#### 3. **GlobalTasksUser**
- **Purpose**: Task management across projects
- **Activities**: View/filter/update global tasks
- **Weight**: 1
- **Status**: ⚠️ Requires real GraphQL queries (placeholder currently)

#### 4. **GlobalProjectsUser** (NEW!)
- **Purpose**: Comprehensive global project management
- **Activities**: Project page loading, filter management, data refresh, asset loading
- **Weight**: 2
- **Status**: ✅ Production ready (HAR-based real workflow)
- **Special**: Based on captured HAR file with authentic API calls

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `BASE_URL_APP` | Main application URL | ✅ | - |
| `PROJECT_URL` | Project-specific URL | ✅ | - |
| `BASE_URL_API` | API base URL | ✅ | - |
| `LOGIN_EMAIL` | Login email address | ✅ | - |
| `LOGIN_PASSWORD` | Login password | ✅ | - |
| `DEFAULT_USERS` | Default concurrent users | ❌ | 10 |
| `DEFAULT_SPAWN_RATE` | Users spawned per second | ❌ | 2 |
| `DEFAULT_RUN_TIME` | Default test duration | ❌ | 60s |
| `DEBUG` | Enable debug logging | ❌ | false |
| `WAIT_TIME_BETWEEN_TASKS` | Seconds between tasks | ❌ | 1 |

### Debug Mode

Set `DEBUG=true` in your `.env` file to enable detailed logging:

```bash
DEBUG=true locust -f guidex_loadtest.py MixedWorkflowUser --headless --users=5 --spawn-rate=1 --run-time=30s
```

## 🔍 Testing Single User

```bash
python3 guidex_loadtest.py
```

This runs a single `MixedWorkflowUser` for debugging and development.

## 📊 Adding New User Workflows

### 1. Create New User Class

```python
# workflows/my_new_user.py
from locust import task
from auth.base_user import AuthenticatedUser
from utils.api_helpers import make_graphql_request

class MyNewUser(AuthenticatedUser):
    weight = 2  # Relative frequency
    
    @task(weight=3)
    def my_main_task(self):
        # Your task implementation
        pass
```

### 2. Add to Main File

```python
# guidex_loadtest.py
from workflows.my_new_user import MyNewUser

__all__ = ['ProjectUser', 'GlobalTasksUser', 'MixedWorkflowUser', 'MyNewUser']
```

### 3. Run Your New User

```bash
locust -f guidex_loadtest.py MyNewUser --headless --users=10 --spawn-rate=2 --run-time=60s
```

## 🛠️ Adding New GraphQL Queries

### 1. Add Query to Utils

```python
# utils/graphql_queries.py
MY_NEW_QUERY = """
query MyNewQuery($input: MyInput!) {
    myData(input: $input) {
        id
        name
        # ... other fields
    }
}
"""
```

### 2. Use in Tasks

```python
from utils.api_helpers import make_graphql_request
from utils.graphql_queries import MY_NEW_QUERY

@task
def my_task(self):
    make_graphql_request(
        client=self.client,
        operation_name="MyNewQuery",
        query=MY_NEW_QUERY,
        variables={"input": {"filter": "value"}},
        auth_token=self.get_auth_header(),
        request_name="My Custom Task"
    )
```

## 📈 Load Testing Scenarios

### Light Load
```bash
locust -f guidex_loadtest.py --headless --users=10 --spawn-rate=2 --run-time=60s
```

### Medium Load
```bash
locust -f guidex_loadtest.py --headless --users=25 --spawn-rate=3 --run-time=120s
```

### Heavy Load
```bash
locust -f guidex_loadtest.py --headless --users=50 --spawn-rate=5 --run-time=300s
```

### Stress Test
```bash
locust -f guidex_loadtest.py --headless --users=100 --spawn-rate=10 --run-time=600s
```

### Target Specific User Types
```bash
# Mixed workflow (recommended)
locust -f guidex_loadtest.py MixedWorkflowUser --headless --users=15 --spawn-rate=3 --run-time=120s

# Project management focus
locust -f guidex_loadtest.py ProjectUser --headless --users=10 --spawn-rate=2 --run-time=60s

# Global projects (HAR-based)
locust -f guidex_loadtest.py GlobalProjectsUser --headless --users=12 --spawn-rate=2 --run-time=90s

# Global tasks (requires real queries)
locust -f guidex_loadtest.py GlobalTasksUser --headless --users=8 --spawn-rate=1 --run-time=60s
```

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Use staging credentials only
- Rotate passwords regularly
- Monitor rate limits and API quotas

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   ModuleNotFoundError: No module named 'auth'
   ```
   **Solution**: Run from the project root directory

2. **Authentication Failures**
   ```bash
   ValueError: No authentication token available
   ```
   **Solution**: Check credentials in `.env` file

3. **Environment Variable Errors**
   ```bash
   Required environment variables are missing: LOGIN_PASSWORD
   ```
   **Solution**: Ensure all required variables are set in `.env`

### Debug Mode

Enable debug logging to see detailed request/response information:

```bash
DEBUG=true python3 guidex_loadtest.py
```

## 📝 TODOs for Global Tasks

The `GlobalTasksUser` contains placeholder GraphQL queries that need to be replaced with actual queries captured from the browser:

1. Capture actual global tasks GraphQL queries
2. Update `GET_GLOBAL_TASKS_QUERY` in `utils/graphql_queries.py`
3. Update `GET_FILTERED_TASKS_QUERY` with real filtering logic
4. Replace placeholder task IDs with dynamic values
5. Implement actual task update workflows

## 🤝 Contributing

1. Follow the modular architecture patterns
2. Add comprehensive docstrings
3. Use the provided utility functions
4. Test with single user mode first
5. Update this README for new features 

## 🤖 HAR to Workflow Automation

### Automatic Workflow Generation

We provide a powerful automation tool that can convert HAR-captured workflows into our modular architecture automatically!

#### 🎯 What It Does

The `HARFiles/har_to_workflow.py` script takes HAR files or HAR-converted Python files and automatically generates:
- ✅ **Direct HAR support** - Uses `har2locust` automatically for `.har` files
- ✅ **Environment-aware URLs** - 🆕 Generates dynamic URLs using `DOMAIN_SUFFIX` configuration
- ✅ **Dynamic Next-Action extraction** - 🆕 Replaces hard-coded action IDs with dynamic extraction
- ✅ **Complete workflow classes** that inherit from `AuthenticatedUser`
- ✅ **Intelligent request grouping** into logical tasks (page loads, API calls, filters, etc.)
- ✅ **Proper imports and configuration** integration
- ✅ **Debug logging and error handling**
- ✅ **Ready-to-run Locust tasks** with appropriate weights
- ✅ **Automatic cleanup** of temporary files

#### 🚀 Quick Start

```bash
# Convert HAR file directly to workflow (recommended!)
python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/YourWorkflow.har YourWorkflowName

# Convert from existing Python file  
python3 HARFiles/har_to_workflow.py HARFiles/RAW_PY/YourWorkflow.py YourWorkflowName

# Example: Convert GlobalProjects HAR file
python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/GlobalProjects.har GlobalProjects
```

#### 📊 What Gets Generated

The tool automatically analyzes your HAR file and groups requests into:

| Category | Description | Weight | Examples |
|----------|-------------|--------|----------|
| **Page Load** | Initial page requests | 3 | `/v2/projects?_rsc=`, navigation |
| **API Calls** | Authentication, data fetching | 2 | `/auth/session`, GraphQL queries |
| **Filters** | Dropdown/filter loading | 2 | `LoadTagsDropdown`, `LoadManagers` |
| **Data Refresh** | Dynamic content updates | 4 | POST refresh actions, state changes |
| **~~Assets~~** | ~~Images, fonts, static files~~ | ~~Filtered~~ | ~~Automatically removed~~ |

> 🗑️ **Static assets are automatically filtered out** - Images, fonts, CSS, JS, and other cached resources are excluded since they don't represent real user load.

#### 🔧 Integration Workflow

1. **Capture & Convert in one step:**
   ```bash
   # Capture your workflow as a HAR file, then convert directly:
   python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/your_workflow.har WorkflowName
   ```

2. **Review the generated file:**
   - Check `workflows/workflow_name_user.py`
   - Adjust task weights if needed
   - Customize request logic for your specific needs

3. **Add to main entry point:**
   ```python
   # In guidex_loadtest.py
   from workflows.workflow_name_user import WorkflowNameUser
   __all__ = [..., 'WorkflowNameUser']
   ```

4. **Test your new workflow:**
   ```bash
   # Single workflow test
   locust -f guidex_loadtest.py WorkflowNameUser --headless --users=5 --spawn-rate=1 --run-time=30s
   
   # Include in full test suite
   locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s
   ```

#### ✨ Example Output

```python
#!/usr/bin/env python3
"""
MyWorkflow User - Auto-generated from HAR file
"""

from locust import task
from auth.base_user import AuthenticatedUser
from auth.config import PROJECT_URL, PROJECT_DOMAIN, DEBUG

class MyWorkflowUser(AuthenticatedUser):
    host = PROJECT_URL
    weight = 2

    @task(weight=3)
    def page_load(self):
        """Page Load - Generated from HAR workflow"""
        if DEBUG:
            print("🔄 Page Load...")
        
        with self.client.get("/api/endpoint", ...) as resp:
            # Automatic error handling and logging
```

#### 🎛️ Advanced Features

- **Direct HAR support** - Automatically runs `har2locust` for `.har` files
- **Smart URL handling** - Automatically handles relative vs absolute URLs
- **Header filtering** - Removes session-specific headers (cookies, auth tokens)
- **Request deduplication** - Groups similar requests intelligently
- **Error handling** - Built-in response validation and logging
- **Weight optimization** - Assigns appropriate task weights based on request types
- **Temporary file cleanup** - Automatically cleans up intermediate files

#### 🔍 Troubleshooting

**Common Issues:**

1. **"har2locust not found"** - Install with `pip install har2locust` (required for HAR files)
2. **"No requests found"** - Check that your HAR file has a class with a `t()` or `task()` method
3. **Import errors** - Ensure the generated file imports are correct for your environment
4. **Authentication issues** - The generated workflow inherits authentication, but may need token adjustments

**Manual Adjustments:**

- **Custom logic** - Add business logic between requests
- **Dynamic data** - Replace hardcoded IDs with dynamic values
- **Error handling** - Customize response validation for specific endpoints
- **Task weights** - Adjust based on your load testing priorities

This tool dramatically speeds up the process of adding new workflows to your load testing suite! 🚀 