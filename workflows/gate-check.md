---
description: 🚧 Gate Check — Kiểm tra chất lượng output giữa các bước workflow trước khi tiếp tục
---

# WORKFLOW: /gate-check - Quality Gate Between Steps

Bạn là **Antigravity Quality Controller**. Trước khi tiếp tục bước tiếp theo trong BẤT KỲ workflow nào, bạn PHẢI chạy Gate Check.

**Mục đích:** Ngăn output lỗi "chảy xuống" các bước sau. Bắt lỗi SỚM, sửa NGAY.

---

## Khi nào dùng Gate Check?

Gate Check được nhúng **tự động** tại các điểm chuyển tiếp:
- `/plan` → `/code`: Output spec có đủ chi tiết?
- `/code` → `/test`: Code có compile/parse được không?
- `/test` → `/deploy`: Tests có pass không?
- Bất kỳ bước nào output sẽ là input cho bước sau

---

## Quy Trình Gate Check (3 bước)

### Bước 1: Validate Output (Kiểm tra đầu ra)

Kiểm tra output vừa tạo theo **4 tiêu chí**:

| # | Tiêu chí | Check |
|---|----------|-------|
| 1 | **Completeness** — Output có đầy đủ so với yêu cầu? | Đối chiếu từng mục trong spec/yêu cầu |
| 2 | **Correctness** — Output có đúng logic/cú pháp? | Parse, compile, hoặc review logic |
| 3 | **Consistency** — Output có nhất quán với context? | So sánh với code/tài liệu hiện có |
| 4 | **Quality** — Output đạt chuẩn Senior Dev? | Code smell, best practices, security |

### Bước 2: Quyết Định (Pass / Retry / Escalate)

```
PASS ✅ → Tiếp tục bước tiếp theo
  Điều kiện: 4/4 tiêu chí đạt

RETRY 🔄 → Tự sửa và check lại (tối đa 2 lần retry)
  Điều kiện: 1-2 tiêu chí không đạt, có thể tự sửa
  Hành động: 
    1. Xác định nguyên nhân cụ thể
    2. Sửa output
    3. Chạy lại Gate Check

ESCALATE 🚨 → Dừng lại, hỏi User
  Điều kiện: 
    - 3+ tiêu chí không đạt
    - Đã retry 2 lần vẫn fail
    - Phát hiện vấn đề thiết kế/kiến trúc
  Hành động: Báo cáo rõ ràng cho User:
    "⚠️ Gate Check FAILED tại [Bước]. Lý do: [Chi tiết]. Đề xuất: [Phương án]"
```

### Bước 3: Ghi Log

Sau mỗi Gate Check, ghi ngắn gọn:
```
📋 Gate Check Log:
  - Bước: [Plan → Code]
  - Kết quả: [PASS/RETRY/ESCALATE]
  - Ghi chú: [Nếu có issue đáng lưu ý]
```

---

## Nhúng Gate Check vào Workflow Hiện Có

### Mẫu nhúng vào /plan → /code:
```
/plan hoàn thành spec
  ↓
🚧 GATE CHECK: Spec đủ chi tiết? Có edge cases? Có security?
  ↓ PASS
/code bắt đầu implement
  ↓
🚧 GATE CHECK: Code chạy được? Match spec? Có bugs?
  ↓ PASS
/test bắt đầu
```

### Mẫu Self-Correction khi RETRY:
```
🚧 Gate Check → RETRY (thiếu error handling)
  ↓
🔄 Agent tự thêm try-catch cho tất cả async operations
  ↓
🚧 Gate Check lần 2 → PASS ✅
```

---

## ⚠️ QUY TẮC QUAN TRỌNG:

1. **KHÔNG bỏ qua Gate Check** — Dù output "trông ổn", vẫn phải check
2. **Tối đa 2 retries** — Không vòng lặp vô tận. Retry 2 lần fail → ESCALATE
3. **Gate Check phải nhanh** — Dưới 30 giây tư duy. Không over-analyze
4. **Log ngắn gọn** — 1-2 dòng, không viết essay

---

## ⚠️ NEXT STEPS:
```
1️⃣ Output PASS? → Tiếp tục workflow bình thường
2️⃣ Output RETRY? → Sửa và check lại
3️⃣ Output ESCALATE? → Dừng, hỏi User
4️⃣ Muốn self-correction tự động? Xem skill /self-correction-engine
```
