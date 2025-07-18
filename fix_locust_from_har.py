#!/usr/bin/env python3
"""
Script to optimize Locust files generated from HAR files:
1. Remove all hardcoded Cookie headers
2. Add on_start method for automatic cookie management if not present
3. Update class to use proper cookie handling
4. Remove all CSS and font file requests (for performance optimization)
5. Remove all image file requests (for performance optimization)
6. Remove all JavaScript and static asset requests (for performance optimization)
7. Add common browser headers to default_headers
8. Remove duplicate headers from individual requests
9. Fix GraphQL request headers (proper Accept/Content-Type headers)
10. Replace hardcoded JWT authorization tokens with dynamic token capture
11. Add authorization token management methods

This script transforms raw HAR-to-Locust conversions into production-ready load test scripts
that focus on testing server-side performance rather than client-side asset loading.
"""
import re
import os

def remove_cookie_headers(content):
    """Remove all Cookie header lines from the content"""
    # Pattern to match Cookie header lines with various indentation
    # Matches: spaces + "Cookie": "..." + comma + optional newline
    pattern = r'[ \t]*"Cookie": "[^"]*",?\r?\n'
    
    # Remove all matches
    new_content = re.sub(pattern, '', content)
    
    # Count how many were removed
    matches = re.findall(pattern, content)
    return new_content, len(matches)

def remove_css_requests(content):
    """Remove all CSS and font file request blocks from the content"""
    # Simple and efficient approach: find CSS/font blocks by looking for key identifiers
    # and then remove the entire with block
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    total_removed = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts a request block that we want to remove
        if 'with self.client.request(' in line:
            # Look ahead to see if this is a CSS request
            is_css_request = False
            block_start = i
            block_end = i
            
            # Scan through the block to find CSS indicators and the closing
            j = i
            while j < len(lines):
                current_line = lines[j]
                
                # Check for CSS and font indicators
                if ('.css"' in current_line or 
                    '"Sec-Fetch-Dest": "style"' in current_line or
                    '"Accept": "text/css' in current_line or
                    '.woff"' in current_line or
                    '.woff2"' in current_line or
                    '.ttf"' in current_line or
                    '.otf"' in current_line or
                    '"Sec-Fetch-Dest": "font"' in current_line or
                    '"Accept": "application/font' in current_line):
                    is_css_request = True
                
                # Find the end of the block
                if ') as resp:' in current_line:
                    # Look for the 'pass' statement
                    k = j + 1
                    while k < len(lines) and 'pass' not in lines[k].strip():
                        k += 1
                    if k < len(lines):
                        block_end = k
                        break
                j += 1
            
            if is_css_request:
                # Skip this entire block
                i = block_end + 1
                total_removed += 1
                continue
        
        # Keep this line
        new_lines.append(line)
        i += 1
    
    return '\n'.join(new_lines), total_removed

def remove_image_requests(content):
    """Remove all image file request blocks from the content"""
    # Simple and efficient approach: find image blocks by looking for key identifiers
    # and then remove the entire with block
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    total_removed = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts a request block that we want to remove
        if 'with self.client.request(' in line:
            # Look ahead to see if this is an image request
            is_image_request = False
            block_start = i
            block_end = i
            
            # Scan through the block to find image indicators and the closing
            j = i
            while j < len(lines):
                current_line = lines[j]
                
                # Check for image indicators
                if (any(ext in current_line for ext in ['.png"', '.jpg"', '.jpeg"', '.gif"', '.svg"', 
                                                       '.webp"', '.ico"', '.bmp"', '.tiff"', '.avif"']) or
                    '"Sec-Fetch-Dest": "image"' in current_line or
                    '"Accept": "image/' in current_line or
                    'cdn.guidecx.com/' in current_line and len(current_line.split('/')[-1].replace('"', '')) > 20 or
                    'intercomcdn.com/' in current_line or
                    'imgur.com/' in current_line or
                    'cloudfront.net/' in current_line or
                    'amazonaws.com/' in current_line):
                    is_image_request = True
                
                # Find the end of the block
                if ') as resp:' in current_line:
                    # Look for the 'pass' statement
                    k = j + 1
                    while k < len(lines) and 'pass' not in lines[k].strip():
                        k += 1
                    if k < len(lines):
                        block_end = k
                        break
                j += 1
            
            if is_image_request:
                # Skip this entire block
                i = block_end + 1
                total_removed += 1
                continue
        
        # Keep this line
        new_lines.append(line)
        i += 1
    
    return '\n'.join(new_lines), total_removed

