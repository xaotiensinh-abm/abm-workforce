---
name: "github-issues-sprint"
description: "Tích hợp GitHub Issues vào Sprint Planning — import issues, convert to stories, assign sprints. Bridge giữa GitHub và ABM."
---

# 📋 GitHub Issues → Sprint Integration

Bridge giữa GitHub Issues và ABM Sprint Planning workflow.

## Sử dụng khi

- Có GitHub repo với issues cần sprint planning
- Cần convert issues → user stories
- Sync sprint progress với GitHub project

## KHÔNG sử dụng khi

- Không dùng GitHub → dùng `sprint-planning` trực tiếp
- Cần quản lý project nội bộ → dùng `task-planning`
- Cần review code → dùng `code-review`

## WORKFLOW

```
GitHub Issues
  │
  ├── 1. IMPORT — Đọc issues từ repo
  │     Command: gh issue list --state open --json number,title,labels,body
  │
  ├── 2. CLASSIFY — Phân loại theo label
  │     bug → fix task
  │     enhancement → feature story
  │     documentation → docs task
  │
  ├── 3. CONVERT — Chuyển thành User Stories
  │     Issue title → Story title
  │     Issue body → Acceptance criteria
  │     Labels → Epic mapping
  │     Milestone → Sprint assignment
  │
  ├── 4. ESTIMATE — T-shirt sizing
  │     Small issues → S(2), Medium → M(3), Large → L(5)
  │
  └── 5. ASSIGN — Đưa vào Sprint Backlog
        Theo capacity + priority
```

## COMMAND REFERENCE

```bash
# List open issues
gh issue list --state open --json number,title,labels,body

# List by label
gh issue list --label "enhancement" --state open

# List by milestone
gh issue list --milestone "Sprint 1"

# Close issue khi done
gh issue close {number} --comment "Done in sprint X"

# Create issue từ story
gh issue create --title "STORY: {title}" --body "{AC}" --label "story"
```

## TEMPLATE MAPPING

```yaml
github_issue:
  number: 42
  title: "Add dark mode support"
  labels: ["enhancement", "UI"]
  body: "Users want dark mode..."

abm_story:
  id: "STORY-UI-001"
  title: "Là user, tôi muốn dark mode, để giảm mỏi mắt"
  epic: "EPIC-UI"
  points: 5
  priority: "Should"
  source: "github#42"
  acceptance_criteria:
    - "Toggle dark/light mode"
    - "Persist preference"
    - "All pages support dark mode"
```

## QUY TẮC

1. Giữ link 2 chiều: Story → Issue#, Issue → Story ID
2. Close GitHub issue khi story DONE
3. Sync labels với ABM categories

---

## Nguồn gốc
- Wave 1 v2.7: GitHub Issues → Sprint
