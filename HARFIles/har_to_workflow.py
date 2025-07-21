#!/usr/bin/env python3
"""
HAR to Workflow Converter

This script takes HAR files or HAR-converted Python files and automatically generates
workflow classes that integrate with our modular architecture.

Features:
- Automatic HAR to Python conversion using har2locust
- Intelligent request grouping and task generation
- Full integration with GuideX modular architecture

Usage:
    python3 HARFiles/har_to_workflow.py <har_file.har|har_file.py> <workflow_name>

Examples:
python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/GlobalProjects.har GlobalProjects
python3 HARFiles/har_to_workflow.py HARFiles/RAW_PY/GlobalProjects.py GlobalProjects

This will generate: workflows/global_projects_user.py
"""

import ast
import re
import sys
import os
import subprocess
import tempfile
from typing import List, Dict, Tuple, Any, Optional
from urllib.parse import urlparse


class HARWorkflowGenerator:
    """Converts HAR files or HAR-converted Python files to modular workflow classes"""
    
    def __init__(self, input_file_path: str, workflow_name: str):
        self.input_file_path = input_file_path
        self.workflow_name = workflow_name
        self.class_name = f"{workflow_name}User"
        self.file_name = self._to_snake_case(workflow_name) + "_user.py"
        self.requests = []
        self.grouped_tasks = {}
        self.temp_python_file = None
        self.keep_python_file = False  # Flag to keep Python files in HARFiles structure
        self.is_har_file = input_file_path.lower().endswith('.har')
        
    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case"""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        
    def _to_method_name(self, description: str) -> str:
        """Convert description to valid Python method name"""
        # Remove special characters and convert to snake_case
        clean = re.sub(r'[^a-zA-Z0-9\s]', '', description)
        words = clean.lower().split()
        return '_'.join(words[:4])  # Limit to 4 words for readability

    def _check_har2locust_available(self) -> bool:
        """Check if har2locust is available in the system"""
        try:
            result = subprocess.run(['har2locust', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def _convert_har_to_python(self) -> str:
        """Convert HAR file to Python using har2locust"""
        if not self.is_har_file:
            return self.input_file_path
            
        print(f"🔄 Converting HAR file to Python using har2locust...")
        
        # Check if har2locust is available
        if not self._check_har2locust_available():
            print("❌ har2locust not found. Please install it:")
            print("   pip install har2locust")
            return None
            
        try:
            # Create organized directory structure for HAR files
            har_files_dir = "HARFiles"
            pyfiles_dir = os.path.join(har_files_dir, "RAW_PY")
            
            # Ensure directories exist
            os.makedirs(har_files_dir, exist_ok=True)
            os.makedirs(pyfiles_dir, exist_ok=True)
            
            # Generate Python file path in organized structure
            base_name = os.path.splitext(os.path.basename(self.input_file_path))[0]
            python_file_path = os.path.join(pyfiles_dir, f"{base_name}.py")
            
            # Run har2locust conversion
            print(f"   • Input HAR: {self.input_file_path}")
            print(f"   • Output Python: {python_file_path}")
            
            with open(python_file_path, 'w') as output_file:
                result = subprocess.run(
                    ['har2locust', self.input_file_path],
                    stdout=output_file,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=30
                )
                
            if result.returncode != 0:
                print(f"❌ har2locust failed: {result.stderr}")
                return None
                
            # Verify the output file was created and has content
            if not os.path.exists(python_file_path) or os.path.getsize(python_file_path) == 0:
                print("❌ har2locust produced no output")
                return None
                
            print("✅ HAR to Python conversion successful")
            print(f"📁 Python file saved: {python_file_path}")
            
            # Keep track of the Python file for reference (don't auto-delete)
            self.temp_python_file = python_file_path
            self.keep_python_file = True  # Flag to indicate this should be kept
            return python_file_path
            
        except subprocess.TimeoutExpired:
            print("❌ har2locust conversion timed out")
            return None
        except Exception as e:
            print(f"❌ Error during HAR conversion: {e}")
            return None

    def _cleanup_temp_files(self):
        """Clean up temporary files created during conversion"""
        # Only clean up if it's a true temporary file, not our organized HARFiles structure
        if (self.temp_python_file and 
            os.path.exists(self.temp_python_file) and 
            not getattr(self, 'keep_python_file', False)):
            try:
                os.remove(self.temp_python_file)
                print(f"🧹 Cleaned up temporary file: {self.temp_python_file}")
            except Exception as e:
                print(f"⚠️ Could not clean up temporary file: {e}")
        elif getattr(self, 'keep_python_file', False):
            print(f"📁 Keeping Python file for reference: {self.temp_python_file}")
        
    def _extract_requests_from_har_file(self, python_file_path: str) -> List[Dict[str, Any]]:
        """Parse HAR-converted Python file and extract request details"""
        try:
            with open(python_file_path, 'r') as f:
                content = f.read()
                
            # Parse the Python AST
            tree = ast.parse(content)
            
            requests = []
            
            # Find the class and its task method
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Find the task method (usually called 't' in HAR conversions)
                    for method in node.body:
                        if isinstance(method, ast.FunctionDef) and method.name in ['t', 'task', 'on_start']:
                            requests.extend(self._extract_requests_from_method(method, content))
                            
            return requests
            
        except Exception as e:
            print(f"Error parsing Python file: {e}")
            return []
    
    def _extract_requests_from_method(self, method_node: ast.FunctionDef, full_content: str) -> List[Dict[str, Any]]:
        """Extract HTTP requests from a method"""
        requests = []
        
        for node in ast.walk(method_node):
            if isinstance(node, ast.With):
                # Look for self.client.request or self.rest calls
                if hasattr(node, 'items') and node.items:
                    for item in node.items:
                        if hasattr(item, 'context_expr') and isinstance(item.context_expr, ast.Call):
                            call = item.context_expr
                            request_info = self._parse_request_call(call, full_content)
                            if request_info:
                                requests.append(request_info)
                                
        return requests
    
    def _parse_request_call(self, call_node: ast.Call, full_content: str) -> Dict[str, Any]:
        """Parse individual request call and extract details"""
        try:
            # Get method and URL
            method = None
            url = None
            headers = {}
            data = None
            
            if hasattr(call_node, 'args') and len(call_node.args) >= 2:
                # First arg is usually method (GET, POST, etc.)
                if isinstance(call_node.args[0], ast.Constant):
                    method = call_node.args[0].value
                # Second arg is usually URL
                if isinstance(call_node.args[1], ast.Constant):
                    url = call_node.args[1].value
                    
            # Extract headers and data from keyword arguments
            if hasattr(call_node, 'keywords'):
                for keyword in call_node.keywords:
                    if keyword.arg == 'headers' and isinstance(keyword.value, ast.Dict):
                        headers = self._extract_dict_from_ast(keyword.value)
                    elif keyword.arg == 'data' and isinstance(keyword.value, ast.Constant):
                        data = keyword.value.value
                        
            if method and url:
                return {
                    'method': method,
                    'url': url,
                    'headers': headers,
                    'data': data,
                    'parsed_url': urlparse(url) if url.startswith('http') else None
                }
                
        except Exception as e:
            print(f"Error parsing request call: {e}")
            
        return None
    
    def _extract_dict_from_ast(self, dict_node: ast.Dict) -> Dict[str, str]:
        """Extract dictionary from AST Dict node"""
        result = {}
        for key, value in zip(dict_node.keys, dict_node.values):
            if isinstance(key, ast.Constant) and isinstance(value, ast.Constant):
                result[key.value] = value.value
        return result
    
    def _group_requests_into_tasks(self, requests: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Group similar requests into logical tasks, filtering out static assets"""
        grouped = {
            'page_load': [],
            'api_calls': [],
            'data_refresh': [],
            'filters': []
        }
        
        assets_filtered = 0
        
        for req in requests:
            url = req['url']
            method = req['method']
            
            # Skip static assets entirely - they don't represent real user load
            if self._is_asset(url, method):
                assets_filtered += 1
                continue
            
            # Categorize meaningful requests
            if self._is_page_load(url, method):
                grouped['page_load'].append(req)
            elif self._is_api_call(url, method):
                grouped['api_calls'].append(req)
            elif self._is_data_refresh(url, method, req.get('data', '')):
                grouped['data_refresh'].append(req)
            elif self._is_filter_request(url, method):
                grouped['filters'].append(req)
            else:
                # Default to API calls
                grouped['api_calls'].append(req)
        
        if assets_filtered > 0:
            print(f"🗑️ Filtered out {assets_filtered} static asset requests (images, fonts, CSS, JS, etc.)")
                
        # Remove empty groups
        return {k: v for k, v in grouped.items() if v}
    
    def _is_page_load(self, url: str, method: str) -> bool:
        """Determine if request is a page load"""
        return (method == 'GET' and 
                ('_rsc=' in url or 'projects' in url or '/v2/' in url) and
                'favicon' not in url and
                not url.endswith('.ico') and
                not self._is_asset(url, method))
    
    def _is_api_call(self, url: str, method: str) -> bool:
        """Determine if request is an API call"""
        return (url.startswith('https://app.') or 
                url.startswith('https://api.') or
                '/auth/' in url or
                '/graphql' in url)
    
    def _is_asset(self, url: str, method: str) -> bool:
        """
        Determine if request is for static assets that should be filtered out.
        These are typically cached by browsers and don't represent real user load.
        """
        if method != 'GET':
            return False
            
        # Common static file extensions
        static_extensions = {
            # Images
            '.ico', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp', '.tiff',
            # Fonts
            '.woff', '.woff2', '.ttf', '.otf', '.eot',
            # Stylesheets & Scripts
            '.css', '.js', '.map',
            # Documents & Media
            '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
            '.mp3', '.mp4', '.wav', '.avi', '.mov', '.wmv',
            # Other assets
            '.zip', '.tar', '.gz', '.rar'
        }
        
        # Check file extension
        url_lower = url.lower()
        for ext in static_extensions:
            if url_lower.endswith(ext):
                return True
                
        # Check for asset-related path patterns
        asset_patterns = [
            'favicon',
            '/static/',
            '/assets/',
            '/css/',
            '/js/',
            '/fonts/',
            '/images/',
            '/img/',
            '/media/',
            '/icons/',
            '/public/',
            '/_next/static/',  # Next.js static assets
            '/__webpack_hmr',  # Webpack hot reload
            '/webpack',
            '/node_modules/',
            '.chunk.',  # Webpack chunks
            '.bundle.',  # Bundled assets
        ]
        
        for pattern in asset_patterns:
            if pattern in url_lower:
                return True
                
        # Check for long random strings (often asset hashes)
        filename = url.split('/')[-1].split('?')[0]  # Remove query params
        if len(filename) > 20 and not '.' in filename[-10:]:  # Long name without extension at end
            return True
            
        # Check for base64 data URLs
        if url.startswith('data:'):
            return True
            
        return False
    
    def _is_data_refresh(self, url: str, method: str, data: str) -> bool:
        """Determine if request is for data refresh"""
        return (method == 'POST' and 
                ('projects' in url or '/v2/' in url) and
                ('Next-Action' in str(data) or '[{' in str(data) or 'refresh' in url))
    
    def _is_filter_request(self, url: str, method: str) -> bool:
        """Determine if request is for loading filters/dropdowns"""
        return ('k2-web' in url and 
                ('Dropdown' in url or 'Load' in url)) or \
               ('filter' in url.lower() or 'dropdown' in url.lower())
    
    def _generate_task_method(self, task_name: str, requests: List[Dict[str, Any]], weight: int, is_first_task: bool = False) -> str:
        """Generate a task method from grouped requests"""
        method_name = self._to_method_name(task_name)
        
        # Create docstring
        docstring = f'"""\n        {task_name.replace("_", " ").title()}\n        Generated from HAR workflow\n        """'
        
        # Generate method body
        method_body = []
        method_body.append(f'    @task(weight={weight})')
        method_body.append(f'    def {method_name}(self):')
        method_body.append(f'        {docstring}')
        method_body.append('        if DEBUG:')
        method_body.append(f'            print("🔄 {task_name.replace("_", " ").title()}...")')
        method_body.append('')
        
        # Add requests
        for i, req in enumerate(requests):
            request_name = f"{task_name}_{i+1}" if len(requests) > 1 else task_name
            is_first_request = (is_first_task and i == 0)
            method_body.extend(self._generate_request_code(req, request_name, is_first_request))
            method_body.append('')
            
        method_body.append('        if DEBUG:')
        method_body.append(f'            print("✅ {task_name.replace("_", " ").title()} completed")')
        
        return '\n'.join(method_body)
    
    def _generate_request_code(self, req: Dict[str, Any], request_name: str, is_first_request: bool = False) -> List[str]:
        """Generate code for a single HTTP request"""
        method = req['method'].lower()
        url = req['url']
        headers = req.get('headers', {})
        data = req.get('data')
        
        # Generate environment-aware URL
        url_var = self._generate_environment_aware_url(url)
            
        # Generate headers dict and check if dynamic extraction is needed
        headers_code, needs_dynamic_action, needs_dynamic_router_state = self._generate_headers_dict(headers, method)
        
        # Generate request code
        code = []
        

        
        # If this request needs dynamic Next-Action, first extract it
        if needs_dynamic_action and method == 'post':
            # Generate code to extract Next-Action ID from current page
            current_page_url = self._get_page_url_for_action(url)
            code.append('        # Extract dynamic Next-Action ID from current page')
            code.append('        next_action_id = None')
            code.append(f'        page_url = f"{current_page_url}"')
            code.append('        with self.client.get(page_url, catch_response=True) as page_resp:')
            code.append('            if page_resp.status_code == 200:')
            code.append('                next_action_id = self.extract_next_action_id(page_resp.text)')
            code.append('                if DEBUG and next_action_id:')
            code.append('                    print(f"✅ Extracted Next-Action ID: {next_action_id}")')
            code.append('            else:')
            code.append('                if DEBUG:')
            code.append('                    print("⚠️ Failed to get current page for Next-Action extraction")')
            code.append('')
            
        # If this request needs dynamic router state, use state from auth base
        if needs_dynamic_router_state:
            code.append('        # Get router state from auth base (captured during login)')
            code.append('        router_state_tree = self.get_current_router_state()')
            code.append('        if DEBUG and router_state_tree:')
            code.append('            print(f"✅ Using router state from auth (length: {len(router_state_tree)})")')
            code.append('        elif DEBUG:')
            code.append('            print("⚠️ No router state available from auth")')
            code.append('')
            
        code.append(f'        with self.client.{method}(')
        code.append(f'            {url_var},')
        
        if headers_code:
            code.append(f'            headers={headers_code},')
            
        if data:
            if isinstance(data, str):
                code.append(f'            data={repr(data)},')
            else:
                code.append(f'            data={data},')
                
        code.append('            catch_response=True,')
        code.append(f'            name="{request_name.replace("_", " ").title()}"')
        code.append('        ) as resp:')
        code.append('            if resp.status_code == 200:')
        code.append('                if DEBUG:')
        code.append(f'                    print("✅ {request_name.replace("_", " ").title()} successful")')
        code.append('            else:')
        code.append('                if DEBUG:')
        code.append(f'                    print(f"❌ {request_name.replace("_", " ").title()} failed: {{resp.status_code}}")')
        
        return code
    
    def _get_page_url_for_action(self, post_url: str) -> str:
        """Determine the page URL to GET for extracting Next-Action ID"""
        # For project-related actions, get the projects page
        if '/v2/projects' in post_url or 'projects' in post_url:
            return "https://arches.{DOMAIN_SUFFIX}/v2/projects"
        
        # For other actions, try to infer the base page
        parsed = urlparse(post_url)
        if parsed.path:
            # Remove the last segment to get the parent page
            path_parts = parsed.path.strip('/').split('/')
            if len(path_parts) > 1:
                parent_path = '/'.join(path_parts[:-1])
                return f"https://arches.{{DOMAIN_SUFFIX}}/{parent_path}"
        
        # Default fallback
        return "https://arches.{DOMAIN_SUFFIX}/v2/projects"
    
    def _generate_environment_aware_url(self, url: str) -> str:
        """Convert absolute URLs to environment-aware template variables using DOMAIN_SUFFIX"""
        if not url.startswith('https://'):
            # Relative URL - keep as-is
            return f'"{url}"'
            
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        path = parsed.path
        query = f"?{parsed.query}" if parsed.query else ""
        fragment = f"#{parsed.fragment}" if parsed.fragment else ""
        
        # Check if this looks like a GuideX domain (has a subdomain pattern)
        if ('.' in domain and 
            (domain.endswith('.guidecx.com') or 
             domain.endswith('.guidecx.io') or 
             'guidecx' in domain)):
            
            # Extract the subdomain (everything before the first dot)
            subdomain = domain.split('.')[0]
            return f'f"https://{subdomain}.{{DOMAIN_SUFFIX}}{path}{query}{fragment}"'
        else:
            # External domain - keep as absolute URL but add a comment
            return f'"{url}"  # External URL - not environment-aware'
    
    def _generate_environment_aware_host(self, host: str) -> str:
        """Convert host headers to use environment-aware domain variables using DOMAIN_SUFFIX"""
        host_lower = host.lower()
        
        # Check if this looks like a GuideX domain
        if ('.' in host_lower and 
            (host_lower.endswith('.guidecx.com') or 
             host_lower.endswith('.guidecx.io') or 
             'guidecx' in host_lower)):
            
            # Extract the subdomain (everything before the first dot)
            subdomain = host_lower.split('.')[0]
            return f"{subdomain}.{{DOMAIN_SUFFIX}}"
        else:
            # External host - keep as-is
            return host
    
    def _generate_environment_aware_url_string(self, url: str) -> str:
        """Convert URL strings to environment-aware variables (for headers like Origin/Referer) using DOMAIN_SUFFIX"""
        if not url.startswith('https://'):
            return url
            
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Check if this looks like a GuideX domain
        if ('.' in domain and 
            (domain.endswith('.guidecx.com') or 
             domain.endswith('.guidecx.io') or 
             'guidecx' in domain)):
            
            # Extract the subdomain (everything before the first dot)
            subdomain = domain.split('.')[0]
            return f"https://{subdomain}.{{DOMAIN_SUFFIX}}"
        else:
            # External domain - keep as-is
            return url
    
    def _generate_environment_aware_router_tree(self, router_tree: str) -> str:
        """Convert Next-Router-State-Tree to use environment-aware URLs"""
        import urllib.parse
        
        try:
            # URL decode the router state tree
            decoded = urllib.parse.unquote(router_tree)
            
            # Replace common URL patterns with environment-aware equivalents
            # For server actions, keep relative URLs to avoid authorization issues
            replacements = {
                # Only replace if it's not already a full URL
                '"/v2/projects"': '"/v2/projects"',  # Keep relative for server actions
                '"/tasks"': '"/tasks"',  # Keep relative for server actions  
                '"/v2/"': '"/v2/"',  # Keep relative for server actions
                '"/projects"': '"/projects"',  # Keep relative for server actions
            }
            
            # Apply replacements
            updated = decoded
            for old_pattern, new_pattern in replacements.items():
                updated = updated.replace(old_pattern, new_pattern)
                
            # Fix common action type issues that cause 405 errors
            # Server actions require specific action types to be authorized
            updated = updated.replace('"refetch"', '"refresh"')  # Server expects 'refresh' not 'refetch'
            
            # If changes were made, return as template that needs f-string formatting  
            if updated != decoded:
                # URL encode the result and return as template
                encoded = urllib.parse.quote(updated, safe='')
                return f"{encoded}"  # This will be handled as template
            else:
                # No changes needed, return original
                return router_tree
                
        except Exception as e:
            # If processing fails, return original value
            print(f"⚠️ Could not process router tree: {e}")
            return router_tree
    
    def _generate_headers_dict(self, headers: Dict[str, str], method: str) -> Tuple[str, bool, bool]:
        """Generate Python dict code for headers, return (headers_code, needs_dynamic_action, needs_dynamic_router_state)"""
        if not headers:
            return None, False, False
            
        # Check if this request needs dynamic Next-Action extraction
        has_next_action = any(key.lower() == 'next-action' for key in headers.keys())
        
        # Check if this request needs dynamic router state extraction 
        # Use fresh router state from auth base for all requests with router state
        has_router_state = any(key.lower() == 'next-router-state-tree' for key in headers.keys())
            
        # Filter out session-specific headers that should be dynamic
        filtered_headers = {}
        for key, value in headers.items():
            if key.lower() not in ['cookie', 'authorization', 'content-length']:
                # Replace hard-coded Next-Action with dynamic extraction
                if key.lower() == 'next-action':
                    filtered_headers[key] = "{next_action_id}"  # Template for replacement
                elif key.lower() == 'next-router-state-tree':
                    # All requests use dynamic router state from auth base
                    filtered_headers[key] = "{router_state_tree}"
                elif key.lower() == 'host':
                    # Make host headers environment-aware
                    filtered_headers[key] = self._generate_environment_aware_host(value)
                elif key.lower() in ['origin', 'referer']:
                    # Make origin and referer headers environment-aware
                    filtered_headers[key] = self._generate_environment_aware_url_string(value)
                else:
                    filtered_headers[key] = value
                
        if not filtered_headers:
            return None, has_next_action
            
        # Format as Python dict with template replacement for dynamic values
        items = []
        for key, value in filtered_headers.items():
            if key.lower() == 'next-action':
                items.append(f'                "{key}": next_action_id')
            elif key.lower() == 'next-router-state-tree':
                if '{router_state_tree}' in str(value):
                    items.append(f'                "{key}": router_state_tree')
                else:
                    # Static router state with potential f-string formatting
                    if '{DOMAIN_SUFFIX}' in str(value) or '%7BDOMAIN_SUFFIX%7D' in str(value):
                        items.append(f'                "{key}": f"{value}"')
                    else:
                        items.append(f'                "{key}": "{value}"')
            elif '{DOMAIN_SUFFIX}' in str(value) or '%7BDOMAIN_SUFFIX%7D' in str(value):
                # Header with DOMAIN_SUFFIX template (literal or URL-encoded) - needs f-string
                items.append(f'                "{key}": f"{value}"')
            else:
                items.append(f'                "{key}": "{value}"')
            
        headers_code = '{\n' + ',\n'.join(items) + '\n            }'
        return headers_code, has_next_action, has_router_state
    
    def _generate_workflow_class(self) -> str:
        """Generate the complete workflow class"""
        template = f'''#!/usr/bin/env python3
"""
{self.workflow_name} User - Auto-generated from HAR file
Converted from HAR file and integrated into modular architecture
"""

from locust import task
from auth.base_user import AuthenticatedUser
from auth.config import (
    DOMAIN_SUFFIX, DEBUG
)


class {self.class_name}(AuthenticatedUser):
    """
    User focused on {self.workflow_name.lower()} activities.
    Auto-generated from HAR workflow for authentic interactions.
    """
    
    # Use arches subdomain as host (adjust if needed)
    host = f"https://arches.{{DOMAIN_SUFFIX}}"
    
    # Relative weight when multiple user classes exist
    weight = 2

{{task_methods}}

    def on_start(self):
        """
        Override to ensure we're properly authenticated before starting tasks
        """
        # Call parent on_start to handle login
        super().on_start()
        
        if DEBUG:
            print("🚀 {self.class_name} initialized and authenticated")
            print(f"   • Host: {{self.host}}")
            print(f"   • Domain Suffix: {{DOMAIN_SUFFIX}}")
'''

        # Generate task methods
        task_methods = []
        weights = {'page_load': 3, 'filters': 2, 'data_refresh': 4, 'api_calls': 2}
        
        # Determine task order for router state optimization
        task_order = ['page_load', 'api_calls', 'data_refresh', 'filters']
        ordered_tasks = []
        for task_name in task_order:
            if task_name in self.grouped_tasks and self.grouped_tasks[task_name]:
                ordered_tasks.append(task_name)
        # Add any remaining tasks not in the standard order
        for task_name in self.grouped_tasks:
            if task_name not in ordered_tasks and self.grouped_tasks[task_name]:
                ordered_tasks.append(task_name)
        
        for i, task_name in enumerate(ordered_tasks):
            requests = self.grouped_tasks[task_name]
            if requests:  # Only generate if there are requests
                weight = weights.get(task_name, 2)
                is_first_task = (i == 0)
                method_code = self._generate_task_method(task_name, requests, weight, is_first_task)
                task_methods.append(method_code)
        
        return template.replace('{task_methods}', '\n\n'.join(task_methods))
    
    def generate(self) -> str:
        """Main method to generate the workflow class"""
        try:
            # Step 1: Convert HAR to Python if needed
            if self.is_har_file:
                print(f"📁 Input: HAR file ({self.input_file_path})")
                python_file_path = self._convert_har_to_python()
                if not python_file_path:
                    return None
            else:
                print(f"📁 Input: Python file ({self.input_file_path})")
                python_file_path = self.input_file_path
            
            # Step 2: Parse the Python file for requests
            print(f"🔄 Parsing Python file: {python_file_path}")
            self.requests = self._extract_requests_from_har_file(python_file_path)
            print(f"📊 Found {len(self.requests)} requests")
            
            if not self.requests:
                print("❌ No requests found in file")
                return None
                
            # Step 3: Group requests into logical tasks
            self.grouped_tasks = self._group_requests_into_tasks(self.requests)
            print(f"📁 Grouped into {len(self.grouped_tasks)} task categories:")
            for task_name, requests in self.grouped_tasks.items():
                print(f"   • {task_name}: {len(requests)} requests")
            
            # Step 4: Generate the workflow class
            print(f"🏗️ Generating {self.class_name}...")
            workflow_code = self._generate_workflow_class()
            
            return workflow_code
            
        finally:
            # Always clean up temp files
            self._cleanup_temp_files()
    
    def save_to_file(self, output_dir: str = "workflows") -> str:
        """Generate and save the workflow to a file"""
        workflow_code = self.generate()
        
        if not workflow_code:
            return None
            
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to file
        output_path = os.path.join(output_dir, self.file_name)
        with open(output_path, 'w') as f:
            f.write(workflow_code)
            
        print(f"✅ Generated workflow saved to: {output_path}")
        return output_path


