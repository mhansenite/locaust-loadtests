from locust import task, run_single_user
from locust import FastHttpUser
import sys
import re
import uuid
import os
from urllib.parse import quote, quote_plus
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# LOAD TESTING CONFIGURATION FROM ENVIRONMENT VARIABLES
# =============================================================================

# URLs - loaded from environment variables
BASE_URL_APP = os.getenv("BASE_URL_APP")
PROJECT_URL = os.getenv("PROJECT_URL")
BASE_URL_API = os.getenv("BASE_URL_API")

# Authentication - loaded from environment variables
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

# Load Testing Parameters (loaded from environment)
DEFAULT_USERS = os.getenv("DEFAULT_USERS")
DEFAULT_SPAWN_RATE = os.getenv("DEFAULT_SPAWN_RATE")
DEFAULT_RUN_TIME = os.getenv("DEFAULT_RUN_TIME")
DEBUG = os.getenv("DEBUG")
WAIT_TIME_BETWEEN_TASKS = os.getenv("WAIT_TIME_BETWEEN_TASKS")

# Validate required environment variables
required_vars = {
    "BASE_URL_APP": BASE_URL_APP,
    "PROJECT_URL": PROJECT_URL,
    "BASE_URL_API": BASE_URL_API,
    "LOGIN_EMAIL": LOGIN_EMAIL,
    "LOGIN_PASSWORD": LOGIN_PASSWORD,
    "DEFAULT_USERS": DEFAULT_USERS,
    "DEFAULT_SPAWN_RATE": DEFAULT_SPAWN_RATE,
    "DEFAULT_RUN_TIME": DEFAULT_RUN_TIME,
    "DEBUG": DEBUG,
    "WAIT_TIME_BETWEEN_TASKS": WAIT_TIME_BETWEEN_TASKS
}

missing_vars = [var for var, value in required_vars.items() if not value]
if missing_vars:
    raise ValueError(f"Required environment variables are missing: {', '.join(missing_vars)}")

# Convert to appropriate types after validation
DEFAULT_USERS = int(DEFAULT_USERS)          # Number of concurrent users to simulate
DEFAULT_SPAWN_RATE = int(DEFAULT_SPAWN_RATE)      # Users to spawn per second
DEBUG = DEBUG.lower() in ("true", "1", "yes")               # Set to False to disable debug prints (recommended for headless mode)
WAIT_TIME_BETWEEN_TASKS = int(WAIT_TIME_BETWEEN_TASKS)  # Seconds to wait between API calls per user

# READY-TO-RUN LOCUST COMMANDS (copy/paste these):
# locust -f login.py --headless --users=10 --spawn-rate=2 --run-time=60s    # Default load test
# locust -f login.py --headless --users=25 --spawn-rate=3 --run-time=120s   # Medium load test  
# locust -f login.py --headless --users=50 --spawn-rate=5 --run-time=300s   # Heavy load test
# locust -f login.py                                                        # Interactive web UI
# Extract domain names for host headers and form data
APP_DOMAIN = BASE_URL_APP.replace("https://", "")       # app.guidecx.com
PROJECT_DOMAIN = PROJECT_URL.replace("https://", "")   # arches.guidecx.com  
API_DOMAIN = BASE_URL_API.replace("https://", "")      # api.guidecx.com
# URL-encoded versions for use in URLs and payloads
LOGIN_EMAIL_ENCODED = quote_plus(LOGIN_EMAIL)  # For URL parameters
LOGIN_EMAIL_JSON_ENCODED = quote(LOGIN_EMAIL)  # For JSON in URLs

