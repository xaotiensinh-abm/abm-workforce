---
name: "email-sequence"
description: "Thiết kế email sequences tự động — welcome, nurture, re-engagement, onboarding. Trigger-based automation."
---

# 📧 Email Sequence — Chuỗi Email Tự Động

## Sử dụng khi

- Thiết kế welcome sequence cho subscribers mới
- Lead nurture trước khi bán
- Re-engagement cho users không hoạt động
- Onboarding sequence cho users mới
- Drip campaigns dài hạn

## KHÔNG sử dụng khi

- Gửi email 1 lần (campaign) → dùng `email-marketing`
- Cold outreach B2B → dùng `cold-email`
- Gửi email thật → dùng `agent-email-cli` (SANDBOX)

## NGUYÊN TẮC

1. **1 email = 1 mục tiêu** — không nhồi nhiều CTA
2. **Giá trị trước, bán sau** — ratio 3:1 (3 value : 1 ask)
3. **Relevance > Volume** — segment đúng > gửi nhiều
4. **Clear path forward** — mỗi email dẫn đến bước tiếp

## SEQUENCE TYPES

### Welcome (Post-Signup) — 5-7 emails, 14 ngày
```
Email 1 (Day 0): Chào mừng + giá trị ngay
Email 2 (Day 1): Quick win / tutorial
Email 3 (Day 3): Case study / social proof
Email 4 (Day 5): Feature highlight
Email 5 (Day 7): Offer / CTA chính
Email 6 (Day 10): Overcome objection
Email 7 (Day 14): Last chance / urgency
```

### Lead Nurture (Pre-Sale) — 4-6 emails, 21 ngày
```
Email 1: Pain point + empathy
Email 2: Education (how-to)
Email 3: Case study
Email 4: Comparison / why us
Email 5: Offer + CTA
Email 6: Follow-up
```

### Re-Engagement — 3-4 emails, 7 ngày
```
Email 1: "Chúng tôi nhớ bạn" + what's new
Email 2: Special offer
Email 3: Last chance
Email 4: Feedback request / unsubscribe option
```

## EMAIL FORMAT

```yaml
email:
  subject: "" # 50 ký tự max, no spam words
  preview_text: "" # 90 ký tự
  from_name: "" # Tên người, không tên công ty
  body:
    hook: "" # 1-2 câu mở đầu
    value: "" # Nội dung chính
    cta: "" # 1 CTA rõ ràng
    ps: "" # Optional P.S. line
  delay: "2 days" # Khoảng cách với email trước
  trigger: "signup" # Event trigger
```

## QUY TẮC

1. Subject line **< 50 ký tự**, không ALL CAPS
2. Unsubscribe link **bắt buộc**
3. Test A/B subject lines
4. Monitor: open rate > 20%, click rate > 2%

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