def replace_auth_tokens(content):
    """Replace hardcoded JWT authorization tokens with dynamic method calls"""
    
    # Pattern to match any JWT Bearer token in authorization headers
    # JWT tokens always start with "eyJ" (base64 encoding of {"alg":...)
    jwt_pattern = r'"authorization": "Bearer eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",'
    
    # Replacement string
    replacement = '"authorization": self.get_auth_header(),'
    
    # Count occurrences before replacement
    count_before = len(re.findall(jwt_pattern, content))
    
    # Replace all occurrences
    new_content = re.sub(jwt_pattern, replacement, content)
    
    return new_content, count_before

def remove_javascript_requests(content):
    """Remove all JavaScript and static asset request blocks from the content"""
    # Simple and efficient approach: find JS/static asset blocks by looking for key identifiers
    # and then remove the entire with block
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    total_removed = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts a request block that we want to remove
        if 'with self.client.request(' in line:
            # Look ahead to see if this is a JavaScript/static asset request
            is_js_request = False
            block_start = i
            block_end = i
            
            # Scan through the block to find JS and static asset indicators
            j = i
            while j < len(lines):
                current_line = lines[j]
                
                # Check for JavaScript and static asset indicators
                if (('.js"' in current_line) or
                    ('/_next/static/' in current_line) or
                    ('/static/chunks/' in current_line) or
                    ('/static/js/' in current_line) or
                    ('webpack-' in current_line) or
                    ('framework-' in current_line) or
                    ('main-app-' in current_line) or
                    ('main-' in current_line and '.js' in current_line) or
                    ('chunks/' in current_line and '.js' in current_line) or
                    ('buildManifest.js' in current_line) or
                    ('ssgManifest.js' in current_line) or
                    ('"Sec-Fetch-Dest": "script"' in current_line) or
                    ('"Accept": "*/*"' in current_line and 'static' in current_line)):
                    is_js_request = True
                
                # Find the end of the block
                if ') as resp:' in current_line:
                    # Look for the 'pass' statement
                    k = j + 1
                    while k < len(lines) and 'pass' not in lines[k].strip():
                        k += 1
                    if k < len(lines):
                        block_end = k
                        break
                j += 1
            
            if is_js_request:
                # Skip this entire block
                i = block_end + 1
                total_removed += 1
                continue
        
        # Keep this line
        new_lines.append(line)
        i += 1
    
    return '\n'.join(new_lines), total_removed

def add_common_headers(content):
    """Add common browser headers to default_headers if they don't exist"""
    
    # Check if default_headers already has common headers
    if '"Accept-Encoding":' in content and 'default_headers' in content:
        return content, False
    
    # Pattern to find default_headers block and add common headers
    pattern = r'(default_headers = \{)([^}]*?)(\})'
    
    # Common headers that browsers typically send
    common_headers = '''
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Connection": "keep-alive",
        "Sec-GPC": "1",'''
    
    def replacement(match):
        existing_headers = match.group(2).strip()
        if existing_headers and not existing_headers.endswith(','):
            # Add comma after existing headers if they don't end with one
            existing_headers += ','
        return match.group(1) + existing_headers + common_headers + '\n    ' + match.group(3)
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Check if replacement was made
    headers_added = '"Accept-Encoding":' in new_content and '"Accept-Encoding":' not in content
    
    return new_content, headers_added

def remove_duplicate_headers(content):
    """Remove duplicate headers that are now in default_headers"""
    
    # Headers to remove from individual requests since they're now in default_headers
    headers_to_remove = [
        r'[ \t]*"Accept-Encoding": "gzip, deflate, br, zstd",?\r?\n',
        r'[ \t]*"Connection": "keep-alive",?\r?\n',
        r'[ \t]*"Sec-GPC": "1",?\r?\n'
    ]
    
    total_removed = 0
    new_content = content
    
    for pattern in headers_to_remove:
        matches = re.findall(pattern, new_content)
        total_removed += len(matches)
        new_content = re.sub(pattern, '', new_content)
    
    return new_content, total_removed

