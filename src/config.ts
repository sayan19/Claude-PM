export interface JiraConfig {
  baseUrl: string;
  token: string;
}

export function loadConfig(): JiraConfig {
  const baseUrl = process.env["JIRA_BASE_URL"];
  const token = process.env["JIRA_PAT"];

  if (!baseUrl) {
    throw new Error("JIRA_BASE_URL environment variable is required (e.g. https://jira.yourcompany.com)");
  }
  if (!token) {
    throw new Error("JIRA_PAT environment variable is required (Personal Access Token)");
  }

  return { baseUrl: baseUrl.replace(/\/+$/, ""), token };
}
