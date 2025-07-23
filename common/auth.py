#!/usr/bin/env python3
"""
Simple Authentication Script for Locust Load Testing
Uses environment variables for credentials and host configuration
"""

import os
import re
import uuid
from locust import HttpUser
from locust import between
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AuthenticatedUser(HttpUser):
    """
    Base Locust user class that handles authentication for GuideX.
    
    This class should be inherited by other test classes that need authenticated access.
    It handles the complete login flow and maintains the session for API calls.
    
    Note: This class is marked as abstract to prevent Locust from trying to run it directly.
    """
    
    abstract = True  # Prevents Locust from instantiating this class directly
    host = os.getenv('LOCUST_HOST')
    """
    Simple authenticated user class for Locust load testing.
    
    Uses environment variables:
    - LOGIN_EMAIL: Email address for authentication
    - LOGIN_PASSWORD: Password for authentication  
    - LOCUST_HOST: Base host URL for the application
    """
    
    wait_time = between(1, 3)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Load credentials from environment variables
        self.login_email = os.getenv('LOGIN_EMAIL')
        self.login_password = os.getenv('LOGIN_PASSWORD')
        self.locust_host = os.getenv('LOCUST_HOST')
        
        if not self.login_email:
            raise ValueError("LOGIN_EMAIL environment variable is required")
        if not self.login_password:
            raise ValueError("LOGIN_PASSWORD environment variable is required")
        if not self.locust_host:
            raise ValueError("LOCUST_HOST environment variable is required")
            
        # Set the host for all requests
        self.host = self.locust_host
        
        # Authentication state
        self.is_authenticated = False
        self.session_data = None
        
        print(f"Initializing user: {self.login_email} @ {self.host}")
    
    def on_start(self):
        """Authenticate user when starting"""
        self.authenticate()
    
    def authenticate(self):
        """Authenticate the user using proven Next.js server action approach"""
        if self.is_authenticated:
            return True
            
        print(f"Authenticating user: {self.login_email}")
        
        try:
            # Step 1: Get login page with proper redirect parameters
            # Extract domain info for URL construction
            if '+' in self.login_email and '@' in self.login_email:
                subdomain = self.login_email.split('+')[1].split('@')[0]
                api_domain = f"{subdomain}.staging.guidecx.io"
            else:
                api_domain = "staging.guidecx.io"
            
            login_url = f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.{api_domain}"
            print(f"🌐 Login URL: {login_url}")
            
            login_response = self.client.get(
                login_url,
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                },
                name="/auth/login"
            )
            
            if login_response.status_code != 200:
                print(f"❌ Failed to load login page: {login_response.status_code}")
                return False
            
            print(f"✅ Login page loaded successfully")
            self.debug_cookies("After login page")
            
            # Step 2: Extract Next-Action ID using proven patterns
            next_action_id = self._extract_next_action_id(login_response.text)
            if not next_action_id:
                print("❌ Could not find Next-Action ID")
                return False
                
            print(f"✅ Found Next-Action ID: {next_action_id}")
            
            # Step 3: Create proper multipart form data for Next.js server action
            boundary = f"----geckoformboundary{uuid.uuid4().hex}"
            
            form_parts = []
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n')
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"{next_action_id}","bound":"$@1"}}')
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]')
            form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\nk0')
            form_parts.append(f'Content-Disposition: form-data; name="1_email"\r\n\r\n{self.login_email}')
            form_parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n{self.login_password}') 
            form_parts.append(f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.{api_domain}')
            form_parts.append(f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]')
            
            form_data = f'--{boundary}\r\n' + f'\r\n--{boundary}\r\n'.join(form_parts) + f'\r\n--{boundary}--\r\n'
            
            # Step 4: Submit authentication with proper Next.js server action format
            auth_response = self.client.post(
                login_url,
                data=form_data,
                headers={
                    'Content-Type': f'multipart/form-data; boundary={boundary}',
                    'Next-Action': next_action_id,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                },
                allow_redirects=False,  # CRITICAL: Don't auto-follow redirects to capture session cookies
                name="submit_next_js_auth"
            )
            
            print(f"🔍 Auth response status: {auth_response.status_code}")
            print(f"🔍 Auth response URL: {auth_response.url}")
            print(f"🍪 Cookies after auth POST: {dict(self.client.cookies)}")
            self.debug_cookies("After auth POST")
            
            # Check for successful login (redirect response) - from base_user.py.backup
            if auth_response.status_code in [303, 302]:
                print(f"🔄 Login redirect received: {auth_response.status_code}")
                
                # Look for redirect location in headers (check both Location and X-Action-Redirect)
                redirect_url = auth_response.headers.get('Location') or auth_response.headers.get('X-Action-Redirect')
                if redirect_url:
                    redirect_source = "Location" if auth_response.headers.get('Location') else "X-Action-Redirect"
                    print(f"🔄 Found {redirect_source} redirect: {redirect_url}")
                    
                    # Follow the redirect to complete authentication and establish session
                    if redirect_url.startswith('/'):
                        redirect_url = f"{self.host}{redirect_url}"
                    
                    final_response = self.client.get(
                        redirect_url, 
                        allow_redirects=True,
                        headers={
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                        },
                        name="follow_auth_redirect"
                    )
                    
                    print(f"🔄 Final redirect response: {final_response.status_code}")
                    print(f"🔄 Final URL: {final_response.url}")
                    print(f"🍪 Cookies after redirect: {dict(self.client.cookies)}")
                    self.debug_cookies("After redirect completion")
                    
                    # Check if we're on the password form page (/auth/basic)
                    if '/auth/basic' in final_response.url:
                        print(f"🔐 Redirected to password form - completing 2-step authentication")
                        
                        # Extract Next-Action ID from the password form
                        password_action_id = self._extract_next_action_id(final_response.text)
                        if not password_action_id:
                            print("❌ Could not find Next-Action ID on password form")
                            return False
                        
                        print(f"✅ Found password form Next-Action ID: {password_action_id}")
                        
                        # Create password form submission
                        password_boundary = f"----geckoformboundary{uuid.uuid4().hex}"
                        
                        password_form_parts = []
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n')
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"{password_action_id}","bound":"$@1"}}')
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]')
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\nk0')
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_email"\r\n\r\n{self.login_email}')
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n{self.login_password}') 
                        password_form_parts.append(f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.{api_domain}')
                        password_form_parts.append(f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]')
                        
                        password_form_data = f'--{password_boundary}\r\n' + f'\r\n--{password_boundary}\r\n'.join(password_form_parts) + f'\r\n--{password_boundary}--\r\n'
                        
                        # Submit password form
                        password_response = self.client.post(
                            final_response.url,  # Submit to the current /auth/basic URL
                            data=password_form_data,
                            headers={
                                'Content-Type': f'multipart/form-data; boundary={password_boundary}',
                                'Next-Action': password_action_id,
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                            },
                            allow_redirects=False,
                            name="submit_password_form"
                        )
                        
                        print(f"🔐 Password form response: {password_response.status_code}")
                        print(f"🔐 Password form URL: {password_response.url}")
                        print(f"🍪 Cookies after password: {dict(self.client.cookies)}")
                        self.debug_cookies("After password submission")
                        
                        # Follow the final redirect after password submission
                        if password_response.status_code in [303, 302]:
                            final_redirect_url = password_response.headers.get('Location') or password_response.headers.get('X-Action-Redirect')
                            if final_redirect_url:
                                print(f"🔐 Following final redirect: {final_redirect_url}")
                                
                                if final_redirect_url.startswith('/'):
                                    final_redirect_url = f"https://thundercats.staging.guidecx.io{final_redirect_url}"
                                
                                final_auth_response = self.client.get(
                                    final_redirect_url,
                                    allow_redirects=True,
                                    headers={
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                                    },
                                    name="follow_final_auth_redirect"
                                )
                                
                                print(f"🔐 Final auth response: {final_auth_response.status_code}")
                                print(f"🔐 Final auth URL: {final_auth_response.url}")
                                print(f"🍪 Final cookies: {dict(self.client.cookies)}")
                                self.debug_cookies("After final authentication")
                                
                                # Use the final authentication response for success checking
                                auth_response = final_auth_response
                            else:
                                print("❌ No redirect after password submission")
                                return False
                        else:
                            print(f"❌ Password submission failed: {password_response.status_code}")
                            return False
                    
                    # Use the final response for success checking (moved down after password handling)
                    auth_response = final_response
                else:
                    print("⚠️ No Location or X-Action-Redirect header found in redirect response!")
             
            # Step 5: Check if authentication was successful
            if self._check_authentication_success(auth_response):
                self.is_authenticated = True
                print("✅ Authentication successful")
                
                # Step 6: Complete the authentication flow
                self._complete_authentication_flow()
                
                # Step 7: Get session data for future API calls
                self._get_session_data()
                
                return True
            else:
                print(f"❌ Authentication failed - Status: {auth_response.status_code}")
                print(f"Final URL: {auth_response.url}")
                
                # Debug: Check if we actually have session cookies despite failed detection
                all_cookies = dict(self.client.cookies)
                session_cookies = [name for name in all_cookies.keys() if 'session' in name.lower()]
                if session_cookies:
                    print(f"🔍 BUT we have session cookies: {session_cookies}")
                    print("🔄 Treating as authentication success due to session cookies")
                    self.is_authenticated = True
                    self._complete_authentication_flow()
                    self._get_session_data()
                    return True
                
                return False
                
        except Exception as e:
            print(f"❌ Authentication error: {e}")
            return False
    
    def debug_cookies(self, context=""):
        """Debug helper to show all cookies - from base_user.py.backup"""
        all_cookies = []
        session_cookies = []
        
        for name, value in self.client.cookies.items():
            all_cookies.append(f"{name}={value[:30]}...")
            if 'session' in name.lower() or 'staging-session' in name.lower() or 'gcx' in name.lower():
                session_cookies.append(f"{name}={value[:50]}...")
        
        print(f"🍪 {context} - Total cookies: {len(all_cookies)}")
        if session_cookies:
            print(f"🍪 {context} - Session cookies: {session_cookies}")
        else:
            print(f"⚠️ {context} - No session cookies found!")
        
        if len(all_cookies) > 0:
            print(f"🍪 {context} - All cookies: {all_cookies}")
    
    def _extract_next_action_id(self, html_content):
        """Extract Next-Action ID using proven patterns from base_user.py"""
        if not html_content:
            return None
        
        print(f"🔍 Searching for Next-Action ID in HTML (length: {len(html_content)})")
        
        # Pattern 1: Look for data-action attribute in forms (most common)
        data_action_pattern = r'data-action="([a-f0-9]{40})"'
        match = re.search(data_action_pattern, html_content)
        if match:
            print(f"✅ Found Next-Action ID via data-action: {match.group(1)}")
            return match.group(1)
        
        # Pattern 2: Look for action ID in JSON format (HTML entity encoded)
        json_entity_pattern = r'&quot;id&quot;:&quot;([a-f0-9]{40})&quot;'
        match = re.search(json_entity_pattern, html_content)
        if match:
            print(f"✅ Found Next-Action ID via HTML entities: {match.group(1)}")
            return match.group(1)
        
        # Pattern 3: Look for action ID in regular JSON format  
        json_pattern = r'"id":"([a-f0-9]{40})"'
        match = re.search(json_pattern, html_content)
        if match:
            print(f"✅ Found Next-Action ID via JSON: {match.group(1)}")
            return match.group(1)
        
        # Pattern 4: Look for value attribute with action ID
        value_pattern = r'value="([a-f0-9]{40})"'
        match = re.search(value_pattern, html_content)
        if match:
            print(f"✅ Found Next-Action ID via value attribute: {match.group(1)}")
            return match.group(1)
        
        print("❌ No Next-Action ID found")
        return None
    
    def _check_authentication_success(self, response):
        """Check if authentication was successful - based on base_user.py approach"""
        # For Next.js authentication, a 303 redirect is typically success
        if response.status_code == 303:
            print(f"✅ Got 303 redirect - authentication likely successful")
            return True
            
        # Check if we reached the final destination (not an auth page) - base_user.py approach
        if response.status_code == 200 and 'auth' not in response.url:
            print(f"✅ Reached non-auth page - authentication successful")
            return True
            
        # Check for successful redirects to expected pages
        if response.status_code in [200, 302, 303]:
            success_indicators = ['/projects', '/dashboard', '/app']
            for indicator in success_indicators:
                if indicator in response.url:
                    print(f"✅ Reached {indicator} page - authentication successful")
                    return True
        
        print(f"❌ Authentication check failed - Status: {response.status_code}, URL: {response.url}")
        return False
    
    def _complete_authentication_flow(self):
        """Complete the authentication flow by visiting the projects page"""
        try:
            print("🔄 Completing authentication flow...")
            projects_response = self.client.get(
                "/projects",
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                },
                name="complete_auth_flow"
            )
            
            # Debug: Check for session cookies after visiting /projects
            print(f"🍪 Projects response Set-Cookie headers:")
            set_cookie_headers = projects_response.headers.get('Set-Cookie', '')
            if set_cookie_headers:
                for header in set_cookie_headers if isinstance(set_cookie_headers, list) else [set_cookie_headers]:
                    print(f"   {header}")
                    if 'gcx' in header and 'session' in header:
                        print(f"   ✅ Session cookie found in Set-Cookie!")
            else:
                print(f"   No Set-Cookie headers in /projects response")
            
            # Check cookies after /projects
            print(f"🍪 Cookies after /projects: {dict(self.client.cookies)}")
            
            if projects_response.status_code == 200:
                print("✅ Authentication flow completed - cookies established")
            else:
                print(f"⚠️ Projects page returned: {projects_response.status_code}")
                
        except Exception as e:
            print(f"⚠️ Error completing authentication flow: {e}")
    
    def _get_session_data(self):
        """Get session data from the session endpoint"""
        try:
            # Debug: Check what cookies we have (HttpUser uses standard requests)
            print(f"🍪 Current cookies: {dict(self.client.cookies)}")
            
            session_response = self.client.get(
                "/auth/session",
                headers={
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                name="get_session"
            )
            
            print(f"🔍 Session endpoint status: {session_response.status_code}")
            print(f"🔍 Session response content: {session_response.text[:200]}")
            
            if session_response.status_code == 200:
                try:
                    import json
                    session_data = json.loads(session_response.text)
                    print(f"🔍 Session data keys: {list(session_data.keys()) if isinstance(session_data, dict) else 'Not a dict'}")
                    
                    if isinstance(session_data, dict) and session_data:
                        self.session_data = session_data
                        print("✅ Session data retrieved from endpoint")
                        
                        # Check if we have an access token
                        if 'accessToken' in session_data:
                            print(f"✅ Access token found: {session_data['accessToken'][:50]}...")
                        else:
                            print("⚠️ No access token in session data")
                            print(f"🔍 Available keys: {list(session_data.keys())}")
                    else:
                        print("⚠️ Session endpoint returned empty data")
                        print("🔍 This usually means session cookies are not being sent properly")
                        # Check for Iron Session cookie names
                        session_cookies = [name for name in self.client.cookies.keys() if 'session' in name.lower() or 'gcx' in name.lower()]
                        print(f"🍪 Session-related cookies found: {session_cookies}")
                        self.session_data = {}
                        
                except json.JSONDecodeError:
                    print("⚠️ Session response is not JSON")
                    self.session_data = {}
            elif session_response.status_code == 401:
                print("⚠️ Unauthorized - session may have expired")
                self.session_data = {}
            else:
                print(f"⚠️ Failed to get session data: {session_response.status_code}")
                self.session_data = {}
                
        except Exception as e:
            print(f"⚠️ Error getting session data: {e}")
            self.session_data = {}
    
    def get_auth_headers(self):
        """Get headers for authenticated requests"""
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        # Add authorization header if we have session data with token
        if self.session_data and isinstance(self.session_data, dict):
            access_token = self.session_data.get('accessToken')
            if access_token:
                headers['Authorization'] = f'Bearer {access_token}'
        
        return headers
    
    def make_authenticated_request(self, method, path, **kwargs):
        """Make an authenticated request with proper headers"""
        if not self.is_authenticated:
            print("⚠️ User not authenticated, attempting to authenticate...")
            if not self.authenticate():
                raise Exception("Authentication required but failed")
        
        # Add authentication headers
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers'].update(self.get_auth_headers())
        
        # Make the request
        return getattr(self.client, method.lower())(path, **kwargs)

# Example usage and testing
if __name__ == "__main__":
    # Test authentication if running directly
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Create test environment
        env = Environment(user_classes=[AuthenticatedUser])
        user = AuthenticatedUser(env)
        
        # Test authentication
        if user.authenticate():
            print("🎉 Authentication test: PASSED")
            
            # Test an authenticated request
            try:
                response = user.make_authenticated_request('GET', '/projects')
                if response.status_code == 200:
                    print("🎉 Authenticated request test: PASSED")
                else:
                    print(f"⚠️ Authenticated request test: Status {response.status_code}")
            except Exception as e:
                print(f"❌ Authenticated request test: {e}")
        else:
            print("❌ Authentication test: FAILED")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}") 