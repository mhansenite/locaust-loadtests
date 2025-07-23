#!/usr/bin/env python3
"""
LoadProjects User - Uses Shared Authentication
Can be run directly with: locust -f workflows/load_projects_user.py

Uses shared authentication from auth.base_user module.
Auto-generated from HAR file: HARFIles/RAW_HAR/LoadProjects.har
"""

import os
import sys
from locust import task
from auth.base_user import AuthenticatedUser

# Add project root to path for imports when run directly
if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

# =============================================================================
# CONFIGURATION - Environment settings
# =============================================================================

# Get configuration from environment or shared auth module
DOMAIN_SUFFIX = os.getenv("DOMAIN_SUFFIX", "staging.guidecx.io")
DEBUG = os.getenv("DEBUG", "false").lower() in ["true", "1", "yes"]

# =============================================================================
# WORKFLOW CLASS - LoadProjectsUser
# =============================================================================

class LoadProjectsUser(AuthenticatedUser):
    """
    User focused on loadprojects activities.
    Standalone version for direct Locust execution.
    
    Uses CSV-driven host configuration from base authentication class.
    """
    
    # Relative weight when multiple user classes exist
    weight = 2
    
    # Primary subdomain for this workflow (determined from HAR file)
    primary_subdomain = "thundercats"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Extract domain from CSV data (already set by base class)
        if hasattr(self, 'test_data') and 'domain' in self.test_data:
            self.api_domain = self.test_data['domain']
        else:
            # Fallback to DOMAIN_SUFFIX
            self.api_domain = DOMAIN_SUFFIX
            
        if DEBUG:
            print(f"{self.__class__.__name__} using domain: {self.api_domain}")

    @task(weight=3)
    def pageload(self):
        """
        Page Load
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Page Load...")

        with self.make_api_request(
            "GET",
            "thundercats",
            "/v2/projects",
            headers={
                "Accept": '*/*',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Page Load successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load failed: {resp.status_code}")

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

        with self.make_api_request(
            "GET",
            "app",
            "/auth/session",
            headers={
                "Accept": 'application/json',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Api Calls 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 1 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "app",
            "/auth/session",
            headers={
                "Accept": 'application/json',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Api Calls 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 2 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "app",
            "/auth/session",
            headers={
                "Accept": 'application/json',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Api Calls 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 3 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "app",
            "/auth/session",
            headers={
                "Accept": 'application/json',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 4 failed: {resp.status_code}")

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

        with self.make_api_request(
            "POST",
            "k2-web",
            "/manager.project.project_list.ProjectListService/LoadTagsDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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

        with self.make_api_request(
            "POST",
            "k2-web",
            "/manager.project.project_list.ProjectListService/LoadProjectManagersDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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

        with self.make_api_request(
            "POST",
            "k2-web",
            "/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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

        with self.make_api_request(
            "POST",
            "k2-web",
            "/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
    print(f"""
{workflow_name} Workflow

Usage:
   locust -f {relative_path}

Configuration:
   export TEST_DATA_CSV=config/test_data_staging.csv
   export DOMAIN_SUFFIX=staging.guidecx.io
   export DEBUG=true

Example Commands:
   # Basic test
   locust -f {relative_path} --headless --users=5 --spawn-rate=1 --run-time=30s

   # With specific CSV data
   export TEST_DATA_CSV=config/test_data_production.csv
   locust -f {relative_path} --headless --users=3 --spawn-rate=1 --run-time=15s

   # Web UI mode
   locust -f {relative_path}
    """)
