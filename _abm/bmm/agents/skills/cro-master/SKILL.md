---
name: "cro-master"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Tối ưu tỷ lệ chuyển đổi toàn diện — landing page, forms, signup flow, popups. 7 trụ cột CRO + frameworks A/B testing."
tags: [marketing, cro]
---

> Skill này thay thế: `page-cro`, `form-cro`, `signup-flow-cro`, `popup-cro`

# 🎯 CRO Master — Tối Ưu Tỷ Lệ Chuyển Đổi Toàn Diện

Đọc `product-marketing-context.md` TRƯỚC khi bắt đầu.

## Quy Trình CRO 5 Bước

```
1. ĐO → Baseline metrics (conversion rate, bounce, time on page)
2. PHÂN TÍCH → Heatmap, session recording, funnel analysis
3. GIẢ THUYẾT → "Nếu thay đổi X thì Y tăng Z%"
4. TEST → A/B test 1 biến mỗi lần, 95% confidence
5. TRIỂN KHAI → Winner → production, lặp lại
```

---

## A. Page CRO — 7 Trụ Cột

### 1. Rõ ràng giá trị (Impact cao nhất)
- Khách hiểu bạn làm gì trong 5 giây?
- Lợi ích cụ thể, khác biệt?
- Viết bằng ngôn ngữ khách hàng, không jargon?

### 2. Headline hiệu quả
- **Outcome**: "Đạt [kết quả] mà không [nỗi đau]"
- **Cụ thể**: Số + timeframe + chi tiết
- **Social proof**: "Hơn 10,000 team đang dùng..."

### 3. CTA — Vị trí, Copy, Phân cấp
| ❌ Yếu | ✅ Mạnh |
|--------|---------|
| Đăng ký | Bắt đầu miễn phí |
| Tìm hiểu thêm | Xem demo 3 phút |
| Submit | Nhận báo giá trong 2 phút |

### 4. Visual Hierarchy & Scannability
- Scan nhanh hiểu message chính?
- Elements quan trọng nổi bật?
- Đủ white space?

### 5. Trust Signals & Social Proof
- Logo khách hàng + Testimonials + Case study
- Đặt GẦN CTA

### 6. Xử lý phản đối
- Giá → ROI calculator
- Phù hợp? → Case study tương tự
- Khó triển khai? → Demo + timeline

### 7. Điểm ma sát
- Form quá nhiều field? Mobile tệ? Load chậm?

---

## B. Form CRO — Tối Ưu Biểu Mẫu

### Conversion rate theo số fields:
```
3 fields: ~25% conversion
5 fields: ~20% conversion
7 fields: ~15% conversion
10+ fields: ~10% conversion
```

### Checklist:
- [ ] Chỉ fields BẮT BUỘC cho bước tiếp theo
- [ ] Email + 1 field max cho giai đoạn đầu
- [ ] Labels trên field (không inside placeholder)
- [ ] Error messages cụ thể + real-time validation
- [ ] Submit button CTA rõ ("Nhận báo giá" > "Submit")

### Multi-Step Form:
```
Step 1: Câu hỏi dễ (chọn mục đích) — commitment thấp
Step 2: Thông tin cơ bản — đã invest effort
Step 3: Contact info — sunk cost effect
→ Progress bar + "Bước 2/3" tăng completion 15-20%
```

---

## C. Signup Flow CRO

### Reduce Friction:
- [ ] Chỉ hỏi email ban đầu
- [ ] Social login (Google, Facebook)
- [ ] Không CAPTCHA (dùng honeypot)
- [ ] Show/hide password
- [ ] Real-time validation

### Quick Wins:
```
✅ Giảm fields: 4 → 2 = +50% conversion
✅ Social login: +20-30% signup
✅ CTA text: "Bắt đầu miễn phí" > "Đăng ký"
✅ Remove navigation bar trên signup page
```

---

## D. Popup CRO

### Popup Types + Conversion:
| Type | Trigger | Conversion | Annoyance |
|------|---------|:----------:|:---------:|
| Exit Intent | Mouse rời viewport | 3-5% | Thấp |
| Scroll (50%) | Scroll 50% page | 2-3% | Thấp |
| Timed (30s) | Sau 30s trên page | 2-4% | TB |
| Click | User click link | 5-10% | Rất thấp |

### Anti-Annoyance Rules:
- Max 1 popup per session
- Dismiss = don't show 7 ngày
- No popup cho logged-in users
- Easy close: ESC, click outside, X button

---

## Output Format

```markdown
## Quick Wins (Làm ngay)
1. [thay đổi cụ thể + tại sao]

## High-Impact (Ưu tiên)
1. [thay đổi + impact dự kiến]

## Test Ideas (A/B)
1. [hypothesis: "Nếu X thì Y tăng Z%"]

## Copy Alternatives
- Headline hiện tại → Đề xuất
- CTA hiện tại → Đề xuất
```

## Related Skills
- copywriting, marketing-psychology, ab-test-setup, analytics-tracking
