---
name: "analytics-tracking"
description: "Event tracking GA4/GTM — tracking plan, event naming, UTM params, privacy compliance. Đo lường marketing hiệu quả."
---

# 📊 Analytics Tracking — Đo Lường Marketing

## Sử dụng khi

- Setup GA4 / Google Tag Manager tracking
- Thiết kế tracking plan cho website/app
- Chuẩn hóa event naming conventions
- UTM parameter strategy cho campaigns
- Privacy compliance (cookies, consent)

## KHÔNG sử dụng khi

- Phân tích dữ liệu đã có → dùng `data-analysis`
- A/B testing → dùng `ab-test-setup`
- SEO audit → dùng `seo-audit`

## NGUYÊN TẮC

1. **Track cho quyết định**, không phải cho data
2. **Bắt đầu từ câu hỏi**: "Cần biết gì để ra quyết định?"
3. **Naming nhất quán**: Object-Action format
4. **Data quality > Data quantity**

## TRACKING PLAN

```yaml
tracking_plan:
  - event: "button_clicked"
    category: "engagement"
    trigger: "User clicks CTA"
    properties:
      - button_text: string
      - page_url: string
      - button_location: string
    platform: "GA4 + GTM"
    priority: "P0"
```

## EVENT NAMING

```
Format: object_action
Ví dụ:
  ✅ signup_completed
  ✅ product_viewed
  ✅ checkout_started
  ❌ click (quá chung)
  ❌ SignUpCompleted (không dùng camelCase)
```

### Events Cần Thiết

**Marketing Site:**
- `page_viewed` (auto GA4)
- `cta_clicked` (button clicks)
- `form_submitted` (lead gen)
- `demo_requested`
- `pricing_viewed`

**Product/App:**
- `signup_completed`
- `onboarding_step_completed`
- `feature_activated`
- `subscription_started`
- `payment_completed`

## UTM STRATEGY

```
utm_source    = nền tảng (facebook, google, newsletter)
utm_medium    = kênh (cpc, email, social, organic)
utm_campaign  = tên chiến dịch (spring_sale_2026)
utm_content   = variant (cta_red, banner_v2)
utm_term      = keyword (only paid search)
```

## QUY TẮC

1. Tracking plan **TRƯỚC khi** implement
2. Test tracking trong staging trước production
3. Document mọi events + properties
4. GDPR/PDPA compliance: consent banner bắt buộc

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
