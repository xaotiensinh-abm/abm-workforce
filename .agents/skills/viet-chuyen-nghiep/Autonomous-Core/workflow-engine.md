# Động cơ Điều phối Pipeline

## Mục đích

Engine **thực thi pipeline** — nhận classification từ task-classifier,
kích hoạt workers theo thứ tự đúng, quản lý handoff contracts giữa workers.

## Pipeline Registry

| Pipeline | Workers (theo thứ tự) | Trigger |
|----------|----------------------|---------|
| `write-new` | intake → research → strategy → writer → quality | Viết mới |
| `edit-draft` | intake → critique → research → writer → quality | Sửa bản nháp |
| `deep-research` | intake → research → quality | Research thuần |
| `critique-content` | intake → research → critique → quality | Phản biện |
| `grade-content` | intake → research → critique → quality | Chấm bài |
| `publish-ready` | intake → quality | Kiểm duyệt xuất bản |

## Execution Protocol

```
┌─────────────────────────────────────────────┐
│              WORKFLOW ENGINE                 │
│                                             │
│  1. Load pipeline definition                │
│  2. For each worker in sequence:            │
│     ├─ Create handoff contract              │
│     ├─ Activate worker                      │
│     ├─ Collect output                       │
│     ├─ Validate output against contract     │
│     └─ Pass to next worker                  │
│  3. Handle NEEDS_REVISION loops             │
│  4. Deliver to Editor-in-Chief              │
└─────────────────────────────────────────────┘
```

## Handoff Contract Template

Mỗi khi giao việc từ Worker A → Worker B:

```yaml
handoff:
  from: "[worker-a]"
  to: "[worker-b]"
  input:
    data: "[output từ worker trước]"
    brief: "[brief gốc]"
    accumulated_context: "[context tích lũy]"
  expected_output:
    format: "[yaml/markdown/text]"
    required_fields: ["field1", "field2"]
  quality_threshold:
    minimum_confidence: "[high/medium]"
```

## Revision Loop

```
Writer output → Quality check
    ├─ PASS → Done ✅
    ├─ NEEDS_REVISION → Writer retry (max 2)
    │   └─ Still fail → Escalate to Editor
    └─ FAIL → Escalate to Editor immediately
```

## Multi-pipeline Execution

Khi user cần nhiều output types:
1. Chạy pipeline chính trước (longform > social > video)
2. Output pipeline 1 = input cho pipeline 2
3. Mỗi pipeline có quality gate riêng
