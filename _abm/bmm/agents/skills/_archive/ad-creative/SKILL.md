---
name: "ad-creative"
description: "Tạo bulk ad copy cho Google/Meta/LinkedIn/TikTok — iterate từ performance data, A/B variants, CSV export."
---

# 📢 Ad Creative — Tạo Quảng Cáo Đa Nền Tảng

## Sử dụng khi

- Chạy quảng cáo Google Ads, Meta (FB/IG), LinkedIn, TikTok
- Cần tạo hàng loạt ad variations nhanh
- Iterate quảng cáo dựa trên performance data
- Cần ad copy đúng specs từng platform

## KHÔNG sử dụng khi

- Viết blog/content dài → dùng `copywriting`
- Email marketing → dùng `email-marketing` hoặc `email-sequence`
- Social organic → dùng `social-content`
- Chưa có product-marketing-context → load `product-marketing-context` trước

## PLATFORM SPECS

### Google Ads (RSA)
- Headlines: 15 max, 30 ký tự/headline
- Descriptions: 4 max, 90 ký tự/description
- Pin headlines 1-3 khi cần control messaging

### Meta Ads (FB/IG)
- Primary text: 125 ký tự (hiển thị trước "Xem thêm")
- Headline: 40 ký tự
- Description: 30 ký tự
- Image: 1080×1080 (1:1) hoặc 1080×1920 (9:16 stories)

### LinkedIn Ads
- Intro text: 150 ký tự (truncate mobile)
- Headline: 70 ký tự
- Description: 100 ký tự
- Image: 1200×627

### TikTok Ads
- Text: 100 ký tự
- Video: 9:16, 15-60s
- Hook trong 3 giây đầu

## WORKFLOW

```
Mode 1: TẠO MỚI
  1. Xác định góc tiếp cận (3-5 angles)
  2. Viết 5+ variations mỗi angle
  3. Validate đúng specs platform
  4. Export CSV cho bulk upload

Mode 2: ITERATE TỪ DATA
  1. Phân tích winners (CTR > avg, CPA < target)
  2. Phân tích losers (tại sao fail?)
  3. Tạo variations từ winners
  4. Document iteration log
```

## OUTPUT FORMAT

```yaml
ad_creative:
  campaign: ""
  platform: "google/meta/linkedin/tiktok"
  angle: ""
  variants:
    - headline: ""
      description: ""
      cta: ""
      predicted_ctr: ""
  export_csv: true
```

## QUY TẮC

1. Mỗi angle ít nhất 5 variants
2. Không dùng clickbait hoặc misleading
3. Test ít nhất 3 angles trước khi scale
4. Log mọi iteration vào performance tracker

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
- Adapted cho ABM Workforce
