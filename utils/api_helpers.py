"""
Common API helper functions for GuideX load testing.
Provides reusable patterns for API calls and response handling.
"""

import os

# Environment-aware configuration (matches auth/base_user.py pattern)
DOMAIN_SUFFIX = os.getenv("DOMAIN_SUFFIX", "staging.guidecx.io")
DEBUG = os.getenv("DEBUG", "false").lower() in ["true", "1", "yes"]

# Dynamic URL construction based on environment
BASE_URL_API = f"https://api.{DOMAIN_SUFFIX}"
PROJECT_URL = f"https://arches.{DOMAIN_SUFFIX}"
API_DOMAIN = f"api.{DOMAIN_SUFFIX}"


def get_graphql_headers(auth_token, operation_name="", referer_path="/projects"):
    """
    Generate standard headers for GraphQL requests
    
    Args:
        auth_token: Bearer token for authorization
        operation_name: GraphQL operation name (for URL)
        referer_path: Path for the referer header
    
    Returns:
        dict: Headers for the request
    """
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Host": API_DOMAIN,
        "Origin": PROJECT_URL,
        "Referer": f"{PROJECT_URL}{referer_path}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "authorization": auth_token,
        "x-graphql-version": "1.0",
    }


def build_graphql_url(operation_name):
    """
    Build GraphQL URL with operation name
    
    Args:
        operation_name: The GraphQL operation name
    
    Returns:
        str: Complete GraphQL URL
    """
    return f"{BASE_URL_API}/graphql?{operation_name}"


def handle_graphql_response(response, operation_name, expected_data_key=None):
    """
    Handle GraphQL response with consistent logging and error handling
    
    Args:
        response: The response object
        operation_name: Name of the operation for logging
        expected_data_key: Key to look for in response data (optional)
    
    Returns:
        dict: Parsed response data or None if failed
    """
    if response.status_code != 200:
        if DEBUG:
            print(f"{operation_name} failed: {response.status_code}")
            response_text = response.text or "No response text"
            print(f"Response text: {response_text[:500]}...")
        response.failure(f"{operation_name} failed: {response.status_code}")
        return None
    
    try:
        data = response.json()
        
        # Check for GraphQL errors
        if 'errors' in data:
            if DEBUG:
                print(f"{operation_name} GraphQL errors: {data['errors']}")
            response.failure(f"{operation_name} GraphQL errors")
            return None
        
        # Log success and extract data
        if expected_data_key and 'data' in data:
            extracted_data = data['data'].get(expected_data_key)
            if extracted_data:
                # Try to extract count information if available
                if isinstance(extracted_data, dict):
                    if 'pageInfo' in extracted_data and 'totalResults' in extracted_data['pageInfo']:
                        total_results = extracted_data['pageInfo']['totalResults']
                        if DEBUG:
                            print(f"{operation_name} success: {total_results} total results")
                    elif isinstance(extracted_data, list):
                        if DEBUG:
                            print(f"{operation_name} success: {len(extracted_data)} items")
                    else:
                        if DEBUG:
                            print(f"{operation_name} success")
                else:
                    if DEBUG:
                        print(f"{operation_name} success")
            else:
                if DEBUG:
                    print(f"{operation_name} success (no {expected_data_key} data)")
        else:
            if DEBUG:
                print(f"{operation_name} success: {response.status_code}")
        
        return data
        
    except Exception as e:
        if DEBUG:
            print(f"{operation_name} success: {response.status_code} (couldn't parse JSON: {e})")
        return {"status": "success", "raw_response": response.text}


def make_graphql_request(client, operation_name, query, variables, auth_token, 
                        referer_path="/projects", expected_data_key=None, 
                        request_name=None):
    """
    Make a GraphQL request with standard error handling
    
    Args:
        client: Locust client object
        operation_name: GraphQL operation name
        query: GraphQL query string
        variables: Query variables
        auth_token: Bearer token
        referer_path: Path for referer header
        expected_data_key: Key to look for in response data
        request_name: Name for Locust statistics (defaults to operation_name)
    
    Returns:
        dict: Response data or None if failed
    """
    if request_name is None:
        request_name = operation_name
    
    headers = get_graphql_headers(auth_token, operation_name, referer_path)
    url = build_graphql_url(operation_name)
    
    with client.rest(
        "POST",
        url,
        headers=headers,
        json={
            "operationName": operation_name,
            "variables": variables,
            "query": query,
        },
        name=request_name
    ) as resp:
        return handle_graphql_response(resp, operation_name, expected_data_key)


class TaskStatusGenerator:
    """
    Helper class to generate realistic task status combinations for testing
    """
    
    COMMON_STATUS_FILTERS = [
        ["OPEN"],
        ["IN_PROGRESS"],
        ["COMPLETED"],
        ["OPEN", "IN_PROGRESS"],
        ["OVERDUE"],
        ["OPEN", "OVERDUE"],
        ["COMPLETED", "CLOSED"]
    ]
    
    TASK_STATUSES = [
        "OPEN",
        "IN_PROGRESS", 
        "COMPLETED",
        "CLOSED",
        "OVERDUE",
        "BLOCKED"
    ]
    
    @classmethod
    def get_random_status_filter(cls):
        """Get a random status filter combination"""
        import random
        return random.choice(cls.COMMON_STATUS_FILTERS)
    
    @classmethod
    def get_random_status(cls):
        """Get a random individual status"""
        import random
        return random.choice(cls.TASK_STATUSES)


class ProjectFilterGenerator:
    """
    Helper class to generate realistic project filter combinations
    """
    
    PROJECT_STATUSES = ["ON_TIME", "ON_HOLD", "LATE", "COMPLETED"]
    SORT_OPTIONS = [
        ("NAME", "ASC"),
        ("NAME", "DESC"),
        ("UPDATED_AT", "DESC"),
        ("CREATED_AT", "DESC"),
        ("DUE_DATE", "ASC")
    ]
    
    @classmethod
    def get_random_sort(cls):
        """Get random sort options"""
        import random
        return random.choice(cls.SORT_OPTIONS)
    
    @classmethod
    def get_random_status_filter(cls):
        """Get random project status filter"""
        import random
        # Sometimes filter by single status, sometimes multiple
        if random.choice([True, False]):
            return [random.choice(cls.PROJECT_STATUSES)]
        else:
            return random.sample(cls.PROJECT_STATUSES, random.randint(2, 3)) 