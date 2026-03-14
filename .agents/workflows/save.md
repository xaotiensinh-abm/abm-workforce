---
description: Lưu trạng thái công việc vào memory — save task, daily save, milestone save
---
// turbo-all

# 💾 Workflow /save — Lưu Trạng Thái Công Việc

## Mục đích
Lưu TOÀN BỘ ngữ cảnh phiên làm việc vào workspace, giúp phiên sau dùng `/recap` để khôi phục context và tiếp tục dự án.

## Bước 1: Thu thập thông tin phiên hiện tại
Tự động quét conversation hiện tại và thu thập:
- Tasks đã hoàn thành / đang làm / bị chặn
- Files đã tạo / sửa / xóa (đường dẫn cụ thể)
- Quyết định quan trọng đã đưa ra
- Kiến thức mới phát hiện
- Trạng thái plan (nếu có)
- Skills đã sử dụng
- Bugs / issues đang mở
- Những gì CẦN LÀM TIẾP ở phiên sau

## Bước 2: Xác định loại save
- Nếu user nói "save" sau 1 task → `task_save`
- Nếu user nói "save" cuối ngày → `daily_save`
- Nếu đạt milestone quan trọng → `milestone_save`

## Bước 3: Tạo thư mục session (nếu chưa có)
```bash
mkdir -p "{workspace-root}/.abm-sessions"
```

## Bước 4: Đếm save tiếp theo
Kiểm tra thư mục `{workspace-root}/.abm-sessions/`:
- Đếm số files `SESSION-*.md` hiện có
- session_id = SESSION-{số tiếp theo, 3 chữ số}

## Bước 5: Tạo file SESSION
Tạo file: `{workspace-root}/.abm-sessions/SESSION-{NNN}-{YYYY-MM-DD}.md`

**Format bắt buộc:**

```markdown
# SESSION-{NNN} — {Tiêu đề ngắn}

**Ngày**: {YYYY-MM-DD HH:MM}
**Loại**: {task_save | daily_save | milestone_save}
**Workspace**: {workspace path}

---

## Tóm tắt phiên
{2-3 câu tóm tắt những gì đã làm trong phiên này}

## ✅ Đã hoàn thành
- {Task 1 — mô tả ngắn}
- {Task 2 — mô tả ngắn}

## 🔄 Đang làm dở
- {Task — trạng thái hiện tại, cần làm gì tiếp}

## ❌ Bị chặn / Issues
- {Blocker — lý do + cách giải quyết đề xuất}

## 📁 Files thay đổi
### Tạo mới
- `{path/to/file}` — {mô tả}

### Sửa đổi
- `{path/to/file}` — {thay đổi gì, bao nhiêu lines}

### Xóa
- `{path/to/file}` — {lý do}

## 💡 Quyết định quan trọng
- {Quyết định 1 — lý do}
- {Quyết định 2 — lý do}

## 🧠 Kiến thức mới
- {Insight 1}
- {Insight 2}

## 📋 Việc cần làm tiếp (NEXT SESSION)
1. {Task ưu tiên cao nhất}
2. {Task ưu tiên 2}
3. {Task ưu tiên 3}

## 🔗 References
- {Link hoặc file reference quan trọng}
```

## Bước 6: Cập nhật file INDEX
Thêm entry mới vào `{workspace-root}/.abm-sessions/INDEX.md`:

```markdown
| SESSION-{NNN} | {date} | {type} | {title} | {status: saved} |
```

Nếu `INDEX.md` chưa tồn tại, tạo mới với header:
```markdown
# 📋 ABM Session Index

| ID | Ngày | Loại | Tiêu đề | Status |
|----|------|------|---------|--------|
```

## Bước 7: Backup vào Second-Brain (tùy chọn)
Copy file session vào: `_abm/Context-Layer/Second-Brain/memory/saves/`
```bash
cp "{workspace-root}/.abm-sessions/SESSION-{NNN}-{date}.md" "_abm/Context-Layer/Second-Brain/memory/saves/"
```

## Bước 8: Hiển thị xác nhận
```
💾 ĐÃ LƯU — SESSION-{NNN} | {date} {time}
📌 {title}
✅ Hoàn thành: {N} | 🔄 Đang làm: {N} | ❌ Blocked: {N}
📋 Phiên sau: {priority task #1}
📂 File: .abm-sessions/SESSION-{NNN}-{date}.md
💡 Dùng /recap để khôi phục context phiên sau!
```

## Bước 9: Sync Dashboard (TỰ ĐỘNG)
Chạy sync script để cập nhật dashboard:
```bash
powershell -ExecutionPolicy Bypass -File "{workspace-root}/dashboard/sync.ps1"
```
Script sẽ:
- Quét workspace: đếm skills, routes, workflows, subagents
- Đọc `task-history.json`
- Tạo lại `dashboard/task-data.js`
- Dashboard tự cập nhật khi refresh (F5)

## Bước 10: Commit (tùy chọn)
Nếu CEO muốn commit:
```bash
git add .abm-sessions/ dashboard/
git commit -m "save: SESSION-{NNN} — {title}"
```

