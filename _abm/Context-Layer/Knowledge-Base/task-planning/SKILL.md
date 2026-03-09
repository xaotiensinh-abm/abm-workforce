---
name: "task-planning"
description: "Lập kế hoạch công việc có cấu trúc — breakdown tasks, timeline, dependencies, resource allocation. Giao tiếp tiếng Việt."
---

# 📋 Task Planning — Lập Kế Hoạch Công Việc

Skill lập kế hoạch công việc có cấu trúc — breakdown → estimate → schedule → track.

## Sử dụng khi

- Lên kế hoạch dự án mới
- Breakdown epics thành tasks cụ thể
- Tạo timeline + milestones
- Phân bổ nguồn lực (người, thời gian)
- Sprint planning / weekly planning

## KHÔNG sử dụng khi

- Cần brainstorm ý tưởng → dùng `brainstorming`
- Cần viết kế hoạch code → dùng `writing-plans`
- Cần chiến lược kinh doanh → dùng `startup-analyst`

## VÍ DỤ NHANH

```
Input:  "Lên kế hoạch triển khai CRM 3 tháng"
Output:
  📋 CRM Implementation Plan
  
  Phase 1: Discovery (Tuần 1-2)
    ├── [P0] Phỏng vấn stakeholders — 3 ngày → PM
    ├── [P0] Audit quy trình hiện tại — 2 ngày → Analyst
    └── [P1] Benchmark competitors — 2 ngày → Analyst
  
  Phase 2: Setup (Tuần 3-6)
    ├── [P0] Configure CRM platform — 5 ngày → Dev
    ├── [P0] Data migration — 3 ngày → Dev
    └── [P1] Custom fields + workflows — 4 ngày → Dev
  
  Phase 3: Training + Launch (Tuần 7-12)
    ├── [P0] Training sessions — 5 ngày → PM
    ├── [P1] Pilot test (1 team) — 10 ngày → All
    └── [P0] Full rollout — 5 ngày → All
```

---

## QUY TRÌNH PLANNING

### Bước 1: Phân tích mục tiêu

```
1. Mục tiêu SMART là gì?
2. Deadline cứng? Deadline mềm?
3. Ràng buộc: budget, people, tech?
4. Definition of Done?
```

### Bước 2: Breakdown (WBS)

```
Epic → Feature → Task → Subtask

Quy tắc:
- Mỗi task ≤ 3 ngày effort
- Nếu > 3 ngày → chia nhỏ hơn
- Mỗi task có 1 owner duy nhất
- Task phải có output đo được
```

### Bước 3: Estimate (T-shirt sizing)

| Size | Effort | Ví dụ |
|------|--------|-------|
| **XS** | < 2 giờ | Fix typo, update config |
| **S** | 2-4 giờ | Tạo 1 component |
| **M** | 1-2 ngày | Feature nhỏ end-to-end |
| **L** | 3-5 ngày | Feature phức tạp |
| **XL** | > 5 ngày | ⚠️ Cần breakdown thêm |

### Bước 4: Schedule + Dependencies

```
Task A ──→ Task B ──→ Task C
                 ╲
                  ──→ Task D (parallel)

- Dependency: finish-to-start (default)
- Critical path: tìm chuỗi dài nhất
- Buffer: +20% cho unknowns
```

### Bước 5: Resource allocation

```
- 1 người = tối đa 3 tasks parallel
- Senior review cho P0 tasks
- Knowledge backup: 2 người biết mỗi area
```

---

## OUTPUT FORMAT

```markdown
# 📋 [Tên dự án] — Kế Hoạch Triển Khai

## Tóm tắt
- **Timeline**: [start] → [end]
- **Team**: [số người] × [roles]
- **Budget**: [nếu có]

## Phases & Tasks

### Phase 1: [Tên] (Tuần X-Y)
| # | Task | Owner | Effort | Priority | Dependencies |
|:-:|------|-------|:------:|:--------:|:------------:|
| 1 | ... | ... | S | P0 | — |
| 2 | ... | ... | M | P1 | Task 1 |

## Milestones
- [ ] Milestone 1 — [date]
- [ ] Milestone 2 — [date]

## Risks
| Risk | Impact | Mitigation |
|------|:------:|-----------|
| ... | HIGH | ... |
```

---

## Nguồn gốc
- Gốc: community skills (task-planning) — adapt cho ABM
- ABM Workforce v2.4 — Jarvis Orchestrator
