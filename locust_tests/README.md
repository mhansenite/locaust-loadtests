# Locust Load Tests

This directory contains Locust load test scripts for testing specific application endpoints.

**NOTE:** The main project load tests have been moved to the `testing_scenarios/` directory for better organization.

## Available Tests

### `testing_scenarios/project.py` - Project Phase and Milestone Load Tests

Tests creating projects, phases and milestones based on HAR file analysis.

**Test Classes:**
- `ProjectPhaseMilestoneLoadTest` - Main test class for project lifecycle testing

**Features:**
- Project creation and deletion
- Phase creation with distribution logic
- Milestone creation and tracking
- Task creation (1-10 tasks per milestone)
- Task updates with realistic data
- Smart phase distribution (2-3 milestones per phase)
- Environment variable configuration

### `testing_scenarios/project_stress.py` - Project Stress Tests

Rapid creation stress testing for projects, phases, milestones, and tasks.

**Test Classes:**
- `ProjectStressTest` - Stress test class for rapid entity creation

**Features:**
- High-frequency task creation (@task(8))
- Milestone creation (@task(5))
- Phase creation (@task(1))
- Faster wait times (1-3 seconds vs 3-8 seconds)
- Environment variable configuration

### `messages.py` - Messaging Load Tests

Tests messaging functionality including viewing messages and submitting new messages via gRPC-Web API.

**Target Endpoints:**
```
/messaging?messageKey=channelId&messageId=dd6ddd7e-8c25-4b5c-a59b-c8389307252a&channelId=dd6ddd7e-8c25-4b5c-a59b-c8389307252a
/manager.message.messages.MessageService/SaveMessage (gRPC-Web)
```

**Test Classes:**
- `MessagingLoadTest` - Main messaging test with view and submit functionality
- `MessageStressTest` - Rapid message submission for stress testing

**Features:**
- Tests messaging page viewing
- gRPC-Web message submission with "loadtest" content
- Recent activity loading
- Mentions loading
- Automatic Bearer token authentication
- Multi-subdomain testing (app.* and k2-web.*)

## Setup

1. **Environment Variables** - Create a `.env` file in the project root:
   ```bash
   LOGIN_EMAIL=your-email@example.com
   LOGIN_PASSWORD=your-password
   LOCUST_HOST=app.staging.guidecx.io
   ```

2. **Dependencies** - Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Quick Test (Single Run)
```bash
# Test project phase/milestone functionality
python testing_scenarios/project.py

# Test stress testing functionality  
python testing_scenarios/project_stress.py

# Test messaging functionality
python locust_tests/messages.py
```

### Full Load Test
```bash
# Run project tests with Locust web UI
locust -f testing_scenarios/project.py --host https://app.staging.guidecx.io

# Run stress tests
locust -f testing_scenarios/project_stress.py --host https://app.staging.guidecx.io

# Run messaging tests
locust -f locust_tests/messages.py --host https://app.staging.guidecx.io

# Run headless with specific users and duration
locust -f testing_scenarios/project.py --host https://app.staging.guidecx.io \
  --users 10 --spawn-rate 2 --run-time 60s --headless
```

### Specific Test Class
```bash
# Run only the main project test
locust -f testing_scenarios/project.py ProjectPhaseMilestoneLoadTest

# Run stress testing
locust -f testing_scenarios/project_stress.py ProjectStressTest

# Run only messaging tests
locust -f locust_tests/messages.py MessagingLoadTest

# Run stress testing for messages
locust -f locust_tests/messages.py MessageStressTest
```

## Test Tasks

### ProjectPhaseMilestoneLoadTest Tasks:
- `view_project_plan` (weight: 6) - Tests project plan page loading
- `create_test_phase` (weight: 6) - Creates new phases for distribution
- `create_task` (weight: 5) - Creates 1-10 tasks under milestones
- `create_milestone` (weight: 4) - Creates milestones in phases
- `update_existing_tasks` (weight: 3) - Updates task assignments and status

### ProjectStressTest Tasks:
- `create_stress_task` (weight: 8) - High-frequency task creation
- `create_stress_milestone` (weight: 5) - Rapid milestone creation
- `create_stress_phase_task` (weight: 1) - Phase creation for stress testing

