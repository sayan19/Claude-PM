import axios, { type AxiosInstance } from "axios";
import type { JiraConfig } from "./config.js";

export interface JiraIssue {
  key: string;
  fields: {
    summary: string;
    status: { name: string };
    assignee: { displayName: string } | null;
    priority: { name: string } | null;
    issuetype: { name: string };
    created: string;
    updated: string;
    [key: string]: unknown;
  };
}

export interface JiraSearchResult {
  startAt: number;
  maxResults: number;
  total: number;
  issues: JiraIssue[];
}

export interface JiraBoard {
  id: number;
  name: string;
  type: string;
}

export interface JiraSprint {
  id: number;
  name: string;
  state: string;
  startDate?: string;
  endDate?: string;
}

export interface JiraProject {
  key: string;
  name: string;
  projectTypeKey: string;
}

export class JiraClient {
  private http: AxiosInstance;

  constructor(config: JiraConfig) {
    this.http = axios.create({
      baseURL: config.baseUrl,
      headers: {
        Authorization: `Bearer ${config.token}`,
        Accept: "application/json",
      },
    });
  }

  async searchIssues(jql: string, maxResults = 50, startAt = 0): Promise<JiraSearchResult> {
    const res = await this.http.get<JiraSearchResult>("/rest/api/2/search", {
      params: { jql, maxResults, startAt },
    });
    return res.data;
  }

  async getIssue(issueKey: string): Promise<JiraIssue> {
    const res = await this.http.get<JiraIssue>(`/rest/api/2/issue/${encodeURIComponent(issueKey)}`);
    return res.data;
  }

  async getProjects(): Promise<JiraProject[]> {
    const res = await this.http.get<JiraProject[]>("/rest/api/2/project");
    return res.data;
  }

  async getBoards(): Promise<JiraBoard[]> {
    const res = await this.http.get<{ values: JiraBoard[] }>("/rest/agile/1.0/board");
    return res.data.values;
  }

  async getSprints(boardId: number): Promise<JiraSprint[]> {
    const res = await this.http.get<{ values: JiraSprint[] }>(
      `/rest/agile/1.0/board/${boardId}/sprint`
    );
    return res.data.values;
  }

  async getSprintIssues(sprintId: number, maxResults = 50): Promise<JiraSearchResult> {
    const res = await this.http.get<JiraSearchResult>(
      `/rest/agile/1.0/sprint/${sprintId}/issue`,
      { params: { maxResults } }
    );
    return res.data;
  }
}
