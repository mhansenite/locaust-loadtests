#!/usr/bin/env python3
"""
GlobalTasks User - Standalone Version for Direct Execution
Can be run directly with: locust -f workflows/admin/global_tasks_user.py

This is a self-contained version that includes all necessary dependencies.
Auto-generated from HAR file: HARFIles/RAW_HAR/GlobalTasks.har
"""

import os
import sys
import csv
import random
import re
from urllib.parse import urljoin, urlparse
from locust import HttpUser, task, between
import requests

# =============================================================================
# CONFIGURATION - Embedded for standalone execution
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
            # For standalone files, adjust relative to project root
            if 'workflows/' in __file__:
                # Calculate project root from workflow file location
                project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
                csv_path = os.path.join(project_root, CSV_FILE_PATH)
            else:
                csv_path = CSV_FILE_PATH
        else:
            csv_path = CSV_FILE_PATH
            
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            if not data:
                raise ValueError("CSV file is empty")
            return data
    except FileNotFoundError:
        print(f"\n❌ CSV file not found: {CSV_FILE_PATH}")
        print("\n📝 Create environment-specific CSV files in config/ directory:")
        print("\n🟡 STAGING: config/test_data_staging.csv")
        print("   domain,login_email,login_password")
        print("   staging.guidecx.io,stage_user1@test.com,stage_pass")
        print("\n🔴 PRODUCTION: config/test_data_production.csv")
        print("   domain,login_email,login_password")
        print("   production.guidecx.com,prod_user1@company.com,prod_pass")
        print("\n🔧 Usage:")
        print("   export TEST_DATA_CSV=config/test_data_staging.csv")
        print("   locust -f <this_file> --users=5")
        raise
    except Exception as e:
        print(f"\n❌ Error loading CSV file: {e}")
        raise

# Load all test data at startup
TEST_DATA = load_test_data()
print(f"✅ Loaded {len(TEST_DATA)} test data rows from {CSV_FILE_PATH}")

# =============================================================================
# AUTHENTICATION BASE CLASS - Embedded for standalone execution  
# =============================================================================

class AuthenticatedUser(HttpUser):
    """
    Base class for authenticated users with CSV data support.
    Embedded version for standalone workflow execution.
    """
    
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
                "Available keys: " + str(list(self.test_data.keys())) + ". "
                "Please add a 'domain' column to your CSV file (e.g., staging.guidecx.io)"
            )
        
        super().__init__(*args, **kwargs)
        
        # Override authentication config with CSV data
        self.login_email = self.test_data.get('login_email', 'default@test.com')
        self.login_password = self.test_data.get('login_password', 'default_pass')
        
        # Authentication state
        self.is_authenticated = False
        self.auth_cookies = {}
        self.csrf_token = None
        self.next_action_id = None
        self.router_state_tree = None
        
        if DEBUG:
            print(f"🚀 User initialized with CSV data:")
            print(f"   • Host: {self.host}")
            print(f"   • Email: {self.login_email}")
            print(f"   • Test Data Keys: {list(self.test_data.keys())}")
    
    def on_start(self):
        """Authenticate user on startup"""
        self.authenticate()
        
    def authenticate(self):
        """Handle user authentication"""
        if DEBUG:
            print("🔑 Starting authentication...")
            
        try:
            # Step 1: Get login page
            login_response = self.client.get("/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.staging.guidecx.io")
            if login_response.status_code != 200:
                if DEBUG:
                    print(f"❌ Login page failed: {login_response.status_code}")
                return False
                
            # Step 2: Extract Next-Action ID
            html_content = login_response.text
            action_pattern = r'name="Next-Action"[^>]*value="([^"]+)"'
            action_match = re.search(action_pattern, html_content)
            
            if action_match:
                self.next_action_id = action_match.group(1)
                if DEBUG:
                    print(f"✅ Found Next-Action ID: {self.next_action_id[:20]}...")
            else:
                if DEBUG:
                    print("❌ Could not find Next-Action ID")
                return False
            
            # Step 3: Perform login
            login_data = {
                'email': self.login_email,
                'password': self.login_password,
                'Next-Action': self.next_action_id
            }
            
            login_submit = self.client.post(
                "/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.staging.guidecx.io",
                data=login_data,
                allow_redirects=False
            )
            
            if login_submit.status_code in [303, 302]:
                self.is_authenticated = True
                if DEBUG:
                    print("✅ Authentication successful")
                return True
            else:
                if DEBUG:
                    print(f"❌ Authentication failed: {login_submit.status_code}")
                return False
                
        except Exception as e:
            if DEBUG:
                print(f"❌ Authentication error: {e}")
            return False
    
    def get_current_router_state(self):
        """Get current router state for Next.js requests"""
        return self.router_state_tree or ""
    
    def get_csv_value(self, key, default=""):
        """Get a value from this user's CSV data"""
        return self.test_data.get(key, default)
    
    def extract_next_action_id(self, html_content):
        """Extract Next-Action ID from HTML content"""
        action_pattern = r'name="Next-Action"[^>]*value="([^"]+)"'
        action_match = re.search(action_pattern, html_content)
        return action_match.group(1) if action_match else None

# =============================================================================
# WORKFLOW CLASS - GlobalTasksUser
# =============================================================================

class GlobalTasksUser(AuthenticatedUser):
    """
    User focused on globaltasks activities.
    Standalone version for direct Locust execution.
    """
    
    # Relative weight when multiple user classes exist
    weight = 2

    @task(weight=2)
    def apicalls(self):
        """
        Api Calls
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Api Calls...")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            "/tasks",
            headers={
                "Accept": '*/*',
                "Host": f'arches.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://arches.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 1 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = f"https://arches.{DOMAIN_SUFFIX}/v2/projects"
        with self.client.get(page_url, catch_response=True) as page_resp:
            if page_resp.status_code == 200:
                next_action_id = self.extract_next_action_id(page_resp.text)
                if DEBUG and next_action_id:
                    print(f"✅ Extracted Next-Action ID: {next_action_id}")
            else:
                if DEBUG:
                    print("⚠️ Failed to get current page for Next-Action extraction")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.post(
            "/tasks",
            headers={
                "Accept": 'text/x-component',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Host": f'arches.{DOMAIN_SUFFIX}',
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": router_state_tree,
                "Origin": f'https://arches.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://arches.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "TE": 'trailers'
            },
            data='[{"type":1}]',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 2 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Api Calls completed")

# =============================================================================
# STANDALONE EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    When run directly, show usage information
    """
    print(f"""
🚀 GlobalTasks Standalone Workflow

📋 Usage:
   locust -f workflows/admin/global_tasks_user.py

🔧 Configuration:
   export TEST_DATA_CSV=config/test_data_staging.csv
   export DOMAIN_SUFFIX=staging.guidecx.io
   export DEBUG=true

📊 Example Commands:
   # Basic test
   locust -f workflows/admin/global_tasks_user.py --headless --users=5 --spawn-rate=1 --run-time=30s

   # With specific CSV data
   export TEST_DATA_CSV=config/test_data_production.csv
   locust -f workflows/admin/global_tasks_user.py --headless --users=3 --spawn-rate=1 --run-time=15s

   # Web UI mode
   locust -f workflows/admin/global_tasks_user.py

✅ This file is self-contained and can run independently!
    """)
