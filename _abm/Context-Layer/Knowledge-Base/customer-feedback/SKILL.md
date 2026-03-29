---
name: "customer-feedback"
description: "Thu thập & phân tích feedback khách hàng — NPS, CSAT, VOC, feature requests, sentiment analysis."
---

# 📣 Customer Feedback — Phản Hồi Khách Hàng

## Sử dụng khi

- Thu thập feedback có hệ thống (NPS, CSAT)
- Voice of Customer (VOC) analysis
- Phân tích feature requests + prioritize
- Sentiment analysis từ reviews/surveys
- Close the feedback loop

## KHÔNG sử dụng khi

- Xử lý ticket → dùng `ticket-management`
- Chống churn → dùng `churn-prevention`
- Khảo sát nhân viên → dùng `employee-engagement`

## NPS (Net Promoter Score)

```
Câu hỏi: "Trên thang 0-10, bạn có giới thiệu [sản phẩm] cho người khác?"

9-10 = Promoters → Hỏi: "Tại sao bạn giới thiệu?"
7-8  = Passives  → Hỏi: "Làm gì để bạn cho 9-10?"
0-6  = Detractors → Hỏi: "Điều gì khiến bạn thất vọng?"

NPS = %Promoters - %Detractors
  > 70 = World-class (Apple, Tesla)
  > 50 = Xuất sắc
  > 30 = Tốt
  > 0  = Ổn
  < 0  = CẢNH BÁO
```

## CSAT (Customer Satisfaction)

```
Câu hỏi: "Bạn hài lòng với [trải nghiệm] không?" (1-5 sao)

Target: > 4.0/5 hoặc > 80%
Trigger: Sau mua hàng, sau support, sau onboarding
```

## VOC ANALYSIS

```yaml
voc_analysis:
  period: "monthly"
  sources:
    - surveys: { count: 0, avg_score: 0 }
    - reviews: { count: 0, sentiment: "" }
    - support_tickets: { count: 0, top_issues: [] }
    - social_media: { mentions: 0, sentiment: "" }
  top_themes:
    - theme: ""
      frequency: 0
      sentiment: "positive/negative/neutral"
      action: ""
  feature_requests:
    - feature: ""
      votes: 0
      effort: "S/M/L"
      impact: "high/medium/low"
      priority: "P0/P1/P2"
```

## CLOSE THE LOOP

```
Thu thập → Phân tích → Hành động → Thông báo KH
                                       ↑
                    "Cảm ơn bạn! Chúng tôi đã [action]."
```

## QUY TẮC

1. **Phản hồi Detractors < 24h** — cơ hội cứu KH
2. Close the loop — KH phải biết feedback được xử lý
3. Feature requests **hàng tháng** report CEO
4. NPS đo hàng quý, CSAT đo theo transaction
