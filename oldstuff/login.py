from locust import task, run_single_user
from locust import FastHttpUser
import sys
from urllib.parse import quote, quote_plus
import json
import time
import asyncio
import websockets
import threading

# Login Configuration - Update these credentials as needed
LOGIN_EMAIL = "mhansen+arches@guidecx.com"
LOGIN_PASSWORD = "CTc5LUpu^G9Xf$"

# URL-encoded versions for use in URLs and payloads
LOGIN_EMAIL_ENCODED = quote_plus(LOGIN_EMAIL)  # For URL parameters
LOGIN_EMAIL_JSON_ENCODED = quote(LOGIN_EMAIL)  # For JSON in URLs

class arches_guidecx_com_Archive__25_07_17_12_43_00_(FastHttpUser):
    host = "https://app.guidecx.com"
    default_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    def get_auth_header(self):
        """
        Get the authorization header for API calls
        Returns the captured token or a fallback if not available
        """
        if self.auth_token:
            return self.auth_token
        else:
            # Fallback to hardcoded token if capture failed
            return "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhZjQ0NDJkLTRkZGYtNGE0ZS1hNmQzLTVhY2NlZTMxMmEzNCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMzhiOTY4N2UtNWVlNy00MTgwLWE1NjgtYmRkYTBmZGYxZTE0IiwiYXVkIjpbIjFiM2U3MWYyLWUxNGMtNGY0NC1hMWM1LTNkYzg4ZDM5NTJiNSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1Mjc3ODY2NywiaWF0IjoxNzUyNzc3NzY3LCJqdGkiOiI4MGU0YmQxNy0zMGM3LTQ5OTQtYmFjMy01NDcyYWRhMThkMDQiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIzOGI5Njg3ZS01ZWU3LTQxODAtYTU2OC1iZGRhMGZkZjFlMTQifQ.LeJbXeqLrMj9uc5a5M8nOOcoHIN6EPa8YHk9GzWmJRCYzs7vBVJVsPgFoUahWTyL42KXQgay6m01oOTqxegWk4WHVhG81BI2aNBjbpO8EPy_ZotKtKhiF9TQwaDtmI_-z5nvxMn_-V-FrZgQBuK8kW2M2uFcBp9mixWLWcipimh9SQBEdJy6quCu3dvWM4d9LNLvFe6aQCbx8Bt-F3V1v6_ihDn5-jQnWGS1supK2szIu93VJuuxgFxHHOyB76RhZ7zy_8sWmpi9dZmV_A8XgDz2v5fwqeZXCIIeO8GnvpouW9dTBfDpenyc7aZJS34il-d5yKyp5rbgZsIrhzVPdQ"

    def setup_guidecx_websocket(self):
        """
        Set up WebSocket connection to GuideX API subscriptions using asyncio
        """
        try:
            print("🔌 Connecting to GuideX WebSocket...")
            
            # Start WebSocket connection in a separate thread
            def run_websocket():
                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    
                    async def connect_and_listen():
                        uri = "wss://api.guidecx.com/subscriptions"
                        headers = {
                            "Origin": "https://arches.guidecx.com",
                            "Sec-WebSocket-Protocol": "actioncable-v1-json, actioncable-unsupported",
                        }
                        
                        self.guidecx_ws_connection = await websockets.connect(uri, additional_headers=headers)
                        print("✅ GuideX WebSocket connected successfully")
                        
                        # Send connection message for ActionCable
                        connection_msg = {
                            "command": "subscribe",
                            "identifier": json.dumps({
                                "channel": "NotificationsChannel"
                            })
                        }
                        await self.guidecx_ws_connection.send(json.dumps(connection_msg))
                        
                        # Listen for messages
                        async for message in self.guidecx_ws_connection:
                            print(f"📨 GuideX WebSocket message: {message}")
                    
                    loop.run_until_complete(connect_and_listen())
                except Exception as e:
                    print(f"❌ GuideX WebSocket error: {e}")
            
            # Start WebSocket thread
            self.guidecx_thread = threading.Thread(target=run_websocket, daemon=True)
            self.guidecx_thread.start()
            
            return True
            
        except Exception as e:
            print(f"❌ GuideX WebSocket connection failed: {e}")
            return None

    def setup_intercom_websocket(self):
        """
        Set up WebSocket connection to Intercom using asyncio  
        """
        try:
            print("🔌 Connecting to Intercom WebSocket...")
            
            # Start WebSocket connection in a separate thread
            def run_websocket():
                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    
                    async def connect_and_listen():
                        uri = "wss://nexus-websocket-a.intercom.io/pubsub/5-qGO328JZJ8shOHfXWacQHQnxTViiN5SRnVRUpZipurUbuyyKZUuDhWZHq2kDKe5LlF7WedABUqteUjcJhcjsuibtrIi3HQwnFOJ3?X-Nexus-New-Client=true&X-Nexus-Version=0.14.0&user_role=user"
                        headers = {
                            "Origin": "https://arches.guidecx.com",
                        }
                        
                        self.intercom_ws_connection = await websockets.connect(uri, additional_headers=headers)
                        print("✅ Intercom WebSocket connected successfully")
                        
                        # Listen for messages
                        async for message in self.intercom_ws_connection:
                            print(f"📨 Intercom WebSocket message: {message}")
                    
                    loop.run_until_complete(connect_and_listen())
                except Exception as e:
                    print(f"❌ Intercom WebSocket error: {e}")
            
            # Start WebSocket thread
            self.intercom_thread = threading.Thread(target=run_websocket, daemon=True)
            self.intercom_thread.start()
            
            return True
            
        except Exception as e:
            print(f"❌ Intercom WebSocket connection failed: {e}")
            return None

    def on_start(self):
        """
        Called when a user starts - cookies will be automatically managed
        by the underlying requests.Session for all subsequent requests
        
        This will run the entire test scenario once and then stop.
        """
        # Optional: Set any initial cookies if needed
        # self.client.cookies.set('_gcx.theme', 'default', domain='app.guidecx.com')
        
        # The first request will capture any Set-Cookie headers automatically
        # No need to manually manage cookies after this point
        
        # Initialize authorization token
        self.auth_token = None
        
        # Initialize WebSocket connections
        self.guidecx_ws = None
        self.intercom_ws = None
        self.guidecx_ws_connection = None
        self.intercom_ws_connection = None
        self.guidecx_thread = None
        self.intercom_thread = None
        
        # Execute the login flow once
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "app.guidecx.com",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True, debug_stream=sys.stderr
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/projects",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "app.guidecx.com",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/auth/logout?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "app.guidecx.com",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "app.guidecx.com",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
            headers={
                "Accept": "text/x-component",
                "Content-Type": "multipart/form-data; boundary=----geckoformboundarydf70c242556fd126d4918254d6dcd1eb",
                "Host": "app.guidecx.com",
                "Next-Action": "8c6d4f21e8485b281b4224a2beffc1e5a4db53ad",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(public)%22%2C%7B%22children%22%3A%5B%22auth%22%2C%7B%22children%22%3A%5B%22login%22%2C%7B%22children%22%3A%5B%5B%22slug%22%2C%22%22%2C%22oc%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22redirect-to%5C%22%3A%5C%22%2Fprojects%2F%3Fhost%3Dapp.guidecx.com%5C%22%7D%22%2C%7B%7D%2C%22%2Fauth%2Flogin%3Fredirect-to%3D%252Fprojects%252F%253Fhost%253Dapp.guidecx.com%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://app.guidecx.com",
                "Priority": "u=0",
                "Referer": "https://app.guidecx.com/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            data=f'------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"8c6d4f21e8485b281b4224a2beffc1e5a4db53ad","bound":"$@1"}}\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\nk3939455420\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_email"\r\n\r\n{LOGIN_EMAIL}\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_password"\r\n\r\n\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.guidecx.com\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb\r\nContent-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]\r\n------geckoformboundarydf70c242556fd126d4918254d6dcd1eb--\r\n',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            f"https://arches.guidecx.com/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "arches.guidecx.com",
                "Priority": "u=0, i",
                "Referer": "https://app.guidecx.com/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            f"https://arches.guidecx.com/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
            headers={
                "Accept": "text/x-component",
                "Content-Type": "multipart/form-data; boundary=----geckoformboundarya093a9eb85f465aa8e949961f6cca502",
                "Host": "arches.guidecx.com",
                "Next-Action": "8eb8615ae699a6509d67a8c34e8000498fd7ad94",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(public)%22%2C%7B%22children%22%3A%5B%22auth%22%2C%7B%22children%22%3A%5B%22basic%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22current-user-email%5C%22%3A%5C%22mhansen%2Barches%40guidecx.com%5C%22%2C%5C%22redirect-to%5C%22%3A%5C%22%2Fprojects%2F%3Fhost%3Dapp.guidecx.com%5C%22%7D%22%2C%7B%7D%2C%22%2Fauth%2Fbasic%3Fcurrent-user-email%3Dmhansen%252Barches%2540guidecx.com%26redirect-to%3D%252Fprojects%252F%253Fhost%253Dapp.guidecx.com%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=0",
                "Referer": f"https://arches.guidecx.com/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "TE": "trailers",
            },
            data=f'------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"8eb8615ae699a6509d67a8c34e8000498fd7ad94","bound":"$@1"}}\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\nk1194475227\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_email"\r\n\r\n{LOGIN_EMAIL}\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_redirect-to"\r\n\r\n/projects/?host=app.guidecx.com\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="1_password"\r\n\r\n{LOGIN_PASSWORD}\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502\r\nContent-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]\r\n------geckoformboundarya093a9eb85f465aa8e949961f6cca502--\r\n',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://arches.guidecx.com/projects/?host=app.guidecx.com",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "arches.guidecx.com",
                "Priority": "u=0, i",
                "Referer": "https://arches.guidecx.com/auth/basic?current-user-email=mhansen%2Barches%40guidecx.com&redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://arches.guidecx.com/projects?host=app.guidecx.com",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": "arches.guidecx.com",
                "Priority": "u=0, i",
                "Referer": "https://arches.guidecx.com/auth/basic?current-user-email=mhansen%2Barches%40guidecx.com&redirect-to=%2Fprojects%2F%3Fhost%3Dapp.guidecx.com",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
            },
        ) as resp:
            # Capture the authorization token from the session response
            if resp.status_code == 200:
                try:
                    session_data = resp.json()
                    if 'access_token' in session_data:
                        self.auth_token = f"Bearer {session_data['access_token']}"
                        print(f"✅ Captured authorization token: {self.auth_token[:50]}...")
                    elif 'accessToken' in session_data:
                        self.auth_token = f"Bearer {session_data['accessToken']}"
                        print(f"✅ Captured authorization token: {self.auth_token[:50]}...")
                    elif 'token' in session_data:
                        self.auth_token = f"Bearer {session_data['token']}"
                        print(f"✅ Captured authorization token: {self.auth_token[:50]}...")
                    else:
                        print("⚠️ No token found in session response, checking other fields...")
                        print(f"Response keys: {list(session_data.keys()) if session_data else 'No JSON data'}")
                except Exception as e:
                    print(f"⚠️ Could not parse session response: {e}")
            else:
                print(f"⚠️ Session request failed with status: {resp.status_code}")
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/mySegments/1b3e71f2-e14c-4f44-a1c5-3dc88d3952b5",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer akjui47oepo9b5p8kl76gfebihlcj0bme935",
                "Content-Type": "application/json",
                "Host": "sdk.split.io",
                "If-None-Match": '"819801577"',
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "SplitSDKVersion": "react-1.11.1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/splitChanges?since=-1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer akjui47oepo9b5p8kl76gfebihlcj0bme935",
                "Content-Type": "application/json",
                "Host": "sdk.split.io",
                "If-Modified-Since": "Wed, 16 Jul 2025 22:40:46 GMT",
                "If-None-Match": '"1752705646811"',
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "SplitSDKVersion": "react-1.11.1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        print("\n🔍 GraphQL Request: CountNotifications")
        auth_token = self.get_auth_header()
        print(f"   Authorization: {auth_token[:50]}...")
        
        # Prepare the GraphQL payload
        graphql_payload = {
            "operationName": "CountNotifications",
            "variables": {},
            "query": "query CountNotifications {\n  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])\n  mentions: unreadNotificationsCount(types: [COMMUNICATION])\n}\n",
        }
        
        print(f"   📦 JSON Payload: {graphql_payload}")
        
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?CountNotifications",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": auth_token,
                "x-graphql-version": "1.0",
            },
            json=graphql_payload,
        ) as resp:
            print(f"   Response Status: {resp.status_code}")
            print(f"   Response Headers: {dict(resp.headers)}")
            
            if resp.status_code == 200:
                try:
                    response_data = resp.json()
                    print(f"   ✅ GraphQL Success: {response_data}")
                except Exception as e:
                    print(f"   ❌ JSON Parse Error: {e}")
                    print(f"   Response Content: {resp.text[:200]}...")
                    resp.failure(f"JSON parse error: {e}")
            else:
                print(f"   ❌ GraphQL Failed: {resp.status_code}")
                print(f"   Response Content: {resp.text[:200]}...")
                resp.failure(f"GraphQL error: {resp.status_code}")
            
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?GetPendingProjectsSummary",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetPendingProjectsSummary",
                "variables": {},
                "query": "query GetPendingProjectsSummary {\n  pendingProjectsSummary {\n    openApi\n    hubspot\n    salesforce\n    __typename\n  }\n}\n",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?GetProjectManagerList",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetProjectManagerList",
                "variables": {
                    "organizationId": "1b3e71f2-e14c-4f44-a1c5-3dc88d3952b5",
                    "excludeAdmins": False,
                },
                "query": "query GetProjectManagerList($organizationId: ID, $excludeAdmins: Boolean) {\n  projectManagers(organizationId: $organizationId, excludeAdmins: $excludeAdmins) {\n    ...ProjectManagerProjectWizard\n    __typename\n  }\n}\n\nfragment ProjectManagerProjectWizard on UserType {\n  avatar {\n    originalUrl\n    __typename\n  }\n  capacity\n  displayOrganization {\n    name\n    __typename\n  }\n  email\n  firstName\n  id\n  jobRole\n  lastName\n  organization {\n    id\n    name\n    __typename\n  }\n  organizationName\n  projectsCount\n  __typename\n}\n",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?ProjectStatus_OrganizationSettings",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "ProjectStatus_OrganizationSettings",
                "variables": {"organizationId": "1b3e71f2-e14c-4f44-a1c5-3dc88d3952b5"},
                "query": "query ProjectStatus_OrganizationSettings($organizationId: ID!) {\n  organization(id: $organizationId) {\n    setting {\n      useStatusChangeReasons\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        ) as resp:
            pass
        # Set up WebSocket connection to GuideX API
        self.guidecx_ws = self.setup_guidecx_websocket()
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?GetChipFilters",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetChipFilters",
                "variables": {
                    "input": {
                        "context": "PROVIDER",
                        "statuses": ["ON_TIME", "ON_HOLD", "LATE"],
                    }
                },
                "query": "query GetChipFilters($input: ProjectFiltersInput!) {\n  projectFilterChips(input: $input) {\n    ...ChipFilter\n    __typename\n  }\n}\n\nfragment ChipFilter on ProjectFilterChipType {\n  label\n  value\n  key\n  __typename\n}\n",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?GetCustomConfigurations",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetCustomConfigurations",
                "variables": {
                    "input": {
                        "layoutIdentifiers": [
                            "project-plan-columns-provider-v1",
                            "project-plan-columns-third-party-v1",
                            "project-plan-columns-customer-v1",
                        ]
                    }
                },
                "query": "query GetCustomConfigurations($input: UserCustomConfigurationConnectionsInputType!) {\n  userCustomConfigurationConnections(input: $input) {\n    customConfigurations {\n      configuration\n      layoutIdentifier\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?GetProjectList",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetProjectList",
                "variables": {
                    "input": {
                        "listInputs": {
                            "perPage": 10,
                            "page": 1,
                            "keyword": "",
                            "sortBy": "NAME",
                            "sortDirection": "ASC",
                        },
                        "projectFilters": {
                            "context": "PROVIDER",
                            "statuses": ["ON_TIME", "ON_HOLD", "LATE"],
                        },
                    }
                },
                "query": "query GetProjectList($input: projectListInput!) {\n  projects(input: $input) {\n    maxCashValue\n    projects {\n      ...ProjectRowProjectList\n      __typename\n    }\n    pageInfo {\n      ...PageInfoProjectList\n      __typename\n    }\n    appliedFilters {\n      ...AppliedFiltersProjectList\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PageInfoProjectList on PageInfoType {\n  currentPage\n  isOutOfBounds\n  limit\n  totalPages\n  totalResults\n  __typename\n}\n\nfragment AppliedFiltersProjectList on AppliedProjectFilters {\n  context\n  statuses\n  tags\n  strict\n  brandNames\n  customerIds\n  cashValueRange\n  projectId\n  projectLateDays\n  projectManagerIds\n  templateIds\n  projectFiltersOperator {\n    tagOperator\n    templateOperator\n    milestoneOperator\n    __typename\n  }\n  activeMilestoneNames\n  endOn\n  startOn\n  filterDateBy\n  lastUpdatedDays\n  __typename\n}\n\nfragment ProjectRowProjectList on ProjectType {\n  id\n  name\n  cashValue\n  totalTasksCount\n  openTasksCount\n  openActionItemsCount\n  overdueTasksCount\n  completedAt\n  startOn\n  endOn\n  projectStatusChangeReasons {\n    ...ProjectStatusChangeReasonsProjectList\n    __typename\n  }\n  completedAt\n  forecastedEndOn\n  deletedAt\n  archivedAt\n  currentUserSettings {\n    projectView\n    restrictAccess\n    __typename\n  }\n  currentUserProjectContext\n  currentUserRestrictedAccess\n  lastActivityAt\n  projectManager {\n    ...ProjectManagerProjectList\n    __typename\n  }\n  status\n  customerV2 {\n    ...ProjectCustomerProjectList\n    __typename\n  }\n  projectType\n  templates {\n    id\n    milestones {\n      id\n      name\n      active\n      __typename\n    }\n    __typename\n  }\n  organization {\n    id\n    name\n    logo {\n      originalUrl\n      __typename\n    }\n    __typename\n  }\n  displayOrganization {\n    name\n    logo {\n      originalUrl\n      __typename\n    }\n    __typename\n  }\n  brand {\n    ...ProjectBrandProjectList\n    __typename\n  }\n  tags {\n    ...ProjectListTable_ProjectTag\n    __typename\n  }\n  errors: errorsCount\n  __typename\n}\n\nfragment ProjectListTable_ProjectTag on TagType {\n  id\n  name\n  color\n  internalOnly\n  __typename\n}\n\nfragment ProjectCustomerProjectList on CustomerType {\n  id\n  name\n  logo {\n    originalUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ProjectBrandProjectList on BrandType {\n  id\n  name\n  logo {\n    originalUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ProjectManagerProjectList on UserType {\n  id\n  firstName\n  lastName\n  status\n  avatar {\n    originalUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ProjectStatusChangeReasonsProjectList on ProjectStatusChangeReasonType {\n  id\n  name\n  description\n  createdAt\n  updatedAt\n  user {\n    id\n    firstName\n    lastName\n    avatar {\n      originalUrl\n      __typename\n    }\n    __typename\n  }\n  statusChangeReason {\n    id\n    name\n    statusChangeReasonGroup {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://auth.split.io/api/v2/auth?users=1b3e71f2-e14c-4f44-a1c5-3dc88d3952b5",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer akjui47oepo9b5p8kl76gfebihlcj0bme935",
                "Host": "auth.split.io",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "SplitSDKVersion": "react-1.11.1",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.authn.workspaces.WorkspaceService/LoadMyWorkspaces",
            headers={
                "Accept": "application/grpc-web-text",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/embedded/content",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://arches.guidecx.com",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
            data="app_id=crui9hdm&v=3&g=8deee548cda53e5881d9e56b48afc69ecf923de5&s=3d0489da-49ee-42ff-a396-4d4ae2638ef5&r=https%3A%2F%2Farches.guidecx.com%2Fauth%2Fbasic%3Fcurrent-user-email%3Dmhansen%252Barches%2540guidecx.com%26redirect-to%3D%252Fprojects%252F%253Fhost%253Dapp.guidecx.com&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=0727c2b1bccb76d0&internal=&is_intersection_booted=false&page_title=Projects&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Barches%40guidecx.com%22%2C%22user_id%22%3A%2238b9687e-5ee7-4180-a568-bdda0fdf1e14%22%2C%22user_hash%22%3A%2257955478490f228e7b904f3f15fc309be9e5cd89212d950522bdecf27a442bef%22%2C%22name%22%3A%22Mike%20Hansen%22%2C%22company%22%3A%7B%22company_id%22%3A%221b3e71f2-e14c-4f44-a1c5-3dc88d3952b5%22%2C%22name%22%3A%22Arches%22%2C%22website%22%3A%22guidecx-demo.com%22%7D%2C%22role%22%3A%22ADMIN%22%2C%22org_type%22%3A%22PROVIDER%22%2C%22trial%22%3Afalse%7D&referer=https%3A%2F%2Farches.guidecx.com%2Fprojects%3Fhost%3Dapp.guidecx.com&anonymous_session=VkpWWG13VldlVHJkampzVDBtaGkrMk14QVJLSGZvU3IvdzNoMUdsZk5pQ2QrYjl4d2ZBdnlKRU5aRmQ3K0JzcDJMRngwa3VhK1l2empyV2ZGSFRQcnA2NTJ2ZkJVb2Vxd0lSVk9DSXVOelk9LS1welRhVEY3Q1ZoVjNYM28yU01EU1B3PT0%3D--52fc46c983008ef69d4e0f95db0f458d9abf66d0&device_identifier=00694d8a-f30d-415e-bfa7-4779236202f4",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/launcher_settings",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://arches.guidecx.com",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
            data="app_id=crui9hdm&v=3&g=8deee548cda53e5881d9e56b48afc69ecf923de5&s=ca2fe61f-e1ff-4692-bb74-5b2c63811054&r=https%3A%2F%2Farches.guidecx.com%2Fauth%2Fbasic%3Fcurrent-user-email%3Dmhansen%252Barches%2540guidecx.com%26redirect-to%3D%252Fprojects%252F%253Fhost%253Dapp.guidecx.com&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=75fd7264afa5fa38&internal=&is_intersection_booted=false&page_title=Projects&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Barches%40guidecx.com%22%2C%22user_id%22%3A%2238b9687e-5ee7-4180-a568-bdda0fdf1e14%22%2C%22user_hash%22%3A%2257955478490f228e7b904f3f15fc309be9e5cd89212d950522bdecf27a442bef%22%7D&referer=https%3A%2F%2Farches.guidecx.com%2Fprojects%3Fhost%3Dapp.guidecx.com&anonymous_session=VkpWWG13VldlVHJkampzVDBtaGkrMk14QVJLSGZvU3IvdzNoMUdsZk5pQ2QrYjl4d2ZBdnlKRU5aRmQ3K0JzcDJMRngwa3VhK1l2empyV2ZGSFRQcnA2NTJ2ZkJVb2Vxd0lSVk9DSXVOelk9LS1welRhVEY3Q1ZoVjNYM28yU01EU1B3PT0%3D--52fc46c983008ef69d4e0f95db0f458d9abf66d0&device_identifier=00694d8a-f30d-415e-bfa7-4779236202f4",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/ping",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://arches.guidecx.com",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            },
            data="app_id=crui9hdm&v=3&g=8deee548cda53e5881d9e56b48afc69ecf923de5&s=fd5abdcc-4e5c-4f11-898d-8c8913964233&r=https%3A%2F%2Farches.guidecx.com%2Fauth%2Fbasic%3Fcurrent-user-email%3Dmhansen%252Barches%2540guidecx.com%26redirect-to%3D%252Fprojects%252F%253Fhost%253Dapp.guidecx.com&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=ea19fdc454e6eb79&internal=%7B%7D&is_intersection_booted=false&page_title=Projects&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Barches%40guidecx.com%22%2C%22user_id%22%3A%2238b9687e-5ee7-4180-a568-bdda0fdf1e14%22%2C%22user_hash%22%3A%2257955478490f228e7b904f3f15fc309be9e5cd89212d950522bdecf27a442bef%22%2C%22name%22%3A%22Mike%20Hansen%22%2C%22company%22%3A%7B%22company_id%22%3A%221b3e71f2-e14c-4f44-a1c5-3dc88d3952b5%22%2C%22name%22%3A%22Arches%22%2C%22website%22%3A%22guidecx-demo.com%22%7D%2C%22role%22%3A%22ADMIN%22%2C%22org_type%22%3A%22PROVIDER%22%2C%22trial%22%3Afalse%7D&source=apiBoot&sampling=false&referer=https%3A%2F%2Farches.guidecx.com%2Fprojects%3Fhost%3Dapp.guidecx.com&anonymous_session=VkpWWG13VldlVHJkampzVDBtaGkrMk14QVJLSGZvU3IvdzNoMUdsZk5pQ2QrYjl4d2ZBdnlKRU5aRmQ3K0JzcDJMRngwa3VhK1l2empyV2ZGSFRQcnA2NTJ2ZkJVb2Vxd0lSVk9DSXVOelk9LS1welRhVEY3Q1ZoVjNYM28yU01EU1B3PT0%3D--52fc46c983008ef69d4e0f95db0f458d9abf66d0&device_identifier=00694d8a-f30d-415e-bfa7-4779236202f4",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        # Set up WebSocket connection to Intercom
        self.intercom_ws = self.setup_intercom_websocket()
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/page_view_events",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://arches.guidecx.com",
                "Referer": "https://arches.guidecx.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "TE": "trailers",
            },
            data="app_id=crui9hdm&v=3&g=8deee548cda53e5881d9e56b48afc69ecf923de5&s=fd5abdcc-4e5c-4f11-898d-8c8913964233&r=https%3A%2F%2Farches.guidecx.com%2Fauth%2Fbasic%3Fcurrent-user-email%3Dmhansen%252Barches%2540guidecx.com%26redirect-to%3D%252Fprojects%252F%253Fhost%253Dapp.guidecx.com&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=a87e0b517b3fa289&internal=&is_intersection_booted=false&page_title=Projects&user_active_company_id=1b3e71f2-e14c-4f44-a1c5-3dc88d3952b5&user_data=%7B%22email%22%3A%22mhansen%2Barches%40guidecx.com%22%2C%22user_id%22%3A%2238b9687e-5ee7-4180-a568-bdda0fdf1e14%22%2C%22user_hash%22%3A%2257955478490f228e7b904f3f15fc309be9e5cd89212d950522bdecf27a442bef%22%7D&referer=https%3A%2F%2Farches.guidecx.com%2Fprojects%3Fhost%3Dapp.guidecx.com&anonymous_session=aTV4VG16U01hQUNGM3lRazdYNkQ3SGExdzdteUJJUU51bDFlWnNhSTFIcm1IMWt6K0tMbEhsaisydFpsNXlCWWJxSXNXM0lWN0hVZU1oSXgvMDVvRDN0blBpc1U0cTVockNVUGEya2lCQWM9LS1VKzFLdDdLL3Y1cmJTeFpTdlZ5SDlRPT0%3D--7a788468517090cb8244d4ac074574bc112cc738&device_identifier=00694d8a-f30d-415e-bfa7-4779236202f4",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.guidecx.com/graphql?GetProjectList",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": "api.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetProjectList",
                "variables": {
                    "input": {
                        "listInputs": {
                            "perPage": 10,
                            "page": 2,
                            "keyword": "",
                            "sortBy": "NAME",
                            "sortDirection": "ASC",
                        },
                        "projectFilters": {
                            "context": "PROVIDER",
                            "statuses": ["ON_TIME", "ON_HOLD", "LATE"],
                        },
                    }
                },
                "query": "query GetProjectList($input: projectListInput!) {\n  projects(input: $input) {\n    maxCashValue\n    projects {\n      ...ProjectRowProjectList\n      __typename\n    }\n    pageInfo {\n      ...PageInfoProjectList\n      __typename\n    }\n    appliedFilters {\n      ...AppliedFiltersProjectList\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PageInfoProjectList on PageInfoType {\n  currentPage\n  isOutOfBounds\n  limit\n  totalPages\n  totalResults\n  __typename\n}\n\nfragment AppliedFiltersProjectList on AppliedProjectFilters {\n  context\n  statuses\n  tags\n  strict\n  brandNames\n  customerIds\n  cashValueRange\n  projectId\n  projectLateDays\n  projectManagerIds\n  templateIds\n  projectFiltersOperator {\n    tagOperator\n    templateOperator\n    milestoneOperator\n    __typename\n  }\n  activeMilestoneNames\n  endOn\n  startOn\n  filterDateBy\n  lastUpdatedDays\n  __typename\n}\n\nfragment ProjectRowProjectList on ProjectType {\n  id\n  name\n  cashValue\n  totalTasksCount\n  openTasksCount\n  openActionItemsCount\n  overdueTasksCount\n  completedAt\n  startOn\n  endOn\n  projectStatusChangeReasons {\n    ...ProjectStatusChangeReasonsProjectList\n    __typename\n  }\n  completedAt\n  forecastedEndOn\n  deletedAt\n  archivedAt\n  currentUserSettings {\n    projectView\n    restrictAccess\n    __typename\n  }\n  currentUserProjectContext\n  currentUserRestrictedAccess\n  lastActivityAt\n  projectManager {\n    ...ProjectManagerProjectList\n    __typename\n  }\n  status\n  customerV2 {\n    ...ProjectCustomerProjectList\n    __typename\n  }\n  projectType\n  templates {\n    id\n    milestones {\n      id\n      name\n      active\n      __typename\n    }\n    __typename\n  }\n  organization {\n    id\n    name\n    logo {\n      originalUrl\n      __typename\n    }\n    __typename\n  }\n  displayOrganization {\n    name\n    logo {\n      originalUrl\n      __typename\n    }\n    __typename\n  }\n  brand {\n    ...ProjectBrandProjectList\n    __typename\n  }\n  tags {\n    ...ProjectListTable_ProjectTag\n    __typename\n  }\n  errors: errorsCount\n  __typename\n}\n\nfragment ProjectListTable_ProjectTag on TagType {\n  id\n  name\n  color\n  internalOnly\n  __typename\n}\n\nfragment ProjectCustomerProjectList on CustomerType {\n  id\n  name\n  logo {\n    originalUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ProjectBrandProjectList on BrandType {\n  id\n  name\n  logo {\n    originalUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ProjectManagerProjectList on UserType {\n  id\n  firstName\n  lastName\n  status\n  avatar {\n    originalUrl\n    __typename\n  }\n  __typename\n}\n\nfragment ProjectStatusChangeReasonsProjectList on ProjectStatusChangeReasonType {\n  id\n  name\n  description\n  createdAt\n  updatedAt\n  user {\n    id\n    firstName\n    lastName\n    avatar {\n      originalUrl\n      __typename\n    }\n    __typename\n  }\n  statusChangeReason {\n    id\n    name\n    statusChangeReasonGroup {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.core.customfields.CustomFieldService/SearchAssigned",
            headers={
                "Accept": "application/grpc-web-text",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
                "authorization": self.get_auth_header(),
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAA5gSJgokNzViNDI0ZjEtMjA1Ny00YzdlLTk4OGYtY2Y3ZTdkZDQzY2E2EiYKJDFmZjdiYzFlLTkxZGQtNDRhNi1hYmM2LTFkNTQ2MjAyNDA3YRImCiQ3OTU3YWJhNS1mM2MyLTQzZWUtYTAwNS00YTg4NTRlMTkyNjUSJgokYTk4MTZkN2QtYWMxZC00ZGM0LTliOTItNWE1ZWJlNDU4Zjg4EiYKJDE5YzcyNTgzLTZmYTEtNGUyZi04ZTkwLTQxZjA5NDYzNGFiNxImCiQxMzJhZTg4Zi1hZDdmLTRiNmYtYmNlNy05Y2YxZjlmZDZmNzkSJgokYTg4MjJlZDItYzM0OC00YjkzLWI0MTEtNjg5NTYyNWEzYjBiEiYKJDY0MGI2NjBmLWM5ODQtNGZkMS04NzEyLWRjMzA5YTlmODljMBImCiRkNjBjYjA4MC01NDA0LTQ0ZDItYWMwOC02YmQ3OTA5ZmZhNjISJgokZDMyODM3NTEtY2UzZS00YzZjLTk5NTUtMzVjNWNiMjFiY2MwGiYKJDRiNDQxYTFmLTU3NjMtNDdkMi1hNDliLTgyOWM1Nzg3NWU4MhomCiQ0NmIwZGQ4NC1hN2M3LTRlN2MtYjA1Zi1kOTM2OTVkZjg5ZDEaJgokNDZiMDljMGEtZTJlMi00NWI4LWFmNWUtZjg5MzgyNTNhNDRjGiYKJDc1NWYzYzUxLTg5NGItNDVkMi1hMzgzLTNhZjRlNmZlMDc2YRomCiQ0NmIwZTFmOS0zOTNiLTQ0NGUtYWMzYi0zNzQ0MDkyM2M5MGQaJgokNGIzZDlkYWYtYmM4Yy00ZDNkLWJhOGItYWZhNjQyOTUyNmI2GiYKJDRiM2U3NWRhLTNmZDQtNDYwZS1hZjhhLTc0Nzk5ZWNmYzNjMBomCiQ0YjQyZTVlMy1hZTExLTRjZmItODUwNy03NzBhZWU1ZWMxNmMaJgokNGI0Njk3NmQtZWNhYy00YzI0LWJjNDAtOGE5M2QzOGU2MjVkGiYKJDRiNGI0MWEzLWQzNWEtNGY3MS05NDk2LWFhZjc5YTUxNTZjYxomCiQ0YjRkN2MwOS0xNWRhLTQ4MmQtOGRjNC02YWZiMjE1Y2YxNmUaJgokNGI0ZWRiMTgtOWFiNi00YWIzLWE2MGUtYWQ0MDBmYWNhODY2GiYKJDRiNTJmOWRlLTZhYzItNDIyOS1iMzM1LTRiNGJkOWYzNDNhYQ==",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.core.customfields.CustomFieldService/SearchAssigned",
            headers={
                "Accept": "application/grpc-web-text",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAABSgSJgokNzViNDI0ZjEtMjA1Ny00YzdlLTk4OGYtY2Y3ZTdkZDQzY2E2EiYKJDFmZjdiYzFlLTkxZGQtNDRhNi1hYmM2LTFkNTQ2MjAyNDA3YRImCiQ3OTU3YWJhNS1mM2MyLTQzZWUtYTAwNS00YTg4NTRlMTkyNjUSJgokYTk4MTZkN2QtYWMxZC00ZGM0LTliOTItNWE1ZWJlNDU4Zjg4EiYKJDE5YzcyNTgzLTZmYTEtNGUyZi04ZTkwLTQxZjA5NDYzNGFiNxImCiQxMzJhZTg4Zi1hZDdmLTRiNmYtYmNlNy05Y2YxZjlmZDZmNzkSJgokYTg4MjJlZDItYzM0OC00YjkzLWI0MTEtNjg5NTYyNWEzYjBiEiYKJDY0MGI2NjBmLWM5ODQtNGZkMS04NzEyLWRjMzA5YTlmODljMBImCiRkNjBjYjA4MC01NDA0LTQ0ZDItYWMwOC02YmQ3OTA5ZmZhNjISJgokZDMyODM3NTEtY2UzZS00YzZjLTk5NTUtMzVjNWNiMjFiY2MwEiYKJGY5Y2UwZWQxLTBjYTAtNGYxZC04Y2Q1LTI2NThkNTE3NDAzOBImCiQ1NWVkMzg3Zi04MWM2LTRkMzgtOTlkMi00MTNiNzAxYjBiM2YSJgokZWE2NmVkYjUtZTJlZi00Y2ZjLThhYjMtYzg3ZmQxNTE4Mjg4EiYKJDljZTg4NGM1LWZiMjMtNGE2Yi1hMTdjLWY0MGIxYzIyNDQ0ZhImCiQ0MTBjNWM2NC1mMTUxLTQyMWQtODk1ZC1lZTg3MjYzNzkyODESJgokZmY5MzU4NDUtYzU2Ni00MDA5LThlNTUtOTU4ZWY3NWQzZWRhEiYKJDQ3ZmNiOTUzLTdmMjktNDA2MC1hYTFkLTc3MGJlZTlmMzYxNhImCiQ5OWU5M2ZiYy00YTYzLTQ1YzYtYmJlNi02NzEyYTQ3M2ZiYWMSJgokNzMyNWYxYzQtNDc4YS00ZjBlLWI0ZTYtN2EyZjdmNTFlMjVlEiYKJDA2ODFmZmRlLWExYWItNGJhMC1iY2JhLTc0NmU3OWQwNzI2OBomCiQ0YjQ0MWExZi01NzYzLTQ3ZDItYTQ5Yi04MjljNTc4NzVlODIaJgokNDZiMGRkODQtYTdjNy00ZTdjLWIwNWYtZDkzNjk1ZGY4OWQxGiYKJDQ2YjA5YzBhLWUyZTItNDViOC1hZjVlLWY4OTM4MjUzYTQ0YxomCiQ3NTVmM2M1MS04OTRiLTQ1ZDItYTM4My0zYWY0ZTZmZTA3NmEaJgokNDZiMGUxZjktMzkzYi00NDRlLWFjM2ItMzc0NDA5MjNjOTBkGiYKJDRiM2Q5ZGFmLWJjOGMtNGQzZC1iYThiLWFmYTY0Mjk1MjZiNhomCiQ0YjNlNzVkYS0zZmQ0LTQ2MGUtYWY4YS03NDc5OWVjZmMzYzAaJgokNGI0MmU1ZTMtYWUxMS00Y2ZiLTg1MDctNzcwYWVlNWVjMTZjGiYKJDRiNDY5NzZkLWVjYWMtNGMyNC1iYzQwLThhOTNkMzhlNjI1ZBomCiQ0YjRiNDFhMy1kMzVhLTRmNzEtOTQ5Ni1hYWY3OWE1MTU2Y2MaJgokNGI0ZDdjMDktMTVkYS00ODJkLThkYzQtNmFmYjIxNWNmMTZlGiYKJDRiNGVkYjE4LTlhYjYtNGFiMy1hNjBlLWFkNDAwZmFjYTg2NhomCiQ0YjUyZjlkZS02YWMyLTQyMjktYjMzNS00YjRiZDlmMzQzYWE=",
            catch_response=True,
        ) as resp:
            pass
        
        # Stop the test after completing the login flow once
        print("✅ Login flow completed successfully - stopping test")
        if hasattr(self, 'environment') and self.environment.runner:
            self.environment.runner.quit()

    def on_stop(self):
        """
        Called when a user stops - clean up WebSocket connections
        """
        self.cleanup_websockets()

    def cleanup_websockets(self):
        """
        Clean up WebSocket connections
        """
        try:
            if hasattr(self, 'guidecx_ws_connection') and self.guidecx_ws_connection:
                print("🔌 Closing GuideX WebSocket connection...")
                asyncio.run(self.guidecx_ws_connection.close())
                print("✅ GuideX WebSocket closed")
        except Exception as e:
            print(f"❌ Error closing GuideX WebSocket: {e}")

        try:
            if hasattr(self, 'intercom_ws_connection') and self.intercom_ws_connection:
                print("🔌 Closing Intercom WebSocket connection...")
                asyncio.run(self.intercom_ws_connection.close())
                print("✅ Intercom WebSocket closed")
        except Exception as e:
            print(f"❌ Error closing Intercom WebSocket: {e}")

    @task
    def idle_task(self):
        """
        Empty task - all the real work is done in on_start()
        This just keeps the user alive briefly before stopping
        """
        pass

    def websocket_message_handler(self):
        """
        Handle incoming WebSocket messages (optional - for demonstration)
        Note: In the new implementation, messages are handled automatically
        in the WebSocket threads, so this method is mainly for reference
        """
        # Messages are now handled automatically in the WebSocket threads
        # This method is kept for demonstration purposes
        pass


if __name__ == "__main__":
    run_single_user(arches_guidecx_com_Archive__25_07_17_12_43_00_)
