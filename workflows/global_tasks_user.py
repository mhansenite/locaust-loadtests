#!/usr/bin/env python3
"""
GlobalTasks User - Auto-generated from HAR file
Converted from HAR file and integrated into modular architecture
"""

from locust import task
from auth.base_user import AuthenticatedUser
from auth.config import (
    DOMAIN_SUFFIX, DEBUG
)


class GlobalTasksUser(AuthenticatedUser):
    """
    User focused on globaltasks activities.
    Auto-generated from HAR workflow for authentic interactions.
    """
    
    # Use arches subdomain as host (adjust if needed)
    host = f"https://arches.{DOMAIN_SUFFIX}"
    
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
            "/tasks?_rsc=cddkm",
            headers={
                "Accept": "*/*",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Router-State-Tree": router_state_tree,
                "Priority": "u=4",
                "RSC": "1",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers"
            },
            catch_response=True,
            name="Page Load"
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
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": router_state_tree,
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers"
            },
            data='[{"type":1}]',
            catch_response=True,
            name="Api Calls"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls failed: {resp.status_code}")

        if DEBUG:
            print("✅ Api Calls completed")

    def on_start(self):
        """
        Override to ensure we're properly authenticated before starting tasks
        """
        # Call parent on_start to handle login
        super().on_start()
        
        if DEBUG:
            print("🚀 GlobalTasksUser initialized and authenticated")
            print(f"   • Host: {self.host}")
            print(f"   • Domain Suffix: {DOMAIN_SUFFIX}")
