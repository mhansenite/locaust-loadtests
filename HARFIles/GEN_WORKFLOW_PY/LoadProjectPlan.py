#!/usr/bin/env python3
"""
LoadProjectPlan User - Uses Shared Authentication
Can be run directly with: locust -f workflows/load_project_plan_user.py

Uses shared authentication from auth.base_user module.
Auto-generated from HAR file: HARFIles/RAW_HAR/LoadProjectPlan.har
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
# WORKFLOW CLASS - LoadProjectPlanUser
# =============================================================================

class LoadProjectPlanUser(AuthenticatedUser):
    """
    User focused on loadprojectplan activities.
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
            "/project/{projectID}/messages?messageKey=projectId&messageId={messageID}".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
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
                "Connection": 'keep-alive',
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
                "Connection": 'keep-alive',
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
                "Connection": 'keep-alive',
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

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = self.get_api_url("thundercats", "/v2/projects")
        with self.client.get(page_url, catch_response=True) as page_resp:
            if page_resp.status_code == 200:
                next_action_id = self.extract_next_action_id(page_resp.text)
                if DEBUG and next_action_id:
                    print(f"✅ Extracted Next-Action ID: {next_action_id}")
            else:
                if DEBUG:
                    print("⚠️ Failed to get current page for Next-Action extraction")

        with self.make_api_request(
            "POST",
            "thundercats",
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Api Calls 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 4 failed: {resp.status_code}")

        with self.make_api_request(
            "POST",
            "k2-web",
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
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
            data='AAAAAE4KJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZiEiQ4YjQ1MjcxMy0yMWZiLTQ3OWYtOTM0My1hMjAxZjYwZjA2NGQ=',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 5 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 5 failed: {resp.status_code}")

        with self.make_api_request(
            "POST",
            "k2-web",
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
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
            data='AAAAACgKJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZi',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 6 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 6 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "thundercats",
            "/project/{projectID}/team".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Router-Prefetch": '1',
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
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
                    print("✅ Api Calls 7 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 7 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "thundercats",
            "/project/{projectID}/overview".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://thundercats.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            },
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 8 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 8 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "thundercats",
            "/project/{projectID}/attachments".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
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
                    print("✅ Api Calls 9 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 9 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "thundercats",
            "/project/{projectID}/custom-fields".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
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
                    print("✅ Api Calls 10 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 10 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = self.get_api_url("thundercats", "/v2/projects")
        with self.client.get(page_url, catch_response=True) as page_resp:
            if page_resp.status_code == 200:
                next_action_id = self.extract_next_action_id(page_resp.text)
                if DEBUG and next_action_id:
                    print(f"✅ Extracted Next-Action ID: {next_action_id}")
            else:
                if DEBUG:
                    print("⚠️ Failed to get current page for Next-Action extraction")

        with self.make_api_request(
            "POST",
            "thundercats",
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"startDate":{"seconds":"1668384000","nanos":0},"dueDate":{"seconds":"1674777600","nanos":0}}]',
            catch_response=True
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 11 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 11 failed: {resp.status_code}")

        with self.make_api_request(
            "GET",
            "thundercats",
            "/project/{projectID}/history".format(**self.test_data),
            headers={
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan',
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
                    print("✅ Api Calls 12 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 12 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = self.get_api_url("thundercats", "/v2/projects")
        with self.client.get(page_url, catch_response=True) as page_resp:
            if page_resp.status_code == 200:
                next_action_id = self.extract_next_action_id(page_resp.text)
                if DEBUG and next_action_id:
                    print(f"✅ Extracted Next-Action ID: {next_action_id}")
            else:
                if DEBUG:
                    print("⚠️ Failed to get current page for Next-Action extraction")

        with self.make_api_request(
            "POST",
            "thundercats",
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Api Calls 13 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 13 failed: {resp.status_code}")

        # Extract dynamic Next-Action ID from current page
        next_action_id = None
        page_url = self.get_api_url("thundercats", "/v2/projects")
        with self.client.get(page_url, catch_response=True) as page_resp:
            if page_resp.status_code == 200:
                next_action_id = self.extract_next_action_id(page_resp.text)
                if DEBUG and next_action_id:
                    print(f"✅ Extracted Next-Action ID: {next_action_id}")
            else:
                if DEBUG:
                    print("⚠️ Failed to get current page for Next-Action extraction")

        with self.make_api_request(
            "POST",
            "thundercats",
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers={
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://thundercats.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://thundercats.{self.api_domain}',
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
                    print("✅ Api Calls 14 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 14 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Api Calls completed")

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
