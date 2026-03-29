---
name: "sprint-planning"
description: "Pipeline PRD → Epics → User Stories → Sprint Backlog → Sprint Plan. Estimation T-shirt sizing, MoSCoW priority, velocity tracking, gate review."
---

# 🏃 Sprint Planning — PRD Đến Sprint

Pipeline chuyển đổi có hệ thống từ PRD → Sprint Plan thực thi.

## Sử dụng khi

- Có PRD cần breakdown thành sprints
- Cần ước lượng effort (story points)
- Lập Sprint Backlog từ Feature Backlog
- Sprint review/retrospective

## KHÔNG sử dụng khi

- Cần lập kế hoạch tổng quát → dùng `task-planning`
- Cần quản lý context hierarchy → dùng `project-hierarchy`
- Cần brainstorm features → dùng `brainstorming`

## PIPELINE

```
PRD (Product Requirements Document)
  │
  ├── 1. BREAKDOWN → Epics
  │     Gate: Council review (đủ scope?)
  │
  ├── 2. DECOMPOSE → User Stories
  │     Format: "Là [role], tôi muốn [action], để [benefit]"
  │     Gate: Acceptance criteria rõ ràng?
  │
  ├── 3. ESTIMATE → Story Points
  │     T-shirt: XS(1) S(2) M(3) L(5) XL(8) XXL(13)
  │     Gate: Không có story > 8 points (phải split)
  │
  ├── 4. PRIORITIZE → MoSCoW
  │     Must have | Should have | Could have | Won't have
  │
  ├── 5. ASSIGN → Sprint Backlog
  │     Velocity = avg points/sprint
  │     Capacity = team size × availability
  │
  └── 6. VALIDATE → Council Review
        Gate: Sprint plan khả thi?
```

## USER STORY FORMAT

```
ID: STORY-{Epic}-{Number}
Tiêu đề: Là [role], tôi muốn [action], để [benefit]
Epic: EPIC-{ID}
Points: {1-13}
Priority: {Must/Should/Could/Won't}
Acceptance Criteria:
  - [ ] Criterion 1
  - [ ] Criterion 2
Dependencies: [STORY-xxx]
```

## SPRINT PLAN TEMPLATE

```yaml
sprint:
  number: 1
  duration: "2 tuần"
  start: "YYYY-MM-DD"
  end: "YYYY-MM-DD"
  goal: ""
  velocity_target: 0

backlog:
  - story_id: "STORY-001"
    title: ""
    points: 0
    priority: "Must"
    assignee: ""
    status: "todo"

total_points: 0
capacity: 0
risk_items: []
```

## GATE REVIEWS

| Gate | Kiểm tra | Ai review |
|------|---------|-----------|
| PRD → Epic | Scope đủ? Thiếu gì? | Council |
| Epic → Story | AC rõ ràng? Testable? | Pragmatist |
| Story → Sprint | Points hợp lý? Dependencies? | Architect |
| Sprint → Execute | Capacity đủ? Risk? | CEO |

## QUY TẮC SẮT

1. **Story > 8 points** → PHẢI split nhỏ hơn
2. **Không có AC** → KHÔNG đưa vào sprint
3. **Sprint overload** (> 120% velocity) → CEO phải duyệt
4. Mỗi sprint kết thúc → **Retrospective** bắt buộc

---

## Nguồn gốc
- BMAD feedback điểm 9: PRD → Sprint plan pipeline
- ABM Workforce v2.6
