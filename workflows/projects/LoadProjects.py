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

        # Get router state from auth base (captured during login)
        router_state_tree = self.get_current_router_state()
        if DEBUG and router_state_tree:
            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")
        elif DEBUG:
            print("⚠️ No router state available from auth")

        with self.client.get(
            "/v2/projects",
            headers={
                "Accept": '*/*',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Next-Router-State-Tree": router_state_tree,
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

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
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
                    print("✅ Api Calls 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 1 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
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
                    print("✅ Api Calls 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 2 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
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
                    print("✅ Api Calls 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 3 failed: {resp.status_code}")

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": 'application/json',
                "Host": f'app.{DOMAIN_SUFFIX}',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
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

        with self.client.get(
            "https://streaming.split.io/sse?channels=MjQ2OTYxMTc2Nw%3D%3D_MTI4MjY3MDc0Mg%3D%3D_control,MjQ2OTYxMTc2Nw%3D%3D_MTI4MjY3MDc0Mg%3D%3D_mySegments,MjQ2OTYxMTc2Nw%3D%3D_MTI4MjY3MDc0Mg%3D%3D_splits,%5B%3Foccupancy%3Dmetrics.publishers%5Dcontrol_pri,%5B%3Foccupancy%3Dmetrics.publishers%5Dcontrol_sec&accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6IkRQVkE3QS44czhnaVEiLCJ0eXAiOiJKV1QifQ.eyJ4LWFibHktY2FwYWJpbGl0eSI6IntcIk1qUTJPVFl4TVRjMk53PT1fTVRJNE1qWTNNRGMwTWc9PV9jb250cm9sXCI6W1wic3Vic2NyaWJlXCJdLFwiTWpRMk9UWXhNVGMyTnc9PV9NVEk0TWpZM01EYzBNZz09X215U2VnbWVudHNcIjpbXCJzdWJzY3JpYmVcIl0sXCJNalEyT1RZeE1UYzJOdz09X01USTRNalkzTURjME1nPT1fc3BsaXRzXCI6W1wic3Vic2NyaWJlXCJdLFwiY29udHJvbF9wcmlcIjpbXCJzdWJzY3JpYmVcIixcImNoYW5uZWwtbWV0YWRhdGE6cHVibGlzaGVyc1wiXSxcImNvbnRyb2xfc2VjXCI6W1wic3Vic2NyaWJlXCIsXCJjaGFubmVsLW1ldGFkYXRhOnB1Ymxpc2hlcnNcIl19IiwieC1hYmx5LWNsaWVudElkIjoiY2xpZW50SWQiLCJleHAiOjE3NTMxNDgxNzAsImlhdCI6MTc1MzE0NDU3MH0.8et0NHpFWJDGL-zethA99wq9KLmh3cB4KVfroWUyg9E&v=1.1&heartbeats=true&SplitSDKVersion=react-1.11.1&SplitSDKClientKey=5c0p",
            headers={
                "Accept": 'text/event-stream',
                "Cache-Control": 'no-cache',
                "Host": 'streaming.split.io',
                "Origin": f'https://app.{DOMAIN_SUFFIX}',
                "Pragma": 'no-cache',
                "Priority": 'u=4',
                "Referer": f'https://app.{DOMAIN_SUFFIX}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'cross-site',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 5 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 5 failed: {resp.status_code}")

        with self.client.get(
            "https://sdk.split.io/api/splitChanges?since=1753135864962",
            headers={
                "Accept": 'application/json',
                "Content-Type": 'application/json',
                "Host": 'sdk.split.io',
                "If-Modified-Since": 'Mon, 21 Jul 2025 22:11:04 GMT',
                "If-None-Match": '"1753135864962"',
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
                    print("✅ Api Calls 6 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 6 failed: {resp.status_code}")

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
            f"https://k2-web.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadTagsDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
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
            f"https://k2-web.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadProjectManagersDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
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
            f"https://k2-web.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
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
            f"https://k2-web.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": 'application/grpc-web-text',
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
    print(f"""
LoadProjects Workflow

Usage:
   locust -f workflows/load_projects_user.py

Configuration:
   export TEST_DATA_CSV=config/test_data_staging.csv
   export DOMAIN_SUFFIX=staging.guidecx.io
   export DEBUG=true

Example Commands:
   # Basic test
   locust -f workflows/load_projects_user.py --headless --users=5 --spawn-rate=1 --run-time=30s

   # With specific CSV data
   export TEST_DATA_CSV=config/test_data_production.csv
   locust -f workflows/load_projects_user.py --headless --users=3 --spawn-rate=1 --run-time=15s

   # Web UI mode
   locust -f workflows/load_projects_user.py
    """)
