---
name: "referral-program"
description: "Thiết kế referral + affiliate programs — incentive design, viral loops, tracking, launch checklist."
---

# 🔗 Referral Program — Chương Trình Giới Thiệu

## Sử dụng khi

- Thiết kế chương trình referral cho khách hàng
- Setup affiliate program
- Tối ưu viral coefficient
- Tạo incentive structure

## KHÔNG sử dụng khi

- Cold outreach → dùng `cold-email`
- Loyalty/churn → dùng `churn-prevention`
- Pricing → dùng `pricing-strategy`

## REFERRAL vs AFFILIATE

| | Referral | Affiliate |
|--|---------|----------|
| Ai giới thiệu | Khách hàng hiện tại | Đối tác/influencer |
| Motivation | Sản phẩm tốt + reward | Hoa hồng |
| Scale | Organic, chậm | Có thể scale nhanh |
| Trust | Rất cao | Trung bình |

## THIẾT KẾ REFERRAL

### The Referral Loop
```
User hài lòng → Share link → Bạn bè click → Signup → Cả 2 được thưởng → Lặp lại
```

### Trigger Moments (khi nào user share?)
- Sau khi đạt kết quả đầu tiên
- Sau khi hoàn thành onboarding
- Sau milestone (30 ngày, 100 actions)
- Khi nhận được kết quả bất ngờ

### Incentive Structure
| Model | Ví dụ | Phù hợp |
|-------|-------|---------|
| Two-sided | Cả 2 được $10 credit | SaaS, apps |
| One-sided | Người giới thiệu được tháng free | Subscription |
| Tiered | 1 ref = 10%, 5 ref = 20%, 10 ref = 50% | Growth aggressive |
| Charitable | Donate $5/ref | Brand purpose |

## METRICS

```yaml
referral_metrics:
  referral_rate: "% users có ít nhất 1 referral"
  viral_coefficient: "invites × conversion_rate"
  time_to_first_referral: "ngày"
  referral_revenue: "doanh thu từ referred users"
  cac_referral: "cost per referred customer"
```

## QUY TẮC

1. Incentive phải **có giá trị thật** — không token rewards
2. Share mechanism **tối đa 2 clicks**
3. Track attribution chính xác
4. Test incentive A/B trước khi scale

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
