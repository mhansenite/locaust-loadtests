# Messaging Workflows

Communication and collaboration workflows for the GuideCX platform.

## 📋 Workflows Needed

- **project_messaging_user.py** - Project-specific messaging and channels
- **team_communication_user.py** - Internal team messaging
- **customer_communication_user.py** - Customer-team communication
- **message_attachments_user.py** - File sharing in messages
- **message_mentions_user.py** - @mentions and notifications
- **message_search_user.py** - Message history and search

## 🎬 HAR Files to Record

- **project_messaging.har** - Record project channel messaging
- **team_communication.har** - Record internal team chat flows
- **customer_communication.har** - Record customer-team messaging
- **message_attachments.har** - Record file sharing in messages
- **message_mentions.har** - Record @mentions and notifications
- **message_search.har** - Record message search and history

## 🚀 Usage

After recording HAR files and generating workflows:

```bash
# Generate workflow from HAR
python3 HARFIles/har_to_workflow.py your_file.har YourWorkflowName messaging

# Test the workflow
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py YourWorkflowNameUser --users=5 --spawn-rate=1
```

## 📁 File Organization

```
messaging/
├── README.md                    # This file
├── workflow_name_user.py        # Generated workflow files
└── __init__.py                  # Python module initialization
```

## 🎯 Priority

- **High**: Core messaging functionality (project messaging, customer communication)
- **Medium**: File attachments and mentions
- **Low**: Advanced search and history features

## 📝 Recording Instructions

### Project Messaging (HIGH PRIORITY)
1. Record project-specific messaging:
   - Opening project message channels
   - Sending messages within project context
   - Real-time message updates
   - Channel navigation

### Customer Communication (HIGH PRIORITY)
1. Record customer-team messaging:
   - Customer sending messages to project team
   - Team responding to customer messages
   - Message threading and conversations
   - Notification delivery

### Team Communication (MEDIUM PRIORITY)
1. Record internal team messaging:
   - Team member to team member communication
   - Private team channels
   - Group messaging workflows
   - Status updates and coordination

### Message Attachments (MEDIUM PRIORITY)
1. Record file sharing in messages:
   - Uploading files to messages
   - Downloading message attachments
   - File preview in message context
   - Multiple file attachments

### Message Mentions (LOW PRIORITY)
1. Record @mention functionality:
   - Mentioning team members
   - Mention notifications
   - Mention navigation and responses

### Message Search (LOW PRIORITY)
1. Record message search and history:
   - Searching message history
   - Filtering messages by date/user
   - Message thread navigation
   - Archive and retrieval

## 📝 Notes

- Focus on real-time messaging performance under load
- Test message delivery and notification systems
- Include error scenarios (failed message delivery)
- Consider mobile messaging workflows
- Test concurrent messaging scenarios 