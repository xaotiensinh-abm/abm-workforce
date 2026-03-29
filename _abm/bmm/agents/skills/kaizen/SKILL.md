---
name: "kaizen"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Cải tiến liên tục Kaizen — 4 trụ cột: cải tiến từng bước, chống lỗi Poka-Yoke, chuẩn hóa công việc, Just-In-Time."
---

# Kaizen: Cải Tiến Liên Tục

Nhiều cải tiến nhỏ, liên tục. Chống lỗi ngay từ thiết kế. Tuân theo quy trình đã chứng minh. Chỉ xây những gì cần.

**Nguyên tắc cốt lõi:** Nhiều cải tiến nhỏ vượt trội hơn một thay đổi lớn. Ngăn chặn lỗi từ giai đoạn thiết kế, không phải bằng sửa chữa.

## Sử dụng skill này khi

- Cải thiện code, quy trình, hoặc workflow
- Refactoring và nâng cấp chất lượng
- Thiết lập quy trình chuẩn hóa
- Xử lý lỗi và validation

## KHÔNG sử dụng khi

- Cần redesign từ đầu → dùng `brainstorming` hoặc `writing-plans`
- Cần đánh giá tổng thể hệ thống → dùng `multi-dimensional-review`

## 4 Trụ Cột

### 1. Cải Tiến Liên Tục (Kaizen)

**Nguyên tắc ưu tiên cải tiến từng bước:**
- Thực hiện thay đổi nhỏ nhất cải thiện chất lượng
- Một cải tiến mỗi lần
- Xác minh từng thay đổi trước khi tiếp
- Tạo momentum qua các chiến thắng nhỏ

**Luôn để code tốt hơn khi rời đi:**
- Sửa vấn đề nhỏ khi gặp
- Refactor trong phạm vi khi đang làm
- Cập nhật comment lỗi thời
- Xóa dead code khi thấy

**Tinh chỉnh lặp:**
1. Lần 1: Làm cho nó **chạy**
2. Lần 2: Làm cho nó **rõ ràng**
3. Lần 3: Làm cho nó **hiệu quả**
- Không cố cả 3 cùng lúc!

### 2. Poka-Yoke (Chống Lỗi)

**Thiết kế loại trừ khả năng sai:**
- Dùng type systems để ngăn giá trị không hợp lệ
- Validate ở biên giới (input/output)
- Dùng enum thay vì magic strings
- Bắt buộc thứ tự đúng qua API design

**3 cấp độ chống lỗi:**
1. **Ngăn chặn** — Không thể xảy ra lỗi (tốt nhất)
2. **Phát hiện** — Phát hiện lỗi ngay khi xảy ra
3. **Giảm thiểu** — Giảm tác động khi lỗi xảy ra

### 3. Chuẩn Hóa Công Việc

**Sau khi tìm ra cách tốt, chuẩn hóa nó:**
- Ghi lại quy trình dưới dạng checklist/template
- Dùng linting rules để enforce chuẩn
- Tạo code patterns tái sử dụng
- Cập nhật chuẩn khi tìm ra cách tốt hơn

**Chuẩn hóa KHÔNG có nghĩa là cứng nhắc:**
- Chuẩn phải tiến hóa
- Mọi người đều được đề xuất cải tiến
- Kết quả đo được quyết định giữ hay bỏ chuẩn

### 4. Just-In-Time (Đúng Lúc)

**Chỉ xây khi cần, không dự đoán quá sớm:**
- Không abstraction sớm — chờ pattern lặp 3 lần
- Không optimize sớm — đo trước, optimize sau
- Không feature sớm — YAGNI (You Aren't Gonna Need It)

## Ứng Dụng Cho ABM

| Tình huống | Áp dụng Kaizen |
|-----------|----------------|
| Review skill | Cải tiến từng section, không rewrite |
| Cập nhật manifest | Thêm 1 skill, test, rồi thêm tiếp |
| Sửa workflow | Sửa 1 bước, xác minh, rồi tiếp |
| Feedback từ CEO | Sửa ngay, nhỏ, có bằng chứng |

## Cảnh Báo Đỏ — DỪNG khi thấy

- 🔴 Cố sửa tất cả cùng lúc
- 🔴 Refactor mà không có test
- 🔴 "Để tôi rewrite hoàn toàn" — KHÔNG
- 🔴 Optimize mà chưa đo baseline

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
