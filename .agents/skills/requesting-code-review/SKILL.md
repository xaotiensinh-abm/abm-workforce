---
name: requesting-code-review
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: "Dùng sau mỗi cụm task lớn để triệu hồi Reviewer từ bên ngoài soát lại lỗi trước khi dính chấu lỗi chuỗi (Cascading bugs)."
---

# Triệu Hồi Giám Khảo (Requesting Code Review)

Triệu hồi thanh tra `superpowers:code-reviewer` (nhân dạng Subagent) để lùng bắt lỗi tàng hình thối trước khi chúng đẻ nhộng sang các file khác. Đưa cho thanh tra đúng Tờ Khai Ngữ Cảnh Tinh Lọc, đéo thảy cả lốc Lịch sử Chat vào cho nó ngồi bươi móc. Cơ chế này bảo toàn token ngữ cảnh quý giá cho chính mạng sống của bạn.

**Tôn Chỉ:** Review càng sớm, Sẹo càng nhỏ (Review early, review often).

## Thời Khắc Triệu Hồi

**Bắt Buộc Nhập Lệnh (Mandatory):**
- Ngay sau mỗi Task hoàn thành trong phương án Lính Đánh Thuê (`subagent-driven-development`).
- Vừa đóng hòm một Feature to nạc đẫy đà.
- Sát giờ G (Ngay trước khi nổ lệnh Merge vào nhánh `main` cấm kỵ).

**Có Thể Nhập Góp Vui (Optional):**
- Đang gắp Code mà thấy rối tung rối mù (Cần bộ não thứ 2).
- Trước cú hích đập đi xây lại (Xin cái baseline check/Screenshot).

## Nghi Thức Triệu Hồi (How to Request)

**Bước 1: Bắt Mạch Lịch Sử (Git SHAs):**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # Hoặc origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**Bước 2: Phát Lệnh Cấm Vệ (Dispatch):**
Điền vào form mẫu triệu hồi (Dùng `Task` tool hoặc gọi lệnh Subagent tương tự) dựa trên chuẩn `/references/code-reviewer-prompt.md`.
**Bộ Tham Số mớm cho nó:**
- `{WHAT_WAS_IMPLEMENTED}` - Bạn vừa rớt nước mắt xây cái quần què gì?
- `{PLAN_OR_REQUIREMENTS}` - Theo Hợp đồng gốc thì đúng ra nó nên múa thế nào?
- `{BASE_SHA}` - Khởi đoan?
- `{HEAD_SHA}` - Cắt ngọn ở đâu?
- `{DESCRIPTION}` - Khái lược (3 dòng).

**Bước 3: Hứng Đá (Act on Feedback):**
- **Lỗi Nghiêm Trọng (Critical)** -> Fix cháy máy ngay tắp lự.
- **Lỗi Quan Trọng (Important)** -> Vá ngay trước khi bốc Task 2.
- Lỗi Rác Mắt (Minor) -> Note lại gọt dũa nếu rảnh.
- **Nói Xàm** -> Bật lại bằng skill `receiving-code-review` (Rất đanh thép).

## Tích hợp Khung Workflow (Integration)

**Băng Lính Đánh Thuê (Subagent-Driven Development):**
- Đứng gác cuối 1 Task. Đập ruồi sớm trước khi chúng gây thối các task sau.

**Băng Tự Múc (Executing Plans):**
- Tuýt còi Review sau mỗi cụm mẻ lưới (3 task gom 1 chẳng hạn).

## Cờ Đỏ Chót

**TUYỆT ĐỐI NGHIÊM CẤM:**
- Bỏ qua review vì thấy task "dễ òm mà có mẹ gì đâu". (Sai rành rành chết mợ!).
- Lơ đẹp các lỗi Critical của thằng Reviewer chỉ ra. Cãi ngu bị CEO tế sống.
- Quăng lên PR Code chưa vá xong lỗi Important.
- Cãi dỗi hờn với một bài Feedback sắc bén đúng chuẩn Kỹ thuật. Hèn!