def fix_graphql_headers(content):
    """Fix GraphQL request headers for proper API communication"""
    print("  Fixing GraphQL headers...")
    
    changes_made = 0
    
    # Fix Content-Length headers - remove hardcoded values
    content_length_pattern = r'"Content-Length": "[^"]*",\s*'
    content_length_matches = len(re.findall(content_length_pattern, content))
    if content_length_matches > 0:
        content = re.sub(content_length_pattern, '', content)
        changes_made += content_length_matches
        print(f"    - Removed {content_length_matches} hardcoded Content-Length headers")
    
    # Fix Accept headers for GraphQL calls  
    accept_pattern = r'"Accept": "\*\/\*",'
    accept_matches = len(re.findall(accept_pattern, content))
    if accept_matches > 0:
        content = re.sub(accept_pattern, '"Accept": "application/json",', content)
        changes_made += accept_matches
        print(f"    - Fixed {accept_matches} Accept headers from '*/*' to 'application/json'")
    
    # Add Content-Type headers where missing for GraphQL calls
    graphql_pattern = r'(POST[^{]*graphql[^{]*headers=\{[^}]*)"Accept": "application/json",(?![^}]*"Content-Type")'
    def add_content_type(match):
        return match.group(1) + '"Accept": "application/json",\n                "Content-Type": "application/json",'
    
    content_type_matches = len(re.findall(graphql_pattern, content, re.MULTILINE | re.DOTALL))
    if content_type_matches > 0:
        content = re.sub(graphql_pattern, add_content_type, content, flags=re.MULTILINE | re.DOTALL)
        changes_made += content_type_matches
        print(f"    - Added {content_type_matches} missing Content-Type headers to GraphQL calls")
    
    return content, changes_made

def add_login_config_and_imports(content):
    """Add login configuration constants and required imports (avoiding duplicates)"""
    # Check if login config already exists
    if 'LOGIN_EMAIL = ' in content:
        return content, False
    
    # List of imports to potentially add, with their check strings
    imports_to_check = [
        ('import sys', 'import sys'),
        ('from urllib.parse import quote, quote_plus', 'from urllib.parse import'),
        ('import json', 'import json'),
        ('import time', 'import time'),
        ('import asyncio', 'import asyncio'),
        ('import websockets', 'import websockets'),
        ('import threading', 'import threading')
    ]
    
    # Build list of imports that don't already exist
    imports_to_add = []
    for import_line, check_string in imports_to_check:
        if check_string not in content:
            imports_to_add.append(import_line)
    
    content_with_imports = content
    
    # Only add imports if there are some to add
    if imports_to_add:
        # Find the end of the existing imports section
        # Look for the last import line before any blank lines or comments
        lines = content.split('\n')
        last_import_index = -1
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            if (stripped.startswith('import ') or 
                stripped.startswith('from ') and ' import ' in stripped):
                last_import_index = i
        
        if last_import_index >= 0:
            # Insert new imports after the last existing import
            lines[last_import_index] = lines[last_import_index] + '\n' + '\n'.join(imports_to_add)
            content_with_imports = '\n'.join(lines)
        else:
            # No existing imports found, add after locust imports
            pattern = r'(from locust import [^\n]*\n)'
            new_imports = '\n'.join(imports_to_add) + '\n'
            
            def replacement(match):
                return match.group(1) + new_imports
            
            content_with_imports = re.sub(pattern, replacement, content)
    
    # Add login configuration constants after imports, before class definition
    config_constants = '''# Login Configuration - Update these credentials as needed
LOGIN_EMAIL = "mhansen+arches@guidecx.com"
LOGIN_PASSWORD = "CTc5LUpu^G9Xf$"

# URL-encoded versions for use in URLs and payloads
LOGIN_EMAIL_ENCODED = quote_plus(LOGIN_EMAIL)  # For URL parameters
LOGIN_EMAIL_JSON_ENCODED = quote(LOGIN_EMAIL)  # For JSON in URLs


'''
    
    # Pattern to find class definition and insert config before it
    class_pattern = r'(class [A-Za-z0-9_]+\(FastHttpUser\):)'
    
    def class_replacement(match):
        return config_constants + match.group(1)
    
    final_content = re.sub(class_pattern, class_replacement, content_with_imports)
    
    # Check if replacement was made (either imports added or config added)
    config_added = ('LOGIN_EMAIL = ' in final_content and 'LOGIN_EMAIL = ' not in content) or len(imports_to_add) > 0
    
    return final_content, config_added

