---
name: "project-hierarchy"
description: "Quản lý context xuyên suốt project — State Machine + Feature Hierarchy. Epic → Feature → Story → Task. Chống loạn não bằng zoom in/out protocol."
---

# 🏗️ Project Hierarchy — Quản Lý Context Xuyên Suốt

Skill quản lý cấu trúc phân cấp project, đảm bảo context không bị mất khi zoom in vào chi tiết.

## Sử dụng khi

- Bắt đầu project mới — cần lập cấu trúc Epic/Feature/Story
- Đang làm story nhưng mất tổng quan → cần zoom out
- Chuyển giữa các Epic/Feature → cần context inheritance
- Review progress tổng thể project

## KHÔNG sử dụng khi

- Task đơn giản không cần hierarchy → tự làm trực tiếp
- Cần lập sprint plan → dùng `sprint-planning`
- Cần brainstorm ý tưởng → dùng `brainstorming`

## STATE MACHINE

```
PROJECT
  ├── Epic 1 (UI/UX)
  │     ├── Feature 1.1
  │     │     ├── Story 1.1.1 [backlog]
  │     │     ├── Story 1.1.2 [in_progress]
  │     │     └── Story 1.1.3 [done]
  │     └── Feature 1.2
  ├── Epic 2 (Data Architecture)
  │     ├── Feature 2.1
  │     └── Feature 2.2
  └── Epic 3 (Backend)
```

### Trạng thái mỗi node

```
backlog → planning → in_progress → review → done
                 ↑                    │
                 └── rejected ────────┘
```

## CONTEXT INHERITANCE

```
Quy tắc: Context CON kế thừa context CHA

Project Context (goals, constraints, tech stack)
  └── Epic Context (scope, acceptance criteria, dependencies)
        └── Feature Context (design decisions, API contracts)
              └── Story Context (implementation details)
```

**Bắt buộc**: Mỗi khi làm Story → đọc lại Epic Context để giữ tổng quan.

## ZOOM IN/OUT PROTOCOL

### Zoom In (Project → Story)

```
1. Đọc Project Context (goals, constraints)
2. Xác định Epic liên quan
3. Đọc Epic Context (scope, dependencies)
4. Chọn Feature → Story
5. Làm Story TRONG PHẠM VI context kế thừa
```

### Zoom Out (Story → Project)

```
1. Hoàn thành hoặc bị chặn ở Story
2. Kiểm tra: Story này ảnh hưởng Feature/Epic nào?
3. Cập nhật Feature status
4. Nếu Feature done → cập nhật Epic status
5. Nếu cần quyết định lớn → escalate lên Epic/Project level
```

## FILE TEMPLATE

```yaml
# _abm-output/project-state.yaml
project:
  name: ""
  goals: []
  constraints: []
  tech_stack: []

epics:
  - id: "EPIC-001"
    name: ""
    status: "planning"
    context: ""
    acceptance_criteria: []
    features:
      - id: "FEAT-001"
        name: ""
        status: "backlog"
        stories:
          - id: "STORY-001"
            name: ""
            status: "backlog"
            points: 0
```

## QUY TẮC SẮT

1. **KHÔNG bao giờ** làm Story mà không đọc Epic Context
2. **LUÔN** cập nhật status khi chuyển trạng thái
3. **Zoom out** ít nhất 1 lần mỗi sprint để kiểm tra tổng quan
4. Context CHA thay đổi → review TẤT CẢ context CON

---

## Nguồn gốc
- BMAD feedback điểm 4: Context hierarchy + state machine
- ABM Workforce v2.6
