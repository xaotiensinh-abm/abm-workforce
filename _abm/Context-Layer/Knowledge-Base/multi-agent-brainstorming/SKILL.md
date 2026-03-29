---
name: "multi-agent-brainstorming"
description: "Brainstorming đa agent — review thiết kế có cấu trúc với 5 vai trò agent: Nhà Thiết Kế, Người Phản Biện, Người Giám Sát Ràng Buộc, Người Đại Diện Người Dùng, Người Tổng Hợp."
---

# Brainstorming Đa Agent (Structured Design Review)

Chuyển đổi thiết kế đơn agent thành thiết kế **đã review, đã xác nhận** bằng cách mô phỏng quy trình peer-review với nhiều agent có vai trò ràng buộc.

## Mục đích

- Phát hiện giả định ẩn
- Xác định failure modes sớm
- Xác nhận ràng buộc phi chức năng
- Stress-test thiết kế trước triển khai
- Ngăn chặn "idea swarm chaos"

> ⚠️ Đây **KHÔNG phải brainstorming song song**. Đây là **review thiết kế tuần tự với vai trò cố định**.

## Sử dụng skill này khi

- Thiết kế hệ thống hoặc tính năng quan trọng
- Cần review đa góc nhìn trước khi triển khai
- Muốn phát hiện rủi ro và điểm mù trong thiết kế
- Nâng cấp brainstorming đơn giản thành review có cấu trúc

## KHÔNG sử dụng khi

- Brainstorming ý tưởng đơn giản → dùng `brainstorming`
- Review code cụ thể → dùng `code-review`
- Đánh giá đa chiều hệ thống đã hoàn thành → dùng `multi-dimensional-review`

## Mô Hình Vận Hành

- Một agent thiết kế
- Các agent khác review
- Không agent nào được vượt phạm vi vai trò
- Sáng tạo tập trung; phản biện phân tán
- Mọi quyết định phải ghi log rõ ràng

## 5 Vai Trò Agent (Bắt buộc)

### 1️⃣ Nhà Thiết Kế Chính (Primary Designer)
- **Sở hữu** bản thiết kế
- Chạy skill `brainstorming` chuẩn
- Duy trì Decision Log
- ✅ ĐƯỢC: hỏi rõ, đề xuất thiết kế, sửa đổi theo feedback
- ❌ KHÔNG ĐƯỢC: tự phê duyệt, bỏ qua objection

### 2️⃣ Người Phản Biện (Skeptic / Challenger)
- **Giả định** thiết kế sẽ thất bại
- Xác định điểm yếu và rủi ro
- ✅ ĐƯỢC: hỏi giả định, tìm edge cases, cảnh báo YAGNI
- ❌ KHÔNG ĐƯỢC: đề xuất tính năng mới, thiết kế lại

> Prompt: "Giả sử thiết kế này thất bại trong production. Tại sao?"

### 3️⃣ Người Giám Sát Ràng Buộc (Constraint Guardian)
- Kiểm tra: hiệu năng, khả năng mở rộng, bảo mật, chi phí
- ✅ ĐƯỢC: từ chối thiết kế vi phạm ràng buộc
- ❌ KHÔNG ĐƯỢC: tranh luận về mục tiêu sản phẩm

### 4️⃣ Người Đại Diện Người Dùng (User Advocate)
- Đại diện quan điểm người dùng cuối
- Kiểm tra: cognitive load, khả năng sử dụng, xử lý lỗi
- ✅ ĐƯỢC: chỉ ra điểm gây nhầm lẫn
- ❌ KHÔNG ĐƯỢC: thêm tính năng, thay đổi kiến trúc

### 5️⃣ Người Tổng Hợp (Integrator / Arbiter)
- Giải quyết xung đột giữa các reviewer
- Phê duyệt hoặc từ chối objection
- Tuyên bố thiết kế hoàn thành
- ✅ ĐƯỢC: chấp nhận/từ chối objection, yêu cầu sửa đổi
- ❌ KHÔNG ĐƯỢC: thêm ý tưởng mới, tạo thêm yêu cầu

## Quy Trình 3 Giai Đoạn

### Giai đoạn 1: Thiết kế đơn agent
1. Nhà Thiết Kế chạy skill `brainstorming`
2. Tạo bản thiết kế ban đầu
3. Khởi tạo Decision Log

### Giai đoạn 2: Review tuần tự
Các agent được gọi **lần lượt** theo thứ tự:
1. Người Phản Biện → feedback
2. Người Giám Sát Ràng Buộc → feedback
3. Người Đại Diện Người Dùng → feedback

Nhà Thiết Kế phải:
- Phản hồi từng objection
- Sửa đổi thiết kế nếu cần
- Cập nhật Decision Log

### Giai đoạn 3: Tổng hợp & phân xử
Người Tổng Hợp review:
- Bản thiết kế cuối
- Decision Log
- Các objection chưa giải quyết

**Quyết định rõ ràng**: objection nào chấp nhận, nào từ chối (kèm lý do).

## Decision Log (Bắt buộc)

```
| # | Quyết định | Lý do | Objections | Trạng thái |
|---|-----------|-------|------------|------------|
| 1 | [mô tả]  | [tại sao] | [objections] | Chấp nhận / Đang xử lý |
```

## Tiêu Chí Kết Thúc
- ✅ Mọi objection đã được phản hồi
- ✅ Decision Log đầy đủ
- ✅ Người Tổng Hợp tuyên bố hoàn thành

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
