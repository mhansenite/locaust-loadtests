#!/usr/bin/env python3
"""
ProjectPlan User - Standalone Version for Direct Execution
Can be run directly with: locust -f workflows/project/project_plan_user.py

This is a self-contained version that includes all necessary dependencies.
Auto-generated from HAR file: HARFIles/RAW_HAR/thundercats.project.plan.har
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
        print("   domain,login_email,login_password,messageID,phaseID,projectID")
        print("   staging.guidecx.io,stage_user1@test.com,stage_pass")
        print("\n🔴 PRODUCTION: config/test_data_production.csv")
        print("   domain,login_email,login_password,messageID,phaseID,projectID")
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
# WORKFLOW CLASS - ProjectPlanUser
# =============================================================================

class ProjectPlanUser(AuthenticatedUser):
    """
    User focused on projectplan activities.
    Standalone version for direct Locust execution.
    """
    
    # Relative weight when multiple user classes exist
    weight = 2

    @task(weight=3)
    def pageload(self):
        """
        Page Load
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Page Load...")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects",
            headers={
                "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Priority": 'u=0, i',
                "Sec-Fetch-Dest": 'document',
                "Sec-Fetch-Mode": 'navigate',
                "Sec-Fetch-Site": 'none',
                "Sec-Fetch-User": '?1',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "Upgrade-Insecure-Requests": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 1 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 2 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 3 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 4 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 5 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 5 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 6 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 6 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 7 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 7 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 8 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 8 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 9 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 9 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 10 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 10 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 11 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 11 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 12 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 12 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 13 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 13 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 14 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 14 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 15 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 15 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 16 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 16 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 17 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 17 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 18 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 18 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 19 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 19 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId&messageId={messageID}".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load 20 successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load 20 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Page Load completed")

    @task(weight=2)
    def apicalls(self):
        """
        Api Calls
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Api Calls...")

        with self.client.post(
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 1 failed: {resp.status_code}")

        with self.client.post(
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 2 failed: {resp.status_code}")

        with self.client.post(
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 3 failed: {resp.status_code}")

        with self.client.post(
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 4 failed: {resp.status_code}")

        with self.client.post(
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 5 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 5 failed: {resp.status_code}")

        with self.client.post(
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 6 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 6 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 7 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 7 failed: {resp.status_code}")

        with self.client.post(
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 8 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 8 failed: {resp.status_code}")

        with self.client.get(
            "wss://api.staging.guidecx.io/subscriptions",
            headers={
                "Accept": '*/*',
                "Cache-Control": 'no-cache',
                "Connection": 'keep-alive, Upgrade',
                "Host": f'api.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Pragma": 'no-cache',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'websocket',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "Sec-WebSocket-Extensions": 'permessage-deflate',
                "Sec-WebSocket-Key": 'KVXLm7r4nGnA1E77KQwAog==',
                "Sec-WebSocket-Protocol": 'actioncable-v1-json, actioncable-unsupported',
                "Sec-WebSocket-Version": '13',
                "Upgrade": 'websocket'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 9 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 9 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 10 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 10 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 11 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 11 failed: {resp.status_code}")

        with self.client.get(
            "https://sdk.split.io/api/splitChanges?since=-1",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Content-Type": 'application/json',
                "Host": 'sdk.split.io',
                "If-Modified-Since": 'Tue, 08 Jul 2025 18:36:29 GMT',
                "If-None-Match": '"1751999789511"',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "SplitSDKVersion": 'react-1.11.1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 12 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 12 failed: {resp.status_code}")

        with self.client.post(
            f"https://api.{DOMAIN_SUFFIX}/graphql",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'api.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "x-graphql-version": '1.0'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 13 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 13 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/tasks",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 14 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 14 failed: {resp.status_code}")

        with self.client.get(
            "https://auth.split.io/api/v2/auth?users=18548de9-f5e4-4441-9c19-f1004cd4dea1",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": 'auth.split.io',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "SplitSDKVersion": 'react-1.11.1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 15 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 15 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/templates",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 16 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 16 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/time-tracking",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 17 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 17 failed: {resp.status_code}")

        with self.client.post(
            "/manager.authn.workspaces.WorkspaceService/LoadMyWorkspaces",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 18 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 18 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/resource-management/project-roles",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 19 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 19 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/customers",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 20 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 20 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/templates/projects",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 21 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 21 failed: {resp.status_code}")

        with self.client.post(
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 22 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 22 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 23 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 23 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 24 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 24 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 25 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 25 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 26 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 26 failed: {resp.status_code}")

        with self.client.get(
            f"https://guidecx.{DOMAIN_SUFFIX}/b/ss/guidecxstaging/1/JS-2.23.0-LDQM/s6993965865396?AQB=1&ndh=1&pf=1&t=21%2F6%2F2025+14%3A58%3A4+1+360&fid=0EE7024574418985-3EF65E226A056508&ce=UTF-8&g=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fv2%2Fprojects&cc=USD&events=event1&page=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fv2%2Fprojects&link=Projects&region=BODY&pid=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fv2%2Fprojects&oid=Projects&oidt=3&ot=SUBMIT&s=3840x2160&c=24&j=1.6&v=N&k=Y&bw=3824&bh=1584&AQE=1",
            headers={
                "Accept": 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
                "Connection": 'keep-alive',
                "Host": f'guidecx.{DOMAIN_SUFFIX}',
                "Referer": f'https://app.{DOMAIN_SUFFIX}'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 27 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 27 failed: {resp.status_code}")

        with self.client.get(
            "https://widget.intercom.io/widget/vtlfk4ov",
            headers={
                "Accept": '*/*',
                "Alt-Used": 'widget.intercom.io',
                "Connection": 'keep-alive',
                "Host": 'widget.intercom.io',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'script',
                "Sec-Fetch-Mode": 'no-cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 28 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 28 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/projects",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 29 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 29 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects/timeline",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 30 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 30 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=1&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 31 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 31 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=2&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 32 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 32 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=3&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 33 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 33 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=4&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 34 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 34 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=0&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 35 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 35 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=9&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 36 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 36 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=5&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 37 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 37 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=6&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 38 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 38 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/v2/projects?sortBy=7&sortOrder=asc",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 39 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 39 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 40 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 40 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 41 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 41 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 42 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 42 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 43 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 43 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 44 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 44 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 45 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 45 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 46 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 46 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 47 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 47 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 48 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 48 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 49 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 49 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 50 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 50 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 51 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 51 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 52 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 52 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 53 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 53 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 54 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 54 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 55 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 55 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 56 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 56 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/messages?messageKey=projectId".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/v2/projects',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 57 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 57 failed: {resp.status_code}")

        with self.client.get(
            "https://sdk.split.io/api/mySegments/BASIC",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Content-Type": 'application/json',
                "Host": 'sdk.split.io',
                "If-None-Match": '"1000002"',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "SplitSDKVersion": 'react-1.11.1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 58 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 58 failed: {resp.status_code}")

        with self.client.post(
            "https://api-iam.intercom.io/messenger/web/launcher_settings",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Content-Type": 'application/x-www-form-urlencoded',
                "Host": 'api-iam.intercom.io',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=79f82d4f-ec95-4d60-b3ed-8bf091550127&r=&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=fa4d508edee9c706&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan&anonymous_session=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0%3D--46bbe57f43c68e1b180b1e82c85afacb5c679437&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 59 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 59 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 60 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 60 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 61 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 61 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 62 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 62 failed: {resp.status_code}")

        with self.client.get(
            "https://sdk.split.io/api/splitChanges?since=-1",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Content-Type": 'application/json',
                "Host": 'sdk.split.io',
                "If-Modified-Since": 'Tue, 08 Jul 2025 18:36:29 GMT',
                "If-None-Match": '"1751999789511"',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "SplitSDKVersion": 'react-1.11.1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 63 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 63 failed: {resp.status_code}")

        with self.client.post(
            "https://api-iam.intercom.io/messenger/web/ping",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Content-Type": 'application/x-www-form-urlencoded',
                "Host": 'api-iam.intercom.io',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=b412a858-c64c-4d70-ab82-b64a3534cbaf&r=&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=65d84089c8486182&internal=%7B%7D&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%2C%22name%22%3A%22Mike%20Hansen%22%2C%22company%22%3A%7B%22company_id%22%3A%2218548de9-f5e4-4441-9c19-f1004cd4dea1%22%2C%22name%22%3A%22ThunderCats%22%2C%22website%22%3A%22thundercats.guidecx.io%22%7D%2C%22role%22%3A%22ADMIN%22%2C%22org_type%22%3A%22PROVIDER%22%2C%22trial%22%3Afalse%7D&source=apiBoot&sampling=false&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0%3D--46bbe57f43c68e1b180b1e82c85afacb5c679437&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 64 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 64 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = f"https://arches.{DOMAIN_SUFFIX}/project/7c235972-a318-430e-b83e-e0c4af6e616b"
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
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": router_state_tree,
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='[{"unitId":{"uuid":"6ee23d15-5122-4788-beaa-7b3f3b3976ab"},"excludeInternal":false}]',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 65 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 65 failed: {resp.status_code}")

        with self.client.get(
            "https://auth.split.io/api/v2/auth?users=BASIC",
            headers={
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Host": 'auth.split.io',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "SplitSDKVersion": 'react-1.11.1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 66 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 66 failed: {resp.status_code}")

        with self.client.post(
            "https://api-iam.intercom.io/messenger/web/page_view_events",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Content-Type": 'application/x-www-form-urlencoded',
                "Host": 'api-iam.intercom.io',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=b412a858-c64c-4d70-ab82-b64a3534cbaf&r=&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=3388a1d4762b01f0&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=18548de9-f5e4-4441-9c19-f1004cd4dea1&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0%3D--131dd1e1ab73af54263fda1f1f091d6c3c8730a5&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 67 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 67 failed: {resp.status_code}")

        with self.client.get(
            f"https://api.{DOMAIN_SUFFIX}/query?query=%7B%22dimensions%22%3A%5B%22workspace_unit_status.label%22%2C%22workspace_unit_status.status_category%22%5D%2C%22measures%22%3A%5B%22unit.count%22%5D%2C%22filters%22%3A%5B%7B%22member%22%3A%22unit.project_id%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%227c235972-a318-430e-b83e-e0c4af6e616b%22%5D%7D%2C%7B%22member%22%3A%22unit.type%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22ACTION%22%5D%7D%2C%7B%22member%22%3A%22unit_status.active%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22true%22%5D%7D%5D%7D",
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'api.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 68 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 68 failed: {resp.status_code}")

        with self.client.post(
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAE4KJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZiEiQ4YjQ1MjcxMy0yMWZiLTQ3OWYtOTM0My1hMjAxZjYwZjA2NGQ=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 69 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 69 failed: {resp.status_code}")

        with self.client.post(
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAACgKJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZi',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 70 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 70 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/team".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-Prefetch": '1',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 71 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 71 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/overview".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 72 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 72 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/attachments".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 73 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 73 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/custom-fields".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 74 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 74 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = f"https://arches.{DOMAIN_SUFFIX}/project/7c235972-a318-430e-b83e-e0c4af6e616b"
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
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": router_state_tree,
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"startDate":{"seconds":"1668384000","nanos":0},"dueDate":{"seconds":"1674777600","nanos":0}}]',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 75 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 75 failed: {resp.status_code}")

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/history".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 76 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 76 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = f"https://arches.{DOMAIN_SUFFIX}/project/7c235972-a318-430e-b83e-e0c4af6e616b"
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
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": router_state_tree,
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"phaseId":{"uuid":"6ee23d15-5122-4788-beaa-7b3f3b3976ab"},"filters":[]}]',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 77 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 77 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = f"https://arches.{DOMAIN_SUFFIX}/project/7c235972-a318-430e-b83e-e0c4af6e616b"
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
            f"https://app.{DOMAIN_SUFFIX}/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": router_state_tree,
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"phaseId":{"uuid":"6ee23d15-5122-4788-beaa-7b3f3b3976ab"},"filters":[]}]',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 78 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 78 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Api Calls completed")

    @task(weight=2)
    def filters(self):
        """
        Filters
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Filters...")

        with self.client.post(
            "/manager.project.project_list.ProjectListService/LoadTagsDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 1 failed: {resp.status_code}")

        with self.client.post(
            "/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 2 failed: {resp.status_code}")

        with self.client.post(
            "/manager.project.project_list.ProjectListService/LoadProjectManagersDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 3 failed: {resp.status_code}")

        with self.client.post(
            "/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Host": f'k2-web.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            },
            data='AAAAAAA=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 4 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Filters completed")

# =============================================================================
# STANDALONE EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    When run directly, show usage information
    """
    print(f"""
🚀 ProjectPlan Standalone Workflow

📋 Usage:
   locust -f workflows/project/project_plan_user.py

🔧 Configuration:
   export TEST_DATA_CSV=config/test_data_staging.csv
   export DOMAIN_SUFFIX=staging.guidecx.io
   export DEBUG=true

📊 Example Commands:
   # Basic test
   locust -f workflows/project/project_plan_user.py --headless --users=5 --spawn-rate=1 --run-time=30s

   # With specific CSV data
   export TEST_DATA_CSV=config/test_data_production.csv
   locust -f workflows/project/project_plan_user.py --headless --users=3 --spawn-rate=1 --run-time=15s

   # Web UI mode
   locust -f workflows/project/project_plan_user.py

✅ This file is self-contained and can run independently!
    """)
