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
    
    def __init__(self, input_file_path: str, workflow_name: str, subdirectory: str = None):
        self.input_file_path = input_file_path
        self.workflow_name = workflow_name
        self.subdirectory = subdirectory
        self.class_name = f"{workflow_name}User"
        self.file_name = f"{workflow_name}.py"
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
        server_actions_filtered = 0
        prefetch_filtered = 0
        external_services_filtered = 0
        
        for req in requests:
            url = req['url']
            method = req['method']
            headers = req.get('headers', {})
            data = req.get('data', '')
            
            # Skip static assets entirely - they don't represent real user load
            if self._is_asset(url, method):
                assets_filtered += 1
                continue
            
            # Skip Next.js server actions - they're often session-specific and cause 405 errors
            if self._is_server_action(url, method, headers, data):
                server_actions_filtered += 1
                continue
            
            # Skip problematic Next.js router prefetch requests - these often cause 404/500 errors
            if self._is_problematic_prefetch(url, method, headers):
                prefetch_filtered += 1
                continue
            
            # Skip external services that aren't core to application functionality
            if self._is_external_service(url, method):
                external_services_filtered += 1
                continue

            
            # Categorize meaningful requests
            if self._is_page_load(url, method, headers):
                grouped['page_load'].append(req)
            elif self._is_api_call(url, method):
                grouped['api_calls'].append(req)
            elif self._is_data_refresh(url, method, data):
                grouped['data_refresh'].append(req)
            elif self._is_filter_request(url, method):
                grouped['filters'].append(req)
            else:
                # Default to API calls
                grouped['api_calls'].append(req)
        
        if assets_filtered > 0:
            print(f"🗑️ Filtered out {assets_filtered} static asset requests (images, fonts, CSS, JS, etc.)")
        
        if server_actions_filtered > 0:
            print(f"🔒 Filtered out {server_actions_filtered} Next.js server actions (session-specific, cause 405 errors)")
        
        if prefetch_filtered > 0:
            print(f"🚫 Filtered out {prefetch_filtered} problematic router prefetch requests (often cause 404/500 errors)")
        
        if external_services_filtered > 0:
            print(f"🌐 Filtered out {external_services_filtered} external/analytics requests (non-guidecx domains + analytics endpoints)")
                
        # Remove empty groups
        return {k: v for k, v in grouped.items() if v}
    
    def _is_page_load(self, url: str, method: str, headers: Dict[str, str] = None) -> bool:
        """Determine if request is a genuine page load (not a prefetch)"""
        if method != 'GET':
            return False
            
        # Exclude assets and favicons
        if self._is_asset(url, method) or 'favicon' in url or url.endswith('.ico'):
            return False
            
        # If we have headers, check if this is a prefetch (which is not a real page load)
        if headers:
            has_prefetch_header = any(key.lower() == 'next-router-prefetch' for key in headers.keys())
            if has_prefetch_header:
                return False
        
        # Core page load patterns that represent real user navigation
        return (
            ('_rsc=' in url and ('projects' in url or '/v2/' in url)) or  # React Server Components for core pages
            (url.endswith('/v2/projects')) or  # Main projects page
            ('/project/' in url and '/plan' in url) or  # Individual project plans
            ('/project/' in url and '/team' in url) or  # Project team pages
            ('/project/' in url and '/messages' in url)  # Project messages
        )
    
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
    
    def _is_server_action(self, url: str, method: str, headers: Dict[str, str], data: str) -> bool:
        """Determine if request is a Next.js server action that should be filtered out"""
        return (method == 'POST' and 
                any(key.lower() == 'next-action' for key in headers.keys()) and
                ('projects' in url or '/v2/' in url))
    
    def _is_problematic_prefetch(self, url: str, method: str, headers: Dict[str, str]) -> bool:
        """
        Determine if request is a problematic Next.js router prefetch that should be filtered out.
        These requests often cause 404/500 errors in load testing environments.
        """
        if method != 'GET':
            return False
            
        # Check for Next.js router prefetch header
        has_prefetch_header = any(key.lower() == 'next-router-prefetch' for key in headers.keys())
        
        if not has_prefetch_header:
            return False
            
        # List of route patterns that are known to cause issues in load testing
        problematic_routes = [
            '/app/support',        # Support page - often 404 in load testing
            '/app/notifications',  # Notifications page - often 404 in load testing  
            '/messaging',          # Messaging page - often 500 in load testing
            '/app/help',           # Help pages
            '/app/settings',       # Settings pages
            '/app/profile',        # Profile pages
            '/admin/',             # Admin routes
            '/support/',           # Support routes
            '/help/',              # Help routes
        ]
        
        # Check if URL contains any problematic route patterns
        url_lower = url.lower()
        for route in problematic_routes:
            if route in url_lower:
                return True
                
        # Also filter prefetch requests to routes that are not core functionality
        # These are typically navigation preloads that don't represent real user actions
        non_core_patterns = [
            '/app/',               # App subdirectory routes (not main app functionality)
            '/static/',            # Static content prefetches
            '/public/',            # Public content prefetches
        ]
        
        for pattern in non_core_patterns:
            if pattern in url_lower and '/app/project' not in url_lower and '/v2/' not in url_lower:
                return True
                
        return False
    
    def _is_external_service(self, url: str, method: str) -> bool:
        """
        Determine if request is to external services that should be filtered out.
        Filter out ALL non-guidecx domains completely, just like static assets.
        """
        # For relative URLs, assume they're internal guidecx requests
        if not url.startswith('https://') and not url.startswith('http://'):
            return False
        
        # Parse the URL to get the domain
        from urllib.parse import urlparse
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Keep only domains that contain 'guidecx'
            if 'guidecx' in domain:
                # Filter out specific analytics endpoints that require special authentication
                # These typically require API keys that aren't available in load testing
                if 'api.' in domain and '/query?query=' in url and 'dimensions' in url:
                    return True  # Filter out analytics query endpoints
                return False  # Keep all other guidecx domains
            else:
                return True   # Filter out all external domains
                
        except Exception:
            # If URL parsing fails, assume it's external and filter it out
            return True
    

    def _is_data_refresh(self, url: str, method: str, data: str) -> bool:
        """Determine if request is for data refresh (excluding server actions)"""
        return (method == 'POST' and 
                ('projects' in url or '/v2/' in url) and
                ('Next-Action' not in str(data)) and  # Exclude server actions
                ('[{' in str(data) or 'refresh' in url))
    
    def _is_filter_request(self, url: str, method: str) -> bool:
        """Determine if request is for loading filters/dropdowns"""
        return ('k2-web' in url and 
                ('Dropdown' in url or 'Load' in url)) or \
               ('filter' in url.lower() or 'dropdown' in url.lower())
    
    def _make_project_ids_configurable(self, url_or_path: str) -> str:
        """
        Replace hard-coded UUIDs with CSV-driven template variables.
        This allows the same workflow to work with CSV data for realistic load testing.
        """
        import re
        
        # Keep track of what parameters we've found
        if not hasattr(self, '_csv_parameters'):
            self._csv_parameters = set()
        
        result = url_or_path
        
        # Replace project UUIDs with CSV template variable
        uuid_pattern = r'/project/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(uuid_pattern, result):
            result = re.sub(uuid_pattern, r'/project/{projectID}', result)
            self._csv_parameters.add('projectID')
        
        # Replace phase UUIDs in query parameters  
        phase_pattern = r'([?&])phase=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(phase_pattern, result):
            result = re.sub(phase_pattern, r'\1phase={phaseID}', result)
            self._csv_parameters.add('phaseID')
            
        # Replace milestone UUIDs in query parameters (standard format)
        milestone_pattern = r'([?&])milestone=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(milestone_pattern, result):
            result = re.sub(milestone_pattern, r'\1milestone={milestoneID}', result)
            self._csv_parameters.add('milestoneID')
            
        # Replace milestone UUIDs in query parameters (hyphenated format)
        milestone_id_pattern = r'([?&])milestone-id=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(milestone_id_pattern, result):
            result = re.sub(milestone_id_pattern, r'\1milestone-id={milestoneID}', result)
            self._csv_parameters.add('milestoneID')
            
        # Replace task UUIDs in query parameters (standard format)
        task_query_pattern = r'([?&])task=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(task_query_pattern, result):
            result = re.sub(task_query_pattern, r'\1task={taskID}', result)
            self._csv_parameters.add('taskID')
            
        # Replace task UUIDs in query parameters (hyphenated format)
        task_id_pattern = r'([?&])task-id=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(task_id_pattern, result):
            result = re.sub(task_id_pattern, r'\1task-id={taskID}', result)
            self._csv_parameters.add('taskID')
            
        # Replace task UUIDs in path segments (e.g., /task/uuid or /tasks/uuid)
        task_path_pattern = r'/tasks?/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(task_path_pattern, result):
            result = re.sub(task_path_pattern, r'/task/{taskID}', result)
            self._csv_parameters.add('taskID')
            
        # Replace messageId UUIDs in query parameters  
        message_id_pattern = r'([?&])messageId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(message_id_pattern, result):
            result = re.sub(message_id_pattern, r'\1messageId={messageID}', result)
            self._csv_parameters.add('messageID')
            
        # Replace channelId UUIDs in query parameters
        channel_id_pattern = r'([?&])channelId=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})'
        if re.search(channel_id_pattern, result):
            result = re.sub(channel_id_pattern, r'\1channelId={channelID}', result)
            self._csv_parameters.add('channelID')
        
        return result
    
    def _generate_project_id_config(self) -> str:
        """Generate configuration section for CSV-driven parameters"""
        
        config_lines = []
        config_lines.append("# CSV Data Loading")
        config_lines.append('CSV_FILE_PATH = os.getenv("TEST_DATA_CSV", "config/test_data_staging.csv")')
        config_lines.append("")
        config_lines.append("def load_test_data():")
        config_lines.append('    """Load test data from CSV file and filter for guidecx domains only"""')
        config_lines.append("    try:")
        config_lines.append("        # Adjust path relative to where Locust is run from")
        config_lines.append("        if not os.path.isabs(CSV_FILE_PATH):")
        config_lines.append("            # For standalone files, adjust relative to project root")
        config_lines.append("            if 'workflows/' in __file__:")
        config_lines.append("                # Calculate project root from workflow file location")
        config_lines.append("                project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))")
        config_lines.append("                csv_path = os.path.join(project_root, CSV_FILE_PATH)")
        config_lines.append("            else:")
        config_lines.append("                csv_path = CSV_FILE_PATH")
        config_lines.append("        else:")
        config_lines.append("            csv_path = CSV_FILE_PATH")
        config_lines.append("            ")
        config_lines.append("        with open(csv_path, 'r') as f:")
        config_lines.append("            reader = csv.DictReader(f)")
        config_lines.append("            all_data = list(reader)")
        config_lines.append("            if not all_data:")
        config_lines.append('                raise ValueError("CSV file is empty")')
        config_lines.append("            ")
        config_lines.append("            # Filter to only include domains that contain 'guidecx'")
        config_lines.append("            filtered_data = []")
        config_lines.append("            for row in all_data:")
        config_lines.append("                domain = row.get('domain', '')")
        config_lines.append("                if 'guidecx' in domain.lower():")
        config_lines.append("                    # Update domain to use the configured DOMAIN_SUFFIX")
        config_lines.append("                    row['domain'] = DOMAIN_SUFFIX")
        config_lines.append("                    filtered_data.append(row)")
        config_lines.append("                else:")
        config_lines.append("                    if DEBUG:")
        config_lines.append("                        print(f'Filtering out domain: {domain} (does not contain \"guidecx\")')")
        config_lines.append("            ")
        config_lines.append("            if not filtered_data:")
        config_lines.append('                raise ValueError("No domains containing \'guidecx\' found in CSV data")')
        config_lines.append("                ")
        config_lines.append("            if DEBUG:")
        config_lines.append("                print(f'Loaded {len(filtered_data)} rows with guidecx domains (filtered from {len(all_data)} total)')")
        config_lines.append("                ")
        config_lines.append("            return filtered_data")
        config_lines.append("    except FileNotFoundError:")
        config_lines.append(f'        print(f"\\n❌ CSV file not found: {{CSV_FILE_PATH}}")')
        
        # Show detected parameters
        if hasattr(self, '_csv_parameters') and self._csv_parameters:
            params_list = sorted(list(self._csv_parameters))
            standard_columns = ['domain', 'login_email', 'login_password']
            all_columns = standard_columns + params_list
        else:
            # Default columns when no parameters detected
            all_columns = ['domain', 'login_email', 'login_password']
        
        config_lines.append('        print("\\n📝 Create environment-specific CSV files in config/ directory:")')
        config_lines.append('        print("\\n🟡 STAGING: config/test_data_staging.csv")')
        config_lines.append(f'        print("   {",".join(all_columns)}")')
        config_lines.append('        print("   staging.guidecx.io,stage_user1@test.com,stage_pass")')
        config_lines.append('        print("\\n🔴 PRODUCTION: config/test_data_production.csv")')
        config_lines.append(f'        print("   {",".join(all_columns)}")')
        config_lines.append('        print("   production.guidecx.com,prod_user1@company.com,prod_pass")')
        config_lines.append('        print("\\n🔧 Usage:")')
        config_lines.append('        print("   export TEST_DATA_CSV=config/test_data_staging.csv")')
        config_lines.append('        print("   locust -f <this_file> --users=5")')
        config_lines.append('        raise')
        config_lines.append("    except Exception as e:")
        config_lines.append(f'        print(f"\\n❌ Error loading CSV file: {{e}}")')
        config_lines.append("        raise")
        config_lines.append("")
        
        config_lines.append("# Load all test data at startup")
        config_lines.append("TEST_DATA = load_test_data()")
        config_lines.append(f'print(f"✅ Loaded {{len(TEST_DATA)}} test data rows from {{CSV_FILE_PATH}}")')
        
        return "\n".join(config_lines)
    
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
        """Generate code for a single HTTP request using common.auth.AuthenticatedUser methods"""
        method = req['method'].lower()
        url = req['url']
        headers = req.get('headers', {})
        data = req.get('data')
        
        # Check if this is a guidecx domain or external domain
        is_guidecx_domain = False
        subdomain = 'app'  # default subdomain for guidecx domains
        path = url
        
        # Determine if this is a guidecx domain
        host_header = headers.get('Host', '')
        if host_header and 'guidecx' in host_header.lower():
            is_guidecx_domain = True
            subdomain = host_header.split('.')[0].lower()
            # For host header case, path is the original url (might be relative)
            if not url.startswith('https://'):
                path = self._filter_session_parameters(url)
            else:
                # Extract path from absolute URL
                from urllib.parse import urlparse
                parsed = urlparse(url)
                path = parsed.path
                if parsed.query:
                    path += f"?{parsed.query}"
        elif url.startswith('https://') and 'guidecx' in url.lower():
            is_guidecx_domain = True
            from urllib.parse import urlparse
            parsed = urlparse(url)
            path = parsed.path
            if parsed.query:
                path += f"?{parsed.query}"
            if parsed.netloc and '.' in parsed.netloc:
                subdomain = parsed.netloc.split('.')[0].lower()
        elif not url.startswith('https://'):
            # Relative URL - assume it's for guidecx domain
            is_guidecx_domain = True
            path = self._filter_session_parameters(url)
        
        # Ensure path is actually a path and not a full URL
        if is_guidecx_domain and path.startswith('https://'):
            # If path still contains full URL, extract just the path portion
            from urllib.parse import urlparse
            parsed = urlparse(path)
            path = parsed.path
            if parsed.query:
                path += f"?{parsed.query}"
        
        # Generate headers dict and check if dynamic extraction is needed
        headers_code, needs_dynamic_action = self._generate_headers_dict(headers, method)
        
        # For guidecx domains, remove Host header since we'll build the full URL
        if is_guidecx_domain and headers_code and '"Host"' in headers_code:
            lines = headers_code.split('\n')
            filtered_lines = [line for line in lines if '"Host"' not in line]
            headers_code = '\n'.join(filtered_lines)
            headers_code = headers_code.replace(',\n            }', '\n            }')
        
        # Generate request code
        code = []
        
        if is_guidecx_domain:
            # GuideX domain - use standard Locust client with proper headers
            path = self._make_project_ids_configurable(path)
            
            # Check if we need Next-Action extraction for this request
            if needs_dynamic_action:
                # Add Next-Action extraction logic
                code.append('        # Extract Next-Action ID for this request')
                code.append('        next_action_id = None')
                code.append('        try:')
                code.append('            # Get the current page to extract Next-Action ID')
                code.append('            with self.client.get("/", catch_response=True, name="extract_next_action") as page_resp:')
                code.append('                if page_resp.status_code == 200:')
                code.append('                    next_action_id = self.extract_next_action_id(page_resp.text)')
                code.append('                    if DEBUG and next_action_id:')
                code.append('                        print(f"✅ Extracted Next-Action ID: {next_action_id}")')
                code.append('        except Exception as e:')
                code.append('            if DEBUG:')
                code.append('                print(f"⚠️ Failed to extract Next-Action ID: {e}")')
                code.append('')
            
            # Determine if we need to use CSV template variables in the path
            has_csv_vars = '{' in path and '}' in path
            if has_csv_vars:
                path_var = f'"{path}".format(**self.test_data)'
            else:
                path_var = f'"{path}"'
            
            # Build the full URL or use relative path
            if subdomain != 'app':
                # For non-app subdomains, use full URL
                url_code = f'f"https://{subdomain}.{{self.api_domain}}{{{path_var}}}"'
            else:
                # For app subdomain, can use relative path
                url_code = path_var
                
            # Merge authentication headers with request headers
            code.append('        # Get authenticated headers')
            code.append('        auth_headers = self.get_auth_headers()')
            
            if headers_code and headers_code.strip() not in ['{}', '{\n            }']:
                code.append(f'        request_headers = {headers_code}')
                code.append('        auth_headers.update(request_headers)')
            
            # Use standard Locust client methods
            code.append(f'        with self.client.{method}(')
            code.append(f'            {url_code},')
            code.append('            headers=auth_headers,')
            
            if data:
                if isinstance(data, str):
                    code.append(f'            data={repr(data)},')
                else:
                    code.append(f'            data={data},')
                    
            code.append('            catch_response=True,')
            code.append(f'            name="{request_name}"')
            code.append('        ) as resp:')
        else:
            # External domain detected - this should not happen as all external domains are filtered out
            print(f"⚠️ WARNING: External domain request found: {url}")
            print("   This should have been filtered out by _is_external_service()")
            print("   Skipping this request to avoid external domain calls")
            
            # Return empty code block - effectively skips this request
            code.append('        # External domain request skipped (filtered out)')
            code.append('        if DEBUG:')
            code.append(f'            print("⚠️ Skipped external domain request: {url[:50]}...")')
            
            # Add a pass statement to make the generated code valid
            code.append('        pass')
        
        # Only add response handling for actual HTTP requests (guidecx domains)
        if is_guidecx_domain:
            # Common response handling
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
    
    def _filter_session_parameters(self, url: str) -> str:
        """
        Remove session-specific query parameters that become invalid after recording.
        These parameters are tied to specific sessions and cause 404/500 errors when reused.
        """
        if '?' not in url:
            return url
            
        # Split URL and query parameters
        base_url, query_string = url.split('?', 1)
        
        # Parse query parameters
        from urllib.parse import parse_qs, urlencode
        params = parse_qs(query_string)
        
        # Remove session-specific parameters
        session_params_to_remove = [
            '_rsc',           # React Server Component identifiers
            '_next_action',   # Next.js action IDs
            'session_id',     # Session identifiers
            'timestamp',      # Time-based parameters
            'nonce',          # One-time use tokens
            'csrf_token',     # CSRF tokens
            'cachebuster',    # Cache busting parameters
        ]
        
        filtered_params = {}
        removed_params = []
        
        for key, values in params.items():
            if key.lower() not in session_params_to_remove:
                filtered_params[key] = values
            else:
                removed_params.append(f"{key}={values[0] if values else ''}")
        
        # Log what was filtered for debugging
        if removed_params:
            print(f"🧹 Filtered session parameters: {', '.join(removed_params)}")
        
        # Rebuild URL
        if filtered_params:
            # Convert back to query string format
            clean_query = urlencode(filtered_params, doseq=True)
            return f"{base_url}?{clean_query}"
        else:
            return base_url
    
    def _normalize_subdomain(self, subdomain: str) -> str:
        """
        Normalize known subdomains to the correct ones for the current environment.
        This handles cases where HAR files contain legacy or environment-specific subdomains.
        """
        # Map known subdomains to the correct ones
        subdomain_mapping = {
            'app': 'app',             # Keep app as-is
            'arches': 'arches',       # Keep arches as-is (auth system)
            'api': 'api',             # Keep api as-is
            'k2-web': 'k2-web',       # Keep k2-web as-is (gRPC services)
            'thundercats': 'thundercats',  # Keep thundercats as-is (specific app instance)
        }
        
        # If it's a known subdomain, use the mapping, otherwise keep original
        normalized = subdomain_mapping.get(subdomain.lower(), subdomain)
        if normalized != subdomain and subdomain.lower() in subdomain_mapping:
            print(f"🔧 Normalized subdomain: {subdomain} → {normalized}")
        
        return normalized
    
    def _generate_environment_aware_url(self, url: str) -> str:
        """Convert absolute URLs to environment-aware template variables using CSV domain data"""
        if not url.startswith('https://'):
            # Relative URL - filter session parameters and make configurable
            filtered_url = self._filter_session_parameters(url)
            configurable_url = self._make_project_ids_configurable(filtered_url)
            if configurable_url != filtered_url:
                # URL contains CSV template variables, use .format() (avoid f-string conflicts)
                return f'"{configurable_url}".format(**self.test_data)'
            return f'"{filtered_url}"'
            
        # Filter session parameters first
        filtered_url = self._filter_session_parameters(url)
        
        parsed = urlparse(filtered_url)
        domain = parsed.netloc.lower()
        path = parsed.path
        query = f"?{parsed.query}" if parsed.query else ""
        fragment = f"#{parsed.fragment}" if parsed.fragment else ""
        
        # Only convert domains that contain 'guidecx' - all others are external services
        is_guidecx_domain = 'guidecx' in domain
        
        if not is_guidecx_domain:
            # External domain (intercom.io, split.io, etc.) - keep as absolute URL without conversion
            return f'"{filtered_url}"'
        
        # Make project IDs configurable in the path
        configurable_path = self._make_project_ids_configurable(path)
        configurable_query = self._make_project_ids_configurable(query)
        
        # This is a GuideX domain, convert it to use api_domain
        if '.' in domain:
            # Extract and normalize the subdomain (everything before the first dot)
            subdomain = domain.split('.')[0]
            normalized_subdomain = self._normalize_subdomain(subdomain)
            
            # Always use absolute URLs for non-auth subdomains to ensure correct routing
            # Check if we have CSV template variables
            has_csv_vars = (configurable_path != path or configurable_query != query)
            
            if has_csv_vars:
                # Use .format() for CSV data substitution (avoid f-string conflicts)
                full_url = f"https://{normalized_subdomain}.{{self.api_domain}}{configurable_path}{configurable_query}{fragment}"
                return f'f"{full_url}".format(**self.test_data)'
            else:
                return f'f"https://{normalized_subdomain}.{{self.api_domain}}{path}{query}{fragment}"'
        else:
            # Domain without subdomain structure - keep as-is
            if configurable_path != path or configurable_query != query:
                # Has CSV variables
                full_url = f"https://{domain}{configurable_path}{configurable_query}{fragment}"
                return f'"{full_url}".format(**self.test_data)'
            else:
                return f'"{filtered_url}"'
    
    def _generate_environment_aware_host(self, host: str) -> str:
        """Convert host headers to use environment-aware domain variables using CSV domain data"""
        host_lower = host.lower()
        
        # Only convert domains that contain 'guidecx' - all others are external services
        is_guidecx_domain = 'guidecx' in host_lower
        
        if not is_guidecx_domain:
            # External domain (intercom.io, split.io, etc.) - keep as-is
            return host
        
        # This is a GuideX domain, convert it to use api_domain
        if '.' in host_lower:
            # Extract and normalize the subdomain (everything before the first dot)
            subdomain = host_lower.split('.')[0]
            normalized_subdomain = self._normalize_subdomain(subdomain)
            return f"{normalized_subdomain}.{{self.api_domain}}"
        else:
            # Domain without subdomain structure - keep as-is
            return host
    
    def _generate_environment_aware_url_string(self, url: str) -> str:
        """Convert URL strings to environment-aware variables (for headers like Origin/Referer) using CSV domain data"""
        if not url.startswith('https://'):
            return url
            
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Only convert domains that contain 'guidecx' - all others are external services
        is_guidecx_domain = 'guidecx' in domain
        
        if not is_guidecx_domain:
            # External domain (intercom.io, split.io, etc.) - keep as-is
            return url
        
        # This is a GuideX domain, convert it to use api_domain
        if '.' in domain:
            # Extract and normalize the subdomain (everything before the first dot)
            subdomain = domain.split('.')[0]
            normalized_subdomain = self._normalize_subdomain(subdomain)
            return f"https://{normalized_subdomain}.{{self.api_domain}}"
        else:
            # Domain without subdomain structure - keep as-is
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
    
    def _escape_header_value(self, value: str) -> str:
        """
        Properly escape header values for Python code generation.
        Handles quotes and special characters in header values.
        """
        # Use repr() to properly escape quotes and special characters
        # This converts "1751999789511" to '"1751999789511"' 
        # and handles other edge cases automatically
        return repr(value)
    
    def _generate_headers_dict(self, headers: Dict[str, str], method: str) -> Tuple[str, bool]:
        """Generate Python dict code for headers, return (headers_code, needs_dynamic_action)"""
        if not headers:
            return None, False
            
        # Check if this request needs dynamic Next-Action extraction
        has_next_action = any(key.lower() == 'next-action' for key in headers.keys())
            
        # Filter out session-specific headers that should be dynamic
        filtered_headers = {}
        for key, value in headers.items():
            if key.lower() not in ['cookie', 'authorization', 'content-length', 'next-router-state-tree']:
                # Replace hard-coded Next-Action with dynamic extraction
                if key.lower() == 'next-action':
                    filtered_headers[key] = "{next_action_id}"  # Template for replacement
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
            elif '{DOMAIN_SUFFIX}' in str(value) or '%7BDOMAIN_SUFFIX%7D' in str(value):
                # Header with DOMAIN_SUFFIX template (literal or URL-encoded) - needs f-string
                items.append(f'                "{key}": f{self._escape_header_value(value)}')
            elif '{self.api_domain}' in str(value) or '%7Bself.api_domain%7D' in str(value):
                # Header with self.api_domain template (literal or URL-encoded) - needs f-string
                items.append(f'                "{key}": f{self._escape_header_value(value)}')
            else:
                items.append(f'                "{key}": {self._escape_header_value(value)}')
            
        headers_code = '{\n' + ',\n'.join(items) + '\n            }'
        return headers_code, has_next_action
    
    def _generate_workflow_class(self) -> str:
        """Generate the complete workflow class using common.auth"""
        
        template = '''#!/usr/bin/env python3
"""
{workflow_name} User - Uses Shared Authentication
Can be run directly with: locust -f {relative_path}

Uses shared authentication from common.auth module.
Auto-generated from HAR file: {input_file}
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

{csv_config}

# =============================================================================
# WORKFLOW CLASS - {class_name}
# =============================================================================

class {class_name}(AuthenticatedUser):
    """
    User focused on {workflow_name_lower} activities.
    Standalone version for direct Locust execution.
    
    Uses environment variable configuration from base authentication class.
    """
    
    # Relative weight when multiple user classes exist
    weight = 2
    
    # Primary subdomain for this workflow (determined from HAR file)
    primary_subdomain = "{primary_subdomain}"

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
                self.test_data = {{
                    'domain': DOMAIN_SUFFIX,
                    'login_email': os.getenv('LOGIN_EMAIL', 'test@example.com'),
                    'login_password': os.getenv('LOGIN_PASSWORD', 'password'),
                    'projectID': 'test-project-id',
                    'phaseID': 'test-phase-id',
                    'milestoneID': 'test-milestone-id',
                    'taskID': 'test-task-id',
                    'messageID': 'test-message-id',
                    'channelID': 'test-channel-id'
                }}
            
        if DEBUG:
            print(f"{{self.__class__.__name__}} using domain: {{self.api_domain}}")

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

{task_methods}

# =============================================================================
# STANDALONE EXECUTION
# =============================================================================

if __name__ == "__main__":
    print(f"""
{workflow_name} Workflow

Usage:
   locust -f {relative_path}

Configuration:
   export DOMAIN_SUFFIX=staging.guidecx.io
   export LOGIN_EMAIL=your-email@example.com
   export LOGIN_PASSWORD=your-password
   export LOCUST_HOST=https://app.staging.guidecx.io
   export DEBUG=true

Example Commands:
   # Basic test
   locust -f {relative_path} --headless --users=5 --spawn-rate=1 --run-time=30s

   # With specific environment
   export DOMAIN_SUFFIX=production.guidecx.com
   export LOGIN_EMAIL=prod_user@company.com
   export LOGIN_PASSWORD=prod_password
   export LOCUST_HOST=https://app.production.guidecx.com
   locust -f {relative_path} --headless --users=3 --spawn-rate=1 --run-time=15s

   # Web UI mode
   locust -f {relative_path}
    """)
'''

        # Generate CSV configuration if we detected CSV parameters
        csv_config = ""
        if hasattr(self, '_csv_parameters') and self._csv_parameters:
            csv_config = self._generate_project_id_config()
        
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
        
        # Determine relative path for usage instructions (after manual move)
        if self.subdirectory:
            relative_path = f"workflows/{self.subdirectory}/{self._to_snake_case(self.workflow_name)}_user.py"
        else:
            relative_path = f"workflows/{self._to_snake_case(self.workflow_name)}_user.py"
        
        return template.format(
            workflow_name=self.workflow_name,
            workflow_name_lower=self.workflow_name.lower(),
            class_name=self.class_name,
            primary_subdomain=self._determine_primary_subdomain(),
            task_methods='\n\n'.join(task_methods),
            relative_path=relative_path,
            input_file=self.input_file_path,
            csv_config=csv_config
        )
    
    def _determine_primary_subdomain(self) -> str:
        """Determine the primary subdomain from the requests in the HAR file"""
        # Return cached value if already determined
        if hasattr(self, '_cached_primary_subdomain'):
            return self._cached_primary_subdomain
            
        subdomain_counts = {}
        
        for req in self.requests:
            headers = req.get('headers', {})
            host_header = headers.get('Host', '')
            url = req.get('url', '')
            
            subdomain = None
            
            # Extract subdomain from Host header
            if host_header and '.' in host_header:
                subdomain = host_header.split('.')[0].lower()
            # Or from absolute URL
            elif url.startswith('https://'):
                from urllib.parse import urlparse
                parsed = urlparse(url)
                if parsed.netloc and '.' in parsed.netloc:
                    subdomain = parsed.netloc.split('.')[0].lower()
            
            # Count subdomains, but ignore auth-related ones and external services
            if subdomain and subdomain not in ['arches', 'streaming', 'sdk']:
                if ('guidecx' in host_header or 'guidecx' in url):  # Only count internal GuideX subdomains
                    subdomain_counts[subdomain] = subdomain_counts.get(subdomain, 0) + 1
        
        # Return the most common subdomain, defaulting to 'app'
        if subdomain_counts:
            primary = max(subdomain_counts, key=subdomain_counts.get)
            print(f"Determined primary subdomain: {primary} (found {subdomain_counts[primary]} requests)")
            self._cached_primary_subdomain = primary
            return primary
        else:
            print("No clear primary subdomain found, defaulting to 'app'")
            self._cached_primary_subdomain = 'app'
            return 'app'
    
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
    
    def save_to_file(self, output_dir: str = "GEN_WORKFLOW_PY") -> str:
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
            
        print(f"Generated workflow saved to: {output_path}")
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


