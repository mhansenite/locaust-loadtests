#!/usr/bin/env python3
"""
TestRouterUpdate User - Auto-generated from HAR file
Converted from HAR file and integrated into modular architecture
"""

from locust import task
from auth.base_user import AuthenticatedUser
from auth.config import (
    DOMAIN_SUFFIX, DEBUG
)


class TestRouterUpdateUser(AuthenticatedUser):
    """
    User focused on testrouterupdate activities.
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

        with self.client.get(
            "/v2/projects?_rsc=d8sqm",
            headers={
                "Accept": "*/*",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22%28protected%29%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22%28list%29%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22https%3A%2F%2Farches.%7BDOMAIN_SUFFIX%7D%2Fv2%2Fprojects%22%2C%22refetch%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%5D",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
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

        with self.client.get(
            f"https://app.{DOMAIN_SUFFIX}/auth/session",
            headers={
                "Accept": "application/json",
                "Host": f"app.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            catch_response=True,
            name="Api Calls 1"
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
                "Accept": "application/json",
                "Host": f"app.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            catch_response=True,
            name="Api Calls 2"
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
                "Accept": "application/json",
                "Host": f"app.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            catch_response=True,
            name="Api Calls 3"
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
                "Accept": "application/json",
                "Host": f"app.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            catch_response=True,
            name="Api Calls 4"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Api Calls 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Api Calls 4 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Api Calls completed")

    @task(weight=4)
    def datarefresh(self):
        """
        Data Refresh
        Generated from HAR workflow
        """
        if DEBUG:
            print("🔄 Data Refresh...")

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

        # Use fallback if extraction failed
        if not next_action_id:
            next_action_id = "7dde6021d1d552016a324b86aabc828d90123a87"
            if DEBUG:
                print(f"⚠️ Using fallback Next-Action ID: {next_action_id}")

        with self.client.post(
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22%28protected%29%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22%28list%29%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22https%3A%2F%2Farches.%7BDOMAIN_SUFFIX%7D%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            data='[{"type":2}]',
            catch_response=True,
            name="Data Refresh 1"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Data Refresh 1 successful")
            else:
                if DEBUG:
                    print(f"❌ Data Refresh 1 failed: {resp.status_code}")

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

        # Use fallback if extraction failed
        if not next_action_id:
            next_action_id = "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181"
            if DEBUG:
                print(f"⚠️ Using fallback Next-Action ID: {next_action_id}")

        with self.client.post(
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22%28protected%29%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22%28list%29%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22https%3A%2F%2Farches.%7BDOMAIN_SUFFIX%7D%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            data='[{}]',
            catch_response=True,
            name="Data Refresh 2"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Data Refresh 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Data Refresh 2 failed: {resp.status_code}")

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

        # Use fallback if extraction failed
        if not next_action_id:
            next_action_id = "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181"
            if DEBUG:
                print(f"⚠️ Using fallback Next-Action ID: {next_action_id}")

        with self.client.post(
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22%28protected%29%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22%28list%29%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22https%3A%2F%2Farches.%7BDOMAIN_SUFFIX%7D%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            data='[{}]',
            catch_response=True,
            name="Data Refresh 3"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Data Refresh 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Data Refresh 3 failed: {resp.status_code}")

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

        # Use fallback if extraction failed
        if not next_action_id:
            next_action_id = "d460095e80259ffd0e3377f81ff6d3eb70666bda"
            if DEBUG:
                print(f"⚠️ Using fallback Next-Action ID: {next_action_id}")

        with self.client.post(
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Type": "text/plain;charset=UTF-8",
                "Host": f"arches.{DOMAIN_SUFFIX}",
                "Next-Action": next_action_id,
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22%28protected%29%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22%28list%29%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22https%3A%2F%2Farches.%7BDOMAIN_SUFFIX%7D%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers"
            },
            data='[{}]',
            catch_response=True,
            name="Data Refresh 4"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Data Refresh 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Data Refresh 4 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Data Refresh completed")

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
                "Accept": "application/grpc-web-text",
                "Host": f"k2-web.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1"
            },
            data='AAAAAAA=',
            catch_response=True,
            name="Filters 1"
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
                "Accept": "application/grpc-web-text",
                "Host": f"k2-web.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1"
            },
            data='AAAAAAA=',
            catch_response=True,
            name="Filters 2"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 2 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 2 failed: {resp.status_code}")

        with self.client.post(
            f"https://k2-web.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Host": f"k2-web.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1"
            },
            data='AAAAAAA=',
            catch_response=True,
            name="Filters 3"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 3 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 3 failed: {resp.status_code}")

        with self.client.post(
            f"https://k2-web.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Host": f"k2-web.{DOMAIN_SUFFIX}",
                "Origin": f"https://arches.{DOMAIN_SUFFIX}",
                "Priority": "u=4",
                "Referer": f"https://arches.{DOMAIN_SUFFIX}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1"
            },
            data='AAAAAAA=',
            catch_response=True,
            name="Filters 4"
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Filters 4 successful")
            else:
                if DEBUG:
                    print(f"❌ Filters 4 failed: {resp.status_code}")

        if DEBUG:
            print("✅ Filters completed")

    def on_start(self):
        """
        Override to ensure we're properly authenticated before starting tasks
        """
        # Call parent on_start to handle login
        super().on_start()
        
        if DEBUG:
            print("🚀 TestRouterUpdateUser initialized and authenticated")
            print(f"   • Host: {self.host}")
            print(f"   • Domain Suffix: {DOMAIN_SUFFIX}")
