#!/usr/bin/env python3
"""
Authentication module for Locust Load Testing
Handles GuideX Next.js server action authentication flow
"""

import os
import re
import uuid
from locust import HttpUser, between
from dotenv import load_dotenv
from .helpers import debug_print

# Load environment variables from .env file
load_dotenv()

class AuthenticatedUser(HttpUser):
    """
    Base Locust user class that handles GuideX authentication.
    
    Implements the complete 2-step authentication flow:
    1. Email submission -> redirect to password form
    2. Password submission -> session establishment
    
    Environment variables required:
    - LOGIN_EMAIL: Email address for authentication
    - LOGIN_PASSWORD: Password for authentication  
    - LOCUST_HOST: Base host URL for the application
    """
    
    abstract = True  # Prevents Locust from instantiating this class directly
    wait_time = between(1, 3)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Load credentials from environment variables
        self.login_email = os.getenv('LOGIN_EMAIL')
        self.login_password = os.getenv('LOGIN_PASSWORD')
        self.locust_host = os.getenv('LOCUST_HOST')
        
        if not all([self.login_email, self.login_password, self.locust_host]):
            raise ValueError("LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST environment variables are required")
            
        self.host = self.locust_host
        self.is_authenticated = False
        self.session_data = None
        
        debug_print(f"Initializing user: {self.login_email} @ {self.host}")
    
    def on_start(self):
        """Authenticate user when starting"""
        self.authenticate()
    
    def authenticate(self):
        """Authenticate using GuideX Next.js server action flow"""
        if self.is_authenticated:
            return True
            
        debug_print(f"Authenticating user: {self.login_email}")
        
        try:
            # Extract domain from email for URL construction
            if '+' in self.login_email and '@' in self.login_email:
                subdomain = self.login_email.split('+')[1].split('@')[0]
                api_domain = f"{subdomain}.staging.guidecx.io"
            else:
                api_domain = "staging.guidecx.io"
            
            # Step 1: Load login page
            login_url = f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.{api_domain}"
            login_response = self.client.get(login_url, name="/auth/login")
            
            if login_response.status_code != 200:
                debug_print(f"Failed to load login page: {login_response.status_code}")
                return False
            
            # Step 2: Extract Next-Action ID
            next_action_id = self._extract_next_action_id(login_response.text)
            if not next_action_id:
                debug_print("Could not find Next-Action ID")
                return False
            
            # Step 3: Submit email form
            form_data = self._create_form_data(next_action_id, api_domain)
            auth_response = self.client.post(
                login_url,
                data=form_data['data'],
                headers=form_data['headers'],
                allow_redirects=False,
                name="submit_next_js_auth"
            )
            
            # Step 4: Handle redirects and password form
            if auth_response.status_code in [303, 302]:
                redirect_url = auth_response.headers.get('Location') or auth_response.headers.get('X-Action-Redirect')
                if redirect_url:
                    if redirect_url.startswith('/'):
                        redirect_url = f"{self.host}{redirect_url}"
                    
                    redirect_response = self.client.get(redirect_url, name="follow_auth_redirect")
                    
                    # Handle password form if redirected to /auth/basic
                    if '/auth/basic' in redirect_response.url:
                        final_response = self._handle_password_form(redirect_response, api_domain)
                        if not final_response:
                            return False
                        auth_response = final_response
                    else:
                        auth_response = redirect_response
            
            # Step 5: Verify authentication success
            if self._is_authentication_successful(auth_response):
                self.is_authenticated = True
                debug_print("Authentication successful")
                self._complete_authentication_flow()
                self._get_session_data()
                return True
            else:
                # Check for session cookies as fallback
                session_cookies = [name for name in self.client.cookies.keys() if 'session' in name.lower()]
                if session_cookies:
                    debug_print("Authentication successful (session cookies found)")
                    self.is_authenticated = True
                    self._complete_authentication_flow()
                    self._get_session_data()
                    return True
                
                debug_print(f"Authentication failed - Status: {auth_response.status_code}")
                return False
                
        except Exception as e:
            debug_print(f"Authentication error: {e}")
            return False
    
    def _extract_next_action_id(self, html_content):
        """Extract Next-Action ID from HTML"""
        patterns = [
            r'data-action="([a-f0-9]{40})"',
            r'&quot;id&quot;:&quot;([a-f0-9]{40})&quot;',
            r'"id":"([a-f0-9]{40})"',
            r'value="([a-f0-9]{40})"'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, html_content)
            if match:
                return match.group(1)
        
        return None
    
    def _create_form_data(self, next_action_id, api_domain):
        """Create multipart form data for Next.js server action"""
        boundary = f"----geckoformboundary{uuid.uuid4().hex}"
        
        form_parts = [
            f'Content-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n',
            f'Content-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"{next_action_id}","bound":"$@1"}}',
            f'Content-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]',
            f'Content-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\nk0',
            f'Content-Disposition: form-data; name="1_email"\r\n\r\n{self.login_email}',
            f'Content-Disposition: form-data; name="1_password"\r\n\r\n{self.login_password}',
            f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.{api_domain}',
            f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]'
        ]
        
        form_data = f'--{boundary}\r\n' + f'\r\n--{boundary}\r\n'.join(form_parts) + f'\r\n--{boundary}--\r\n'
        
        return {
            'data': form_data,
            'headers': {
                'Content-Type': f'multipart/form-data; boundary={boundary}',
                'Next-Action': next_action_id
            }
        }
    
    def _handle_password_form(self, response, api_domain):
        """Handle the second step of 2-factor authentication"""
        password_action_id = self._extract_next_action_id(response.text)
        if not password_action_id:
            debug_print("Could not find Next-Action ID on password form")
            return None
        
        # Submit password form
        form_data = self._create_form_data(password_action_id, api_domain)
        password_response = self.client.post(
            response.url,
            data=form_data['data'],
            headers=form_data['headers'],
            allow_redirects=False,
            name="submit_password_form"
        )
        
        # Follow final redirect after password submission
        if password_response.status_code in [303, 302]:
            final_redirect_url = password_response.headers.get('Location') or password_response.headers.get('X-Action-Redirect')
            if final_redirect_url:
                if final_redirect_url.startswith('/'):
                    final_redirect_url = f"https://thundercats.staging.guidecx.io{final_redirect_url}"
                
                return self.client.get(final_redirect_url, name="follow_final_auth_redirect")
        
        return None
    
    def _is_authentication_successful(self, response):
        """Check if authentication was successful"""
        if response.status_code == 303:
            return True
        
        if response.status_code == 200 and 'auth' not in response.url:
            return True
        
        if response.status_code in [200, 302, 303]:
            success_indicators = ['/projects', '/dashboard', '/app']
            return any(indicator in response.url for indicator in success_indicators)
        
        return False
    
    def _complete_authentication_flow(self):
        """Complete authentication by visiting the projects page"""
        try:
            self.client.get("/projects", name="complete_auth_flow")
        except Exception as e:
            debug_print(f"Error completing authentication flow: {e}")
    
    def _get_session_data(self):
        """Retrieve session data from the session endpoint"""
        try:
            session_response = self.client.get("/auth/session", name="get_session")
            
            if session_response.status_code == 200:
                try:
                    import json
                    session_data = json.loads(session_response.text)
                    
                    if isinstance(session_data, dict) and session_data:
                        self.session_data = session_data
                        if 'accessToken' in session_data:
                            debug_print(f"Access token found: {session_data['accessToken'][:50]}...")
                    else:
                        self.session_data = {}
                        
                except json.JSONDecodeError:
                    self.session_data = {}
            else:
                self.session_data = {}
                
        except Exception as e:
            debug_print(f"Error getting session data: {e}")
            self.session_data = {}
    
    def get_auth_headers(self):
        """Get headers for authenticated requests"""
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        if self.session_data and isinstance(self.session_data, dict):
            access_token = self.session_data.get('accessToken')
            if access_token:
                headers['Authorization'] = f'Bearer {access_token}'
        
        return headers
    
    def make_authenticated_request(self, method, path, **kwargs):
        """Make an authenticated request with proper headers"""
        if not self.is_authenticated:
            if not self.authenticate():
                raise Exception("Authentication required but failed")
        
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers'].update(self.get_auth_headers())
        
        return getattr(self.client, method.lower())(path, **kwargs)

# Test authentication if running directly
if __name__ == "__main__":
    try:
        from locust.env import Environment
        
        env = Environment(user_classes=[AuthenticatedUser])
        user = AuthenticatedUser(env)
        
        if user.authenticate():
            debug_print("Authentication test: PASSED")
            
            response = user.make_authenticated_request('GET', '/projects')
            if response.status_code == 200:
                debug_print("Authenticated request test: PASSED")
            else:
                debug_print(f"Authenticated request test: Status {response.status_code}")
        else:
            debug_print("Authentication test: FAILED")
            
    except ImportError:
        debug_print("Install locust to run the test: pip install locust")
    except Exception as e:
        debug_print(f"Test failed: {e}") 