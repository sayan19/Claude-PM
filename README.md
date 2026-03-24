# Claude-PM — Jira Data Center Integration

Read-only sync with Jira Data Center. Fetch projects, boards, sprints, and issues from the command line.

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Configure environment variables (copy `.env.example` to `.env` and fill in your values):
   ```bash
   cp .env.example .env
   ```

   | Variable | Description |
   |---|---|
   | `JIRA_BASE_URL` | Your Jira Data Center URL (e.g. `https://jira.yourcompany.com`) |
   | `JIRA_PAT` | Personal Access Token ([how to create one](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html)) |

3. Build:
   ```bash
   npm run build
   ```

## Usage

```bash
# List all projects
node dist/index.js projects

# List all boards
node dist/index.js boards

# List sprints for a board
node dist/index.js sprints <boardId>

# Show issues in a sprint
node dist/index.js sprint <sprintId>

# Search issues with JQL
node dist/index.js search "project = MYPROJ AND status = 'In Progress'"

# Get a single issue
node dist/index.js issue MYPROJ-123
```

## Programmatic Usage

```typescript
import { JiraClient } from "./jira-client.js";

const client = new JiraClient({
  baseUrl: "https://jira.yourcompany.com",
  token: "your-pat",
});

const issues = await client.searchIssues("project = MYPROJ ORDER BY updated DESC");
console.log(issues);
```
