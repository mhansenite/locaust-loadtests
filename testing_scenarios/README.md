# Testing Scenarios

This directory contains organized load test scenarios for different aspects of the application.

## Directory Structure

```
testing_scenarios/
├── project.py           # Main project lifecycle testing
├── project_stress.py    # Stress testing for rapid creation
├── messages.py          # Messaging functionality tests  
└── README.md           # This file
```

## Test Files

### `project.py` - Project Lifecycle Testing

**Class:** `ProjectPhaseMilestoneLoadTest`

**Purpose:** Comprehensive testing of project, phase, milestone, and task creation with realistic user behavior patterns.

**Key Features:**
- Project creation and deletion (configurable)
- Smart phase distribution (maintains 2-3 milestones per phase)
- Milestone creation with random phase selection
- Task creation (1-10 tasks per milestone batch)
- Task updates with realistic data patterns
- Moderate wait times (3-8 seconds) for realistic simulation

**Task Weights:**
- `view_project_plan` (6) - Primary viewing activity
- `create_test_phase` (6) - Phase creation for distribution
- `create_task` (5) - Batch task creation
- `create_milestone` (4) - Milestone creation
- `update_existing_tasks` (3) - Task management

### `project_stress.py` - Stress Testing

**Class:** `ProjectStressTest`

**Purpose:** High-frequency creation testing to stress test the system under rapid entity creation loads.

**Key Features:**
- Rapid task creation (highest frequency)
- Fast milestone creation
- Quick phase creation
- Minimal wait times (1-3 seconds) for maximum load
- Environment variable configuration

**Task Weights:**
- `create_stress_task` (8) - High-frequency task creation
- `create_stress_milestone` (5) - Rapid milestone creation
- `create_stress_phase_task` (1) - Phase creation as needed

### `messages.py` - Messaging Tests

**Classes:** `MessagingLoadTest`, `MessageStressTest`

**Purpose:** Testing messaging functionality including gRPC-Web communication.

**Note:** This file was moved here from `locust_tests/` for better organization.

## Environment Variables

Both project test files support extensive configuration:

### Project Management
```bash
CREATE_NEW_PROJECT="true|false"    # Whether to create new projects
PROJECT_NAME_TXT="LoadTestProject" # Base name for projects
PROJECT_ID="uuid"                  # Existing project ID (when CREATE_NEW_PROJECT=false)
```

### Phase Management
```bash
CREATE_NEW_PHASE="true|false"      # Whether to create new phases
PHASE_ID="uuid"                    # Existing phase ID (when CREATE_NEW_PHASE=false)
TEST_PHASE_NAME="LoadTestPhase"    # Base name for phases
```

### Content Configuration
```bash
TEST_MILESTONE_NAME="LoadTestMilestone" # Base name for milestones
TEST_TASK_NAME="LoadTestTask"           # Base name for tasks
```

### Authentication
```bash
LOGIN_EMAIL="user@example.com"
LOGIN_PASSWORD="password"
LOCUST_HOST="https://app.staging.guidecx.io"
```

## Usage Examples

### Standard Load Testing
```bash
# Run normal project lifecycle testing
locust -f testing_scenarios/project.py --users 5 --spawn-rate 1

# Run with environment variables for new project creation
CREATE_NEW_PROJECT="true" PROJECT_NAME_TXT="MyLoadTest" \
locust -f testing_scenarios/project.py --users 5 --spawn-rate 1
```

### Stress Testing
```bash
# Run high-frequency stress testing
locust -f testing_scenarios/project_stress.py --users 10 --spawn-rate 2

# Run headless stress test for 5 minutes
locust -f testing_scenarios/project_stress.py \
  --users 15 --spawn-rate 3 --run-time 300s --headless
```

### Using Existing Project/Phase
```bash
# Test with existing project and phase
CREATE_NEW_PROJECT="false" PROJECT_ID="existing-uuid" \
CREATE_NEW_PHASE="false" PHASE_ID="existing-phase-uuid" \
locust -f testing_scenarios/project.py --users 3 --spawn-rate 1
```

### Quick Testing (Single Run)
```bash
# Test basic functionality without Locust UI
python testing_scenarios/project.py
python testing_scenarios/project_stress.py
```

## Test Strategies

### Normal Load Testing (`project.py`)
- **Use case:** Simulate realistic user behavior
- **Characteristics:** Moderate creation rates, realistic wait times, smart distribution
- **Recommended users:** 5-20 concurrent users
- **Best for:** Baseline performance testing, realistic load simulation

### Stress Testing (`project_stress.py`)
- **Use case:** Test system limits and rapid creation capabilities
- **Characteristics:** High-frequency creation, minimal wait times, rapid scaling
- **Recommended users:** 10-50+ concurrent users
- **Best for:** Capacity testing, system limit discovery, performance bottleneck identification

### Mixed Testing
```bash
# Run both simultaneously for comprehensive testing
# Terminal 1:
locust -f testing_scenarios/project.py --users 10 --spawn-rate 1 --web-port 8089

# Terminal 2: 
locust -f testing_scenarios/project_stress.py --users 5 --spawn-rate 1 --web-port 8090
```

## Data Management

### Project Cleanup
- **Normal mode:** Project deletion is temporarily disabled for inspection
- **Enable cleanup:** Uncomment deletion calls in `on_stop()` methods
- **Naming:** All created entities use timestamps and UUIDs for uniqueness

### Test Data Isolation
- Projects: `LoadTestProject-{timestamp}-{uuid}`
- Phases: `LoadTestPhase-{timestamp}-{uuid}`
- Milestones: `LoadTestMilestone-{timestamp}-{uuid}`
- Tasks: `LoadTestTask-{timestamp}-{uuid}`

## Best Practices

### Environment Setup
1. Use separate test environments
2. Configure appropriate user permissions
3. Monitor system resources during tests
4. Use test-specific naming conventions

### Test Execution
1. Start with low user counts (1-5)
2. Gradually increase load based on system response
3. Monitor both application and infrastructure metrics
4. Use realistic data patterns

### Results Analysis
1. Focus on response times for creation operations
2. Monitor database performance during rapid creation
3. Check for memory leaks during extended runs
4. Validate data integrity after test completion

## Common Issues

### Authentication
- Ensure user has project creation permissions
- Verify login credentials are correct
- Check session timeout settings

### Performance
- Database connection pool limits
- File system I/O for project storage
- Memory usage during rapid creation
- Network latency for API calls

### Data Integrity
- Verify all created entities are properly linked
- Check for orphaned tasks/milestones
- Validate project hierarchy consistency 