def _har_filename_to_workflow_name(har_file_path: str) -> str:
    """Convert HAR filename to PascalCase workflow name"""
    import os
    
    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(har_file_path))[0]
    
    # First split on common separators: underscores, hyphens, dots, spaces
    words = re.split(r'[-_.:\s]+', base_name)
    
    # Then handle camelCase by splitting on capital letters
    final_words = []
    for word in words:
        if word:
            # Split camelCase words (e.g., "clickProject" -> ["click", "Project"])
            camel_split = re.findall(r'[A-Z][a-z]*|[a-z]+', word)
            if camel_split:
                final_words.extend(camel_split)
            else:
                final_words.append(word)
    
    # Convert each word to title case and join
    pascal_case = ''.join(word.capitalize() for word in final_words if word)
    
    return pascal_case

def main():
    """Main function to handle command line arguments and workflow generation"""
    if len(sys.argv) < 2:
        print("Usage: python har_to_workflow.py <har_file> [subdirectory]")
        print("")
        print("Arguments:")
        print("  har_file:      Path to HAR file to convert")
        print("  subdirectory:  Optional subdirectory in workflows/ (e.g., 'project', 'admin', 'testing')")
        print("")
        print("Examples:")
        print("  python har_to_workflow.py GlobalProjects.har")
        print("  python har_to_workflow.py project_plan.har project")
        print("  python har_to_workflow.py global-tasks.har admin")
        print("")
        print("Available subdirectories:")
        print("  • project  - Project management and planning workflows")
        print("  • admin    - Administrative and global system workflows")  
        print("  • testing  - Testing utilities and debugging workflows")
        print("")
        print("Note: Workflow name is automatically derived from HAR filename")
        sys.exit(1)
    
    har_file = sys.argv[1]
    subdirectory = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Auto-generate workflow name from HAR filename
    workflow_name = _har_filename_to_workflow_name(har_file)
    
    # Validate subdirectory if provided
    valid_subdirs = ['project', 'admin', 'testing']
    if subdirectory and subdirectory not in valid_subdirs:
        print(f"Invalid subdirectory '{subdirectory}'")
        print(f"Available subdirectories: {', '.join(valid_subdirs)}")
        sys.exit(1)
    
    print("Starting HAR to Workflow conversion...")
    print(f"Input: {har_file}")
    print(f"Workflow name: {workflow_name} (auto-generated from filename)")
    if subdirectory:
        print(f"Subdirectory: workflows/{subdirectory}/")
    
    try:
        generator = HARWorkflowGenerator(har_file, workflow_name, subdirectory)
        workflow_code = generator.generate()
        
        if workflow_code:
            # Determine output path - create GEN_WORKFLOW_PY in HARFIles directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            gen_dir = os.path.join(script_dir, "GEN_WORKFLOW_PY")
            os.makedirs(gen_dir, exist_ok=True)
            
            output_filename = f"{workflow_name}.py"
            output_path = os.path.join(gen_dir, output_filename)
            
            # Write the workflow file
            with open(output_path, 'w') as f:
                f.write(workflow_code)
            
            print(f"Generated workflow saved to: {output_path}")
            print(f"Suggested target: workflows/{subdirectory + '/' if subdirectory else ''}{workflow_name}.py")
            
            # Show completion message with subdirectory info
            python_file_info = ""
            if generator.is_har_file and hasattr(generator, 'temp_python_file'):
                python_file_info = f"Python conversion: {generator.temp_python_file}\n"
            
            # Show configuration message for environment variables
            config_msg = f"""
⚙️  SHARED AUTHENTICATION WITH ENVIRONMENT VARIABLES:
This workflow uses common.auth module with environment variable configuration.

🔧 Required Environment Variables:
   export DOMAIN_SUFFIX=staging.guidecx.io
   export LOGIN_EMAIL=your-email@example.com  
   export LOGIN_PASSWORD=your-password
   export LOCUST_HOST=https://app.staging.guidecx.io
   export DEBUG=true

🟡 STAGING Environment:
   export DOMAIN_SUFFIX=staging.guidecx.io
   export LOGIN_EMAIL=stage_user@test.com
   export LOGIN_PASSWORD=stage_password
   export LOCUST_HOST=https://app.staging.guidecx.io

🔴 PRODUCTION Environment:
   export DOMAIN_SUFFIX=production.guidecx.com
   export LOGIN_EMAIL=prod_user@company.com
   export LOGIN_PASSWORD=prod_password
   export LOCUST_HOST=https://app.production.guidecx.com

🔧 Usage Examples:
   # Test staging environment:
   export DOMAIN_SUFFIX=staging.guidecx.io
   export LOGIN_EMAIL=stage_user@test.com
   export LOGIN_PASSWORD=stage_password
   export LOCUST_HOST=https://app.staging.guidecx.io
   locust -f {output_path} --users=10 --spawn-rate=2
   
   # Test production environment:
   export DOMAIN_SUFFIX=production.guidecx.com
   export LOGIN_EMAIL=prod_user@company.com
   export LOGIN_PASSWORD=prod_password
   export LOCUST_HOST=https://app.production.guidecx.com
   locust -f {output_path} --users=5 --spawn-rate=1

✅ Benefits:
   • Centralized authentication: Changes in one place (common/auth.py)
   • No regeneration needed: Auth updates apply to all workflows
   • Environment-aware: Different credentials per environment
   • Simple configuration: Just set environment variables

📝 Authentication changes: Edit common/auth.py (affects all workflows)
"""

            # Show directory structure with subdirectory
            subdir_info = f"/{subdirectory}" if subdirectory else ""
            import_path = f"workflows.{subdirectory}.{generator._to_snake_case(workflow_name)}_user" if subdirectory else f"workflows.{generator._to_snake_case(workflow_name)}_user"
            
            print(f"""
HAR to Workflow Conversion Complete!

Generated workflow: {output_path}
{python_file_info}
Next steps:
1. Move the generated file to your desired location:
   # For {subdirectory or 'general'} workflows:
   mv {output_path} workflows/{subdirectory + '/' if subdirectory else ''}{workflow_name}.py

2. Set environment variables for authentication:
   export DOMAIN_SUFFIX=staging.guidecx.io
   export LOGIN_EMAIL=your-email@example.com
   export LOGIN_PASSWORD=your-password
   export LOCUST_HOST=https://app.staging.guidecx.io

3. Test the workflow:
   locust -f workflows/{subdirectory + '/' if subdirectory else ''}{workflow_name}.py --users=1 --spawn-rate=2 --run-time=10s

{config_msg}

Authentication changes: Edit common/auth.py (affects ALL workflows automatically!)
""")
        else:
            print("Failed to generate workflow")
            sys.exit(1)
    
    except Exception as e:
        print(f"Error during conversion: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main() 