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

class AuthenticatedUser(HttpUser):
    """
    Modern shared authentication base class.
    Features:
    - CSV-driven test data
    - Environment-aware (staging/production)
    - Centralized authentication logic
    - Router state management for Next.js
    """
    
    abstract = True  # Prevent Locust from instantiating this base class
    wait_time = between(3, 8)
    
    def __init__(self, *args, **kwargs):
        # Assign CSV data to this user instance BEFORE calling super()
        self.test_data = random.choice(TEST_DATA)
        
        # Set host from CSV data BEFORE calling super()
        if 'domain' in self.test_data and self.test_data['domain']:
            self.host = "https://arches." + self.test_data['domain']
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
        
        if DEBUG:
            print(f"User: {self.login_email} @ {self.host}")
    
    def on_start(self):
        """Authenticate user on startup"""
        self.authenticate()
        
    def authenticate(self):
        """Handle user authentication with modern Next.js flow"""
        if DEBUG:
            print("Authenticating...")
            
        try:
            # Step 1: Get login page and extract Next-Action ID
            login_response = self.client.get(f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.{DOMAIN_SUFFIX}")
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
            form_parts.append(f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.{DOMAIN_SUFFIX}')
            form_parts.append(f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]')
            
            # Join all parts with boundary
            form_data = f'--{boundary}\r\n' + f'\r\n--{boundary}\r\n'.join(form_parts) + f'\r\n--{boundary}--\r\n'
            
            login_submit = self.client.post(
                f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.{DOMAIN_SUFFIX}",
                data=form_data,
                headers={
                    'Content-Type': f'multipart/form-data; boundary={boundary}',
                    'Next-Action': next_action_id
                },
                allow_redirects=False
            )
            
            if login_submit.status_code in [303, 302]:
                self.is_authenticated = True
                
                # Step 4: Follow redirect to capture router state
                redirect_location = login_submit.headers.get('Location', f'/projects?host=app.{DOMAIN_SUFFIX}')
                
                # Navigate to projects page to capture router state
                projects_response = self.client.get(redirect_location)
                if projects_response.status_code == 200:
                    # Try to capture router state from response headers
                    router_state_header = None
                    for header_name, header_value in projects_response.headers.items():
                        if header_name.lower() == 'next-router-state-tree':
                            router_state_header = header_value
                            break
                    
                    if router_state_header:
                        self.current_router_state = router_state_header
                        if DEBUG:
                            print(f"Captured router state (length: {len(self.current_router_state)})")
                    else:
                        # Try extracting from HTML as fallback
                        self.current_router_state = self.extract_router_state_tree(projects_response.text)
                        if self.current_router_state:
                            if DEBUG:
                                print(f"Captured router state from HTML (length: {len(self.current_router_state)})")
                        else:
                            if DEBUG:
                                print("No router state available")
                
                if DEBUG:
                    print("Authentication successful")
                return True
            else:
                if DEBUG:
                    print(f"Authentication failed: {login_submit.status_code}")
                return False
                
        except Exception as e:
            if DEBUG:
                print(f"Authentication error: {e}")
            return False
    
    def get_auth_header(self):
        """Get authorization header for API calls"""
        return self.auth_token
    
    def get_current_router_state(self):
        """Get current router state for Next.js requests"""
        return getattr(self, 'current_router_state', None)
    
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
    
    def extract_router_state_tree(self, html_content):
        """Extract Next-Router-State-Tree from HTML content"""
        if not html_content:
            return None
            
        if DEBUG:
            print(f"Searching for router state in HTML (length: {len(html_content)})")
            
        # Most common pattern - look for URL-encoded router state trees (start with %5B which is '[')
        encoded_pattern = r'(%5B[A-Za-z0-9%_-]{100,}%5D)'
        match = re.search(encoded_pattern, html_content)
        if match:
            if DEBUG:
                print(f"Found router state (length: {len(match.group(1))})")
            return match.group(1)
        
        if DEBUG:
            print("No router state found")
        
        return None


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