# Performance Workflows

Performance and stress testing scenarios for the GuideCX platform.

## 📋 Workflows Needed

- **high_load_user.py** - High concurrent user load scenarios
- **data_intensive_user.py** - Large dataset handling
- **concurrent_editing_user.py** - Multiple users editing simultaneously
- **peak_hours_user.py** - Peak business hours simulation
- **failover_testing_user.py** - System resilience testing

## 🎬 HAR Files to Record

- **high_load.har** - Record workflows under high load conditions
- **data_intensive.har** - Record large data operations
- **concurrent_editing.har** - Record simultaneous editing scenarios
- **peak_hours.har** - Record peak usage scenarios
- **failover_testing.har** - Record system failover scenarios

## 🚀 Usage

After recording HAR files and generating workflows:

```bash
# Generate workflow from HAR
python3 HARFIles/har_to_workflow.py your_file.har YourWorkflowName performance

# Test the workflow (with higher user counts)
export TEST_DATA_CSV=config/test_data_staging.csv
locust -f guidex_loadtest.py YourWorkflowNameUser --users=50 --spawn-rate=5
```

## 📁 File Organization

```
performance/
├── README.md                    # This file
├── workflow_name_user.py        # Generated workflow files
└── __init__.py                  # Python module initialization
```

## 🎯 Priority

- **High**: High load and concurrent user scenarios
- **Medium**: Data-intensive operations and peak hours
- **Low**: Advanced failover and resilience testing

## 📝 Recording Instructions

### High Load (HIGH PRIORITY)
1. Record workflows designed for high concurrent user loads:
   - Standard user workflows optimized for scale
   - Minimal wait times between actions
   - Focus on core business operations
   - Streamlined navigation patterns
   - Essential functionality only

### Data Intensive (HIGH PRIORITY)
1. Record workflows with large data operations:
   - Loading large project lists
   - Bulk data imports/exports
   - Complex report generation
   - Large file operations
   - Database-heavy queries

### Concurrent Editing (MEDIUM PRIORITY)
1. Record scenarios for simultaneous editing:
   - Multiple users editing same project
   - Concurrent task updates
   - Real-time collaboration workflows
   - Conflict resolution scenarios
   - Version control interactions

### Peak Hours (MEDIUM PRIORITY)
1. Record typical peak business hour activities:
   - Morning project check-ins
   - End-of-day status updates
   - Meeting preparation workflows
   - Deadline-driven activities
   - High-frequency user interactions

### Failover Testing (LOW PRIORITY)
1. Record system resilience scenarios:
   - Graceful degradation workflows
   - Error recovery procedures
   - Timeout handling
   - Retry mechanisms
   - System recovery patterns

## 📝 Performance Testing Strategies

### Load Testing Scenarios
```bash
# Light Load (baseline)
locust -f performance_workflow.py --users=5 --spawn-rate=1 --run-time=5m

# Medium Load 
locust -f performance_workflow.py --users=25 --spawn-rate=5 --run-time=10m

# Heavy Load
locust -f performance_workflow.py --users=100 --spawn-rate=10 --run-time=15m

# Stress Testing
locust -f performance_workflow.py --users=200 --spawn-rate=20 --run-time=20m
```

### Monitoring Key Metrics
- Response times (p50, p95, p99)
- Error rates and types
- Throughput (requests per second)
- System resource utilization
- Database performance
- Cache hit rates

### Performance Benchmarks
Establish baseline performance metrics:
- Page load times < 2 seconds
- API response times < 500ms
- File upload success rate > 99%
- Concurrent user support: 100+ users
- System availability > 99.9%

## 📝 Notes

- Focus on realistic user behavior patterns
- Include think time for realistic load simulation
- Test both read and write-heavy operations
- Monitor system resources during testing
- Include error scenarios and edge cases
- Test across different network conditions
- Consider geographic distribution of users
- Validate performance against SLA requirements 