# RAW_HAR Directory

This directory contains your original HAR (HTTP Archive) files captured from browser developer tools.

## 📁 Purpose
- **Store original HAR captures** - Keep your browser-recorded HTTP traffic here
- **Source files for conversion** - These files are used as input for the workflow converter
- **Version control friendly** - Track changes to your captured workflows over time

## 🚀 How to Add HAR Files

### 1. Capture HAR File in Browser
1. Open browser developer tools (F12)
2. Go to **Network** tab
3. **Clear** existing entries  
4. Perform your complete workflow in the application
5. **Right-click** in Network tab → **Save all as HAR**
6. Save the HAR file to this directory

### 2. Convert to Workflow
```bash
# Convert your HAR file to a load testing workflow
python3 HARFiles/har_to_workflow.py HARFiles/RAW_HAR/YourWorkflow.har WorkflowName
```

## 📊 File Organization
```
RAW_HAR/
├── GlobalProjects.har     # Project management workflow
├── GlobalTasks.har        # Task management workflow  
├── UserManagement.har     # User administration workflow
└── YourWorkflow.har       # Your custom workflow
```

## ✅ Best Practices
- **Descriptive names** - Use clear, descriptive HAR file names
- **Complete workflows** - Capture full user journeys, not just single actions
- **Clean sessions** - Start with a clean browser session for consistent captures
- **Realistic data** - Use representative data that matches production usage patterns 