from locust import FastHttpUser
import re
import uuid
from .config import (
    BASE_URL_APP, PROJECT_URL, BASE_URL_API,
    APP_DOMAIN, PROJECT_DOMAIN, API_DOMAIN,
    LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_EMAIL_ENCODED,
    DEBUG, WAIT_TIME_BETWEEN_TASKS
)


class AuthenticatedUser(FastHttpUser):
    """
    Base class for all authenticated users.
    Handles login flow and provides common authentication methods.
    """
    host = BASE_URL_APP
    
    # Default wait time between tasks (in seconds)
    wait_time = lambda self: WAIT_TIME_BETWEEN_TASKS
    
    default_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    def on_start(self):
        """
        Called when a user starts - performs essential login flow
        """
        # Initialize authorization token
        self.auth_token = None
        
        # Execute the essential login flow
        self.login()
        
        # Verify login was successful
        self.verify_authentication()

    def get_auth_header(self):
        """
        Get the authorization header for API calls
        Returns the captured token or raises an error if not available
        """
        if self.auth_token:
            return self.auth_token
        else:
            raise ValueError("No authentication token available - login flow may have failed")

    def login(self):
        """
        Perform the complete login flow
        """
        if DEBUG:
            print("🔑 Starting essential login flow...")

        # Step 1: Get login page
        login_html = self._get_login_page()
        
        # Step 2: Extract login action details
        login_action_id, login_action_key = self._extract_login_action_details(login_html)
        
        # Step 3: Submit email
        self._submit_email(login_action_id, login_action_key, login_html)
        
        # Step 4: Get password page
        password_html = self._get_password_page()
        
        # Step 5: Extract password action details
        password_action_id, password_action_key = self._extract_password_action_details(password_html)
        
        # Step 6: Submit password
        self._submit_password(password_action_id, password_action_key, password_html)
        
        # Step 7: Navigate to projects
        self._navigate_to_projects()
        
        # Step 8: Capture auth token
        self._capture_auth_token()
        
        if DEBUG:
            print("✅ Essential login flow completed successfully")

    def _get_login_page(self):
        """Get the initial login page"""
        login_html = None
        with self.client.request(
            "GET",
            f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": APP_DOMAIN,
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Login page: {resp.status_code}")
            if resp.status_code == 200:
                login_html = resp.text
        return login_html

    def _extract_login_action_details(self, login_html):
        """Extract login action ID and key from HTML"""
        login_action_id = self.extract_next_action_id(login_html)
        login_action_key = self.extract_action_key(login_html)
        
        # Fallback to hardcoded values if extraction fails
        if not login_action_id:
            login_action_id = "8c6d4f21e8485b281b4224a2beffc1e5a4db53ad"
            if DEBUG:
                print(f"   ⚠️ Using fallback login action ID: {login_action_id}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted login action ID: {login_action_id}")
                
        if not login_action_key:
            login_action_key = "k3939455420"
            if DEBUG:
                print(f"   ⚠️ Using fallback action key: {login_action_key}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted action key: {login_action_key}")
                
        return login_action_id, login_action_key

    def _submit_email(self, login_action_id, login_action_key, login_html):
        """Submit email (first step of login)"""
        login_boundary = self.get_boundary_for_context("login", login_html)
        form_data = self.build_form_data(
            action_id=login_action_id,
            action_key=login_action_key,
            boundary=login_boundary,
            email=LOGIN_EMAIL,
            redirect_to=f"/projects/?host={APP_DOMAIN}"
        )
        
        with self.client.request(
            "POST",
            f"/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/x-component",
                "Content-Type": f"multipart/form-data; boundary={login_boundary}",
                "Host": APP_DOMAIN,
                "Next-Action": login_action_id,
                "Origin": BASE_URL_APP,
                "Referer": f"{BASE_URL_APP}/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            },
            data=form_data,
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Email submission: {resp.status_code}")

    def _get_password_page(self):
        """Get the password page"""
        password_html = None
        with self.client.request(
            "GET",
            f"{PROJECT_URL}/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": PROJECT_DOMAIN,
                "Referer": f"{BASE_URL_APP}/auth/login?redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True, 
        ) as resp:
            if DEBUG:
                print(f"   ✅ Arches auth page: {resp.status_code}")
            if resp.status_code == 200:
                password_html = resp.text
        return password_html

    def _extract_password_action_details(self, password_html):
        """Extract password action ID and key from HTML"""
        password_action_id = self.extract_next_action_id(password_html)
        password_action_key = self.extract_action_key(password_html)
        
        # Fallback to hardcoded values if extraction fails
        if not password_action_id:
            password_action_id = "8eb8615ae699a6509d67a8c34e8000498fd7ad94"
            if DEBUG:
                print(f"   ⚠️ Using fallback password action ID: {password_action_id}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted password action ID: {password_action_id}")
                
        if not password_action_key:
            password_action_key = "k1194475227"
            if DEBUG:
                print(f"   ⚠️ Using fallback password action key: {password_action_key}")
        else:
            if DEBUG:
                print(f"   ✅ Extracted password action key: {password_action_key}")
                
        return password_action_id, password_action_key

    def _submit_password(self, password_action_id, password_action_key, password_html):
        """Submit password (second step of login)"""
        password_boundary = self.get_boundary_for_context("password", password_html)
        password_form_data = self.build_form_data(
            action_id=password_action_id,
            action_key=password_action_key,
            boundary=password_boundary,
            email=LOGIN_EMAIL,
            password=LOGIN_PASSWORD,
            redirect_to=f"/projects/?host={APP_DOMAIN}"
        )
        
        with self.client.request(
            "POST",
            f"{PROJECT_URL}/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
            headers={
                "Accept": "text/x-component",
                "Content-Type": f"multipart/form-data; boundary={password_boundary}",
                "Host": PROJECT_DOMAIN,
                "Next-Action": password_action_id,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/auth/basic?current-user-email={LOGIN_EMAIL_ENCODED}&redirect-to=%2Fprojects%2F%3Fhost%3D{APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            },
            data=password_form_data,
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Password submission: {resp.status_code}")

    def _navigate_to_projects(self):
        """Navigate to projects after successful login"""
        with self.client.request(
            "GET",
            f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Host": PROJECT_DOMAIN,
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            if DEBUG:
                print(f"   ✅ Projects page: {resp.status_code}")
            
                    # Capture fresh router state from response headers
        if resp.status_code == 200:
            # Debug: Show available headers
            if DEBUG:
                print(f"   🔍 Response headers: {list(resp.headers.keys())}")
            
            # Look for router state in response headers
            router_state_header = None
            for header_name, header_value in resp.headers.items():
                if header_name.lower() == 'next-router-state-tree':
                    router_state_header = header_value
                    break
            
            if router_state_header:
                self.current_router_state = router_state_header
                if DEBUG:
                    print(f"   ✅ Captured router state from headers (length: {len(self.current_router_state)})")
            else:
                # Try extracting from HTML as fallback
                self.current_router_state = self.extract_router_state_tree(resp.text)
                if self.current_router_state:
                    if DEBUG:
                        print(f"   ✅ Captured router state from HTML (length: {len(self.current_router_state)})")
                else:
                    # No router state available - workflows will handle this gracefully
                    self.current_router_state = None
                    if DEBUG:
                        print("   ⚠️ No router state available - workflows will continue without it")
        else:
            self.current_router_state = None

    def _capture_auth_token(self):
        """Get session info to capture auth token"""
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Host": APP_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
            },
        ) as resp:
            # Capture the authorization token from the session response
            if resp.status_code == 200:
                try:
                    session_data = resp.json()
                    if 'access_token' in session_data:
                        self.auth_token = f"Bearer {session_data['access_token']}"
                        if DEBUG:
                            print(f"   ✅ Captured fresh authorization token")
                    elif 'accessToken' in session_data:
                        self.auth_token = f"Bearer {session_data['accessToken']}"
                        if DEBUG:
                            print(f"   ✅ Captured fresh authorization token")
                    elif 'token' in session_data:
                        self.auth_token = f"Bearer {session_data['token']}"
                        if DEBUG:
                            print(f"   ✅ Captured fresh authorization token")
                    else:
                        if DEBUG:
                            print("   ⚠️ No token found in session response")
                except Exception as e:
                    if DEBUG:
                        print(f"   ⚠️ Could not parse session response: {e}")
            else:
                if DEBUG:
                    print(f"   ⚠️ Session request failed with status: {resp.status_code}")

    def verify_authentication(self):
        """
        Verify login with a simple API call
        """
        if DEBUG:
            print("\n🔍 Verifying login with API call...")
        
        with self.rest(
            "POST",
            f"{BASE_URL_API}/graphql?CountNotifications",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": API_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "CountNotifications",
                "variables": {},
                "query": "query CountNotifications {\n  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])\n  mentions: unreadNotificationsCount(types: [COMMUNICATION])\n}\n",
            },
        ) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print(f"   ✅ Login verification successful: {resp.status_code}")
            else:
                if DEBUG:
                    print(f"   ❌ Login verification failed: {resp.status_code}")
                resp.failure(f"Login verification failed: {resp.status_code}")

    # =========================================================================
    # UTILITY METHODS (extracted from original login.py)
    # =========================================================================

    def extract_next_action_id(self, html_content):
        """
        Extract Next-Action ID from HTML content
        """
        if not html_content:
            return None
        
        # Debug logging to help understand what we're working with
        if DEBUG:
            print(f"🔍 Searching for Next-Action ID in HTML content (length: {len(html_content)})")
            
        # Pattern 1: Look for data-action attribute in forms
        action_pattern = r'data-action="([a-f0-9]{40})"'
        match = re.search(action_pattern, html_content)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via data-action pattern: {match.group(1)}")
            return match.group(1)
        
        # Pattern 2: Look for action ID in hidden input values (JSON format)
        json_pattern = r'"id":"([a-f0-9]{40})"'
        match = re.search(json_pattern, html_content)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via JSON pattern: {match.group(1)}")
            return match.group(1)
        
        # Pattern 3: Look for Next-Action in script tags or meta tags
        script_pattern = r'Next-Action["\']?\s*[:\=]\s*["\']([a-f0-9]{40})["\']'
        match = re.search(script_pattern, html_content, re.IGNORECASE)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via script pattern: {match.group(1)}")
            return match.group(1)
        
        # Pattern 4: Look for the action ID in form elements
        form_pattern = r'name="[^"]*\$ACTION[^"]*"\s*value="[^"]*([a-f0-9]{40})[^"]*"'
        match = re.search(form_pattern, html_content)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via form pattern: {match.group(1)}")
            return match.group(1)
        
        # Pattern 5: Look for Next.js specific server action patterns
        # Next.js often embeds actions in script tags with specific formats
        nextjs_pattern1 = r'"([a-f0-9]{40})",null,null'
        match = re.search(nextjs_pattern1, html_content)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via Next.js pattern 1: {match.group(1)}")
            return match.group(1)
        
        # Pattern 6: Look for action IDs in __NEXT_DATA__ script
        next_data_pattern = r'__NEXT_DATA__[^{]*{[^}]*"action[Ii]d"\s*:\s*"([a-f0-9]{40})"'
        match = re.search(next_data_pattern, html_content, re.DOTALL)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via __NEXT_DATA__ pattern: {match.group(1)}")
            return match.group(1)
        
        # Pattern 7: Look for action IDs in form action attributes
        form_action_pattern = r'action="[^"]*([a-f0-9]{40})[^"]*"'
        match = re.search(form_action_pattern, html_content)
        if match:
            if DEBUG:
                print(f"✅ Found Next-Action via form action pattern: {match.group(1)}")
            return match.group(1)
        
        # Pattern 8: Generic fallback - use any valid 40-character hex string
        # This catches Next.js server actions that don't match specific patterns
        potential_actions = re.findall(r'[a-f0-9]{40}', html_content)
        if potential_actions:
            # Use the first unique action ID found
            action_id = potential_actions[0]
            if DEBUG:
                print(f"✅ Found Next-Action via generic pattern: {action_id}")
                print(f"🔍 Available action IDs: {potential_actions[:3]}...")
            return action_id
        
        # Debug: Show what we found if no patterns matched
        if DEBUG:
            print("🔍 No 40-character hex strings found in HTML content")
            # Show a sample of the content to help with debugging
            sample_content = html_content[:500] + "..." if len(html_content) > 500 else html_content
            print(f"🔍 HTML sample: {sample_content}")
        
        return None
    
    def get_current_router_state(self):
        """
        Get the current router state captured during authentication
        Returns the router state captured from the projects page, or None if not available
        """
        return getattr(self, 'current_router_state', None)
    
    def extract_router_state_tree(self, html_content):
        """
        Extract Next-Router-State-Tree from HTML content
        This extracts the current router state dynamically from the page
        """
        if not html_content:
            return None
            
        if DEBUG:
            print(f"🔍 Searching for router state in HTML content (length: {len(html_content)})")
            
        # Pattern 1: Look for router state in Next.js script tags
        script_pattern = r'"routerStateTree"\s*:\s*"([^"]*)"'
        match = re.search(script_pattern, html_content)
        if match:
            if DEBUG:
                print(f"✅ Found router state via script pattern")
            return match.group(1)
        
        # Pattern 2: Look for router state in __NEXT_DATA__ script
        next_data_pattern = r'__NEXT_DATA__[^{]*({.*?"routerStateTree"\s*:\s*"([^"]*)".*?})'
        match = re.search(next_data_pattern, html_content, re.DOTALL)
        if match:
            if DEBUG:
                print(f"✅ Found router state via __NEXT_DATA__ pattern")
            return match.group(2)
        
        # Pattern 3: Look for Next-Router-State-Tree in meta tags or headers
        meta_pattern = r'next-router-state-tree["\']?\s*[:\=]\s*["\']([^"\']*)["\']'
        match = re.search(meta_pattern, html_content, re.IGNORECASE)
        if match:
            if DEBUG:
                print(f"✅ Found router state via meta pattern")
            return match.group(1)
        
        # Pattern 4: Look for encoded router state trees in any context
        # Look for URL-encoded structures that look like router states
        encoded_patterns = [
            r'(%5B%22[^"]*%22%2C%7B[^}]*children[^}]*%7D[^]]*%5D)',  # Original pattern
            r'(%5B%22%22%2C%7B%22children%22%3A%5B[^]]+%5D)',  # Simplified children pattern
            r'(%5B[A-Za-z0-9%_-]{200,}%5D)',  # Long encoded arrays
        ]
        
        for pattern in encoded_patterns:
            match = re.search(pattern, html_content)
            if match:
                if DEBUG:
                    print(f"✅ Found router state via encoded pattern")
                return match.group(1)
        
        # Pattern 5: Look for any URL-encoded router state trees (they start with %5B which is '[')
        encoded_pattern = r'(%5B[A-Za-z0-9%_-]{100,})'
        matches = re.findall(encoded_pattern, html_content)
        if matches:
            # Filter for matches that look like router states (contain typical keywords)
            for match in matches:
                decoded_check = match.lower()
                if any(keyword in decoded_check for keyword in ['children', 'projects', 'page', 'navigation']):
                    if DEBUG:
                        print(f"✅ Found router state via keyword match")
                    return match
            # Return the longest match as fallback
            longest_match = max(matches, key=len)
            if len(longest_match) > 200:  # Only if it's substantial
                if DEBUG:
                    print(f"✅ Found router state via length heuristic")
                return longest_match
        
        # Pattern 6: Look for any encoded content that might be a router state
        # Check for patterns like those we see in the HAR file
        specific_patterns = [
            r'%5B%22%22%2C%7B%22children%22%3A%5B%22%28protected%29%22[^]]+%5D',
            r'%5B%22%22%2C%7B[^]]*projects[^]]*%5D',
            r'["\']([^"\']*%5B%22%22%2C%7B%22children%22[^"\']*)["\']',
        ]
        
        for pattern in specific_patterns:
            match = re.search(pattern, html_content, re.IGNORECASE)
            if match:
                router_state = match.group(1) if match.lastindex and match.lastindex >= 1 else match.group(0)
                if '%5B' in router_state and len(router_state) > 100:
                    if DEBUG:
                        print(f"✅ Found router state via specific pattern")
                    return router_state
        
        # Debug: Enhanced debugging information
        if DEBUG:
            if '__NEXT_DATA__' in html_content:
                print("🔍 Found __NEXT_DATA__ but no routerStateTree")
                # Look for any router-related terms
                router_terms = ['router', 'navigation', 'children', 'projects', '%5B', 'state']
                found_terms = [term for term in router_terms if term in html_content.lower()]
                if found_terms:
                    print(f"🔍 Found router-related terms: {found_terms}")
            else:
                print("🔍 No __NEXT_DATA__ found in HTML")
                
            # Look for any %5B patterns (URL-encoded '[')
            encoded_matches = re.findall(r'%5B[^%\s]{20,}', html_content)
            if encoded_matches:
                print(f"🔍 Found {len(encoded_matches)} encoded patterns, lengths: {[len(m) for m in encoded_matches[:3]]}")
                
            # Show a sample of the content to help with debugging
            sample_content = html_content[:500] + "..." if len(html_content) > 500 else html_content
            print(f"🔍 HTML sample: {sample_content}")
        
        return None
    
    def extract_action_key(self, html_content):
        """
        Extract the action key from HTML content
        """
        if not html_content:
            return None
            
        # Look for action key in form data
        key_pattern = r'name="[^"]*\$ACTION_KEY[^"]*"\s*value="([^"]*)"'
        match = re.search(key_pattern, html_content)
        if match:
            return match.group(1)
        
        # Alternative pattern for action keys
        key_pattern2 = r'"[^"]*\$ACTION_KEY[^"]*"[^"]*"([^"]*)"'
        match = re.search(key_pattern2, html_content)
        if match:
            return match.group(1)
            
        return "k3939455420"  # Fallback to hardcoded value
    
    def extract_or_generate_boundary(self, html_content=None):
        """
        Extract boundary from HTML content or generate a random one
        """
        if html_content:
            # Pattern 1: Look for boundary in Content-Type headers or JavaScript
            boundary_pattern = r'boundary[=:]?\s*["\']?([a-zA-Z0-9\-_]{10,})["\']?'
            match = re.search(boundary_pattern, html_content, re.IGNORECASE)
            if match:
                boundary = match.group(1)
                # Ensure it has the proper prefix
                if not boundary.startswith('----'):
                    boundary = f"----{boundary}"
                return boundary
            
            # Pattern 2: Look for gecko form boundary specifically (common pattern)
            gecko_pattern = r'----geckoformboundary([a-f0-9]{32})'
            match = re.search(gecko_pattern, html_content)
            if match:
                return f"----geckoformboundary{match.group(1)}"
        
        # Generate a random boundary if none found
        random_suffix = uuid.uuid4().hex  # 32 character hex string
        return f"----geckoformboundary{random_suffix}"
        
    def get_boundary_for_context(self, context="login", html_content=None):
        """
        Get an appropriate boundary for the given context
        """
        # Try to extract from HTML first
        if html_content:
            extracted_boundary = self.extract_or_generate_boundary(html_content)
            if extracted_boundary and not extracted_boundary.endswith(uuid.uuid4().hex):
                if DEBUG:
                    print(f"   ✅ Extracted boundary for {context}: {extracted_boundary[:50]}...")
                return extracted_boundary
        
        # Generate context-specific boundary
        if context == "login":
            boundary = "----geckoformboundarydf70c242556fd126d4918254d6dcd1eb"
            if DEBUG:
                print(f"   ✅ Using login boundary: {boundary[:50]}...")
        elif context == "password":
            boundary = "----geckoformboundarya093a9eb85f465aa8e949961f6cca502"
            if DEBUG:
                print(f"   ✅ Using password boundary: {boundary[:50]}...")
        else:
            boundary = self.extract_or_generate_boundary()
            if DEBUG:
                print(f"   ✅ Generated random boundary for {context}: {boundary[:50]}...")
        
        return boundary

    def build_form_data(self, action_id, action_key, boundary, email=None, password=None, redirect_to=None):
        """
        Build the multipart form data with extracted values
        """
        parts = []
        
        # Action reference
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_REF_1"\r\n\r\n')
        
        # Action with ID
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:0"\r\n\r\n{{"id":"{action_id}","bound":"$@1"}}')
        
        # Errors array
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_1:1"\r\n\r\n[{{"errors":[]}}]')
        
        # Action key
        parts.append(f'Content-Disposition: form-data; name="1_$ACTION_KEY"\r\n\r\n{action_key}')
        
        # Email field
        if email:
            parts.append(f'Content-Disposition: form-data; name="1_email"\r\n\r\n{email}')
        
        # Password field  
        if password:
            parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n{password}')
        else:
            parts.append(f'Content-Disposition: form-data; name="1_password"\r\n\r\n')
        
        # Redirect URL
        if redirect_to:
            parts.append(f'Content-Disposition: form-data; name="1_redirect-to"\r\n\r\n{redirect_to}')
        
        # Final data field
        parts.append(f'Content-Disposition: form-data; name="0"\r\n\r\n[{{"errors":[]}},"$K1"]')
        
        # Join all parts with boundary
        form_data = f'--{boundary}\r\n' + f'\r\n--{boundary}\r\n'.join(parts) + f'\r\n--{boundary}--\r\n'
        
        return form_data 