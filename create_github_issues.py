import requests
from datetime import datetime

# GitHub configuration
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
REPO_OWNER = 'YOUR_GITHUB_USERNAME'
REPO_NAME = 'YOUR_REPOSITORY_NAME'
API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Define categories and tasks
categories = {
    "Planning & Research": [
        {"title": "Define project scope", "deadline": "2024-06-30", "priority": "High", "labels": ["Planning"]},
        {"title": "Competitor analysis", "deadline": "2024-07-05", "priority": "Medium", "labels": ["Research"]},
        {"title": "User persona development", "deadline": "2024-07-07", "priority": "High", "labels": ["Planning"]}
    ],
    "Design": [
        {"title": "Create wireframes", "deadline": "2024-07-15", "priority": "High", "labels": ["Design"]},
        {"title": "Design mockups", "deadline": "2024-07-20", "priority": "Medium", "labels": ["Design"]},
        {"title": "Design review and approval", "deadline": "2024-07-25", "priority": "Medium", "labels": ["Design"]}
    ],
    "Development": [
        {"title": "Set up development environment", "deadline": "2024-07-10", "priority": "High", "labels": ["Setup"]},
        {"title": "Frontend development", "deadline": "2024-08-10", "priority": "High", "labels": ["Development"]},
        {"title": "Backend development", "deadline": "2024-08-20", "priority": "High", "labels": ["Development"]},
        {"title": "Integrate API", "deadline": "2024-08-25", "priority": "Medium", "labels": ["Integration"]}
    ],
    "Content Creation": [
        {"title": "Develop content strategy", "deadline": "2024-07-12", "priority": "Medium", "labels": ["Content"]},
        {"title": "Write website copy", "deadline": "2024-08-15", "priority": "High", "labels": ["Content"]},
        {"title": "Gather images and videos", "deadline": "2024-08-10", "priority": "Medium", "labels": ["Content"]}
    ],
    "Testing & QA": [
        {"title": "Unit testing", "deadline": "2024-08-30", "priority": "High", "labels": ["Testing"]},
        {"title": "Usability testing", "deadline": "2024-09-05", "priority": "Medium", "labels": ["Testing"]},
        {"title": "Bug fixing", "deadline": "2024-09-10", "priority": "High", "labels": ["QA"]}
    ],
    "Deployment": [
        {"title": "Prepare deployment checklist", "deadline": "2024-09-12", "priority": "Medium", "labels": ["Deployment"]},
        {"title": "Deploy to production server", "deadline": "2024-09-15", "priority": "High", "labels": ["Deployment"]},
        {"title": "Post-deployment testing", "deadline": "2024-09-17", "priority": "High", "labels": ["QA"]}
    ],
    "Maintenance & Updates": [
        {"title": "Monitor website performance", "deadline": "", "priority": "High", "labels": ["Maintenance"]},
        {"title": "Regular content updates", "deadline": "", "priority": "Medium", "labels": ["Content"]},
        {"title": "Security audits", "deadline": "", "priority": "High", "labels": ["Maintenance"]}
    ]
}

# Function to create an issue in GitHub
def create_github_issue(title, body, labels, due_date):
    issue = {
        'title': title,
        'body': body,
        'labels': labels
    }
    response = requests.post(API_URL, headers=headers, json=issue)
    if response.status_code == 201:
        issue_data = response.json()
        if due_date:
            due_date_str = due_date.strftime('%Y-%m-%dT%H:%M:%SZ')
            requests.patch(issue_data['url'], headers=headers, json={"due_on": due_date_str})
        print(f"Issue '{title}' created successfully.")
    else:
        print(f"Failed to create issue '{title}': {response.content}")

# Create categorized tasks as GitHub issues
for category, tasks in categories.items():
    for task in tasks:
        title = f"[{category}] {task['title']}"
        body = f"**Priority**: {task['priority']}\n**Deadline**: {task['deadline'] or 'N/A'}"
        labels = task['labels']
        due_date = datetime.strptime(task['deadline'], "%Y-%m-%d") if task['deadline'] else None
        create_github_issue(title, body, labels, due_date)

print("All tasks created in GitHub repository successfully!")