def add_auth_token_init(content):
    """Add auth_token initialization to the class"""
    # Check if auth_token initialization already exists
    if 'self.auth_token = None' in content:
        return content, False
    
    # Pattern to find default_headers and add auth_token initialization after it
    pattern = r'(default_headers = \{[^}]*\}\s*\n)'
    
    auth_init = '''
    def __init__(self):
        super().__init__()
        # Initialize auth token for dynamic capture
        self.auth_token = None
'''
    
    def replacement(match):
        return match.group(1) + auth_init
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Check if replacement was made
    init_added = 'self.auth_token = None' in new_content and 'self.auth_token = None' not in content
    
    return new_content, init_added

def add_get_auth_header_method(content):
    """Add get_auth_header method to the class"""
    # Check if get_auth_header method already exists
    if 'def get_auth_header(' in content:
        return content, False
    
    # Pattern to find where to insert the method (after __init__ or before on_start)
    # Look for either __init__ method or on_start method
    pattern = r'(self\.auth_token = None\s*\n)([ \t]*)(def on_start|@task)'
    
    get_auth_method = '''
    def get_auth_header(self):
        """
        Get the authorization header for API calls
        Returns the captured token or raises an error if not available
        """
        if self.auth_token:
            return self.auth_token
        else:
            # No fallback - force proper token capture
            raise Exception("No authorization token available. Ensure the /auth/session endpoint is called first to capture tokens.")

'''
    
    def replacement(match):
        return match.group(1) + match.group(2) + get_auth_method + match.group(2) + match.group(3)
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Check if replacement was made
    method_added = 'def get_auth_header(' in new_content and 'def get_auth_header(' not in content
    
    return new_content, method_added

def add_token_capture_to_auth_session(content):
    """Add token capture logic to the first /auth/session endpoint"""
    # Check if token capture already exists
    if 'self.auth_token = f"Bearer {session_data[' in content:
        return content, False
    
    # Pattern to find the first /auth/session endpoint and add token capture
    # Look for the specific pattern with "GET", "/auth/session" and ") as resp:"
    pattern = r'(with self\..*?"GET",\s*"/auth/session",.*?\) as resp:)\s*\n(\s*)pass'
    
    token_capture = '''
            # Capture the authorization token from the session response
            print(f"🔍 Session response status: {resp.status_code}")
            print(f"🔍 Session response headers: {dict(resp.headers)}")
            print(f"🔍 Session response content (first 200 chars): {resp.text[:200]}...")
            
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
                    print(f"⚠️ Failed to parse session response for token: {e}")
                    print(f"   Raw response: {resp.text[:300]}...")
            else:
                print(f"⚠️ Auth session request failed with status: {resp.status_code}")
                print(f"   Error response: {resp.text[:200]}...")'''
    
    def replacement(match):
        return match.group(1) + '\n' + match.group(2) + token_capture
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Check if replacement was made
    capture_added = 'self.auth_token = f"Bearer {session_data[' in new_content and 'self.auth_token = f"Bearer {session_data[' not in content
    
    return new_content, capture_added

def add_on_start_method(content):
    """Add on_start method if it doesn't exist"""
    # Check if on_start method already exists
    if 'def on_start(' in content:
        return content, False
    
    # Pattern to find class definition and insert on_start method after get_auth_header method
    # Look for the pattern after get_auth_header method, before @task or other methods
    pattern = r'(raise Exception\("No authorization token available.*?"\)\s*\n)([ \t]*)(@task|def (?!on_start))'
    
    on_start_method = '''
    def on_start(self):
        """
        Called when a user starts - cookies will be automatically managed
        by the underlying requests.Session for all subsequent requests.
        Authorization tokens will be captured from the first /auth/session call.
        """
        # Optional: Set any initial cookies if needed
        # self.client.cookies.set('_gcx.theme', 'default', domain='app.guidecx.com')
        
        # The first request will capture any Set-Cookie headers automatically
        # Authorization tokens will be captured from /auth/session responses
        # No need to manually manage cookies or tokens after this point
        pass

'''
    
    def replacement(match):
        return match.group(1) + match.group(2) + on_start_method + match.group(2) + match.group(3)
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Check if replacement was made
    method_added = 'def on_start(' in new_content and 'def on_start(' not in content
    
    return new_content, method_added

