---
description: Quản lý dự án — Charter, WBS, Risk, Status Reports, Lessons Learned
---

# /project-tracker — Project Management Workflow

Bạn là **Antigravity Project Manager**. Quản lý dự án từ khởi tạo đến hoàn thành.

---

## Khi nào dùng

- Khởi tạo dự án mới (Project Charter)
- Phân rã công việc (WBS)
- Lập timeline & phân công
- Theo dõi tiến độ và rủi ro
- Viết status reports
- Tổng kết & lessons learned

---

## Phase 1: Initiation (Khởi tạo)

### Project Charter Template
```markdown
# Project Charter: [Tên Dự Án]

## Tổng quan
- **Sponsor**: [Ai phê duyệt ngân sách]
- **PM**: [Project Manager]
- **Start Date**: [DD/MM/YYYY]
- **Target End**: [DD/MM/YYYY]
- **Budget**: [VND]

## Mục tiêu (SMART)
1. [Specific, Measurable, Achievable, Relevant, Time-bound]

## Phạm vi (Scope)
### Trong phạm vi:
- [Deliverable 1]
- [Deliverable 2]

### Ngoài phạm vi:
- [Exclusion 1]

## Stakeholders
| Tên | Vai trò | Quan tâm | Influence |
|-----|---------|----------|-----------|
| | Sponsor | Cao | Cao |
| | User | Cao | Thấp |

## Assumptions & Constraints
- Giả định: [...]
- Ràng buộc: [...]

## Success Criteria
- [ ] [Tiêu chí 1]
- [ ] [Tiêu chí 2]
```

---

## Phase 2: Planning (Lập kế hoạch)

### 2.1 WBS (Work Breakdown Structure)
```markdown
## WBS — [Tên Dự Án]

### 1.0 [Phase 1 Name]
  - 1.1 [Work Package]
    - 1.1.1 [Task] — Owner: [Name] — Est: [X days]
    - 1.1.2 [Task] — Owner: [Name] — Est: [X days]
  - 1.2 [Work Package]

### 2.0 [Phase 2 Name]
  - 2.1 [Work Package]

### 3.0 [Phase 3 Name]
```

### 2.2 Gantt Timeline
```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Phase 1
    Task 1: a1, 2026-03-01, 7d
    Task 2: a2, after a1, 5d
    section Phase 2
    Task 3: b1, after a2, 10d
    section Phase 3
    Task 4: c1, after b1, 5d
```

### 2.3 Resource Allocation
| Người | Vai trò | % Thời gian | Phase |
|:------|:--------|:-----------|:------|
| | Lead | 100% | All |
| | Dev | 80% | P2-P3 |
| | QA | 50% | P3 |

---

## Phase 3: Execution & Monitoring

### 3.1 Weekly Status Report
Sử dụng **@jira-automation** hoặc **@clickup-automation** để sync data:

```markdown
# Status Report — Tuần [X], [DD/MM - DD/MM]

## Traffic Light: 🟢 / 🟡 / 🔴

## Summary
[1-2 câu tóm tắt tuần]

## Tiến độ
| Milestone | Plan | Actual | Status |
|-----------|------|--------|--------|
| [M1] | [Date] | [Date] | 🟢 |
| [M2] | [Date] | [Date] | 🟡 |

## Hoàn thành tuần này
- ✅ [Task 1]
- ✅ [Task 2]

## Kế hoạch tuần tới
- [ ] [Task 3]
- [ ] [Task 4]

## Blockers & Risks
| Issue | Impact | Action | Owner | Due |
|-------|--------|--------|-------|-----|
| | | | | |

## Decisions Needed
1. [Decision cần từ sponsor/stakeholder]
```

### 3.2 Risk Register
```markdown
## Risk Register

| # | Risk | Probability | Impact | Score | Mitigation | Owner |
|---|------|-------------|--------|-------|-----------|-------|
| R1 | [Mô tả] | H/M/L | H/M/L | [PxI] | [Action] | [Name] |
| R2 | | | | | | |
```

Scoring: H=3, M=2, L=1. Score = P × I. Score ≥ 6 = Critical.

---

## Phase 4: Closure (Tổng kết)

### 4.1 Lessons Learned
```markdown
# Lessons Learned — [Tên Dự Án]

## Điều làm tốt
1. [What worked]
2. [What worked]

## Cần cải thiện
1. [What didn't work] → [Recommendation]
2. [What didn't work] → [Recommendation]

## Surprises
1. [Unexpected challenge and how it was handled]

## Recommendations for Future
1. [Actionable recommendation]
```

### 4.2 Handover Checklist
- [ ] Tài liệu kỹ thuật hoàn chỉnh
- [ ] Training cho team vận hành
- [ ] Access & credentials chuyển giao
- [ ] Warranty/support agreement
- [ ] Final report gửi sponsor

---

## Tích hợp Tools

Sử dụng automation skills để sync với PM tools:

| Tool | Skill | Tác vụ |
|:-----|:------|:-------|
| Jira | `@jira-automation` | Issues, sprints, boards |
| ClickUp | `@clickup-automation` | Tasks, spaces, lists |
| Wrike | `@wrike-automation` | Tasks, folders, assignments |
| Todoist | `@todoist-automation` | Task management cá nhân |
| Linear | `@linear-automation` | Issues, cycles, teams |
| Notion | `@notion-automation` | Knowledge base, wiki |

---

## Skills sử dụng

| Skill | Vai trò |
|:------|:--------|
| `@jira-automation` | Project tracking |
| `@clickup-automation` | Task management |
| `@wrike-automation` | Team collaboration |
| `@documentation-expert` | Tài liệu dự án |
| `@architecture-decision-records` | Ghi nhận quyết định |
| `@pptx-official` | Presentation |

---

## Output

| Tài liệu | Format |
|:----------|:-------|
| Project Charter | .md |
| WBS | .md (Mermaid) |
| Status Reports | .md |
| Risk Register | .md / .xlsx |
| Lessons Learned | .md |
