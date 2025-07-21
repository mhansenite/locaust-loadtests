from locust import task
from auth.base_user import AuthenticatedUser
from auth.config import (
    BASE_URL_API, PROJECT_URL, APP_DOMAIN, API_DOMAIN, DEBUG
)


class ProjectUser(AuthenticatedUser):
    """
    User focused on project-related activities.
    Includes browsing projects, authentication verification, etc.
    """
    
    # Relative weight when multiple user classes exist
    weight = 1

    @task
    def verify_authenticated_access(self):
        """
        Continuously verify that we can make authenticated API calls
        This simulates ongoing user activity after login
        """
        # Make a simple authenticated API call to verify session is still valid
        with self.rest(
            "POST",
            f"{BASE_URL_API}/graphql?CountNotifications",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": API_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects?host={APP_DOMAIN}",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "CountNotifications",
                "variables": {},
                "query": "query CountNotifications {\n  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])\n  mentions: unreadNotificationsCount(types: [COMMUNICATION])\n}\n",
            },
            name="Verify Authentication"
        ) as resp:
            if resp.status_code != 200:
                resp.failure(f"Authentication verification failed: {resp.status_code}")

    @task(weight=4)
    def browse_project_list(self):
        """
        Simulate user browsing the project list with pagination and filters
        This is a common activity so it gets higher weight
        """
        with self.rest(
            "POST",
            f"{BASE_URL_API}/graphql?GetProjectList",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Host": API_DOMAIN,
                "Origin": PROJECT_URL,
                "Referer": f"{PROJECT_URL}/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "authorization": self.get_auth_header(),
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "GetProjectList",
                "variables": {
                    "input": {
                        "listInputs": {
                            "perPage": 10,
                            "page": 1,
                            "keyword": "",
                            "sortBy": "NAME",
                            "sortDirection": "ASC",
                        },
                        "projectFilters": {
                            "context": "PROVIDER",
                            "statuses": ["ON_TIME", "ON_HOLD", "LATE"],
                        },
                    }
                },
                "query": """query GetProjectList($input: projectListInput!) {
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
}""",
            },
            name="Browse Project List"
        ) as resp:
            if resp.status_code != 200:
                if DEBUG:
                    print(f"❌ Browse project list failed: {resp.status_code}")
                    response_text = resp.text or "No response text"
                    print(f"   Response text: {response_text[:500]}...")  # First 500 chars
                resp.failure(f"Browse project list failed: {resp.status_code}")
            else:
                # Optional: Print success data too
                try:
                    data = resp.json()
                    # Extract project count safely
                    if 'data' in data and 'projects' in data['data'] and 'projects' in data['data']['projects']:
                        project_count = len(data['data']['projects']['projects'])
                        if DEBUG:
                            print(f"✅ Browse project list success: Found {project_count} projects")
                    else:
                        if DEBUG:
                            print(f"✅ Browse project list success: {resp.status_code} (unexpected response structure)")
                except Exception as e:
                    if DEBUG:
                        print(f"✅ Browse project list success: {resp.status_code} (couldn't parse JSON: {e})") 