### MessagingLoadTest Tasks:
- `view_messaging_page` (weight: 4) - Tests messaging page loading
- `submit_message_grpc` (weight: 3) - Tests gRPC-Web message submission
- `load_recent_activity` (weight: 2) - Tests recent activity loading
- `load_mentions` (weight: 1) - Tests mentions loading

### Expected Responses:
- **200**: Success - request completed
- **403**: Access denied - check user permissions
- **404**: Resource not found - verify IDs are correct
- **401**: Authentication failed - check Bearer token

## Environment Variables for Project Tests

The project tests support extensive configuration via environment variables:

```bash
# Project Configuration
export CREATE_NEW_PROJECT="true"  # Set to "false" to use existing PROJECT_ID
export PROJECT_NAME_TXT="LoadTestProject"  # Base name for created projects
export PROJECT_ID="existing-project-uuid"  # Use when CREATE_NEW_PROJECT=false

# Phase Configuration  
export CREATE_NEW_PHASE="true"  # Set to "false" to use existing PHASE_ID
export PHASE_ID="existing-phase-uuid"  # Use when CREATE_NEW_PHASE=false
export TEST_PHASE_NAME="LoadTestPhase"  # Base name for created phases

# Task/Milestone Configuration
export TEST_MILESTONE_NAME="LoadTestMilestone"  # Base name for milestones
export TEST_TASK_NAME="LoadTestTask"  # Base name for tasks

# Authentication
export LOGIN_EMAIL="your-email@example.com"
export LOGIN_PASSWORD="your-password"
export LOCUST_HOST="https://app.staging.guidecx.io"
```

### Example Usage with Environment Variables:
```bash
# Test with new project creation
CREATE_NEW_PROJECT="true" PROJECT_NAME_TXT="LoadTestProject" \
CREATE_NEW_PHASE="true" TEST_PHASE_NAME="LoadTestPhase" \
TEST_MILESTONE_NAME="LoadTestMilestone" TEST_TASK_NAME="LoadTestTask" \
python testing_scenarios/project.py

# Test with existing project
CREATE_NEW_PROJECT="false" PROJECT_ID="existing-project-id" \
CREATE_NEW_PHASE="false" PHASE_ID="existing-phase-id" \
python testing_scenarios/project.py
```

## Customization

### Adding More Message/Channel IDs
Edit the constants in `MessagingLoadTest`:

```python
MESSAGE_ID = "your-message-id"
CHANNEL_ID = "your-channel-id"
TEST_MESSAGE_TEXT = "your-test-message"
```

### Creating New Tests
1. Create a new `.py` file in the `testing_scenarios/` directory
2. Import `AuthenticatedUser` from the common directory:
   ```python
   import sys
   import os
   sys.path.append(os.path.dirname(os.path.dirname(__file__)))
   from common.auth import AuthenticatedUser
   ```
3. Create your test class inheriting from `AuthenticatedUser`

## Authentication

All tests automatically handle authentication using the `common/auth.py` module:
- ✅ Automatic login on test start
- ✅ Session cookie management
- ✅ Bearer token handling for API calls
- ✅ Re-authentication if session expires

## Troubleshooting

### Authentication Issues
```bash
# Test authentication directly
python common/auth.py
```

### Project Access Issues
- Verify the user has access to the specific project ID
- Check if the phase ID exists in the project
- Confirm the user role has appropriate permissions

### Environment Variable Issues
```bash
# Verify environment variables
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('Email:', os.getenv('LOGIN_EMAIL'))
print('Host:', os.getenv('LOCUST_HOST'))
print('Create New Project:', os.getenv('CREATE_NEW_PROJECT'))
print('Project ID:', os.getenv('PROJECT_ID'))
print('Password set:', bool(os.getenv('LOGIN_PASSWORD')))
"
```

### Messaging Issues
- Verify the user has access to the specific channel/message IDs
- Check if the gRPC-Web endpoints are accessible
- Confirm Bearer token is being properly extracted from session 