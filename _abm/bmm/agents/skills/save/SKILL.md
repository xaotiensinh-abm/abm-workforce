---
name: save
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Lưu trạng thái phiên làm việc vào workspace — session history, context persistence, cross-session continuity"
---

# 💾 Session Save — Lưu Phiên Làm Việc

## Mục đích
Skill này giúp lưu toàn bộ ngữ cảnh phiên làm việc vào workspace, cho phép `/recap` khôi phục context ở phiên sau.

## Storage Location

```
{workspace-root}/
└── .abm-sessions/           ← Thư mục chính
    ├── INDEX.md              ← Danh sách tất cả sessions
    ├── SESSION-001-2026-03-12.md
    ├── SESSION-002-2026-03-13.md
    └── ...
```

**Tại sao `.abm-sessions/` nằm ở workspace root?**
- Agent mới mở workspace → scan `.abm-sessions/` → biết context ngay
- Git-trackable (commit cùng code)
- Không phụ thuộc brain/antigravity directory (portable)

## Cấu Trúc Session File

```yaml
session_structure:
  header:
    session_id: "SESSION-{NNN}"
    title: "Tiêu đề ngắn gọn"
    date: "YYYY-MM-DD HH:MM"
    type: "task_save | daily_save | milestone_save"
    workspace: "{absolute path}"
  
  summary: "2-3 câu tóm tắt toàn phiên"
  
  completed_tasks:
    - "Mô tả task + kết quả"
  
  in_progress:
    - task: "Mô tả"
      status: "Trạng thái hiện tại"
      next_step: "Cần làm gì tiếp"
  
  blocked:
    - task: "Mô tả"
      reason: "Lý do bị chặn"
      proposed_fix: "Đề xuất giải quyết"
  
  files_changed:
    created: ["path → description"]
    modified: ["path → changes"]
    deleted: ["path → reason"]
  
  decisions:
    - "Quyết định → Lý do"
  
  knowledge:
    - "Insight mới phát hiện"
  
  next_session:
    - "Task ưu tiên 1"
    - "Task ưu tiên 2"
    - "Task ưu tiên 3"
  
  references:
    - "Links / files quan trọng"
```

## 3 Loại Save

### Task Save
```yaml
trigger: "Sau khi hoàn thành 1 task/feature cụ thể"
content: "Chỉ focus vào task vừa hoàn thành"
detail_level: "medium"
```

### Daily Save
```yaml
trigger: "Cuối ngày làm việc"
content: "Tổng hợp TẤT CẢ tasks trong ngày"
detail_level: "high"
includes:
  - "Tất cả tasks: done + in-progress + blocked"
  - "Tổng files changed"
  - "Tomorrow priorities"
```

### Milestone Save
```yaml
trigger: "Hoàn thành milestone quan trọng (deploy, release, audit xong)"
content: "Full snapshot trạng thái project"
detail_level: "highest"
includes:
  - "Architecture decisions"
  - "Technical debt notes"
  - "Performance metrics"
  - "Dependencies hiện tại"
```

## INDEX.md Format

```markdown
# 📋 ABM Session Index

| ID | Ngày | Loại | Tiêu đề | Status |
|----|------|------|---------|--------|
| SESSION-001 | 2026-03-08 | daily | Setup ABM Workforce repo | ✅ saved |
| SESSION-002 | 2026-03-12 | milestone | Training + R&D departments | ✅ saved |
```

## Quy tắc quan trọng

1. **Một file = Một phiên**: Không ghi đè, luôn tạo file mới
2. **Next session PHẢI có**: Mục "Việc cần làm tiếp" là BẮT BUỘC
3. **Files changed PHẢI cụ thể**: Đường dẫn + mô tả thay đổi
4. **Decisions PHẢI có lý do**: Không chỉ ghi "đã quyết định X"
5. **Maximum 1 save/task**: Tránh save quá nhiều → noise

## Output khi được yêu cầu

1. **Session file** — Markdown đầy đủ theo template
2. **INDEX update** — Thêm entry mới
3. **Confirmation** — Bảng tóm tắt cho CEO
4. **Git commit** — Nếu CEO muốn
