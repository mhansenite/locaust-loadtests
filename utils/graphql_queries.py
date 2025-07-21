"""
Reusable GraphQL queries for GuideX load testing.
Centralizes all GraphQL operations for easier maintenance.
"""

# =============================================================================
# AUTHENTICATION & SESSION QUERIES
# =============================================================================

COUNT_NOTIFICATIONS_QUERY = """
query CountNotifications {
  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])
  mentions: unreadNotificationsCount(types: [COMMUNICATION])
}
"""

# =============================================================================
# PROJECT-RELATED QUERIES
# =============================================================================

GET_PROJECT_LIST_QUERY = """
query GetProjectList($input: projectListInput!) {
  projects(input: $input) {
    maxCashValue
    projects {
      ...ProjectRowProjectList
      __typename
    }
    pageInfo {
      ...PageInfoProjectList
      __typename
    }
    appliedFilters {
      ...AppliedFiltersProjectList
      __typename
    }
    __typename
  }
}

fragment PageInfoProjectList on PageInfoType {
  currentPage
  isOutOfBounds
  limit
  totalPages
  totalResults
  __typename
}

fragment AppliedFiltersProjectList on AppliedProjectFilters {
  context
  statuses
  tags
  strict
  brandNames
  customerIds
  cashValueRange
  projectId
  projectLateDays
  projectManagerIds
  templateIds
  projectFiltersOperator {
    tagOperator
    templateOperator
    milestoneOperator
    __typename
  }
  activeMilestoneNames
  endOn
  startOn
  filterDateBy
  lastUpdatedDays
  __typename
}

fragment ProjectRowProjectList on ProjectType {
  id
  name
  cashValue
  totalTasksCount
  openTasksCount
  openActionItemsCount
  overdueTasksCount
  completedAt
  startOn
  endOn
  projectStatusChangeReasons {
    ...ProjectStatusChangeReasonsProjectList
    __typename
  }
  completedAt
  forecastedEndOn
  deletedAt
  archivedAt
  currentUserSettings {
    projectView
    restrictAccess
    __typename
  }
  currentUserProjectContext
  currentUserRestrictedAccess
  lastActivityAt
  projectManager {
    ...ProjectManagerProjectList
    __typename
  }
  status
  customerV2 {
    ...ProjectCustomerProjectList
    __typename
  }
  projectType
  templates {
    id
    milestones {
      id
      name
      active
      __typename
    }
    __typename
  }
  organization {
    id
    name
    logo {
      originalUrl
      __typename
    }
    __typename
  }
  displayOrganization {
    name
    logo {
      originalUrl
      __typename
    }
    __typename
  }
  brand {
    ...ProjectBrandProjectList
    __typename
  }
  tags {
    ...ProjectListTable_ProjectTag
    __typename
  }
  errors: errorsCount
  __typename
}

fragment ProjectListTable_ProjectTag on TagType {
  id
  name
  color
  internalOnly
  __typename
}

fragment ProjectCustomerProjectList on CustomerType {
  id
  name
  logo {
    originalUrl
    __typename
  }
  __typename
}

fragment ProjectBrandProjectList on BrandType {
  id
  name
  logo {
    originalUrl
    __typename
  }
  __typename
}

fragment ProjectManagerProjectList on UserType {
  id
  firstName
  lastName
  status
  avatar {
    originalUrl
    __typename
  }
  __typename
}

fragment ProjectStatusChangeReasonsProjectList on ProjectStatusChangeReasonType {
  id
  name
  description
  createdAt
  updatedAt
  user {
    id
    firstName
    lastName
    avatar {
      originalUrl
      __typename
    }
    __typename
  }
  statusChangeReason {
    id
    name
    statusChangeReasonGroup {
      id
      name
      __typename
    }
    __typename
  }
  __typename
}
"""

# =============================================================================
# TASK-RELATED QUERIES (PLACEHOLDERS)
# =============================================================================

# TODO: Replace these with actual captured queries from the browser
GET_GLOBAL_TASKS_QUERY = """
query GetGlobalTasks($input: TaskListInput!) {
    tasks(input: $input) {
        tasks {
            id
            name
            description
            status
            dueDate
            project {
                id
                name
            }
            assignee {
                id
                firstName
                lastName
            }
        }
        pageInfo {
            currentPage
            totalPages
            totalResults
        }
    }
}
"""

GET_FILTERED_TASKS_QUERY = """
query GetFilteredTasks($input: TaskListInput!) {
    tasks(input: $input) {
        tasks {
            id
            name
            status
            dueDate
        }
        pageInfo {
            currentPage
            totalPages
            totalResults
        }
    }
}
"""

GET_TASK_DETAILS_QUERY = """
query GetTaskDetails($taskId: ID!) {
    task(id: $taskId) {
        id
        name
        description
        status
        dueDate
        project {
            id
            name
        }
        assignee {
            id
            firstName
            lastName
            email
        }
        comments {
            id
            content
            createdAt
            author {
                firstName
                lastName
            }
        }
    }
}
"""

# =============================================================================
# MUTATION QUERIES
# =============================================================================

UPDATE_TASK_STATUS_MUTATION = """
mutation UpdateTaskStatus($taskId: ID!, $status: TaskStatus!) {
    updateTaskStatus(taskId: $taskId, status: $status) {
        id
        status
        updatedAt
    }
}
"""

# =============================================================================
# COMMON VARIABLES
# =============================================================================

def get_project_list_variables(page=1, per_page=10, sort_by="NAME", sort_direction="ASC"):
    """
    Generate variables for project list query
    """
    return {
        "input": {
            "listInputs": {
                "perPage": per_page,
                "page": page,
                "keyword": "",
                "sortBy": sort_by,
                "sortDirection": sort_direction,
            },
            "projectFilters": {
                "context": "PROVIDER",
                "statuses": ["ON_TIME", "ON_HOLD", "LATE"],
            },
        }
    }

def get_global_tasks_variables(page=1, per_page=20, statuses=None):
    """
    Generate variables for global tasks query
    """
    if statuses is None:
        statuses = ["OPEN", "IN_PROGRESS"]
    
    return {
        "input": {
            "perPage": per_page,
            "page": page,
            "filters": {
                "statuses": statuses,
            }
        }
    } 