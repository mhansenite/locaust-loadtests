# 🚀 Quick Start Guide - Test Configurations

Super simple way to run load tests with predefined configurations!

## 🎯 **Easiest Method - Use Shell Script**

### **Step 1: See all available tests**
```bash
source TestFiles/test_configurations.sh
```

### **Step 2: Pick a test and run it**
```bash
# Load Test 1 configuration and run it
source TestFiles/test_configurations.sh 1
locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2

# Or try Test 3 for heavy creation testing
source TestFiles/test_configurations.sh 3
locust -f TestFiles/master_test_controller.py --users 15 --spawn-rate 3
```

## 🔧 **Alternative Method - Python Script**

### **See all test options**
```bash
python3 TestFiles/test_configurations.py --list
```

### **See details for a specific test**
```bash
python3 TestFiles/test_configurations.py --show 1
```

### **Apply and run a test**
```bash
python3 TestFiles/test_configurations.py --test 1
locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2
```

## 🗂️ **Quick Test Reference**

| Test # | Name | What It Does | Best For |
|--------|------|--------------|----------|
| **1** | 🆕 Full New Project Creation | Creates everything from scratch | Complete testing |
| **2** | 📂 Use Existing Project | Uses existing project, focuses on tasks | Quick task testing |
| **3** | 🔥 Creation Heavy Load Test | Lots of creation operations | Stress testing creation APIs |
| **4** | 👁️ View Heavy Load Test | Lots of viewing operations | Testing read performance |
| **5** | 📝 Task Management Focus | Concentrated on task operations | Task feature testing |
| **6** | 🐛 Debug/Development Mode | Sequential, predictable behavior | Debugging issues |
| **7** | 🏗️ Project Creation Only | Only project operations | Project API testing |
| **8** | ⚡ High Performance Test | Maximum load testing | Performance benchmarking |
| **9** | 🔄 Mixed Operations Test | Realistic mix of everything | Real user simulation |
| **10** | 🧪 Custom Template | Template for your own tests | Creating custom scenarios |

## 🎉 **Most Common Usage**

### **For general testing:**
```bash
source TestFiles/test_configurations.sh 1
locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2
```

### **For task-focused testing:**
```bash
source TestFiles/test_configurations.sh 5
locust -f TestFiles/master_test_controller.py --users 8 --spawn-rate 2
```

### **For stress testing:**
```bash
source TestFiles/test_configurations.sh 3
locust -f TestFiles/master_test_controller.py --users 20 --spawn-rate 3
```

## ⚠️ **Important Notes**

1. **Update authentication**: Edit the `LOGIN_EMAIL`, `LOGIN_PASSWORD`, and `LOCUST_HOST` in your `.env` file or in the test configurations

2. **Update project/phase IDs**: For tests that use existing projects (Test 2, 4), update the `PROJECT_ID` and `PHASE_ID` values:
   ```bash
   # Edit TestFiles/test_configurations.py and change these lines:
   "PROJECT_ID": "your-actual-project-id",
   "PHASE_ID": "your-actual-phase-id",
   ```

3. **Run from project root**: Always run commands from the `/Users/mhansen/git/locaust-loadtests/` directory

## 🎛️ **What Each Configuration Controls**

- **ENABLED_MODULES**: Which test modules to run (projects, phases, milestones, tasks)
- **TEST_SCENARIO**: How often different operations happen (balanced, creation_heavy, view_heavy, task_focused)  
- **COORDINATION_MODE**: How modules work together (sequential, parallel, smart)

## 🏃‍♂️ **Ready to Run!**

Just pick a test number and go:
```bash
source TestFiles/test_configurations.sh 1
locust -f TestFiles/master_test_controller.py --users 10 --spawn-rate 2
```

That's it! Your test environment is configured and ready to run. 🎉 