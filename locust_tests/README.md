# Locust Load Tests

This directory contains Locust load test scripts for testing specific application endpoints.

## Available Tests

### `project.py` - Project Plan Load Tests

Tests the project plan endpoints with specific project and phase IDs.

**Target Endpoint:**
```
/project/7c235b03-d4ea-4d0d-a499-a466b43a3c83/plan?phase=6ee9e420-f690-45ff-b5cd-860f15423a3e&view=board
```

**Test Classes:**
- `ProjectPlanLoadTest` - Main test class for the specific project
- `MultiProjectLoadTest` - Extensible test for multiple project scenarios

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
# Test authentication and basic functionality
python locust_tests/project.py

# Test messaging functionality
python locust_tests/messages.py
```

### Full Load Test
```bash
# Run with Locust web UI
locust -f locust_tests/project.py --host https://app.staging.guidecx.io

# Run messaging tests
locust -f locust_tests/messages.py --host https://app.staging.guidecx.io

# Run headless with specific users and duration
locust -f locust_tests/project.py --host https://app.staging.guidecx.io \
  --users 10 --spawn-rate 2 --run-time 60s --headless
```

### Specific Test Class
```bash
# Run only the main project test
locust -f locust_tests/project.py ProjectPlanLoadTest

# Run the multi-project test
locust -f locust_tests/project.py MultiProjectLoadTest

# Run only messaging tests
locust -f locust_tests/messages.py MessagingLoadTest

# Run stress testing for messages
locust -f locust_tests/messages.py MessageStressTest
```

## Test Tasks

### ProjectPlanLoadTest Tasks:
- `view_project_plan_board` (weight: 5) - Tests board view with phase
- `view_project_plan_without_phase` (weight: 3) - Tests default view
- `view_project_plan_list_view` (weight: 2) - Tests list view
- `test_project_api_call` (weight: 1) - Tests API endpoint

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

## Customization

### Adding More Project IDs
Edit the `TEST_SCENARIOS` in `MultiProjectLoadTest`:

```python
TEST_SCENARIOS = [
    {
        'project_id': '7c235b03-d4ea-4d0d-a499-a466b43a3c83',
        'phase_id': '6ee9e420-f690-45ff-b5cd-860f15423a3e',
        'view': 'board'
    },
    {
        'project_id': 'your-project-id',
        'phase_id': 'your-phase-id',
        'view': 'list'
    }
]
```

### Adding More Message/Channel IDs
Edit the constants in `MessagingLoadTest`:

```python
MESSAGE_ID = "your-message-id"
CHANNEL_ID = "your-channel-id"
TEST_MESSAGE_TEXT = "your-test-message"
```

### Creating New Tests
1. Create a new `.py` file in this directory
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

### Messaging Issues
- Verify the user has access to the specific channel/message IDs
- Check if the gRPC-Web endpoints are accessible
- Confirm Bearer token is being properly extracted from session

### Environment Issues
```bash
# Verify environment variables
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('Email:', os.getenv('LOGIN_EMAIL'))
print('Host:', os.getenv('LOCUST_HOST'))
print('Password set:', bool(os.getenv('LOGIN_PASSWORD')))
"
``` 