---
name: "critical-thinking"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Meta-skill tư duy phản biện — Devil's Advocate, 5 Whys, First Principles, Pre-mortem. Nhúng vào mọi planning phase để challenge assumptions."
---

# 🧠 Critical Thinking — Tư Duy Phản Biện

Meta-skill nhúng vào quá trình planning/decision-making — challenge mọi assumptions TRƯỚC khi commit.

## Sử dụng khi

- Đang lập plan → tự challenge trước khi trình CEO
- Ra quyết định quan trọng → kiểm tra blind spots
- Review solution → tìm edge cases
- Đánh giá trade-offs giữa các phương án

## KHÔNG sử dụng khi

- Review toàn diện → dùng `multi-dimensional-review`
- Cần brainstorm ý tưởng → dùng `brainstorming`
- Cần lập kế hoạch → dùng `writing-plans`

## 4 FRAMEWORK

### 1. Devil's Advocate (Luật sư của Quỷ)

```
Với MỖI quyết định, hỏi:
1. "Tại sao KHÔNG nên làm cách này?"
2. "Ai sẽ PHẢN ĐỐI quyết định này và vì sao?"
3. "Nếu đối thủ biết plan này, họ sẽ khai thác điểm yếu nào?"
```

### 2. Five Whys (5 Lần Hỏi Tại Sao)

```
Vấn đề: [X]
→ Tại sao? Vì [A]
  → Tại sao A? Vì [B]
    → Tại sao B? Vì [C]
      → Tại sao C? Vì [D]
        → Tại sao D? → ROOT CAUSE
```

### 3. First Principles (Nguyên Lý Đầu Tiên)

```
1. Bỏ hết assumptions → chỉ giữ sự thật đã chứng minh
2. Hỏi: "Cái gì chắc chắn ĐÚNG?"
3. Xây dựng lại solution từ những sự thật đó
4. So sánh: solution mới vs solution cũ
```

### 4. Pre-mortem (Khám Nghiệm Trước)

```
Giả sử project ĐÃ THẤT BẠI. Hỏi:
1. "Lý do thất bại là gì?"
2. "Dấu hiệu nào chúng ta đã bỏ qua?"
3. "Chúng ta có thể ngăn chặn bằng cách nào?"
```

## QUY TRÌNH PHẢN BIỆN TỰ ĐỘNG

```
Sau khi lập PLAN, tự động chạy 3 bước:

Bước 1: Devil's Advocate → 3 lý do KHÔNG nên
Bước 2: Pre-mortem → 3 kịch bản thất bại
Bước 3: First Principles → verify assumptions

Kết quả:
- Nếu plan vượt qua 3 bước → ĐỦ TIN TƯỞNG trình CEO
- Nếu phát hiện vấn đề → SỬA PLAN trước khi trình
```

## QUY TẮC SẮT

1. **MỌI plan** phải qua ít nhất Devil's Advocate
2. **Quyết định > 1 triệu VND** hoặc ảnh hưởng > 1 tuần → chạy ĐỦ 4 frameworks
3. KHÔNG dùng "chắc là", "có lẽ" → phải có bằng chứng

### 5. Inversion Thinking (Tư Duy Ngược)

```
Thay vì hỏi "Làm sao để thành công?"
→ Hỏi: "Làm sao để CHẮC CHẮN thất bại?"
→ Liệt kê 5 cách thất bại
→ Đảo ngược → Đó là 5 việc PHẢI tránh
```

### 6. Second-Order Effects (Hệ Quả Bậc 2)

```
Quyết định: [X]
→ Hệ quả bậc 1: [Kết quả trực tiếp]
→ Hệ quả bậc 2: [Phản ứng từ thị trường/team/client]
→ Hệ quả bậc 3: [Ảnh hưởng dài hạn 6-12 tháng]

Ví dụ: Tăng giá coaching 250tr → 300tr
  Bậc 1: Revenue/client tăng 20%
  Bậc 2: Số clients giảm 15%? ICP thay đổi?
  Bậc 3: Brand perception "premium hơn" → attract better clients?
```

## Decision Scoring Matrix

| Criteria | Weight | Option A | Option B |
|----------|:------:|:--------:|:--------:|
| Revenue impact | 30% | [1-10] | [1-10] |
| Risk level | 25% | [1-10] | [1-10] |
| Time to implement | 20% | [1-10] | [1-10] |
| Reversibility | 15% | [1-10] | [1-10] |
| Team buy-in | 10% | [1-10] | [1-10] |
| **Weighted Score** | **100%** | **[sum]** | **[sum]** |

---

## Related Skills
- multi-dimensional-review, brainstorming, verification-before-completion

## Nguồn gốc
- BMAD feedback điểm 1: Tư duy phản biện trong planning
- ABM Workforce v2.6
