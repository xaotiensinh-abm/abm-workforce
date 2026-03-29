---
description: Khôi phục ngữ cảnh phiên trước — đọc session history, list công việc, tiếp tục dự án
---
// turbo-all

# 🔄 Workflow /recap — Khôi Phục Ngữ Cảnh

## Mục đích
Đọc lịch sử làm việc đã lưu bởi `/save`, hiển thị tóm tắt cho agent và user, giúp tiếp tục dự án mà không mất context.

## Bước 1: Tìm thư mục sessions
Kiểm tra tồn tại: `{workspace-root}/.abm-sessions/`

Nếu KHÔNG tồn tại:
```
⚠️ Chưa có session history nào.
Dùng /save để lưu trạng thái công việc trước.
```
→ Dừng workflow.

## Bước 2: Đọc INDEX
Đọc file `{workspace-root}/.abm-sessions/INDEX.md`
- Hiển thị danh sách TẤT CẢ sessions đã lưu
- Highlight session MỚI NHẤT (cuối bảng)

## Bước 3: Đọc session mới nhất
Tự động đọc file SESSION mới nhất (file có số NNN cao nhất):
- `{workspace-root}/.abm-sessions/SESSION-{NNN}-{date}.md`

## Bước 4: Hiển thị Recap cho user
Format hiển thị:

```
🔄 RECAP — Phiên trước: SESSION-{NNN} | {date}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 {Tiêu đề phiên}

📖 Tóm tắt:
{2-3 câu tóm tắt}

✅ Đã hoàn thành:
  • {Task 1}
  • {Task 2}

🔄 Đang làm dở:
  • {Task — trạng thái}

📋 Việc cần làm tiếp:
  1. {Priority 1}
  2. {Priority 2}
  3. {Priority 3}

📁 Files đã thay đổi: {N} files
💡 Quyết định: {N} quyết định quan trọng

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bạn muốn tiếp tục từ đâu?
```

## Bước 5: Load context vào agent
Sau khi hiển thị recap, agent ĐÃ CÓ context đầy đủ:
- Biết project đang làm gì
- Biết files nào đã thay đổi
- Biết task tiếp theo là gì
- Biết decisions đã đưa ra

→ Agent sẵn sàng tiếp tục dự án.

## Bước 6: Hỏi user muốn làm gì
Đề xuất 3 options:
1. **Tiếp tục** — làm task ưu tiên cao nhất từ "Việc cần làm tiếp"
2. **Xem chi tiết** — đọc full session file
3. **Xem lịch sử** — list tất cả sessions

## Tham số tùy chọn

```
/recap              → Đọc session mới nhất
/recap all          → List tất cả sessions (INDEX.md)
/recap {NNN}        → Đọc session cụ thể theo ID
/recap search {keyword} → Tìm trong tất cả sessions
```
