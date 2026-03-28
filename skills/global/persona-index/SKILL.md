---
name: persona-index
description: Google Workspace persona index — 10 role-based workflows for content, support, HR, sales, IT, and project management.
---

# Goal

> **Use this skill when:** Google Workspace role-based persona workflows

Match the user's task to a specialized persona role, then apply the role's workflow patterns.

# Instructions

1. Identify which persona best fits the user's request
2. Load the persona file from `personas/[role].md`
3. Execute the workflow steps defined by that persona

# Persona Index

| Persona | Role | Key Workflows |
|---------|------|---------------|
| `content-creator` | Content production | Create, organize, distribute across Workspace |
| `customer-support` | Support agent | Track tickets, respond, escalate |
| `event-coordinator` | Event planner | Scheduling, invitations, logistics |
| `exec-assistant` | Executive assistant | Schedule, inbox, communications |
| `hr-coordinator` | HR coordinator | Onboarding, announcements, employee comms |
| `it-admin` | IT administrator | Security, Workspace config, monitoring |
| `project-manager` | Project manager | Tasks, meetings, doc sharing |
| `researcher` | Research coordinator | References, notes, collaboration |
| `sales-ops` | Sales operations | Deals, calls, client comms |
| `team-lead` | Team leader | Standups, coordination, communication |

# Constraints

- Each persona applies GWS tools in a role-specific way
- Load persona definitions from `personas/` subdirectory on demand
