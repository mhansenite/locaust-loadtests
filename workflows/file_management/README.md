# File Management Workflows

File upload, storage, and sharing workflows for the GuideCX platform.

## 📋 Workflows Needed

- **file_upload_user.py** - Document and file uploading
- **file_download_user.py** - File access and downloading
- **file_sharing_user.py** - File sharing with customers and teams
- **file_organization_user.py** - File categorization and organization
- **large_file_handling_user.py** - Large file upload/download stress testing
- **file_versioning_user.py** - File version management

## 🎬 HAR Files to Record

- **file_upload.har** - Record various file upload scenarios
- **file_download.har** - Record file download and access
- **file_sharing.har** - Record file sharing workflows
- **file_organization.har** - Record file management and organization
- **large_file_handling.har** - Record large file operations
- **file_versioning.har** - Record file version management

## 🚀 Usage

After recording HAR files and generating workflows:

```bash
# Generate workflow from HAR
python3 HARFIles/har_to_workflow.py your_file.har YourWorkflowName file_management

# Test the workflow
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py YourWorkflowNameUser --users=5 --spawn-rate=1
```

## 📁 File Organization

```
file_management/
├── README.md                    # This file
├── workflow_name_user.py        # Generated workflow files
└── __init__.py                  # Python module initialization
```

## 🎯 Priority

- **High**: Core file operations (upload/download)
- **Medium**: File sharing and organization
- **Low**: Advanced features like versioning

## 📝 Recording Instructions

### File Upload (HIGH PRIORITY)
1. Record various file upload scenarios:
   - Single file uploads (PDF, DOC, images)
   - Multiple file uploads
   - Drag and drop uploads
   - Upload progress and validation
   - Upload error handling

### File Download (HIGH PRIORITY)
1. Record file download workflows:
   - Direct file downloads
   - Bulk file downloads
   - File preview before download
   - Download from different contexts (project, messages, etc.)

### File Sharing (MEDIUM PRIORITY)
1. Record file sharing workflows:
   - Sharing files with customers
   - Sharing files with team members
   - Permission-based file access
   - Shared folder management

### File Organization (MEDIUM PRIORITY)
1. Record file organization workflows:
   - Creating file folders
   - Moving files between folders
   - File categorization and tagging
   - File search and filtering

### Large File Handling (LOW PRIORITY)
1. Record large file operations:
   - Uploading files >10MB
   - Large file download performance
   - Progress tracking for large files
   - Timeout and retry scenarios

### File Versioning (LOW PRIORITY)
1. Record file version management:
   - Uploading new file versions
   - Viewing version history
   - Downloading specific versions
   - Version comparison workflows

## 📝 Notes

- Test different file types and sizes
- Include error scenarios (file too large, unsupported format)
- Test concurrent file operations
- Consider mobile file operations
- Focus on upload/download performance under load
- Test file storage limitations and quotas 