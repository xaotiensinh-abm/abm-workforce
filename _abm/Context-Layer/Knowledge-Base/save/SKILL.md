---
name: "save"
description: "Lưu trạng thái công việc vào Second Brain — snapshot task/ngày làm việc, knowledge gained, plan status, files changed. Hỗ trợ /save, /list-memory, /find-memory."
---

## KHONG su dung khi

- Can tinh che tri thuc -> dung knowledge-crystallizer. Can backup git -> dung memory-keeper.


# 💾 Save — Lưu Trạng Thái Công Việc

Skill lưu trạng thái công việc vào bộ nhớ dài hạn (Second Brain). Khi user nói **"save"** hoặc dùng lệnh **/save**, Jarvis sẽ tự động thu thập và lưu toàn bộ thông tin phiên làm việc.

## Khi nào kích hoạt

- User nói "save", "lưu lại", "ghi nhớ"
- Kết thúc 1 task quan trọng
- Cuối ngày làm việc
- Trước khi chuyển sang dự án khác
- User cần snapshot trạng thái hiện tại

## KHÔNG tự động kích hoạt khi

- Giữa chừng task (chưa có gì đáng lưu)
- User chỉ hỏi câu hỏi đơn giản

---

## QUY TRÌNH SAVE — 5 BƯỚC

### Bước 1: Thu thập thông tin

Jarvis tự động quét và thu thập:

| Nguồn | Thông tin thu thập |
|-------|-------------------|
| **Conversation** | Tóm tắt nội dung chính, quyết định quan trọng |
| **Tasks** | Task nào đã hoàn thành, đang làm, còn lại |
| **Files** | Danh sách files đã tạo/sửa/xóa |
| **Plans** | Trạng thái plan hiện tại (% hoàn thành) |
| **Knowledge** | Kiến thức mới học được, patterns phát hiện |
| **Decisions** | Quyết định quan trọng của CEO |

### Bước 2: Tạo Memory Entry

Tạo file mới trong `_abm/Context-Layer/Second-Brain/memory/saves/`:

```yaml
# File: SAVE-{NNN}-{YYYY-MM-DD}.yaml
save_id: "SAVE-{NNN}"
date: "{YYYY-MM-DD}"
time: "{HH:MM}"
type: "task_save" | "daily_save" | "milestone_save"

# === TÓM TẮT ===
title: "[Tiêu đề ngắn gọn mô tả phiên làm việc]"
summary: |
  [Tóm tắt 3-5 câu về những gì đã làm trong phiên này]

# === CÔNG VIỆC ===
work:
  completed:
    - task: "[Tên task]"
      result: "[Kết quả]"
      files: ["file1.md", "file2.yaml"]
  in_progress:
    - task: "[Tên task đang làm]"
      progress: "60%"
      next_step: "[Bước tiếp theo]"
  blocked:
    - task: "[Task bị chặn]"
      reason: "[Lý do]"

# === KIẾN THỨC ===
knowledge_gained:
  - "[Điều mới học được 1]"
  - "[Điều mới học được 2]"

# === QUYẾT ĐỊNH ===
key_decisions:
  - decision: "[Quyết định gì]"
    by: "CEO" | "Jarvis"
    reason: "[Lý do]"

# === FILES ĐÃ THAY ĐỔI ===
files_changed:
  created: ["file1.md"]
  modified: ["file2.yaml"]
  deleted: ["file3.md"]

# === PLAN STATUS ===
plan_status:
  plan_name: "[Tên plan nếu có]"
  progress: "70%"
  remaining: ["item 1", "item 2"]

# === NEXT SESSION ===
next_session:
  priority: "[Việc cần làm đầu tiên ngày mai]"
  context: "[Context quan trọng cần nhớ]"
  reminders:
    - "[Nhắc nhở 1]"
    - "[Nhắc nhở 2]"

# === META ===
skills_used: ["skill1", "skill2"]
mood: "productive" | "research" | "creative" | "debugging" | "planning"
tags: ["tag1", "tag2"]
```

### Bước 3: Lưu file

```
Đường dẫn: _abm/Context-Layer/Second-Brain/memory/saves/SAVE-{NNN}-{YYYY-MM-DD}.yaml
```

Quy tắc đánh số:
- Đếm files trong `saves/` → số tiếp theo
- Format: `SAVE-001`, `SAVE-002`, ...

### Bước 4: Xác nhận với CEO

Hiển thị tóm tắt:

```
💾 ĐÃ LƯU — SAVE-{NNN} | {YYYY-MM-DD} {HH:MM}

📌 {title}
━━━━━━━━━━━━━━━━━━━━━━━
✅ Hoàn thành: {N} tasks
🔄 Đang làm: {N} tasks
📂 Files: +{created} ~{modified} -{deleted}
🧠 Kiến thức: {N} điểm mới
📋 Việc ngày mai: {priority}
```

### Bước 5: Commit (tùy chọn)

Nếu CEO yêu cầu, tự động commit save:
```
git add _abm/Context-Layer/Second-Brain/memory/saves/
git commit -m "save: SAVE-{NNN} — {title}"
```

---

## LỆNH /list-memory — XEM DANH SÁCH

Khi user nói "list memory", "xem lại", "danh sách saves":

```
📋 DANH SÁCH MEMORY SAVES
━━━━━━━━━━━━━━━━━━━━━━━
| # | Ngày | Loại | Tiêu đề | Tasks |
|---|------|------|---------|-------|
| SAVE-005 | 09/03 | daily | Multimedia skills v2.2 | 6 ✅ |
| SAVE-004 | 09/03 | task | Deep research VEO/Grok | 3 ✅ |
| SAVE-003 | 08/03 | daily | System audit + push | 11 ✅ |
| ...
```

**Cách thực hiện:**
1. Đọc tất cả files trong `memory/saves/`
2. Parse YAML → lấy save_id, date, type, title, completed count
3. Hiển thị bảng sắp xếp theo ngày (mới nhất trước)

---

## LỆNH /find-memory — TÌM KIẾM

Khi user nói "tìm memory về...", "find memory...":

```
/find-memory [keyword]
```

**Cách thực hiện:**
1. Grep tất cả files trong `memory/saves/` theo keyword
2. Trả về danh sách matches với context

---

## LỆNH /load-memory — NẠP LẠI CONTEXT

Khi user nói "load save 005", "nạp lại phiên trước":

```
/load-memory SAVE-{NNN}
```

**Cách thực hiện:**
1. Đọc file `SAVE-{NNN}-{date}.yaml`
2. Hiển thị toàn bộ thông tin
3. Đặc biệt highlight `next_session` — việc cần làm tiếp

---

## PHÂN LOẠI SAVE

| Loại | Khi dùng | Ký hiệu |
|------|---------|---------|
| **task_save** | Xong 1 task cụ thể | 📌 |
| **daily_save** | Cuối ngày làm việc | 📅 |
| **milestone_save** | Đạt cột mốc quan trọng | 🏆 |

---

## QUY TẮC

1. **KHÔNG XÓA** saves cũ — chỉ append
2. **Mỗi save = 1 file** riêng biệt (dễ tìm, dễ quản lý)
3. **Tags** giúp tìm kiếm nhanh
4. **next_session** luôn phải có — để ngày mai biết bắt đầu từ đâu
5. Saves > 30 ngày → xem xét crystallize vào `patterns/` nếu có pattern lặp lại

## Nguồn gốc
- Xây dựng bởi: ABM Workforce v2.2 — Jarvis Orchestrator
- Tích hợp: Second Brain memory layer
