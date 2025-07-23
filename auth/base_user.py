#!/usr/bin/env python3
"""
Modern Shared Authentication Base Class
Combines centralized auth with CSV data support and environment awareness
"""

import os
import csv
import random
import re
import uuid
from locust import HttpUser, between
from dotenv import load_dotenv
from locust.contrib.fasthttp import FastHttpUser

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# CONFIGURATION - Environment-aware and CSV-driven
# =============================================================================

# Environment Configuration
DOMAIN_SUFFIX = os.getenv("DOMAIN_SUFFIX", "staging.guidecx.io")
DEBUG = os.getenv("DEBUG", "false").lower() in ["true", "1", "yes"]

# CSV Data Loading
CSV_FILE_PATH = os.getenv("TEST_DATA_CSV", "config/test_data_staging.csv")

def load_test_data():
    """Load test data from CSV file"""
    try:
        # Adjust path relative to where Locust is run from
        if not os.path.isabs(CSV_FILE_PATH):
            # Calculate project root from auth module location
            project_root = os.path.dirname(os.path.dirname(__file__))
            csv_path = os.path.join(project_root, CSV_FILE_PATH)
        else:
            csv_path = CSV_FILE_PATH
            
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            if not data:
                raise ValueError("CSV file is empty")
            return data
    except FileNotFoundError:
        print(f"CSV file not found: {CSV_FILE_PATH}")
        print("Create CSV files:")
        print("  config/test_data_staging.csv")
        print("  config/test_data_production.csv")
        raise
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        raise

# Load test data at module import
TEST_DATA = load_test_data()