class LoginFlow(FastHttpUser):
    host = BASE_URL_APP
    
    # Load testing configuration
    weight = 1  # Relative weight when multiple user classes exist
    
    # Default wait time between tasks (in seconds)
    wait_time = lambda self: WAIT_TIME_BETWEEN_TASKS
    
    default_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    def get_auth_header(self):
        """
        Get the authorization header for API calls
        Returns the captured token or raises an error if not available
        """
        if self.auth_token:
            return self.auth_token
        else:
            raise ValueError("No authentication token available - login flow may have failed")

    def extract_next_action_id(self, html_content):
        """
        Extract Next-Action ID from HTML content
        Looks for patterns like:
        - <form ... data-action="ID">
        - <input name="$ACTION_1:0" value='{"id":"ID",...}'>
        - JavaScript variables containing action IDs
        """
        if not html_content:
            return None
            
        # Pattern 1: Look for data-action attribute in forms
        action_pattern = r'data-action="([a-f0-9]{40})"'
        match = re.search(action_pattern, html_content)
        if match:
            return match.group(1)
        
        # Pattern 2: Look for action ID in hidden input values (JSON format)
        json_pattern = r'"id":"([a-f0-9]{40})"'
        match = re.search(json_pattern, html_content)
        if match:
            return match.group(1)
        
        # Pattern 3: Look for Next-Action in script tags or meta tags
        script_pattern = r'Next-Action["\']?\s*[:\=]\s*["\']([a-f0-9]{40})["\']'
        match = re.search(script_pattern, html_content, re.IGNORECASE)
        if match:
            return match.group(1)
        
        # Pattern 4: Look for the action ID in form elements
        form_pattern = r'name="[^"]*\$ACTION[^"]*"\s*value="[^"]*([a-f0-9]{40})[^"]*"'
        match = re.search(form_pattern, html_content)
        if match:
            return match.group(1)
        
        return None
    
    def extract_action_key(self, html_content):
        """
        Extract the action key (like k3939455420) from HTML content
        """
        if not html_content:
            return None
            
        # Look for action key in form data
        key_pattern = r'name="[^"]*\$ACTION_KEY[^"]*"\s*value="([^"]*)"'
        match = re.search(key_pattern, html_content)
        if match:
            return match.group(1)
        
        # Alternative pattern for action keys
        key_pattern2 = r'"[^"]*\$ACTION_KEY[^"]*"[^"]*"([^"]*)"'
        match = re.search(key_pattern2, html_content)
        if match:
            return match.group(1)
            
        return "k3939455420"  # Fallback to hardcoded value
    
    def extract_or_generate_boundary(self, html_content=None):
        """
        Extract boundary from HTML content or generate a random one
        Boundaries are used in multipart form data and should be unique
        """
        if html_content:
            # Pattern 1: Look for boundary in Content-Type headers or JavaScript
            boundary_pattern = r'boundary[=:]?\s*["\']?([a-zA-Z0-9\-_]{10,})["\']?'
            match = re.search(boundary_pattern, html_content, re.IGNORECASE)
            if match:
                boundary = match.group(1)
                # Ensure it has the proper prefix
                if not boundary.startswith('----'):
                    boundary = f"----{boundary}"
                return boundary
            
            # Pattern 2: Look for gecko form boundary specifically (common pattern)
            gecko_pattern = r'----geckoformboundary([a-f0-9]{32})'
            match = re.search(gecko_pattern, html_content)
            if match:
                return f"----geckoformboundary{match.group(1)}"
        
        # Generate a random boundary if none found
        # Use a format similar to what browsers typically generate
        random_suffix = uuid.uuid4().hex  # 32 character hex string
        return f"----geckoformboundary{random_suffix}"
        
    def get_boundary_for_context(self, context="login", html_content=None):
        """
        Get an appropriate boundary for the given context
        Different forms might need different boundaries
        """
        # Try to extract from HTML first
        if html_content:
            extracted_boundary = self.extract_or_generate_boundary(html_content)
            if extracted_boundary and not extracted_boundary.endswith(uuid.uuid4().hex):
                if DEBUG:
                    print(f"   ✅ Extracted boundary for {context}: {extracted_boundary[:50]}...")
                return extracted_boundary
        
        # Generate context-specific boundary
        if context == "login":
            # Use the original boundary for login to maintain compatibility
            boundary = "----geckoformboundarydf70c242556fd126d4918254d6dcd1eb"
            if DEBUG:
                print(f"   ✅ Using login boundary: {boundary[:50]}...")
        elif context == "password":
            # Use the original password boundary for compatibility
            boundary = "----geckoformboundarya093a9eb85f465aa8e949961f6cca502"
            if DEBUG:
                print(f"   ✅ Using password boundary: {boundary[:50]}...")
        else:
            # Generate a new random boundary
            boundary = self.extract_or_generate_boundary()
            if DEBUG:
                print(f"   ✅ Generated random boundary for {context}: {boundary[:50]}...")
        
        return boundary

    def build_form_data(self, action_id, action_key, boundary, email=None, password=None, redirect_to=None):
        """
        Build the multipart form data with extracted values
        """
        
        parts = []
        
        # Action reference
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n')
        
        # Action with ID
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"{action_id}","bound":"$@1"}}')
        
        # Errors array
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]')
        
        # Action key
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\n{action_key}')
        
        # Email field
        if email:
            parts.append(f'Content-Disposition: form-data; name="1_email"\r\n\r\n{email}')
        
        # Password field  
        if password:
            parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n{password}')
        else:
            parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n')
        
        # Redirect URL
        if redirect_to:
            parts.append(f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n{redirect_to}')
        
        # Final data field
        parts.append(f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]')
        
        # Join all parts with boundary
        form_data = f'--{boundary}\r\n' + f'\r\n--{boundary}\r\n'.join(parts) + f'\r\n--{boundary}--\r\n'
        
        return form_data
##################################################################################
# start the actual calls
##################################################################################
    def on_start(self):
        """
        Called when a user starts - performs essential login flow only
        """
        # Initialize authorization token
        self.auth_token = None
        
        # Execute the essential login flow
        if DEBUG:
            print("🔑 Starting essential login flow...")

        login_html = None
        with self.client.request(
            "GET",
            f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": APP_DOMAIN,
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Login page: {resp.status_code}")
            if resp.status_code == 200:
                login_html = resp.text

        # Extract login action ID and key from HTML
        login_action_id = self.extract_next_action_id(login_html)
        login_action_key = self.extract_action_key(login_html)
        
        # Fallback to hardcoded values if extraction fails
        if not login_action_id:
            login_action_id = "8c6d4f21e8485b281b4224a2beffc1e5a4db53ad"
            if DEBUG:
                print(f"   ⚠️ Using fallback login action ID: {login_action_id}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted login action ID: {login_action_id}")
            
        if not login_action_key:
            login_action_key = "k3939455420"
            if DEBUG:
                print(f"   ⚠️ Using fallback action key: {login_action_key}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted action key: {login_action_key}")

        # Step 4: Submit email (first step of login) with dynamic data
        login_boundary = self.get_boundary_for_context("login", login_html)
        form_data = self.build_form_data(
            action_id=login_action_id,
            action_key=login_action_key,
            boundary=login_boundary,
            email=LOGIN_EMAIL,
            redirect_to=f"/projects/?host={APP_DOMAIN}"
        )
        
        with self.client.request(
            "POST",
            f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/x-component",
                "Content-Type": f"multipart/form-data; boundary={login_boundary}",
                "Host": APP_DOMAIN,
                "Next-Action": login_action_id,
                "Origin": BASE_URL_APP,
                "Referer": f"{BASE_URL_APP}/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            },
            data=form_data,
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Email submission: {resp.status_code}")

        # Step 5: Redirect to Arches domain for password and extract action ID
        password_html = None
        with self.client.request(
            "GET",
            f"{PROJECT_URL}/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": PROJECT_DOMAIN,
                "Referer": f"{BASE_URL_APP}/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True, 
        ) as resp:
            if DEBUG:
                print(f"   ✅ Arches auth page: {resp.status_code}")
            if resp.status_code == 200:
                password_html = resp.text

        # Extract password action ID and key from HTML
        password_action_id = self.extract_next_action_id(password_html)
        password_action_key = self.extract_action_key(password_html)
        
        # Fallback to hardcoded values if extraction fails
        if not password_action_id:
            password_action_id = "8eb8615ae699a6509d67a8c34e8000498fd7ad94"
            if DEBUG:
                print(f"   ⚠️ Using fallback password action ID: {password_action_id}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted password action ID: {password_action_id}")
            
        if not password_action_key:
            password_action_key = "k1194475227"
            if DEBUG:
                print(f"   ⚠️ Using fallback password action key: {password_action_key}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted password action key: {password_action_key}")

        # Step 6: Submit password with dynamic data
        password_boundary = self.get_boundary_for_context("password", password_html)
        password_form_data = self.build_form_data(
            action_id=password_action_id,
            action_key=password_action_key,
            boundary=password_boundary,
            email=LOGIN_EMAIL,
            password=LOGIN_PASSWORD,
            redirect_to=f"/projects/?host={APP_DOMAIN}"
        )
        
        with self.client.request(
            "POST",
            f"{PROJECT_URL}/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/x-component",
                "Content-Type": f"multipart/form-data; boundary={password_boundary}",
                "Host": PROJECT_DOMAIN,
                "Next-Action": password_action_id,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            },
            data=password_form_data,
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Password submission: {resp.status_code}")

        # Step 7: Navigate to projects after successful login
        with self.client.request(
            "GET",
            f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": PROJECT_DOMAIN,
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Projects page: {resp.status_code}")

        # Step 8: Get session info to capture auth token
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Host": APP_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            # Capture the authorization token from the session response
            if resp.status_code == 200:
                try:
                    session_data = resp.json()
                    if 'access_token' in session_data:
                        self.auth_token = f"Bearer {session_data['access_token']}"
                        if DEBUG:
                            print(f"   ✅ Captured fresh authorization token")
                    elif 'accessToken' in session_data:
                        self.auth_token = f"Bearer {session_data['accessToken']}"
                        if DEBUG:
                            print(f"   ✅ Captured fresh authorization token")
                    elif 'token' in session_data:
                        self.auth_token = f"Bearer {session_data['token']}"
                        if DEBUG:
                            print(f"   ✅ Captured fresh authorization token")
                    else:
                        if DEBUG:
                            print("   ⚠️ No token found in session response - will use fallback")
                except Exception as e:
                    if DEBUG:
                        print(f"   ⚠️ Could not parse session response: {e}")
            else:
                if DEBUG:
                    print(f"   ⚠️ Session request failed with status: {resp.status_code}")

        # Step 9: Verify login with a simple API call
        if DEBUG:
            print("\n🔍 Verifying login with API call...")
        
        with self.rest(
            "POST",
            f"{BASE_URL_API}/graphql?CountNotifications",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": API_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "CountNotifications",
                "variables": {},
                "query": "query CountNotifications {\n  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])\n  mentions: unreadNotificationsCount(types: [COMMUNICATION])\n}\n",
            },
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print(f"   ✅ Login verification successful: {resp.status_code}")
            else:
                if DEBUG:
                    print(f"   ❌ Login verification failed: {resp.status_code}")
                resp.failure(f"Login verification failed: {resp.status_code}")
        
        if DEBUG:
            print("✅ Essential login flow completed successfully")

    @task
    def verify_authenticated_access(self):
        """
        Continuously verify that we can make authenticated API calls
        This simulates ongoing user activity after login
        """
        # Make a simple authenticated API call to verify session is still valid
        with self.rest(
            "POST",
            f"{BASE_URL_API}/graphql?CountNotifications",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": API_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "CountNotifications",
                "variables": {},
                "query": "query CountNotifications {\n  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])\n  mentions: unreadNotificationsCount(types: [COMMUNICATION])\n}\n",
            },
            name="Verify Authentication"
        ) as resp:
            if resp.status_code != 200:
                resp.failure(f"Authentication verification failed: {resp.status_code}")

    @task(weight=4)
    def browse_project_list(self):
        """
        Simulate user browsing the project list with pagination and filters
        This is a common activity so it gets higher weight
        """
        with self.rest(
            "POST",
            f"{BASE_URL_API}/graphql?GetProjectList",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": API_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetProjectList",
                "variables": {
                    "input": {
                        "listInputs": {
                            "perPage": 10,
                            "page": 1,
                            "keyword": "",
                            "sortBy": "NAME",
                            "sortDirection": "ASC",
                        },
                        "projectFilters": {
                            "context": "PROVIDER",
                            "statuses": ["ON_TIME", "ON_HOLD", "LATE"],
                        },
                    }
                },
                "query": """query GetProjectList($input: projectListInput!) {
  projects(input: $input) {
    maxCashValue
    projects {
      ...ProjectRowProjectList
      __typename
    }
    pageInfo {
      ...PageInfoProjectList
      __typename
    }
    appliedFilters {
      ...AppliedFiltersProjectList
      __typename
    }
    __typename
  }
}

fragment PageInfoProjectList on PageInfoType {
  currentPage
  isOutOfBounds
  limit
  totalPages
  totalResults
  __typename
}

fragment AppliedFiltersProjectList on AppliedProjectFilters {
  context
  statuses
  tags
  strict
  brandNames
  customerIds
  cashValueRange
  projectId
  projectLateDays
  projectManagerIds
  templateIds
  projectFiltersOperator {
    tagOperator
    templateOperator
    milestoneOperator
    __typename
  }
  activeMilestoneNames
  endOn
  startOn
  filterDateBy
  lastUpdatedDays
  __typename
}

fragment ProjectRowProjectList on ProjectType {
  id
  name
  cashValue
  totalTasksCount
  openTasksCount
  openActionItemsCount
  overdueTasksCount
  completedAt
  startOn
  endOn
  projectStatusChangeReasons {
    ...ProjectStatusChangeReasonsProjectList
    __typename
  }
  completedAt
  forecastedEndOn
  deletedAt
  archivedAt
  currentUserSettings {
    projectView
    restrictAccess
    __typename
  }
  currentUserProjectContext
  currentUserRestrictedAccess
  lastActivityAt
  projectManager {
    ...ProjectManagerProjectList
    __typename
  }
  status
  customerV2 {
    ...ProjectCustomerProjectList
    __typename
  }
  projectType
  templates {
    id
    milestones {
      id
      name
      active
      __typename
    }
    __typename
  }
  organization {
    id
    name
    logo {
      originalUrl
      __typename
    }
    __typename
  }
  displayOrganization {
    name
    logo {
      originalUrl
      __typename
    }
    __typename
  }
  brand {
    ...ProjectBrandProjectList
    __typename
  }
  tags {
    ...ProjectListTable_ProjectTag
    __typename
  }
  errors: errorsCount
  __typename
}

fragment ProjectListTable_ProjectTag on TagType {
  id
  name
  color
  internalOnly
  __typename
}

fragment ProjectCustomerProjectList on CustomerType {
  id
  name
  logo {
    originalUrl
    __typename
  }
  __typename
}

fragment ProjectBrandProjectList on BrandType {
  id
  name
  logo {
    originalUrl
    __typename
  }
  __typename
}

fragment ProjectManagerProjectList on UserType {
  id
  firstName
  lastName
  status
  avatar {
    originalUrl
    __typename
  }
  __typename
}

fragment ProjectStatusChangeReasonsProjectList on ProjectStatusChangeReasonType {
  id
  name
  description
  createdAt
  updatedAt
  user {
    id
    firstName
    lastName
    avatar {
      originalUrl
      __typename
    }
    __typename
  }
  statusChangeReason {
    id
    name
    statusChangeReasonGroup {
      id
      name
      __typename
    }
    __typename
  }
  __typename
}""",
            },
            name="Browse Project List"
        ) as resp:
            if resp.status_code != 200:
                if DEBUG:
                    print(f"❌ Browse project list failed: {resp.status_code}")
                    response_text = resp.text or "No response text"
                    print(f"   Response text: {response_text[:500]}...")  # First 500 chars
                resp.failure(f"Browse project list failed: {resp.status_code}")
            else:
                # Optional: Print success data too
                try:
                    data = resp.json()
                    # Extract project count safely
                    if 'data' in data and 'projects' in data['data'] and 'projects' in data['data']['projects']:
                        project_count = len(data['data']['projects']['projects'])
                        if DEBUG:
                            print(f"✅ Browse project list success: Found {project_count} projects")
                    else:
                        if DEBUG:
                            print(f"✅ Browse project list success: {resp.status_code} (unexpected response structure)")
                except Exception as e:
                    if DEBUG:
                        print(f"✅ Browse project list success: {resp.status_code} (couldn't parse JSON: {e})")


if __name__ == "__main__":
    # =============================================================================
    # COMMAND LINE EXECUTION
    # =============================================================================
    
    if DEBUG:
        print(f"""
🚀 GuideX Login Load Test Ready!

📊 Configuration:
   • Login Email: {LOGIN_EMAIL}
   • Wait Between Tasks: {WAIT_TIME_BETWEEN_TASKS}s per user

🎯 COPY & RUN THESE LOCUST COMMANDS:

   # Light Load Test (10 users, 60 seconds)
   locust -f login.py --headless --users=10 --spawn-rate=2 --run-time=60s
   
   # Medium Load Test (25 users, 2 minutes)  
   locust -f login.py --headless --users=25 --spawn-rate=3 --run-time=120s
   
   # Heavy Load Test (50 users, 5 minutes)
   locust -f login.py --headless --users=50 --spawn-rate=5 --run-time=300s
   
   # Interactive Web UI (open http://localhost:8089)
   locust -f login.py

📝 Single User Debug Mode Running Below...
    """)
    
    # Run single user for testing/debugging
    run_single_user(LoginFlow)
