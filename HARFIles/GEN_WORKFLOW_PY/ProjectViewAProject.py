#!/usr/bin/env python3
"""
ProjectViewAProject User - Uses Shared Authentication
Can be run directly with: locust -f workflows/project_view_a_project_user.py

Uses shared authentication from common.auth module.
Auto-generated from HAR file: HARFIles/RAW_HAR/Projects/ProjectViewAProject.har
"""

import os
import sys
import csv
import random
from locust import task
from common.auth import AuthenticatedUser

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
# WORKFLOW CLASS - ProjectViewAProjectUser
# =============================================================================

class ProjectViewAProjectUser(AuthenticatedUser):
    """
    User focused on projectviewaproject activities.
    Standalone version for direct Locust execution.
    
    Uses environment variable configuration from base authentication class.
    """
    
    # Relative weight when multiple user classes exist
    weight = 2
    
    # Primary subdomain for this workflow (determined from HAR file)
    primary_subdomain = "app"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Extract domain from environment or use default
        self.api_domain = DOMAIN_SUFFIX
        
        # Initialize test data for CSV template variables
        if hasattr(self, 'test_data') and 'domain' in self.test_data:
            self.api_domain = self.test_data['domain']
        else:
            # For standalone execution, select random test data row
            if TEST_DATA:
                self.test_data = random.choice(TEST_DATA)
                self.api_domain = self.test_data.get('domain', DOMAIN_SUFFIX)
            else:
                # Fallback to default test data structure
                self.test_data = {
                    'domain': DOMAIN_SUFFIX,
                    'login_email': os.getenv('LOGIN_EMAIL', 'test@example.com'),
                    'login_password': os.getenv('LOGIN_PASSWORD', 'password'),
                    'projectID': 'test-project-id',
                    'phaseID': 'test-phase-id',
                    'milestoneID': 'test-milestone-id',
                    'taskID': 'test-task-id',
                    'messageID': 'test-message-id',
                    'channelID': 'test-channel-id'
                }
            
        if DEBUG:
            print(f"{self.__class__.__name__} using domain: {self.api_domain}")

    def extract_next_action_id(self, html_content):
        """
        Extract Next-Action ID from HTML content for Next.js server actions.
        This method should match the implementation in common.auth.
        """
        import re
        
        # Look for Next-Action ID in script tags
        patterns = [
            r'"__next_action_id__"\s*:\s*"([^"]+)"',
            r'actionId\s*:\s*"([^"]+)"',
            r'data-action-id="([^"]+)"',
            r'action-id:\s*([a-f0-9]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, html_content)
            if match:
                return match.group(1)
        
        # If no pattern matches, return None (will be handled gracefully)
        return None

    @task(weight=3)
    def pageload(self):
        """
        Page Load
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Page Load...")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/project/{projectID}/messages?messageKey=projectId&messageId={messageID}".format(**self.test_data),
            headers=auth_headers,
            catch_response=True,
            name="page_load"
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

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/auth/session",
            headers=auth_headers,
            catch_response=True,
            name="api_calls_1"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 1 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/auth/session",
            headers=auth_headers,
            catch_response=True,
            name="api_calls_2"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 2 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'application/json',
                "Connection": 'keep-alive',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/auth/session",
            headers=auth_headers,
            catch_response=True,
            name="api_calls_3"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 3 failed: {resp.status_code}")

        # Extract Next-Action ID for this request
        next_action_id = None
        try:
            # Get the current page to extract Next-Action ID
            with self.client.get("/", catch_response=True, name="extract_next_action") as page_resp:
                if page_resp.status_code == 200:
                    next_action_id = self.extract_next_action_id(page_resp.text)
                    if DEBUG and next_action_id:
                        print(f"✅ Extracted Next-Action ID: {next_action_id}")
        except Exception as e:
            if DEBUG:
                print(f"⚠️ Failed to extract Next-Action ID: {e}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://app.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.post(
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers=auth_headers,
            data='[{"unitId":{"uuid":"ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a"},"excludeInternal":false}]',
            catch_response=True,
            name="api_calls_4"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 4 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Origin": f'https://app.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            }
        auth_headers.update(request_headers)
        with self.client.post(
            f"https://k2-web.{self.api_domain}{"/manager.message.channels.ChannelService/GetTotalUnreadMessageCount"}",
            headers=auth_headers,
            data='AAAAAE4KJgokZWEyYzMyYTEtZWM4NS00MjI4LWJiNjYtYjlmOTQyY2ViNmE0EiRlYTJjMzJhMS1lYzg1LTQyMjgtYmI2Ni1iOWY5NDJjZWI2YTQ=',
            catch_response=True,
            name="api_calls_5"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 5 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 5 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Origin": f'https://app.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            }
        auth_headers.update(request_headers)
        with self.client.post(
            f"https://k2-web.{self.api_domain}{"/manager.project.plan.ProjectPlanService/StreamProjectDetails"}",
            headers=auth_headers,
            data='AAAAACgKJgokZWEyYzMyYTEtZWM4NS00MjI4LWJiNjYtYjlmOTQyY2ViNmE0',
            catch_response=True,
            name="api_calls_6"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 6 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 6 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'application/grpc-web-text',
                "Connection": 'keep-alive',
                "Origin": f'https://app.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-site',
                "Sec-GPC": '1',
                "TE": 'trailers',
                "content-type": 'application/grpc-web-text',
                "x-grpc-web": '1'
            }
        auth_headers.update(request_headers)
        with self.client.post(
            f"https://k2-web.{self.api_domain}{"/manager.project.plan.ProjectPlanService/StreamProjectDetails"}",
            headers=auth_headers,
            catch_response=True,
            name="api_calls_7"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 7 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 7 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Router-Prefetch": '1',
                "Next-Url": '/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/project/{projectID}/team".format(**self.test_data),
            headers=auth_headers,
            catch_response=True,
            name="api_calls_8"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 8 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 8 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/project/{projectID}/overview".format(**self.test_data),
            headers=auth_headers,
            catch_response=True,
            name="api_calls_9"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 9 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 9 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/project/{projectID}/attachments".format(**self.test_data),
            headers=auth_headers,
            catch_response=True,
            name="api_calls_10"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 10 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 10 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/project/{projectID}/custom-fields".format(**self.test_data),
            headers=auth_headers,
            catch_response=True,
            name="api_calls_11"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 11 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 11 failed: {resp.status_code}")

        # Extract Next-Action ID for this request
        next_action_id = None
        try:
            # Get the current page to extract Next-Action ID
            with self.client.get("/", catch_response=True, name="extract_next_action") as page_resp:
                if page_resp.status_code == 200:
                    next_action_id = self.extract_next_action_id(page_resp.text)
                    if DEBUG and next_action_id:
                        print(f"✅ Extracted Next-Action ID: {next_action_id}")
        except Exception as e:
            if DEBUG:
                print(f"⚠️ Failed to extract Next-Action ID: {e}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://app.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.post(
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers=auth_headers,
            data='[{"projectId":{"uuid":"ea2c32a1-ec85-4228-bb66-b9f942ceb6a4"},"startDate":{"seconds":"1753408091","nanos":0},"dueDate":{"seconds":"1754012891","nanos":0}}]',
            catch_response=True,
            name="api_calls_12"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 12 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 12 failed: {resp.status_code}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": '*/*',
                "Connection": 'keep-alive',
                "Next-Url": '/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan',
                "Priority": 'u=4',
                "RSC": '1',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.get(
            "/project/{projectID}/history".format(**self.test_data),
            headers=auth_headers,
            catch_response=True,
            name="api_calls_13"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 13 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 13 failed: {resp.status_code}")

        # Extract Next-Action ID for this request
        next_action_id = None
        try:
            # Get the current page to extract Next-Action ID
            with self.client.get("/", catch_response=True, name="extract_next_action") as page_resp:
                if page_resp.status_code == 200:
                    next_action_id = self.extract_next_action_id(page_resp.text)
                    if DEBUG and next_action_id:
                        print(f"✅ Extracted Next-Action ID: {next_action_id}")
        except Exception as e:
            if DEBUG:
                print(f"⚠️ Failed to extract Next-Action ID: {e}")

        # Get authenticated headers
        auth_headers = self.get_auth_headers()
        request_headers = {
                "Accept": 'text/x-component',
                "Connection": 'keep-alive',
                "Content-Type": 'text/plain;charset=UTF-8',
                "Next-Action": next_action_id,
                "Origin": f'https://app.{self.api_domain}',
                "Priority": 'u=4',
                "Referer": f'https://app.{self.api_domain}',
                "Sec-Fetch-Dest": 'empty',
                "Sec-Fetch-Mode": 'cors',
                "Sec-Fetch-Site": 'same-origin',
                "Sec-GPC": '1',
                "TE": 'trailers'
            }
        auth_headers.update(request_headers)
        with self.client.post(
            "/project/{projectID}/plan?phase={phaseID}&view=board".format(**self.test_data),
            headers=auth_headers,
            data='[{"projectId":{"uuid":"ea2c32a1-ec85-4228-bb66-b9f942ceb6a4"},"phaseId":{"uuid":"ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a"},"filters":[]}]',
            catch_response=True,
            name="api_calls_14"
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
ProjectViewAProject Workflow

Usage:
   locust -f workflows/project_view_a_project_user.py

Configuration:
   export DOMAIN_SUFFIX=staging.guidecx.io
   export LOGIN_EMAIL=your-email@example.com
   export LOGIN_PASSWORD=your-password
   export LOCUST_HOST=https://app.staging.guidecx.io
   export DEBUG=true

Example Commands:
   # Basic test
   locust -f workflows/project_view_a_project_user.py --headless --users=5 --spawn-rate=1 --run-time=30s

   # With specific environment
   export DOMAIN_SUFFIX=production.guidecx.com
   export LOGIN_EMAIL=prod_user@company.com
   export LOGIN_PASSWORD=prod_password
   export LOCUST_HOST=https://app.production.guidecx.com
   locust -f workflows/project_view_a_project_user.py --headless --users=3 --spawn-rate=1 --run-time=15s

   # Web UI mode
   locust -f workflows/project_view_a_project_user.py
    """)