def fix_referer_urls(content):
    """Fix Referer URLs to include the ?host=app.guidecx.com parameter"""
    # Pattern to find auth/session requests with missing host parameter
    pattern = r'"Referer": "https://arches\.guidecx\.com/projects"'
    replacement = r'"Referer": "https://arches.guidecx.com/projects?host=app.guidecx.com"'
    
    new_content = re.sub(pattern, replacement, content)
    
    # Check if replacement was made
    referer_fixed = '?host=app.guidecx.com' in new_content and '?host=app.guidecx.com' not in content
    
    return new_content, referer_fixed

def fix_init_method(content):
    """Fix __init__ method to accept environment parameter for Locust compatibility"""
    # Check if __init__ method already has environment parameter
    if 'def __init__(self, environment):' in content:
        return content, False
    
    # Pattern to find __init__ method that only accepts self
    pattern = r'def __init__\(self\):\s*\n(\s*)super\(\).__init__\(\)'
    replacement = r'def __init__(self, environment):\n\1super().__init__(environment)'
    
    new_content = re.sub(pattern, replacement, content)
    
    # Check if replacement was made
    init_fixed = 'def __init__(self, environment):' in new_content and 'def __init__(self, environment):' not in content
    
    return new_content, init_fixed

def simplify_websocket_methods(content):
    """Simplify WebSocket methods to avoid asyncio conflicts in Locust"""
    # Check if WebSocket methods already simplified
    if 'placeholder - avoiding asyncio conflicts' in content:
        return content, False
    
    changes_made = False
    
    # Replace complex GuideX WebSocket setup
    guidecx_pattern = r'def setup_guidecx_websocket\(self\):.*?return (?:True|None)'
    guidecx_replacement = '''def setup_guidecx_websocket(self):
        """
        Set up WebSocket connection for GuideX API subscriptions
        Note: Simplified to avoid asyncio event loop conflicts in Locust
        """
        print("🔌 GuideX WebSocket setup (placeholder - avoiding asyncio conflicts)")
        # In a production load test, WebSocket connections would be handled separately
        # or with a different WebSocket library that doesn't conflict with Locust's event loop
        return True'''
    
    new_content = re.sub(guidecx_pattern, guidecx_replacement, content, flags=re.DOTALL)
    if new_content != content:
        changes_made = True
        content = new_content
    
    # Replace complex Intercom WebSocket setup
    intercom_pattern = r'def setup_intercom_websocket\(self\):.*?return (?:True|None)'
    intercom_replacement = '''def setup_intercom_websocket(self):
        """
        Set up WebSocket connection for Intercom chat system
        Note: Simplified to avoid asyncio event loop conflicts in Locust
        """
        print("🔌 Intercom WebSocket setup (placeholder - avoiding asyncio conflicts)")
        # In a production load test, WebSocket connections would be handled separately
        # or with a different WebSocket library that doesn't conflict with Locust's event loop
        return True'''
    
    new_content = re.sub(intercom_pattern, intercom_replacement, content, flags=re.DOTALL)
    if new_content != content:
        changes_made = True
    
    return new_content, changes_made

