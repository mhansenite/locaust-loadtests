# GuideCX Load Testing Workflows

Comprehensive workflow collection for load testing the GuideCX platform, organized by business domain.

## 📁 Workflow Structure

```
workflows/
├── 🔐 authentication/          # Login, logout, session management
├── 👥 customer_portal/         # Customer-facing experiences  
├── 📁 file_management/         # File upload, download, sharing
├── 🔗 integration/             # Third-party integrations and APIs
├── 💬 messaging/               # Communication and collaboration
├── 📱 mobile/                  # Mobile and responsive workflows
├── ⚡ performance/             # Stress testing and load scenarios
├── ⚙️  admin/                  # ✅ Administrative workflows (existing)
├── 🏗️  project/               # ✅ Project management (existing)
├── 📋 tasks/                   # Task management
├── ⏱️  time_tracking/          # Time tracking and billing
├── 📊 reports/                 # Analytics and reporting
├── 📝 templates/               # Template management
└── 🧪 testing/                # ✅ Testing utilities (existing)
```

## 🎯 Priority Levels

### 🔴 HIGH PRIORITY (Core Business Functionality)
Record these workflows first as they directly impact customer experience:

1. **Customer Portal** - Customer onboarding, dashboard, tasks
2. **Authentication** - Login/logout flows for all user types
3. **Project Management** - Project creation, planning, team management
4. **Messaging** - Project communication, customer-team messaging
5. **File Management** - Document uploads, downloads, sharing

### 🟡 MEDIUM PRIORITY (Important Operations)
Record these after completing high-priority workflows:

1. **Time Tracking** - Time entry, categories, reporting
2. **Task Management** - Task creation, assignment, status updates
3. **Mobile Workflows** - Mobile dashboard, tasks, messaging
4. **Admin Functions** - User management, system configuration

### 🟢 LOW PRIORITY (Advanced Features)
Record these for comprehensive coverage:

1. **Integration** - Third-party APIs, webhooks, data sync
2. **Performance** - Stress testing, concurrent editing
3. **Reports** - Analytics, custom reports, data export
4. **Templates** - Template creation and management

## 🚀 Quick Start Guide

### 1. Record Your First Workflow
```bash
# 1. Open browser dev tools → Network tab
# 2. Enable "Preserve log"
# 3. Navigate through your workflow
# 4. Save as HAR file

# Example: Customer onboarding
# Navigate: Login → Dashboard → View Project → Check Tasks → Send Message
# Save as: customer_onboarding.har
```

### 2. Generate Workflow Class
```bash
# Convert HAR to Python workflow
python3 HARFIles/har_to_workflow.py customer_onboarding.har CustomerOnboarding customer_portal

# This creates: workflows/customer_portal/customer_onboarding_user.py
```

### 3. Test the Workflow
```bash
# Set up CSV test data
export TEST_DATA_CSV=config/test_data_staging.csv

# Test the workflow
locust -f guidex_loadtest.py CustomerOnboardingUser --users=5 --spawn-rate=1
```

## 📋 Folder Contents

Each workflow folder contains:

- **README.md** - Detailed instructions and workflow descriptions
- **__init__.py** - Python module initialization
- **\*_user.py** - Generated workflow classes (created from HAR files)

## 🎬 HAR Recording Best Practices

### Before Recording
✅ Use incognito/private browser mode  
✅ Clear browser cache and cookies  
✅ Enable "Preserve log" in Network tab  
✅ Plan your complete workflow journey  

### During Recording
✅ Navigate naturally with realistic wait times  
✅ Include error scenarios where appropriate  
✅ Test different user roles (customer, admin, PM)  
✅ Focus on business-critical paths  

### After Recording
✅ Review HAR file for sensitive data  
✅ Test HAR conversion with har_to_workflow.py  
✅ Validate generated workflow with small load test  
✅ Create environment-specific CSV test data  

## 📊 CSV Test Data Structure

Create environment-specific CSV files in `config/` directory:

### Staging: `config/test_data_staging.csv`
```csv
domain,login_email,login_password,projectID,taskID,milestoneID
staging.guidecx.io,stage_user1@test.com,stage_pass,uuid1,uuid2,uuid3
staging.guidecx.io,stage_user2@test.com,stage_pass,uuid4,uuid5,uuid6
```

### Production: `config/test_data_production.csv`
```csv
domain,login_email,login_password,projectID,taskID,milestoneID
production.guidecx.com,prod_user1@company.com,prod_pass,uuid7,uuid8,uuid9
production.guidecx.com,prod_user2@company.com,prod_pass,uuid10,uuid11,uuid12
```

## 🔧 Usage Examples

### Single Workflow Testing
```bash
# Test specific workflow
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py CustomerOnboardingUser --headless --users=5 --spawn-rate=1 --run-time=30s
```

### Multi-Workflow Load Testing
```bash
# Test multiple workflows simultaneously
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py \
  CustomerOnboardingUser \
  ProjectPlanUser \
  MessagingUser \
  --headless --users=20 --spawn-rate=2 --run-time=5m
```

### Environment-Specific Testing
```bash
# Staging environment
export TEST_DATA_CSV=config/test_data_staging.csv
export DOMAIN_SUFFIX=staging.guidecx.io
locust -f guidex_loadtest.py --users=10

# Production environment  
export TEST_DATA_CSV=config/test_data_production.csv
export DOMAIN_SUFFIX=production.guidecx.com
locust -f guidex_loadtest.py --users=5
```

## 📝 Next Steps

1. **Review folder READMEs** - Each folder contains specific recording instructions
2. **Start with HIGH priority** - Focus on customer-facing workflows first
3. **Record systematically** - Complete one business domain before moving to next
4. **Test incrementally** - Validate each workflow before recording the next
5. **Create CSV data** - Set up realistic test data for your environments

## 🔗 Related Documentation

- `HARFIles/har_to_workflow.py` - HAR conversion tool
- `auth/base_user.py` - Authentication base classes
- `config/test_data_*.csv` - Environment-specific test data
- Individual folder READMEs - Detailed workflow instructions

## 📞 Support

For questions about workflow creation or HAR recording:
1. Check the specific folder's README.md file
2. Review existing workflow examples in `admin/` and `project/` folders
3. Test HAR conversion with small examples first 