class AuthenticatedUser(FastHttpUser):
    """
    Modern shared authentication base class.
    Features:
    - CSV-driven test data
    - Environment-aware (staging/production)
    - Centralized authentication logic
    - Router state management for Next.js
    - Configurable primary subdomain per workflow
    """
    
    abstract = True  # Prevent Locust from instantiating this base class
    wait_time = between(3, 8)
    
    # Subclasses can override this to specify their primary subdomain
    primary_subdomain = "app"  # Default to app subdomain
    
    def __init__(self, *args, **kwargs):
        # Assign CSV data to this user instance BEFORE calling super()
        self.test_data = random.choice(TEST_DATA)
        
        # Set host from CSV data BEFORE calling super()
        if 'domain' in self.test_data and self.test_data['domain']:
            # Use the workflow's primary subdomain for the base host
            self.host = f"https://{self.primary_subdomain}." + self.test_data['domain']
            # Store the domain for use by workflows
            self.api_domain = self.test_data['domain']
        else:
            raise ValueError(
                "No 'domain' found in CSV test data. "
                f"Available keys: {list(self.test_data.keys())}. "
                "Please add a 'domain' column to your CSV file (e.g., staging.guidecx.io)"
            )
        
        super().__init__(*args, **kwargs)
        
        # Override authentication config with CSV data
        self.login_email = self.test_data.get('login_email', 'default@test.com')
        self.login_password = self.test_data.get('login_password', 'default_pass')
        
        # Authentication state
        self.is_authenticated = False
        self.auth_token = None
        self.current_router_state = None
        self.api_token = None  # Store API token from /auth/session calls
        
        if DEBUG:
            print(f"User: {self.login_email} @ {self.host}")
            print(f"API Domain: {self.api_domain}")
            print(f"Primary Subdomain: {self.primary_subdomain}")
    
    def on_start(self):
        """Authenticate user on startup"""
        self.authenticate()
    
    def debug_cookies(self, context=""):
        """Debug helper to show all cookies"""
        if DEBUG and hasattr(self.client, 'cookiejar'):
            all_cookies = []
            session_cookies = []
            for cookie in self.client.cookiejar:
                all_cookies.append(f"{cookie.name}={cookie.value[:30]}...")
                if 'session' in cookie.name.lower() or 'staging-session' in cookie.name.lower():
                    session_cookies.append(f"{cookie.name}={cookie.value[:50]}...")
            
            print(f"🍪 {context} - Total cookies: {len(all_cookies)}")
            if session_cookies:
                print(f"🍪 {context} - Session cookies: {session_cookies}")
            else:
                print(f"⚠️ {context} - No session cookies found!")
            
            if DEBUG and len(all_cookies) > 0:
                print(f"🍪 {context} - All cookies: {all_cookies}")
        
    def authenticate(self):
        """Handle user authentication with modern Next.js flow - uses workflow's primary subdomain"""
        if DEBUG:
            print("Authenticating...")
            
        try:
            # Step 1: Get login page and extract Next-Action ID (use workflow's primary subdomain)
            auth_url = f"https://{self.primary_subdomain}.{self.api_domain}"
            login_response = self.client.get(f"{auth_url}/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.{self.api_domain}")
            
            if DEBUG:
                self.debug_cookies("After login page")
            
            if login_response.status_code != 200:
                if DEBUG:
                    print(f"Login page failed: {login_response.status_code}")
                return False
                
            # Step 2: Extract Next-Action ID
            html_content = login_response.text
            next_action_id = self.extract_next_action_id(html_content)
            
            if not next_action_id:
                if DEBUG:
                    print("Could not find Next-Action ID")
                return False
                
            # Step 3: Perform login with proper Next.js form format
            # Generate boundary for multipart form data
            import uuid
            boundary = f"----geckoformboundary{uuid.uuid4().hex}"
            
            # Build the multipart form data that GuideX expects
            form_parts = []
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n')
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"{next_action_id}","bound":"$@1"}}')
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]')
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\nk0')  # Default action key
            form_parts.append(f'Content-Disposition: form-data; name="1_email"\r\n\r\n{self.login_email}')
            form_parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n{self.login_password}') 
            form_parts.append(f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.{self.api_domain}')
            form_parts.append(f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]')
            
            # Join all parts with boundary
            form_data = f'--{boundary}\r\n' + f'\r\n--{boundary}\r\n'.join(form_parts) + f'\r\n--{boundary}--\r\n'
            
            login_submit = self.client.post(
                f"{auth_url}/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.{self.api_domain}",
                data=form_data,
                headers={
                    'Content-Type': f'multipart/form-data; boundary={boundary}',
                    'Next-Action': next_action_id
                },
                allow_redirects=False
            )
            
            if DEBUG:
                print(f"🔍 LOGIN POST RESPONSE:")
                print(f"  Status: {login_submit.status_code}")
                print(f"  Headers: {dict(login_submit.headers)}")
                print(f"  Body length: {len(login_submit.text)}")
                print(f"  Body preview: {login_submit.text[:200]}...")
                self.debug_cookies("After login POST")
            
            # Step 4: Check for successful login (redirect response)
            if login_submit.status_code in [303, 302]:
                if DEBUG:
                    print(f"🔄 Login redirect received: {login_submit.status_code}")
                    print(f"🔄 Redirect location: {login_submit.headers.get('Location', 'N/A')}")
                
                # Follow the redirect to establish session cookies
                redirect_url = login_submit.headers.get('Location') or login_submit.headers.get('X-Action-Redirect')
                if redirect_url:
                    if DEBUG:
                        redirect_source = "Location" if login_submit.headers.get('Location') else "X-Action-Redirect"
                        print(f"🔄 Following {redirect_source} redirect to establish session cookies...")
                        print(f"🔄 Redirect URL: {redirect_url}")
                    
                    # Follow the redirect to complete authentication and establish session
                    if redirect_url.startswith('/'):
                        redirect_url = f"{auth_url}{redirect_url}"
                    
                    final_response = self.client.get(redirect_url, allow_redirects=True)
                    
                    if DEBUG:
                        print(f"🔄 Final redirect response: {final_response.status_code}")
                        self.debug_cookies("After redirect completion")
                else:
                    if DEBUG:
                        print("⚠️ No Location or X-Action-Redirect header found in redirect response!")
                
                self.is_authenticated = True
                
                # Try to extract API token from login response headers/cookies
                try:
                    # For Locust, we need to access the response properly  
                    response_text = getattr(login_submit, 'text', '')
                    response_headers = getattr(login_submit, 'headers', {})
                    response_cookies = getattr(login_submit, 'cookies', {})
                    
                    token = self.extract_api_token(
                        response_text, 
                        response_headers, 
                        response_cookies
                    )
                    if token:
                        self.api_token = token
                        if DEBUG:
                            print(f"🔑 Stored API token from login response")
                except Exception as e:
                    if DEBUG:
                        print(f"⚠️ Error extracting API token from login: {e}")
                
                if DEBUG:
                    print("Authentication successful")
                return True
            elif login_submit.status_code == 200:
                # Check if this is a form error or contains redirect information
                if DEBUG:
                    print(f"🔍 Got 200 response - checking for redirect info in body...")
                    # Look for redirect information in the response body
                    if 'redirect' in login_submit.text.lower() or 'location' in login_submit.text.lower():
                        print(f"🔍 Found redirect-related content in response")
                    else:
                        print(f"⚠️ No redirect info found - might be an error page")
                        print(f"Response preview: {login_submit.text[:500]}...")
                        
                # For now, assume authentication failed if we get a 200
                return False
            else:
                if DEBUG:
                    print(f"Authentication failed: {login_submit.status_code}")
                    print(f"Response body preview: {login_submit.text[:500]}...")
                return False
                
        except Exception as e:
            if DEBUG:
                print(f"Authentication error: {e}")
            return False
    
    def get_auth_header(self):
        """Get authorization header for API calls"""
        return self.auth_token
    
    def get_csv_value(self, key, default=""):
        """Get a value from this user's CSV data"""
        return self.test_data.get(key, default)
    
    def extract_next_action_id(self, html_content):
        """Extract Next-Action ID from HTML content"""
        if not html_content:
            return None
        
        if DEBUG:
            print(f"Searching for Next-Action ID in HTML (length: {len(html_content)})")
            
        # Pattern 1: Look for data-action attribute in forms (most common)
        data_action_pattern = r'data-action="([a-f0-9]{40})"'
        match = re.search(data_action_pattern, html_content)
        if match:
            if DEBUG:
                print(f"Found Next-Action ID via data-action: {match.group(1)}")
            return match.group(1)
        
        # Pattern 2: Look for action ID in JSON format (HTML entity encoded)
        json_entity_pattern = r'&quot;id&quot;:&quot;([a-f0-9]{40})&quot;'
        match = re.search(json_entity_pattern, html_content)
        if match:
            if DEBUG:
                print(f"Found Next-Action ID via HTML entities: {match.group(1)}")
            return match.group(1)
        
        # Pattern 3: Look for action ID in regular JSON format  
        json_pattern = r'"id":"([a-f0-9]{40})"'
        match = re.search(json_pattern, html_content)
        if match:
            if DEBUG:
                print(f"Found Next-Action ID via JSON: {match.group(1)}")
            return match.group(1)
        
        # Pattern 4: Look for value attribute with action ID
        value_pattern = r'value="([a-f0-9]{40})"'
        match = re.search(value_pattern, html_content)
        if match:
            if DEBUG:
                print(f"Found Next-Action ID via value attribute: {match.group(1)}")
            return match.group(1)
        
        if DEBUG:
            print("No Next-Action ID found")
        
        return None
    
    def extract_api_token(self, response_text, response_headers=None, response_cookies=None):
        """Extract API token from /auth/session response, headers, or cookies"""
        try:
            import json
            
            # Log EVERYTHING for debugging
            if DEBUG:
                print("🔍" + "="*60)
                print("🔍 COMPLETE AUTH/SESSION RESPONSE ANALYSIS")
                print("🔍" + "="*60)
                print(f"📄 Response body (full): {response_text}")
                print(f"📄 Response body length: {len(response_text)} characters")
                print(f"📄 Response body type: {type(response_text)}")
                
                if response_headers:
                    print("📋 ALL RESPONSE HEADERS:")
                    for key, value in response_headers.items():
                        print(f"    {key}: {value}")
                else:
                    print("📋 No response headers available")
                
                if response_cookies:
                    print("🍪 ALL RESPONSE COOKIES:")
                    for key, value in response_cookies.items():
                        print(f"    {key}: {value}")
                else:
                    print("🍪 No response cookies available")
                
                print("🔍" + "="*60)
            
            # Try to parse as JSON first
            try:
                session_data = json.loads(response_text)
                if DEBUG:
                    print(f"✅ JSON parsing successful. Type: {type(session_data)}")
                    if isinstance(session_data, dict):
                        print(f"📝 JSON object keys: {list(session_data.keys())}")
                        print(f"📝 Full JSON content: {json.dumps(session_data, indent=2)}")
                    elif isinstance(session_data, list):
                        print(f"📝 JSON array length: {len(session_data)}")
                        print(f"📝 JSON array content: {session_data}")
                    else:
                        print(f"📝 JSON content: {session_data}")
            except json.JSONDecodeError as e:
                session_data = None
                if DEBUG:
                    print(f"❌ JSON parsing failed: {e}")
                    print(f"📝 Raw response (first 500 chars): {response_text[:500]}")
                    
            # If it's a valid JSON object (not array), look for tokens
            if session_data and isinstance(session_data, dict):
                # Common patterns for API tokens in session responses
                token_fields = [
                    'token', 'apiToken', 'api_token', 'accessToken', 'access_token',
                    'authToken', 'auth_token', 'bearerToken', 'bearer_token',
                    'sessionToken', 'session_token', 'jwt', 'jwtToken', 'jwt_token'
                ]
                
                if DEBUG:
                    print("🔍 Searching for tokens in JSON response...")
                
                # Look for token in root level
                for field in token_fields:
                    if field in session_data and session_data[field]:
                        if DEBUG:
                            print(f"✅ Found API token in field '{field}': {session_data[field][:20]}...")
                        return session_data[field]
                
                # Look for token in nested user/session objects
                for nested_key in ['user', 'session', 'data', 'auth', 'authentication', 'credentials']:
                    if nested_key in session_data and isinstance(session_data[nested_key], dict):
                        nested_obj = session_data[nested_key]
                        if DEBUG:
                            print(f"🔍 Checking nested object '{nested_key}': {list(nested_obj.keys())}")
                        for field in token_fields:
                            if field in nested_obj and nested_obj[field]:
                                if DEBUG:
                                    print(f"✅ Found API token in nested field '{nested_key}.{field}': {nested_obj[field][:20]}...")
                                return nested_obj[field]
            
            # If JSON parsing failed or didn't contain tokens, check cookies
            if response_cookies:
                token_cookie_names = [
                    'token', 'auth_token', 'access_token', 'session_token',
                    'apiToken', 'authToken', 'accessToken', 'sessionToken',
                    'jwt', 'jwtToken', 'auth', 'authorization'
                ]
                
                if DEBUG:
                    print("🔍 Searching for tokens in cookies...")
                
                for cookie_name in token_cookie_names:
                    if cookie_name in response_cookies and response_cookies[cookie_name]:
                        if DEBUG:
                            print(f"✅ Found API token in cookie '{cookie_name}': {response_cookies[cookie_name][:20]}...")
                        return response_cookies[cookie_name]
            
            # Check response headers for tokens
            if response_headers:
                token_header_names = [
                    'authorization', 'x-auth-token', 'x-access-token', 
                    'x-api-token', 'x-session-token', 'x-jwt-token',
                    'auth-token', 'access-token', 'api-token', 'session-token'
                ]
                
                if DEBUG:
                    print("🔍 Searching for tokens in headers...")
                
                for header_name in token_header_names:
                    header_value = None
                    # Check both original case and lowercase
                    for key, value in response_headers.items():
                        if key.lower() == header_name.lower():
                            header_value = value
                            break
                    
                    if header_value:
                        # Remove "Bearer " prefix if present
                        token = header_value.replace('Bearer ', '').replace('bearer ', '')
                        if DEBUG:
                            print(f"✅ Found API token in header '{header_name}': {token[:20]}...")
                        return token
                
            if DEBUG:
                print("⚠️ No API token found in session response, cookies, or headers")
                print("🔍" + "="*60)
                    
        except Exception as e:
            if DEBUG:
                print(f"⚠️ Error extracting API token: {e}")
                import traceback
                traceback.print_exc()
        
        return None
    
    def get_api_url(self, subdomain: str, path: str = "") -> str:
        """
        Generate API URL for a specific subdomain using CSV domain data.
        
        Args:
            subdomain: The subdomain to use (e.g., 'thundercats', 'k2-web', 'app')
            path: The path to append (e.g., '/v2/projects')
            
        Returns:
            Full URL like 'https://thundercats.staging.guidecx.io/v2/projects'
        """
        return f"https://{subdomain}.{self.api_domain}{path}"
    
    def make_api_request(self, method: str, subdomain: str, path: str, **kwargs):
        """
        Make an API request to a specific subdomain.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            subdomain: The subdomain to use (e.g., 'thundercats', 'k2-web', 'app') 
            path: The API path (e.g., '/v2/projects')
            **kwargs: Additional arguments for the request (headers, data, etc.)
            
        Returns:
            Response object from the request
        """
        url = self.get_api_url(subdomain, path)
        
        # Add Host header if not already present
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        if 'Host' not in kwargs['headers']:
            kwargs['headers']['Host'] = f"{subdomain}.{self.api_domain}"
        
        # For API calls, ensure we get JSON responses not page components
        if subdomain == 'app' and '/auth/session' in path:
            # Force JSON response for auth/session API calls
            kwargs['headers']['Accept'] = 'application/json'
            kwargs['headers']['Content-Type'] = 'application/json'
            if DEBUG:
                print(f"🔧 Forcing JSON response for /auth/session API call")
                # Debug: Show what cookies we're sending
                if hasattr(self.client, 'cookiejar'):
                    cookies_sent = []
                    for cookie in self.client.cookiejar:
                        if 'session' in cookie.name.lower() or 'staging-session' in cookie.name.lower():
                            cookies_sent.append(f"{cookie.name}={cookie.value[:50]}...")
                    if cookies_sent:
                        print(f"🍪 Session cookies being sent: {cookies_sent}")
                    else:
                        print(f"⚠️ NO SESSION COOKIES FOUND!")
                        
                # Show all cookies for debugging
                self.debug_cookies("Before /auth/session call")
        
        # Add API authentication for api subdomain
        if subdomain == 'api':
            # Use stored API token if available
            if self.api_token:
                kwargs['headers']['Authorization'] = f'Bearer {self.api_token}'
                if DEBUG:
                    print(f"🔑 Using stored API token for {subdomain} subdomain")
            else:
                # Try to get API token from CSV data as fallback
                api_token = self.get_csv_value('api_token', '')
                if api_token:
                    kwargs['headers']['Authorization'] = f'Bearer {api_token}'
                    if DEBUG:
                        print(f"🔑 Using CSV API token for {subdomain} subdomain")
                else:
                    # Final fallback: Use session cookies for API authentication
                    # Many systems use session-based auth for API calls
                    if self.is_authenticated:
                        if DEBUG:
                            print(f"🔑 Using session cookies for {subdomain} subdomain authentication")
                        # Session cookies will be automatically included by the client
                    else:
                        if DEBUG:
                            print(f"⚠️ No API token or session available for {subdomain} subdomain - request may fail")
        
        # Make the request
        response = getattr(self.client, method.lower())(url, **kwargs)
        
        # Check if this is an /auth/session call and extract API token
        if subdomain == 'app' and '/auth/session' in path and response.status_code == 200:
            try:
                # For Locust, we need to access the response properly
                response_text = response.text
                response_headers = getattr(response, 'headers', {})
                response_cookies = getattr(response, 'cookies', {})
                
                token = self.extract_api_token(
                    response_text, 
                    response_headers, 
                    response_cookies
                )
                if token:
                    self.api_token = token
                    if DEBUG:
                        print(f"🔑 Stored API token from session response")
            except Exception as e:
                if DEBUG:
                    print(f"⚠️ Error extracting API token: {e}")
        
        return response


# =============================================================================
# DIRECT TESTING - Run this file directly to test authentication
# =============================================================================

if __name__ == "__main__":
    print("Testing authentication...")
    print(f"CSV file: {CSV_FILE_PATH}")
    print(f"Rows loaded: {len(TEST_DATA)}")
    print(f"Domain: {DOMAIN_SUFFIX}")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        env = Environment(user_classes=[AuthenticatedUser])
        user = AuthenticatedUser(env)
        
        auth_result = user.authenticate()
        
        if auth_result:
            print("Authentication: PASSED")
            resp = user.client.get("/projects")
            if resp.status_code == 200:
                print("Request test: PASSED")
            else:
                print(f"Request test: FAILED ({resp.status_code})")
        else:
            print("Authentication: FAILED")
            
    except ImportError:
        print("Install locust to run full test")
    except Exception as e:
        print(f"Test failed: {e}") 