def replace_hardcoded_credentials(content):
    """Replace hardcoded usernames, emails, and passwords in form requests with configurable constants"""
    
    changes_made = 0
    new_content = content
    
    # Email patterns to replace (comprehensive list)
    email_patterns = [
        # Direct email in JSON/form data
        (r'"email":\s*"[^"]*@[^"]*"', '"email": LOGIN_EMAIL'),
        (r'"username":\s*"[^"]*@[^"]*"', '"username": LOGIN_EMAIL'),
        (r'"user":\s*"[^"]*@[^"]*"', '"user": LOGIN_EMAIL'),
        
        # Multipart form data patterns (simpler approach)
        (r'(name="[^"]*email[^"]*"\\r\\n\\r\\n)[^\\r]*@[^\\r]*', r'\1" + LOGIN_EMAIL + "'),
        (r'(name="[^"]*user[^"]*"\\r\\n\\r\\n)[^\\r]*@[^\\r]*', r'\1" + LOGIN_EMAIL + "'),
        
        # URL-encoded form data
        (r'email=[^&\s"]*%40[^&\s"]*', 'email=" + LOGIN_EMAIL_ENCODED + "'),
        (r'username=[^&\s"]*%40[^&\s"]*', 'username=" + LOGIN_EMAIL_ENCODED + "'),
        (r'user=[^&\s"]*%40[^&\s"]*', 'user=" + LOGIN_EMAIL_ENCODED + "'),
        
        # URL-encoded JSON data (like %7B%22email%22%3A%22...%22%7D)
        (r'%22email%22%3A%22[^%]*%40[^%]*%22', '%22email%22%3A%22" + quote(LOGIN_EMAIL) + "%22'),
        (r'%22username%22%3A%22[^%]*%40[^%]*%22', '%22username%22%3A%22" + quote(LOGIN_EMAIL) + "%22'),
        
        # Query parameters in URLs
        (r'current-user-email=[^&\s"]*%2B[^&\s"]*%40[^&\s"]*', 'current-user-email=" + LOGIN_EMAIL_ENCODED + "'),
        (r'user-email=[^&\s"]*%2B[^&\s"]*%40[^&\s"]*', 'user-email=" + LOGIN_EMAIL_ENCODED + "'),
        
        # Double-encoded patterns
        (r'current-user-email%3D[^&\s"]*%252B[^&\s"]*%2540[^&\s"]*', 'current-user-email%3D" + quote(LOGIN_EMAIL_ENCODED) + "'),
        
        # User data parameters
        (r'user_data=%7B%22email%22%3A%22[^%]*%40[^%]*%22', 'user_data=%7B%22email%22%3A%22" + quote(LOGIN_EMAIL) + "%22'),
    ]
    
    # Password patterns to replace
    password_patterns = [
        # Direct password in JSON/form data  
        (r'"password":\s*"[^"]{6,}"', '"password": LOGIN_PASSWORD'),
        (r'"pwd":\s*"[^"]{6,}"', '"pwd": LOGIN_PASSWORD'),
        (r'"pass":\s*"[^"]{6,}"', '"pass": LOGIN_PASSWORD'),
        
        # Multipart form data patterns (simpler approach)
        (r'(name="[^"]*password[^"]*"\\r\\n\\r\\n)[^\\r]{6,}', r'\1" + LOGIN_PASSWORD + "'),
        (r'(name="[^"]*pwd[^"]*"\\r\\n\\r\\n)[^\\r]{6,}', r'\1" + LOGIN_PASSWORD + "'),
        
        # URL-encoded form data
        (r'password=[^&\s"]{6,}', 'password=" + quote_plus(LOGIN_PASSWORD) + "'),
        (r'pwd=[^&\s"]{6,}', 'pwd=" + quote_plus(LOGIN_PASSWORD) + "'),
        
        # URL-encoded JSON data
        (r'%22password%22%3A%22[^%]{6,}%22', '%22password%22%3A%22" + quote(LOGIN_PASSWORD) + "%22'),
        (r'%22pwd%22%3A%22[^%]{6,}%22', '%22pwd%22%3A%22" + quote(LOGIN_PASSWORD) + "%22'),
    ]
    
    # Apply email replacements
    for pattern, replacement in email_patterns:
        matches = len(re.findall(pattern, new_content))
        if matches > 0:
            new_content = re.sub(pattern, replacement, new_content)
            changes_made += matches
    
    # Apply password replacements
    for pattern, replacement in password_patterns:
        matches = len(re.findall(pattern, new_content))
        if matches > 0:
            new_content = re.sub(pattern, replacement, new_content)
            changes_made += matches
    
    # Special case: Replace specific hardcoded email patterns we know exist
    specific_replacements = [
        # Direct email in plain text
        (r'mhansen\+arches@guidecx\.com', '" + LOGIN_EMAIL + "'),
        # Single URL-encoded
        (r'mhansen%2Barches%40guidecx\.com', '" + LOGIN_EMAIL_ENCODED + "'),
        # Double URL-encoded  
        (r'mhansen%252Barches%2540guidecx\.com', '" + quote(LOGIN_EMAIL_ENCODED) + "'),
        # In quoted strings
        (r'"mhansen\+arches@guidecx\.com"', 'LOGIN_EMAIL'),
        # Specific password
        (r'CTc5LUpu\^G9Xf\$', '" + LOGIN_PASSWORD + "'),
        (r'"CTc5LUpu\^G9Xf\$"', 'LOGIN_PASSWORD'),
    ]
    
    for pattern, replacement in specific_replacements:
        matches = len(re.findall(pattern, new_content))
        if matches > 0:
            new_content = re.sub(pattern, replacement, new_content)
            changes_made += matches
    
    return new_content, changes_made

