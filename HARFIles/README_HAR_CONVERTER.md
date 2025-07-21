# 🤖 HAR to Workflow Converter

**Automatically convert HAR files directly into GuideX load testing workflows!**

## 🚀 Quick Reference

### Basic Usage
```bash
python3 HARFiles/har_to_workflow.py <input_file> <WorkflowName>
```

### Supported Input Formats
- **`.har` files** (recommended) - Automatically converted using `har2locust`
- **`.py` files** - Already converted from HAR using other tools

### Example Commands
```bash
# Convert directly from HAR file (easiest method!)
python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/GlobalProjects.har GlobalProjects

# Convert from HAR file in different directory
python3 HARFiles/har_to_workflow.py /path/to/UserManagement.har UserManagement

# Convert from existing Python file
python3 HARFiles/har_to_workflow.py HARFiles/RAW_PY/GlobalProjects.py GlobalProjects
```

## 📋 Complete End-to-End Process

### 1. Capture HAR File
1. Open browser developer tools (F12)
2. Go to **Network** tab
3. **Clear** existing entries
4. Perform your complete workflow in the application
5. **Right-click** in Network tab → **Save all as HAR**
6. Save as `YourWorkflow.har`

### 2. Run Converter (One Command!)
```bash
cd /path/to/locaust-loadtests
python3 utils/har_to_workflow.py YourWorkflow.har YourWorkflowName
```

The converter will automatically:
- ✅ Run `har2locust` to convert HAR → Python
- ✅ Parse the Python code for HTTP requests  
- ✅ **🗑️ Filter out static assets** (images, fonts, CSS, JS, etc.)
- ✅ Group requests into logical task categories
- ✅ **🆕 Replace hard-coded Next-Action IDs with dynamic extraction**
- ✅ Generate a complete workflow class
- ✅ Clean up temporary files

### 3. Integration
1. **Review generated file**: `workflows/your_workflow_name_user.py`
2. **Add import** to `guidex_loadtest.py`:
   ```python
   from workflows.your_workflow_name_user import YourWorkflowNameUser
   ```
3. **Add to exports**:
   ```python
   __all__ = ['ProjectUser', 'GlobalTasksUser', 'GlobalProjectsUser', 'MixedWorkflowUser', 'YourWorkflowNameUser']
   ```

### 4. Test
```bash
# Test the specific workflow
locust -f guidex_loadtest.py YourWorkflowNameUser --headless --users=5 --spawn-rate=1 --run-time=30s

# Test all workflows together
locust -f guidex_loadtest.py --headless --users=20 --spawn-rate=4 --run-time=120s
```

## 🛠️ Prerequisites

### Required Tools
```bash
# Install har2locust (for HAR file support)
pip install har2locust

# Install locust (if not already installed)  
pip install locust
```

### Verify Installation
```bash
# Check har2locust is working
har2locust --version

# Check our converter is working
python3 utils/har_to_workflow.py --help
```

## 🎯 What the Converter Does

### Automatic HAR Processing Pipeline

```
📁 YourWorkflow.har
    ↓ (har2locust)
📄 HARFiles/pyfiles/YourWorkflow.py  
    ↓ (AST parsing)
📊 HTTP requests extracted
    ↓ (intelligent grouping)
📋 Task categories created
    ↓ (code generation)
✅ workflows/your_workflow_user.py
```

### File Organization

The converter maintains a clean, organized directory structure:

```
locaust-loadtests/
├── HARFiles/
│   ├── RAW_HAR/               # Your original HAR captures
│   │   ├── GlobalProjects.har
│   │   ├── UserManagement.har
│   │   └── YourWorkflow.har
│   ├── RAW_PY/                # HAR→Python conversions (kept for reference)
│   │   ├── GlobalProjects.py
│   │   ├── UserManagement.py
│   │   └── YourWorkflow.py
│   ├── har_to_workflow.py     # Converter script
│   └── README_HAR_CONVERTER.md # This documentation
├── workflows/                 # Generated workflow classes
│   ├── global_projects_user.py
│   ├── user_management_user.py  
│   └── your_workflow_user.py
└── guidex_loadtest.py         # Main entry point
```

**Benefits of this organization:**
- ✅ **Clear separation** - HAR files and conversions in one place
- ✅ **Reference files** - Keep Python conversions for debugging
- ✅ **Clean workflows** - Generated classes in dedicated directory
- ✅ **Version control** - Easy to track changes and history

