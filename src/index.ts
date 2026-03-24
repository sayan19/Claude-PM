import { loadConfig } from "./config.js";
import { JiraClient } from "./jira-client.js";

function formatIssue(issue: { key: string; fields: { summary: string; status: { name: string }; assignee: { displayName: string } | null; priority: { name: string } | null; issuetype: { name: string } } }) {
  const assignee = issue.fields.assignee?.displayName ?? "Unassigned";
  const priority = issue.fields.priority?.name ?? "None";
  return `  ${issue.key}  [${issue.fields.issuetype.name}] ${issue.fields.summary}\n    Status: ${issue.fields.status.name} | Assignee: ${assignee} | Priority: ${priority}`;
}

async function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  if (!command || command === "help") {
    console.log(`Claude-PM — Jira Data Center read-only sync

Usage:
  npx claude-pm projects              List all projects
  npx claude-pm boards                List all boards
  npx claude-pm sprints <boardId>     List sprints for a board
  npx claude-pm sprint <sprintId>     Show issues in a sprint
  npx claude-pm search <JQL>          Search issues with JQL
  npx claude-pm issue <KEY>           Get a single issue

Environment variables:
  JIRA_BASE_URL   Your Jira Data Center URL (e.g. https://jira.yourcompany.com)
  JIRA_PAT        Personal Access Token for authentication`);
    return;
  }

  const config = loadConfig();
  const client = new JiraClient(config);

  switch (command) {
    case "projects": {
      const projects = await client.getProjects();
      console.log("Projects:\n");
      for (const p of projects) {
        console.log(`  ${p.key}  ${p.name}  (${p.projectTypeKey})`);
      }
      break;
    }

    case "boards": {
      const boards = await client.getBoards();
      console.log("Boards:\n");
      for (const b of boards) {
        console.log(`  [${b.id}] ${b.name}  (${b.type})`);
      }
      break;
    }

    case "sprints": {
      const boardId = Number(args[1]);
      if (!boardId) {
        console.error("Usage: sprints <boardId>");
        process.exit(1);
      }
      const sprints = await client.getSprints(boardId);
      console.log(`Sprints for board ${boardId}:\n`);
      for (const s of sprints) {
        const dates = s.startDate && s.endDate ? `${s.startDate} → ${s.endDate}` : "";
        console.log(`  [${s.id}] ${s.name}  (${s.state}) ${dates}`);
      }
      break;
    }

    case "sprint": {
      const sprintId = Number(args[1]);
      if (!sprintId) {
        console.error("Usage: sprint <sprintId>");
        process.exit(1);
      }
      const result = await client.getSprintIssues(sprintId);
      console.log(`Sprint ${sprintId} — ${result.total} issues:\n`);
      for (const issue of result.issues) {
        console.log(formatIssue(issue));
      }
      break;
    }

    case "search": {
      const jql = args.slice(1).join(" ");
      if (!jql) {
        console.error("Usage: search <JQL query>");
        process.exit(1);
      }
      const result = await client.searchIssues(jql);
      console.log(`Search results (${result.total} total, showing ${result.issues.length}):\n`);
      for (const issue of result.issues) {
        console.log(formatIssue(issue));
      }
      break;
    }

    case "issue": {
      const key = args[1];
      if (!key) {
        console.error("Usage: issue <ISSUE-KEY>");
        process.exit(1);
      }
      const issue = await client.getIssue(key);
      console.log(formatIssue(issue));
      console.log(`    Created: ${issue.fields.created}`);
      console.log(`    Updated: ${issue.fields.updated}`);
      break;
    }

    default:
      console.error(`Unknown command: ${command}. Run with "help" to see usage.`);
      process.exit(1);
  }
}

main().catch((err: unknown) => {
  if (err instanceof Error) {
    console.error("Error:", err.message);
  } else {
    console.error("Error:", err);
  }
  process.exit(1);
});
