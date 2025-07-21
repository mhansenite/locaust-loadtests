# Authentication Workflows

Authentication and authorization workflows for the GuideCX platform.

## 📋 Workflows Needed

- **login_user.py** - Standard login flows for different user types
- **logout_user.py** - Logout and session termination
- **password_reset_user.py** - Password reset workflows
- **session_management_user.py** - Session handling and timeout
- **multi_role_access_user.py** - Users with multiple role access
- **sso_integration_user.py** - Single sign-on authentication flows

## 🎬 HAR Files to Record

- **login.har** - Record login for customer, admin, PM users
- **logout.har** - Record logout and session cleanup
- **password_reset.har** - Record password reset workflow
- **session_management.har** - Record session timeout handling
- **multi_role_access.har** - Record role switching workflows
- **sso_integration.har** - Record SSO authentication flows

## 🚀 Usage

After recording HAR files and generating workflows:

```bash
# Generate workflow from HAR
python3 HARFIles/har_to_workflow.py your_file.har YourWorkflowName authentication

# Test the workflow
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py YourWorkflowNameUser --users=5 --spawn-rate=1
```

## 📁 File Organization

```
authentication/
├── README.md                    # This file
├── workflow_name_user.py        # Generated workflow files
└── __init__.py                  # Python module initialization
```

## 🎯 Priority

- **High**: Core authentication flows (login/logout)
- **Medium**: Password reset and session management
- **Low**: SSO and advanced role switching

## 📝 Recording Instructions

### Login Flows (HIGH PRIORITY)
1. Record different user types:
   - Customer user login
   - Project manager login
   - Admin user login
2. Include failed login attempts
3. Capture redirect flows after login

### Logout (MEDIUM PRIORITY)
1. Record complete logout process
2. Session cleanup verification
3. Redirect to login page

### Password Reset (MEDIUM PRIORITY)
1. Record full password reset flow:
   - Request reset email
   - Email link interaction
   - New password submission
   - Login with new password

### Session Management (LOW PRIORITY)
1. Record session timeout scenarios
2. Session refresh workflows
3. Concurrent session handling

## 📝 Notes

- Test across different environments (staging/production)
- Include error scenarios and validation
- Capture authentication tokens and session cookies
- Test mobile authentication flows 