## 🎯 Advanced Features

### Dynamic Next-Action Extraction

The converter automatically detects and handles Next-Action headers in POST requests, generating code that:

```python
# Extract dynamic Next-Action ID from current page
next_action_id = None
page_url = f"{PROJECT_URL}/v2/projects"
with self.client.get(page_url, catch_response=True) as page_resp:
    if page_resp.status_code == 200:
        next_action_id = self.extract_next_action_id(page_resp.text)
        if DEBUG and next_action_id:
            print(f"✅ Extracted Next-Action ID: {next_action_id}")

# Use fallback if extraction failed
if not next_action_id:
    next_action_id = "7dde6021d1d552016a324b86aabc828d90123a87"  # Original from HAR
    if DEBUG:
        print(f"⚠️ Using fallback Next-Action ID: {next_action_id}")

# Use dynamic ID in actual request
with self.client.post(
    "/v2/projects",
    headers={
        "Next-Action": next_action_id,  # Dynamic value!
        # ... other headers
    }
)
```

**Benefits:**
- ✅ **No more hard-coded action IDs** - Extracted dynamically from current page state
- ✅ **Reliable fallbacks** - Uses original HAR values if extraction fails  
- ✅ **Automatic detection** - Converter identifies Next-Action headers automatically
- ✅ **Production-ready** - Works with real application state changes

### Smart Asset Filtering

Static assets like images, fonts, CSS, and JavaScript files are automatically filtered out because:

- ✅ **Browsers cache these** - Not representative of real user load
- ✅ **No user interaction** - These don't require user decisions or actions  
- ✅ **CDN-served content** - Often served from different infrastructure
- ✅ **Consistent response times** - Don't vary with application performance

**Filtered Asset Types:**
```bash
🗑️ Images:      .ico, .png, .jpg, .jpeg, .gif, .svg, .webp, .bmp
🗑️ Fonts:       .woff, .woff2, .ttf, .otf, .eot  
🗑️ Stylesheets: .css, .map
🗑️ Scripts:     .js, .bundle.*, .chunk.*
🗑️ Paths:       /static/, /assets/, /css/, /js/, /fonts/, /images/
🗑️ Patterns:    favicon, /_next/static/, /__webpack_hmr, node_modules/
```

### Intelligent Request Grouping

| Category | Weight | Purpose | Examples |
|----------|--------|---------|----------|
| **Page Load** | 3 | Initial navigation, page loads | `/v2/projects`, route changes |
| **API Calls** | 2 | Authentication, data fetching | `/auth/session`, GraphQL |
| **Filters** | 2 | Loading dropdowns, filters | `LoadTags`, `LoadManagers` |
| **Data Refresh** | 4 | Dynamic updates, mutations | POST actions, state changes |

### Generated Code Features

✅ **Full integration** - Inherits from `AuthenticatedUser`  
✅ **Environment configuration** - Uses your `.env` settings
✅ **Automatic imports** - All necessary Locust and auth imports
✅ **Error handling** - Built-in response validation and logging
✅ **Debug support** - Configurable debug output
✅ **Clean headers** - Removes sensitive/session-specific headers
✅ **Optimal weights** - Task execution frequency based on request types

## 📝 Generated File Structure

```python
#!/usr/bin/env python3
"""
WorkflowName User - Auto-generated from HAR file
"""

from locust import task
from auth.base_user import AuthenticatedUser
from auth.config import PROJECT_URL, PROJECT_DOMAIN, DEBUG

class WorkflowNameUser(AuthenticatedUser):
    """Auto-generated workflow for authentic interactions"""
    
    host = PROJECT_URL
    weight = 2

    @task(weight=3)
    def page_load(self):
        """Page Load - Generated from HAR workflow"""
        if DEBUG:
            print("🔄 Page Load...")
        
        with self.client.get("/endpoint", headers={...}) as resp:
            if resp.status_code == 200:
                if DEBUG:
                    print("✅ Page Load successful")
            else:
                if DEBUG:
                    print(f"❌ Page Load failed: {resp.status_code}")
        
        if DEBUG:
            print("✅ Page Load completed")

    # Additional tasks generated automatically...
```

## 🔧 Advanced Usage