def show_help():
    """Show help information"""
    help_text = """
🤖 HAR to Workflow Converter

Automatically converts HAR files or HAR-converted Python files into GuideX load testing workflows.

USAGE:
    python3 utils/har_to_workflow.py <input_file> <workflow_name>

INPUT FORMATS:
    • .har files (automatically converted using har2locust)  
    • .py files (already converted from HAR)

EXAMPLES:
    # Convert directly from HAR file (recommended)
    python3 utils/har_to_workflow.py GlobalProjects.har GlobalProjects
    
    # Convert from existing Python file
    python3 utils/har_to_workflow.py HARFiles/pyfiles/GlobalProjects.py GlobalProjects
    
    # Convert user management workflow
    python3 utils/har_to_workflow.py UserManagement.har UserManagement

REQUIREMENTS:
    • har2locust (for .har files): pip install har2locust
    • locust: pip install locust
    
OUTPUT:
    • workflows/{workflow_name}_user.py
    • Ready-to-use Locust workflow class
    
NEXT STEPS:
    1. Add import to guidex_loadtest.py
    2. Test: locust -f guidex_loadtest.py YourWorkflowUser --headless --users=5
    
For more information, see: utils/README_HAR_CONVERTER.md
"""
    print(help_text)


def main():
    """Command line interface"""
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help', 'help']):
        show_help()
        sys.exit(0)
        
    if len(sys.argv) != 3:
        print("❌ Invalid arguments")
        show_help()
        sys.exit(1)
        
    input_file_path = sys.argv[1]
    workflow_name = sys.argv[2]
    
    # Validate input file
    if not os.path.exists(input_file_path):
        print(f"❌ Input file not found: {input_file_path}")
        sys.exit(1)
        
    # Validate file extension
    file_ext = os.path.splitext(input_file_path)[1].lower()
    if file_ext not in ['.har', '.py']:
        print(f"❌ Unsupported file type: {file_ext}")
        print("   Supported formats: .har, .py")
        sys.exit(1)
        
    # Generate the workflow
    print(f"🚀 Starting HAR to Workflow conversion...")
    print(f"   • Input: {input_file_path}")
    print(f"   • Workflow: {workflow_name}")
    print("")
    
    generator = HARWorkflowGenerator(input_file_path, workflow_name)
    output_path = generator.save_to_file()
    
    if output_path:
        python_file_info = ""
        if generator.is_har_file and hasattr(generator, 'temp_python_file'):
            python_file_info = f"Python conversion: {generator.temp_python_file}\n"
        
        print(f"""
🎉 HAR to Workflow Conversion Complete!

📁 File Organization:
{python_file_info}Generated workflow: {output_path}

📊 Directory Structure:
   HARFiles/
   ├── RAW_HAR/          # Original HAR files  
   ├── RAW_PY/           # HAR→Python conversions
   │   └── {os.path.basename(generator.temp_python_file) if hasattr(generator, 'temp_python_file') else 'YourFile.py'}
   │
   workflows/             # Generated workflow classes  
   └── {os.path.basename(output_path)}

Next steps:
1. Review the generated workflow file
2. Adjust weights and task logic if needed
3. Add to guidex_loadtest.py:
   from workflows.{generator._to_snake_case(workflow_name)}_user import {generator.class_name}
   __all__ = [..., '{generator.class_name}']

4. Test the workflow:
   locust -f guidex_loadtest.py {generator.class_name} --headless --users=5 --spawn-rate=1 --run-time=30s

📖 For more details, see: utils/README_HAR_CONVERTER.md
""")
    else:
        print("❌ Failed to generate workflow")
        sys.exit(1)


if __name__ == "__main__":
    main() 