def fix_locust_file(filename):
    """Fix cookie management, optimize Locust file, and add dynamic auth token handling"""
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found!")
        return False
    
    # Read original file
    with open(filename, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    print(f"Processing {filename}...")
    
    # Remove hardcoded cookies
    content_no_cookies, cookies_removed = remove_cookie_headers(original_content)
    print(f"  - Removed {cookies_removed} hardcoded Cookie headers")
    
    # Remove CSS and font file requests
    content_no_css, css_removed = remove_css_requests(content_no_cookies)
    print(f"  - Removed {css_removed} CSS and font file requests")
    
    # Remove image file requests
    content_no_images, images_removed = remove_image_requests(content_no_css)
    print(f"  - Removed {images_removed} image file requests")
    
    # Remove JavaScript and static asset requests
    content_no_js, js_removed = remove_javascript_requests(content_no_images)
    print(f"  - Removed {js_removed} JavaScript and static asset requests")
    
    # Add common headers to default_headers
    content_with_headers, headers_added = add_common_headers(content_no_js)
    if headers_added:
        print(f"  - Added common browser headers to default_headers")
    else:
        print(f"  - Common headers already exist in default_headers")
    
    # Remove duplicate headers from individual requests
    content_no_duplicates, duplicates_removed = remove_duplicate_headers(content_with_headers)
    print(f"  - Removed {duplicates_removed} duplicate header instances")
    
    # Fix GraphQL headers for proper API communication
    content_fixed_graphql, graphql_fixed = fix_graphql_headers(content_no_duplicates)
    if graphql_fixed > 0:
        print(f"  - Fixed {graphql_fixed} GraphQL header issues")
    else:
        print(f"  - No GraphQL header issues found")
    
    # Add login configuration and imports
    content_with_config, config_added = add_login_config_and_imports(content_fixed_graphql)
    if config_added:
        print(f"  - Added login configuration constants and required imports")
    else:
        print(f"  - Login configuration already exists")
    
    # Replace hardcoded credentials in form requests
    content_with_dynamic_creds, creds_replaced = replace_hardcoded_credentials(content_with_config)
    if creds_replaced > 0:
        print(f"  - Replaced {creds_replaced} hardcoded email/password instances with configurable constants")
    else:
        print(f"  - No hardcoded credentials found to replace")
    
    # Add auth token initialization
    content_with_init, init_added = add_auth_token_init(content_with_dynamic_creds)
    if init_added:
        print(f"  - Added auth token initialization")
    else:
        print(f"  - Auth token initialization already exists")
    
    # Add get_auth_header method
    content_with_auth_method, auth_method_added = add_get_auth_header_method(content_with_init)
    if auth_method_added:
        print(f"  - Added get_auth_header method")
    else:
        print(f"  - get_auth_header method already exists")
    
    # Replace hardcoded auth tokens
    content_dynamic_tokens, tokens_replaced = replace_auth_tokens(content_with_auth_method)
    print(f"  - Replaced {tokens_replaced} hardcoded authorization tokens with dynamic calls")
    
    # Add token capture to auth session
    content_with_capture, capture_added = add_token_capture_to_auth_session(content_dynamic_tokens)
    if capture_added:
        print(f"  - Added token capture logic to /auth/session endpoint")
    else:
        print(f"  - Token capture logic already exists or no /auth/session endpoint found")
    
    # Fix Referer URLs
    content_with_referer, referer_fixed = fix_referer_urls(content_with_capture)
    if referer_fixed:
        print(f"  - Fixed Referer URLs to include ?host=app.guidecx.com parameter")
    else:
        print(f"  - Referer URLs already correct or not found")
    
    # Fix __init__ method for Locust compatibility
    content_with_init, init_fixed = fix_init_method(content_with_referer)
    if init_fixed:
        print(f"  - Fixed __init__ method to accept environment parameter")
    else:
        print(f"  - __init__ method already correct")
    
    # Simplify WebSocket methods to avoid asyncio conflicts
    content_with_websocket, websocket_fixed = simplify_websocket_methods(content_with_init)
    if websocket_fixed:
        print(f"  - Simplified WebSocket methods to avoid asyncio conflicts")
    else:
        print(f"  - WebSocket methods already simplified or not found")
    
    # Add on_start method if needed
    final_content, method_added = add_on_start_method(content_with_websocket)
    if method_added:
        print(f"  - Added on_start method for automatic cookie and token management")
    else:
        print(f"  - on_start method already exists")
    
    # Write updated file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    # Create backup of original
    backup_filename = f"{filename}.backup"
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(original_content)
    print(f"  - Original file backed up as {backup_filename}")
    
    return True

def main():
    """Main function"""
    import sys
    
    print("HAR-to-Locust Optimizer & Performance Enhancement Tool")
    print("=" * 57)
    
    if len(sys.argv) < 2:
        print("❌ Error: Please specify a filename to process")
        print()
        print("Usage:")
        print("  python3 fix_locust_from_har.py <filename>")
        print()
        print("Example:")
        print("  python3 fix_locust_from_har.py login.py")
        print("  python3 fix_locust_from_har.py my_locust_script.py")
        print()
        print("What this script does:")
        print("- Removes all hardcoded 'Cookie' headers")
        print("- Removes all CSS and font file requests (performance optimization)")
        print("- Removes all image file requests (performance optimization)")
        print("- Removes all JavaScript and static asset requests (performance optimization)")
        print("- Adds common browser headers to default_headers")
        print("- Removes duplicate headers from individual requests")
        print("- Fixes GraphQL request headers (proper Accept/Content-Type headers)")
        print("- Adds login configuration constants and required imports")
        print("- Replaces hardcoded usernames/emails and passwords with configurable constants")
        print("- Replaces hardcoded JWT authorization tokens with dynamic token capture")
        print("- Adds auth token initialization and management methods")
        print("- Adds enhanced token capture logic to /auth/session endpoints (access_token, accessToken, token)")
        print("- Adds debug logging for token capture troubleshooting")
        print("- Fixes Referer URLs to include required ?host=app.guidecx.com parameter")
        print("- Fixes __init__ method to accept environment parameter for Locust compatibility")
        print("- Simplifies WebSocket methods to avoid asyncio event loop conflicts")
        print("- Adds on_start() method for automatic cookie and token management")
        print("- Creates a backup of the original file")
        return
    
    filename = sys.argv[1]
    print(f"Target file: {filename}")
    print()
    
    success = fix_locust_file(filename)
    
    if success:
        print()
        print("✅ Locust file has been optimized!")
        print()
        print("Changes made:")
        print("1. Removed all hardcoded 'Cookie' headers")
        print("2. Removed all CSS and font file requests (performance optimization)")
        print("3. Removed all image file requests (performance optimization)")
        print("4. Removed all JavaScript and static asset requests (performance optimization)")
        print("5. Added common browser headers to default_headers")
        print("6. Removed duplicate headers from individual requests")
        print("7. Fixed GraphQL request headers (proper Accept/Content-Type headers)")
        print("8. Added login configuration constants and required imports")
        print("9. Replaced hardcoded usernames/emails and passwords with configurable constants")
        print("10. Added auth token initialization and get_auth_header() method")
        print("11. Replaced hardcoded JWT tokens with dynamic token capture")
        print("12. Added enhanced token capture logic to /auth/session endpoints")
        print("13. Added debug logging for token capture troubleshooting")
        print("14. Fixed Referer URLs to include ?host=app.guidecx.com parameter")
        print("15. Fixed __init__ method to accept environment parameter")
        print("16. Simplified WebSocket methods to avoid asyncio conflicts")
        print("17. Added on_start() method for automatic cookie and token management")
        print("18. Each virtual user now gets their own cookie jar and auth token")
        print()
        print("Benefits:")
        print("- Realistic browser-like cookie behavior") 
        print("- Dynamic authorization token management")
        print("- Automatic session and token management")
        print("- No hardcoded values to maintain")
        print("- Faster test execution (no static asset downloads)")
        print("- Significantly reduced bandwidth usage during load testing")
        print("- Focus on server-side performance testing instead of client assets")
        print("- Cleaner, more maintainable test code with common headers centralized")
        print("- Scales properly with multiple users")
        print("- Tokens are captured fresh for each test run")
    else:
        print("❌ Failed to process file")

if __name__ == "__main__":
    main() 