### Converting Multiple Workflows
```bash
# Convert several workflows in batch
python3 utils/har_to_workflow.py LoginFlow.har LoginFlow
python3 utils/har_to_workflow.py ReportsView.har Reports  
python3 utils/har_to_workflow.py UserAdmin.har UserAdmin
```

### Custom Output Directory
```python
# In your own script
from utils.har_to_workflow import HARWorkflowGenerator

generator = HARWorkflowGenerator("MyWorkflow.har", "MyWorkflow")
output_path = generator.save_to_file(output_dir="custom_workflows")
```

### Integration with CI/CD
```bash
#!/bin/bash
# automated_workflow_generation.sh

echo "Converting HAR files to workflows..."
for har_file in *.har; do
    workflow_name=$(basename "$har_file" .har)
    python3 utils/har_to_workflow.py "$har_file" "$workflow_name"
done
echo "All workflows generated!"
```

## 🚨 Troubleshooting

### Common Issues & Solutions

**❌ "har2locust not found"**
```bash
# Install har2locust
pip install har2locust

# Verify installation
har2locust --version
```

**❌ "No requests found in file"**
- Ensure your HAR file contains actual network requests
- Check that you captured a complete workflow (not just page loads)
- Verify the HAR file isn't corrupted

**❌ "har2locust failed"**
- Try a smaller HAR file first
- Check the HAR file format is valid
- Ensure no special characters in the HAR filename

**❌ Import errors when running generated workflow**
- Verify you're in the correct directory (`locaust-loadtests`)
- Check that `requirements.txt` packages are installed
- Ensure the generated file syntax is valid

**❌ Authentication failures in generated workflow**
- Generated workflows inherit authentication from `AuthenticatedUser`
- Check your `.env` file has correct credentials
- Verify the workflow doesn't override authentication headers

### Performance Tips

1. **Capture focused workflows** - Record only the essential user journey
2. **Exclude unnecessary requests** - Filter out analytics, tracking, ads
3. **Test incrementally** - Start with 1 user, then scale up
4. **Review generated tasks** - Adjust weights based on your priorities

### HAR Capture Best Practices

1. **Clear network tab** before starting
2. **Disable cache** to capture all requests
3. **Complete full workflow** in one session
4. **Include authentication** if needed
5. **Save immediately** after completing workflow

## 🎉 Success Workflow

1. **Capture HAR** - Record your user workflow
2. **Convert** - `python3 utils/har_to_workflow.py workflow.har WorkflowName`
3. **Review** - Check generated `workflows/workflow_name_user.py`
4. **Integrate** - Add import to `guidex_loadtest.py`
5. **Test** - Run with small load first
6. **Scale** - Increase users/spawn rate gradually
7. **Monitor** - Watch for errors or performance issues

## 📊 Example Conversion Output

```bash
🚀 Starting HAR to Workflow conversion...
   • Input: UserManagement.har
   • Workflow: UserManagement

📁 Input: HAR file (UserManagement.har)
🔄 Converting HAR file to Python using har2locust...
   • Input HAR: UserManagement.har
   • Output Python: HARFiles/pyfiles/UserManagement.py
✅ HAR to Python conversion successful
📁 Python file saved: HARFiles/pyfiles/UserManagement.py
🔄 Parsing Python file: HARFiles/pyfiles/UserManagement.py
📊 Found 23 requests
📁 Grouped into 4 task categories:
   • page_load: 2 requests
   • api_calls: 8 requests  
   • data_refresh: 7 requests
   • filters: 6 requests
🏗️ Generating UserManagementUser...
✅ Generated workflow saved to: workflows/user_management_user.py
📁 Keeping Python file for reference: HARFiles/pyfiles/UserManagement.py

🎉 HAR to Workflow Conversion Complete!

📁 File Organization:
Python conversion: HARFiles/pyfiles/UserManagement.py
Generated workflow: workflows/user_management_user.py

📊 Directory Structure:
   HARFiles/
   ├── pyfiles/          # HAR→Python conversions
   │   └── UserManagement.py
   │
   workflows/             # Generated workflow classes  
   └── user_management_user.py
```

---

**🔗 Related Files:**
- `utils/har_to_workflow.py` - Main converter script
- `auth/base_user.py` - Base authentication class  
- `guidex_loadtest.py` - Main entry point for all workflows
- `README.md` - Complete project documentation 