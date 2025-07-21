import os
from dotenv import load_dotenv
from urllib.parse import quote, quote_plus

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# LOAD TESTING CONFIGURATION FROM ENVIRONMENT VARIABLES
# =============================================================================

# Domain Configuration
DOMAIN_SUFFIX = os.getenv("DOMAIN_SUFFIX")  # e.g., "guidecx.com" or "staging.guidecx.io"

# Dynamic URL construction based on environment
if DOMAIN_SUFFIX:
    # Environment-aware URL construction
    BASE_URL_APP = f"https://app.{DOMAIN_SUFFIX}"
    PROJECT_URL = f"https://arches.{DOMAIN_SUFFIX}"
    BASE_URL_API = f"https://api.{DOMAIN_SUFFIX}"
    BASE_URL_K2_WEB = f"https://web-k2.{DOMAIN_SUFFIX}"
else:
    # Fallback to legacy environment variables
    BASE_URL_APP = os.getenv("BASE_URL_APP")
    PROJECT_URL = os.getenv("PROJECT_URL")
    BASE_URL_API = os.getenv("BASE_URL_API")
    BASE_URL_K2_WEB = os.getenv("BASE_URL_K2_WEB")

# Authentication - loaded from environment variables
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

# Load Testing Parameters (loaded from environment)
DEFAULT_USERS = os.getenv("DEFAULT_USERS")
DEFAULT_SPAWN_RATE = os.getenv("DEFAULT_SPAWN_RATE")
DEFAULT_RUN_TIME = os.getenv("DEFAULT_RUN_TIME")
DEBUG = os.getenv("DEBUG")
WAIT_TIME_BETWEEN_TASKS = os.getenv("WAIT_TIME_BETWEEN_TASKS")

# Validate required environment variables
if DOMAIN_SUFFIX:
    # When using DOMAIN_SUFFIX, these are dynamically constructed
    required_vars = {
        "DOMAIN_SUFFIX": DOMAIN_SUFFIX,
        "LOGIN_EMAIL": LOGIN_EMAIL,
        "LOGIN_PASSWORD": LOGIN_PASSWORD,
        "DEFAULT_USERS": DEFAULT_USERS,
        "DEFAULT_SPAWN_RATE": DEFAULT_SPAWN_RATE,
        "DEFAULT_RUN_TIME": DEFAULT_RUN_TIME,
        "DEBUG": DEBUG,
        "WAIT_TIME_BETWEEN_TASKS": WAIT_TIME_BETWEEN_TASKS
    }
else:
    # Legacy mode - require individual URL variables
    required_vars = {
        "BASE_URL_APP": BASE_URL_APP,
        "PROJECT_URL": PROJECT_URL,
        "BASE_URL_API": BASE_URL_API,
        "LOGIN_EMAIL": LOGIN_EMAIL,
        "LOGIN_PASSWORD": LOGIN_PASSWORD,
        "DEFAULT_USERS": DEFAULT_USERS,
        "DEFAULT_SPAWN_RATE": DEFAULT_SPAWN_RATE,
        "DEFAULT_RUN_TIME": DEFAULT_RUN_TIME,
        "DEBUG": DEBUG,
        "WAIT_TIME_BETWEEN_TASKS": WAIT_TIME_BETWEEN_TASKS
    }

missing_vars = [var for var, value in required_vars.items() if not value]
if missing_vars:
    raise ValueError(f"Required environment variables are missing: {', '.join(missing_vars)}")

# Convert to appropriate types after validation
DEFAULT_USERS = int(DEFAULT_USERS)          # Number of concurrent users to simulate
DEFAULT_SPAWN_RATE = int(DEFAULT_SPAWN_RATE)      # Users to spawn per second
DEBUG = DEBUG.lower() in ("true", "1", "yes")               # Set to False to disable debug prints (recommended for headless mode)
WAIT_TIME_BETWEEN_TASKS = int(WAIT_TIME_BETWEEN_TASKS)  # Seconds to wait between API calls per user

# Extract domain names for host headers and form data
APP_DOMAIN = BASE_URL_APP.replace("https://", "")       # app.guidecx.com
PROJECT_DOMAIN = PROJECT_URL.replace("https://", "")   # arches.guidecx.com  
API_DOMAIN = BASE_URL_API.replace("https://", "")      # api.guidecx.com
K2_WEB_DOMAIN = BASE_URL_K2_WEB.replace("https://", "") # web-k2.guidecx.com

# URL-encoded versions for use in URLs and payloads
LOGIN_EMAIL_ENCODED = quote_plus(LOGIN_EMAIL)  # For URL parameters
LOGIN_EMAIL_JSON_ENCODED = quote(LOGIN_EMAIL)  # For JSON in URLs 