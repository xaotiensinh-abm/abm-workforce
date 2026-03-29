---
name: executing-plans
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng để tự tay Code Nguyên Khối (Inline Execution) dựa trên một bản Hợp đồng (Plan) đã được phê duyệt."
---

# Tự Triển Khai Hợp Đồng (Executing Plans)

## Tổng Quan

Khác với chế độ thuê lính đánh thuê Subagent, ở chế độ này, chính Bạn (Main Agent) sẽ tự tay đọc file Hợp đồng, tự review, tự gõ code toàn bộ các task và tự báo cáo.

**Khai báo lúc bắt đầu:** "Tôi sẽ dùng skill `executing-plans` để tự tay gõ code thực thi Hợp đồng này."

**Lưu ý cho CEO:** ABM Workforce hoạt động tối ưu nhất khi có phân quyền Subagent. Nếu nền tảng hiện tại (Claude Code, Cursor) cho phép gọi Agent đệ quy, hãy đốc thúc CEO dùng skill `subagent-driven-development` thay vì skill này.

## Quy Trình Thực Thi

### Bước 1: Đọc và Duyệt Hợp Đồng (Review Plan)
1. Đọc kỹ file Hợp đồng `.md`.
2. Duyệt phản biện - có thấy task nào vô lý hay cấn cá không?
3. Nếu cấn: Báo cáo với CEO/User ngay lập tức để chấn chỉnh.
4. Nếu mượt: Bật Checklist TodoWrite và xông pha.

### Bước 2: Thi Hành Từng Task
Với mỗi Task:
1. Đánh dấu Đang tiến hành (`in_progress`).
2. Làm đúng y xì đúc từng Step nhỏ trong file Hợp đồng (Bite-sized steps).
3. BẮT BUỘC chạy các lệnh Test / Linter để kiểm chứng. Áp dụng kỷ luật `verification-before-completion`.
4. Đánh dấu Hoàn thành.

### Bước 3: Nghiệm Thu Phân Hệ
Sau khi gạch xong 100% các Task trong Hợp đồng:
- Gáy lên câu: "Tôi sẽ dùng skill `finishing-a-development-branch` để gút lại phiên làm việc này."
- **BẮT BUỘC GỌI SUB-SKILL:** `superpowers:finishing-a-development-branch`
- Tuân thủ hướng dẫn nghiệm thu của nó.

## Cờ Đỏ - Dừng Lại Xin Viện Binh

**DỪNG MỌI HOẠT ĐỘNG CODE VÀ BÁO CÁO KHI:**
- Bị Block (Thiếu thư viện, Test đỏ mãi không xanh, prompt khó hiểu).
- Hợp đồng ghi lủng củng không rõ phải làm gì.
- Xác minh lệnh Fail.

**Mở miệng hỏi CEO, đừng tự ý đoán mò.**

## Khi Nào Quay Lại Bước Đầu

**Trở lại Bước 1 (Duyệt Hợp Đồng) khi:**
- CEO sửa lại file Hợp đồng dựa trên feedback của bạn.
- Cần đập đi xây lại phương án kiến trúc.

**TUYỆT ĐỐI KHÔNG CỐ ĐẤM ĂN XÔI** - Bug sinh ra từ sự ngoan cố.

## Tích Hợp Hệ Sinh Thái (Integration)
- **`using-git-worktrees`** - BẮT BUỘC: Dựng workspace cách ly trước khi code nếu dự án lớn.
- **`writing-plans`** - Nguồn gốc sinh ra cái Hợp đồng bạn đang code.
- **`finishing-a-development-branch`** - Mộc kiểm duyệt kết thúc dự án.
