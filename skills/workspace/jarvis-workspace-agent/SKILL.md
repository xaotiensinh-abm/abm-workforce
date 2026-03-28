---
name: jarvis-workspace-agent
description: >
  W10: Google Workspace Agent. Quản lý Drive, Gmail, Calendar, Sheets, Docs,
  Slides, Tasks, Chat, Meet qua gws CLI. 96 skills tích hợp.
  Auto-activate khi task liên quan đến email, drive, calendar, sheets, docs,
  workspace, google, gws, meeting, schedule, file sharing, spreadsheet.
---

# 🏢 W10: WorkspaceAgent — Google Workspace Manager

> Jarvis Worker quản lý toàn bộ Google Workspace thông qua `gws` CLI.

## When to Activate

Khi user yêu cầu bất kỳ thao tác nào liên quan:
- **Drive**: upload, download, search, share files, organize folders
- **Gmail**: send email, read inbox, label, filter, draft, attachment
- **Calendar**: create event, check schedule, find free time, meeting prep
- **Sheets**: create spreadsheet, read data, append rows
- **Docs**: create document, write content, template-based
- **Slides**: create presentation
- **Tasks**: manage task lists, create/complete tasks
- **Chat**: send messages to spaces
- **Cross-service workflows**: email-to-task, standup report, weekly digest

## Prerequisites

```bash
# gws CLI must be installed and authenticated
gws --version     # verify installed
gws auth status   # verify auth
```

## Architecture

```
W10: WorkspaceAgent
└── SA-24: WorkspaceOpsSubAgent
    ├── 16 Core service skills (gws-drive, gws-gmail, ...)
    ├── 13 Shortcut skills (gws-gmail-send, ...)
    ├── 6 Workflow skills (gws-workflow-*, ...)
    ├── 10 Persona skills (persona-exec-assistant, ...)
    ├── 50 Recipe skills (recipe-*, ...)
    └── 1 Shared skill (gws-shared)
```

## How to Use

### Basic Pattern
```bash
gws <service> <resource> <method> --params '{...}' --json '{...}'
```

### Common Operations

```bash
# List files
gws drive files list --params '{"pageSize": 10}'

# Send email
gws gmail users messages send --params '{"userId": "me"}' --json '{"raw": "base64"}'

# Create event
gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Meeting"}'

# Read spreadsheet
gws sheets spreadsheets values get --params '{"spreadsheetId": "ID", "range": "Sheet1!A1:C10"}'

# Create document
gws docs documents create --json '{"title": "Report"}'
```

### Workflow Examples

```bash
# Today's standup: meetings + open tasks
# → Use gws-workflow-standup-report skill

# Convert email to task
# → Use gws-workflow-email-to-task skill

# Weekly digest: meetings + unread count
# → Use gws-workflow-weekly-digest skill
```

## PowerShell Note

```powershell
# Escape double quotes in PowerShell
gws drive files list --params '{\"pageSize\": 5}'
```

## Safety Rules

1. **HITL required** for: delete, share-public, bulk operations (>10 items)
2. Use `--dry-run` flag for destructive operations preview
3. Verify `gws auth status` before first command in session

## Cross-Worker Collaboration

| Scenario | Worker |
|---|---|
| Draft email content | W02: ContentAgent |
| Business reports from Sheets data | W03: BusinessAgent |
| Data pipelines to/from Sheets | W05: DataAgent |
| Security audit of shared resources | W06: SecurityAgent |

## Related Skills

Read individual skill files for detailed usage:
- `gws-shared/SKILL.md` — Auth patterns, CLI reference
- `gws-drive/SKILL.md` — Drive file operations
- `gws-gmail/SKILL.md` — Gmail operations
- `gws-calendar/SKILL.md` — Calendar management
- `gws-sheets/SKILL.md` — Spreadsheet operations
