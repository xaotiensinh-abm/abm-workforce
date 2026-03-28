---
name: gws-recipe-index
description: Google Workspace recipe index — 41 pre-built automation patterns for Gmail, Calendar, Drive, Sheets, Tasks.
---

# Goal

> **Use this skill when:** Google Workspace automation recipes or patterns

Provide a lookup index, match user requests to specific GWS recipe, then load and execute the recipe from the `recipes/` subdirectory.

# Instructions

1. When user describes a GWS automation task, match it to a recipe below
2. Load the recipe file from `recipes/[name].md`
3. Execute the steps using gws CLI commands

# Recipe Index

## Email & Gmail
| Recipe | Description |
|--------|-------------|
| `create-gmail-filter` | Auto-label/star incoming messages |
| `create-vacation-responder` | Out-of-office auto-reply |
| `draft-email-from-doc` | Use Google Doc as email body |
| `email-drive-link` | Share Drive file via email |
| `forward-labeled-emails` | Forward messages with specific label |
| `label-and-archive-emails` | Bulk label + archive |
| `save-email-attachments` | Save attachments to Drive |
| `save-email-to-doc` | Archive email body to Google Doc |
| `send-team-announcement` | Announce via Gmail + Chat |

## Calendar & Scheduling
| Recipe | Description |
|--------|-------------|
| `batch-invite-to-event` | Add attendees to existing event |
| `block-focus-time` | Recurring deep work blocks |
| `create-events-from-sheet` | Bulk create events from spreadsheet |
| `find-free-time` | Query free/busy for meeting slots |
| `plan-weekly-schedule` | Review week, fill gaps |
| `reschedule-meeting` | Move event + notify attendees |
| `schedule-recurring-event` | Create recurring event |
| `share-event-materials` | Share Drive files with attendees |

## Drive & Files
| Recipe | Description |
|--------|-------------|
| `backup-sheet-as-csv` | Export Sheet as CSV |
| `bulk-download-folder` | Download all files from folder |
| `find-large-files` | Identify storage-heavy files |
| `organize-drive-folder` | Create folder structure + move files |
| `share-folder-with-team` | Share folder with collaborators |
| `watch-drive-changes` | Subscribe to change notifications |

## Sheets & Data
| Recipe | Description |
|--------|-------------|
| `compare-sheet-tabs` | Diff two tabs in a spreadsheet |
| `copy-sheet-for-new-month` | Duplicate template tab |
| `create-expense-tracker` | Set up expense tracking sheet |
| `generate-report-from-sheet` | Sheet data → Google Doc report |
| `log-deal-update` | Append deal status to sales tracker |
| `sync-contacts-to-sheet` | Export contacts to spreadsheet |

## Docs & Presentations
| Recipe | Description |
|--------|-------------|
| `create-doc-from-template` | Copy template, fill, share |
| `create-presentation` | New Slides + initial content |
| `share-doc-and-notify` | Share doc + email collaborators |

## Tasks & Forms
| Recipe | Description |
|--------|-------------|
| `collect-form-responses` | Retrieve Google Form responses |
| `create-feedback-form` | Create form + share via email |
| `create-task-list` | New Tasks list with initial items |
| `review-overdue-tasks` | Find past-due tasks |

## Classroom & Meet
| Recipe | Description |
|--------|-------------|
| `create-classroom-course` | Create course + invite students |
| `create-meet-space` | Create meeting + share link |
| `review-meet-participants` | Attendance + duration report |
| `create-shared-drive` | Create Shared Drive + add members |

## Cross-Service Workflows
| Recipe | Description |
|--------|-------------|
| `post-mortem-setup` | Doc + Calendar review + Chat notify |

# Constraints

- Each recipe is a self-contained automation pattern
- Use `gws` CLI for all operations
- Recipes are stored in `recipes/` subdirectory — load on demand
