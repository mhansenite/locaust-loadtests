# Customer Portal Workflows

Customer-facing workflows and experiences for the GuideCX platform.

## 📋 Workflows Needed

- **customer_onboarding_user.py** - Customer's first-time project experience
- **customer_dashboard_user.py** - Customer project dashboard usage
- **customer_tasks_user.py** - Customer task viewing and completion
- **customer_messaging_user.py** - Customer communication with project teams
- **customer_file_sharing_user.py** - Document uploads and downloads
- **customer_feedback_user.py** - CSAT surveys and feedback submission

## 🎬 HAR Files to Record

- **customer_onboarding.har** - Record customer's first project experience
- **customer_dashboard.har** - Record customer dashboard navigation
- **customer_tasks.har** - Record task viewing, status updates
- **customer_messaging.har** - Record messaging and communication flows
- **customer_file_sharing.har** - Record file uploads, downloads
- **customer_feedback.har** - Record CSAT surveys, feedback forms

## 🚀 Usage

After recording HAR files and generating workflows:

```bash
# Record HAR file (example)
# 1. Open browser dev tools → Network tab
# 2. Navigate and perform workflow
# 3. Save as HAR file

# Generate workflow from HAR
python3 HARFIles/har_to_workflow.py your_file.har YourWorkflowName customer_portal

# Test the workflow
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py YourWorkflowNameUser --users=5 --spawn-rate=1
```

## 📁 File Organization

```
customer_portal/
├── README.md                    # This file
├── workflow_name_user.py        # Generated workflow files
└── __init__.py                  # Python module initialization
```

## 🎯 Priority

- **High**: Core business functionality that directly impacts customer experience
- **Medium**: Important features that support business operations
- **Low**: Nice-to-have features and edge cases

## 📝 Recording Instructions

### Customer Onboarding (HIGH PRIORITY)
1. Use a fresh browser session (incognito mode)
2. Login as a customer user
3. Record the complete first-time project experience:
   - Initial project dashboard load
   - First task interaction
   - Project overview navigation
   - Team member introductions

### Customer Dashboard (HIGH PRIORITY)
1. Login as existing customer
2. Record dashboard usage:
   - Project status overview
   - Task list viewing
   - Progress indicators
   - Navigation between sections

### Customer Tasks (HIGH PRIORITY)
1. Record task-related workflows:
   - Viewing task details
   - Updating task status
   - Adding task comments
   - Task dependencies viewing

### Customer Messaging (MEDIUM PRIORITY)
1. Record communication flows:
   - Sending messages to project team
   - Viewing message history
   - File sharing in messages
   - Notification interactions

### Customer File Sharing (MEDIUM PRIORITY)
1. Record file operations:
   - Uploading documents
   - Downloading project files
   - File preview functionality
   - Version management

### Customer Feedback (LOW PRIORITY)
1. Record feedback workflows:
   - CSAT survey completion
   - Project feedback submission
   - Rating and review processes

## 📝 Notes

- Focus on realistic customer journeys that represent actual business value
- Include error scenarios and edge cases where appropriate
- Consider mobile/responsive design workflows where applicable
- Test different customer personas (new vs experienced users)
- Capture authentic wait times between user actions 