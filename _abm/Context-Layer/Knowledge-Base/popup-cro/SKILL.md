---
name: "popup-cro"
description: "Tối ưu popups/modals — exit intent, scroll trigger, timed display. Không spam, maximize conversion."
---

# 💬 Popup CRO — Tối Ưu Popups & Modals

## Sử dụng khi

- Cần tăng email signups
- Exit intent popup cho e-commerce
- Announcement/promotion modal
- Content upgrade/lead magnet delivery

## KHÔNG sử dụng khi

- Form trên page → dùng `form-cro`
- Signup flow → dùng `signup-flow-cro`
- Landing page → dùng `page-cro`
- Popup ads → KHÔNG hỗ trợ spam

## POPUP TYPES

| Type | Trigger | Conversion | Annoyance |
|------|---------|:----------:|:---------:|
| Exit Intent | Mouse rời viewport | 3-5% | Thấp |
| Timed (30s) | Sau 30s trên page | 2-4% | Trung bình |
| Scroll (50%) | Scroll 50% page | 2-3% | Thấp |
| Click | User click link/button | 5-10% | Rất thấp |
| Welcome Mat | Full-screen khi vào | 3-7% | Cao |

## CHECKLIST

### Design
- [ ] Close button **RÕ RÀNG** (X lớn, góc trên phải)
- [ ] Mobile: full-screen hoặc bottom sheet (không overlay nhỏ)
- [ ] Contrast đủ với background
- [ ] Headline + 1 sentence + 1 CTA
- [ ] Image/icon relevant

### Timing Rules
```
KHÔNG hiện popup:
  - Trước 15 giây (chưa đọc gì)
  - Khi user đang fill form
  - Cho returning visitors đã dismiss
  - Trên mobile nếu intrusive (Google penalty)

NÊN hiện popup:
  - Exit intent (desktop)
  - Scroll 50%+ (engaged user)
  - Sau 30-60s trên content dài
  - Click-triggered (highest quality)
```

### Anti-Annoyance Rules
- [ ] Max 1 popup per session
- [ ] Dismiss = don't show again 7 ngày (cookie)
- [ ] No popup cho logged-in users
- [ ] Easy close: ESC, click outside, X button

## QUY TẮC

1. **1 popup per session MAX**
2. Exit intent > timed > scroll
3. Dismiss cookie ít nhất 7 ngày
4. A/B test headline + offer

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
