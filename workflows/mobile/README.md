# Mobile Workflows

Mobile application workflows and responsive testing for the GuideCX platform.

## 📋 Workflows Needed

- **mobile_dashboard_user.py** - Mobile dashboard access and navigation
- **mobile_tasks_user.py** - Mobile task management
- **mobile_messaging_user.py** - Mobile messaging and notifications
- **mobile_file_access_user.py** - Mobile file access and sharing
- **responsive_design_user.py** - Responsive design stress testing

## 🎬 HAR Files to Record

- **mobile_dashboard.har** - Record mobile dashboard usage
- **mobile_tasks.har** - Record mobile task management
- **mobile_messaging.har** - Record mobile messaging flows
- **mobile_file_access.har** - Record mobile file operations
- **responsive_design.har** - Record responsive design interactions

## 🚀 Usage

After recording HAR files and generating workflows:

```bash
# Generate workflow from HAR
python3 HARFIles/har_to_workflow.py your_file.har YourWorkflowName mobile

# Test the workflow
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py YourWorkflowNameUser --users=5 --spawn-rate=1
```

## 📁 File Organization

```
mobile/
├── README.md                    # This file
├── workflow_name_user.py        # Generated workflow files
└── __init__.py                  # Python module initialization
```

## 🎯 Priority

- **High**: Core mobile functionality (dashboard, tasks)
- **Medium**: Mobile messaging and file operations
- **Low**: Advanced responsive design testing

## 📝 Recording Instructions

### Mobile Dashboard (HIGH PRIORITY)
1. Record mobile dashboard workflows:
   - Mobile browser navigation
   - Touch-optimized interface interactions
   - Mobile menu and navigation
   - Project overview on mobile
   - Performance on slower mobile networks

### Mobile Tasks (HIGH PRIORITY)
1. Record mobile task management:
   - Viewing tasks on mobile devices
   - Updating task status via mobile
   - Mobile task creation workflows
   - Touch interactions for task operations
   - Mobile task filtering and search

### Mobile Messaging (MEDIUM PRIORITY)
1. Record mobile messaging workflows:
   - Sending messages via mobile
   - Mobile notification handling
   - Mobile keyboard interactions
   - Touch-optimized message interface
   - Mobile file attachments

### Mobile File Access (MEDIUM PRIORITY)
1. Record mobile file operations:
   - File uploads from mobile devices
   - Mobile file downloads
   - Mobile file preview functionality
   - Camera integration for file uploads
   - Mobile file sharing workflows

### Responsive Design (LOW PRIORITY)
1. Record responsive design testing:
   - Different screen sizes and orientations
   - Tablet-specific interactions
   - Cross-device consistency testing
   - Progressive web app functionality
   - Mobile performance optimization

## 📝 Browser Setup for Mobile Recording

### Chrome Mobile Simulation
1. Open Chrome DevTools (F12)
2. Click device toolbar icon (📱) or Ctrl+Shift+M
3. Select mobile device (iPhone, Android, etc.)
4. Record HAR file while navigating mobile interface

### Real Mobile Device Testing
1. Enable remote debugging on mobile device
2. Connect device via USB
3. Use Chrome's remote debugging to record HAR
4. Capture real mobile network conditions

### Mobile User Agents
Common mobile user agents to test:
- iPhone: `Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)`
- Android: `Mozilla/5.0 (Linux; Android 11; SM-G991B)`
- iPad: `Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X)`

## 📝 Notes

- Test on various mobile devices and screen sizes
- Include slow network conditions (3G, 4G)
- Test touch interactions and gestures
- Consider mobile-specific error scenarios
- Test both portrait and landscape orientations
- Focus on mobile performance and responsiveness
- Include mobile accessibility testing 