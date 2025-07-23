# Authentication Script for Locust Load Testing

This `common/auth.py` script provides a simple authentication implementation for Locust load testing using the FastHttpUser class.

## Environment Variables Required

Create a `.env` file in the project root with the following variables:

```bash
# Login credentials
LOGIN_EMAIL=your-email@example.com
LOGIN_PASSWORD=your-password

# Host configuration  
LOCUST_HOST=https://app.staging.guidecx.io

# Optional: Debug mode for verbose logging
DEBUG=false
```

## Environment Examples

```bash
# Development
LOCUST_HOST=https://app.dev.guidecx.io

# Staging  
LOCUST_HOST=https://app.staging.guidecx.io

# Production
LOCUST_HOST=https://app.guidecx.com
```

## Usage

### Basic Usage

```python
from common.auth import AuthenticatedUser

class MyLoadTest(AuthenticatedUser):
    def test_projects(self):
        # This will automatically authenticate if needed
        response = self.make_authenticated_request('GET', '/projects')
        assert response.status_code == 200
```

### Direct Authentication Testing

Run the script directly to test authentication:

```bash
python common/auth.py
```

### Using with Locust

```bash
# Using the auth script in a locustfile
locust -f common/auth.py --host https://app.staging.guidecx.io
```

## Features

- **Environment Variable Configuration**: Uses LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST
- **Automatic Authentication**: Authenticates on startup using `on_start()` 
- **Complete Cookie Handling**: Ensures all session cookies are properly established
- **Session Management**: Retrieves and stores session data for API calls
- **Next.js Support**: Handles Next.js action IDs for form submissions
- **Bearer Token Support**: Automatically adds Authorization headers when available
- **Error Handling**: Comprehensive error handling and logging
- **Cookie Debugging**: Shows active cookies for troubleshooting
- **Testing Support**: Can be run directly for authentication testing

## Authentication Flow

The script implements the authentication flow discovered in the codebase analysis:

1. **Get Login Page**: Retrieves `/auth/login` to extract any required tokens
2. **Extract Action ID**: Parses Next.js action IDs from the login page if present
3. **Submit Credentials**: Posts to `/auth/basic` with email/password
4. **Validate Success**: Checks for successful redirect away from auth pages
5. **Complete Flow**: Visits `/projects` to ensure all cookies are properly established
6. **Get Session Data**: Retrieves session information from `/auth/session`
7. **Store Tokens**: Extracts and stores access tokens for future API calls

## Methods

### `authenticate()`
Performs the complete authentication flow and returns True/False for success.

### `make_authenticated_request(method, path, **kwargs)`
Makes an authenticated HTTP request with proper headers and tokens.

### `get_auth_headers()`
Returns authentication headers including Bearer tokens when available.

## Error Handling

The script provides detailed error messages and logging:
- Missing environment variables
- Authentication failures  
- Session retrieval issues
- API request problems

## Dependencies

Required packages (already in requirements.txt):
- `locust>=2.0.0`
- `python-dotenv>=0.19.0` 