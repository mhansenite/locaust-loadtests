# Environment Configuration Examples

The load testing framework now supports **environment-aware domain configuration** for easier multi-environment deployments.

## 🎯 Recommended Approach: DOMAIN_SUFFIX

Create a `.env` file with just the domain suffix for your environment:

### Production Environment
```bash
# .env
DOMAIN_SUFFIX=guidecx.com

# Authentication
LOGIN_EMAIL=your.email@company.com
LOGIN_PASSWORD=your_password_here

# Load Testing Parameters
DEFAULT_USERS=10
DEFAULT_SPAWN_RATE=2
DEFAULT_RUN_TIME=300
DEBUG=true
WAIT_TIME_BETWEEN_TASKS=1
```

This automatically constructs:
- `BASE_URL_APP=https://app.guidecx.com`
- `PROJECT_URL=https://arches.guidecx.com`
- `BASE_URL_API=https://api.guidecx.com`
- `BASE_URL_K2_WEB=https://web-k2.guidecx.com`

### Staging Environment
```bash
# .env
DOMAIN_SUFFIX=staging.guidecx.io

# Authentication
LOGIN_EMAIL=your.email@company.com
LOGIN_PASSWORD=your_password_here

# Load Testing Parameters (same as production)
DEFAULT_USERS=10
DEFAULT_SPAWN_RATE=2
DEFAULT_RUN_TIME=300
DEBUG=true
WAIT_TIME_BETWEEN_TASKS=1
```

This automatically constructs:
- `BASE_URL_APP=https://app.staging.guidecx.io`
- `PROJECT_URL=https://arches.staging.guidecx.io`
- `BASE_URL_API=https://api.staging.guidecx.io`
- `BASE_URL_K2_WEB=https://web-k2.staging.guidecx.io`

## 🔄 Legacy Approach: Individual URLs

If you prefer to set each URL individually, leave `DOMAIN_SUFFIX` empty:

```bash
# .env
# Legacy individual URL configuration
BASE_URL_APP=https://app.guidecx.com
PROJECT_URL=https://arches.guidecx.com
BASE_URL_API=https://api.guidecx.com
BASE_URL_K2_WEB=https://web-k2.guidecx.com

# Authentication
LOGIN_EMAIL=your.email@company.com
LOGIN_PASSWORD=your_password_here

# Load Testing Parameters
DEFAULT_USERS=10
DEFAULT_SPAWN_RATE=2
DEFAULT_RUN_TIME=300
DEBUG=true
WAIT_TIME_BETWEEN_TASKS=1
```

## ✅ Benefits of DOMAIN_SUFFIX Approach

1. **Single Variable Configuration** - Only need `DOMAIN_SUFFIX` to define environment
2. **Environment Switching** - Change one variable to switch environments  
3. **Consistency** - All subdomains automatically match the environment
4. **Simplified Configuration** - Minimal variables to manage
5. **Generated Workflows** - HAR converter generates environment-aware URLs automatically

## 🚀 Generated Workflow Benefits

When using the HAR to workflow converter, URLs and headers are automatically generated as environment-aware:

```python
# Auto-generated environment-aware URLs using DOMAIN_SUFFIX
with self.client.get(
    f"https://app.{DOMAIN_SUFFIX}/auth/session",
    headers={
        "Host": f"app.{DOMAIN_SUFFIX}",
        "Origin": f"https://arches.{DOMAIN_SUFFIX}",
        "Referer": f"https://arches.{DOMAIN_SUFFIX}",
        # ...
    }
)

# Complex subdomain example (like web-k2)
with self.client.post(
    f"https://web-k2.{DOMAIN_SUFFIX}/manager.project.project_list.ProjectListService/LoadTagsDropdown",
    headers={
        "Host": f"web-k2.{DOMAIN_SUFFIX}",
        # ...
    }
)
```

This means **one workflow works in all environments** - just change your `.env` file! 