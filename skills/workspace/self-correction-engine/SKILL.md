---
name: self-correction-engine
description: Tự đánh giá và sửa lỗi output AI agent. Kích hoạt khi Gate Check phát hiện lỗi hoặc khi cần self-review trước khi giao output. Use when agent output fails validation, needs quality improvement, or when self-review is triggered by gate-check workflow.
metadata:
  author: Antigravity
  version: "1.0"
  category: quality-assurance
---

# Self-Correction Engine

## Khi nào sử dụng
- Gate Check trả về **RETRY**
- User yêu cầu review/improve output
- Agent tự nhận thấy output chưa đạt chuẩn
- Sau khi `/code` hoặc `/plan` để validate trước khi handover

## Quy trình Self-Correction (4 bước)

### Bước 1: Đánh giá (Evaluate)
Tự đánh giá output theo rubric:

```
| Tiêu chí         | Điểm (1-5) | Ghi chú           |
|-------------------|-----------|---------------------|
| Completeness      |           | Đủ yêu cầu?        |
| Correctness       |           | Đúng logic/cú pháp? |
| Quality           |           | Best practices?     |
| Security          |           | Có lỗ hổng?         |
| Edge Cases        |           | Cover đủ?           |
```

**Ngưỡng:** Trung bình ≥4 → PASS. Bất kỳ tiêu chí nào <3 → MUST FIX.

### Bước 2: Phân tích (Diagnose)
Cho mỗi tiêu chí <4, xác định:
1. **Root cause** — Tại sao thiếu/sai?
2. **Fix type** — Sửa nhỏ (tweak) hay sửa lớn (rewrite)?
3. **Blast radius** — Sửa chỗ này có ảnh hưởng chỗ khác?

### Bước 3: Sửa lỗi (Fix)
- **Sửa nhỏ**: Áp dụng trực tiếp, không cần confirm
- **Sửa lớn**: Liệt kê thay đổi → xin confirm user nếu đang trong context quan trọng
- **Sửa liên hoàn**: Nếu fix A ảnh hưởng B → fix cả B

### Bước 4: Verify (Kiểm tra lại)
- Chạy lại đánh giá rubric
- Confirm tất cả tiêu chí ≥4
- Không tạo regression (lỗi mới từ việc sửa)

## Quy tắc quan trọng

1. **Tối đa 2 vòng self-correction** → Nếu vẫn fail → escalate tới user
2. **Không over-engineer** → Fix đúng vấn đề, không refactor toàn bộ
3. **Log mỗi correction** → Ghi vào `tasks/lessons.md` nếu lỗi có pattern
4. **Speed > Perfection** → Correction phải nhanh (<60s tư duy mỗi vòng)

## Ví dụ

**Input**: Code thiếu error handling cho API calls
```
Evaluate: Correctness=4, Security=3 (thiếu error handling), Quality=3
Diagnose: Root cause = quên wrap async calls trong try-catch
Fix: Thêm try-catch cho tất cả fetch/axios calls + error response chuẩn
Verify: Security=5, Quality=4 → PASS ✅
```

## Tích hợp với các workflow khác
- `/code` → Tự động chạy self-correction trước Handover (Giai đoạn 4)
- `/plan` → Validate spec trước khi confirm với user
- `/refactor` → Review kết quả refactor trước khi commit
- `/gate-check` → Khi RETRY, trigger self-correction engine
