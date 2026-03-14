---
name: "ticket-management"
description: "Quản lý ticket CSKH — phân loại, SLA, escalation, đóng ticket, báo cáo."
---

# 🎫 Ticket Management — Quản Lý Ticket

## Sử dụng khi

- Quản lý ticket từ khách hàng
- Thiết lập SLA response/resolution
- Escalation workflow
- Báo cáo CSKH: volume, SLA, CSAT

## KHÔNG sử dụng khi

- Churn prevention → dùng `churn-prevention`
- Thu thập feedback → dùng `customer-feedback`
- Email → dùng `agent-email-cli`

## PHÂN LOẠI TICKET

| Priority | SLA Response | SLA Resolution | Ví dụ |
|:--------:|:-----------:|:-------------:|-------|
| P0 Critical | 15 phút | 2 giờ | Hệ thống down, mất dữ liệu |
| P1 High | 1 giờ | 8 giờ | Không login được, lỗi thanh toán |
| P2 Medium | 4 giờ | 24 giờ | Feature lỗi, hiển thị sai |
| P3 Low | 8 giờ | 72 giờ | Hỏi đáp, đề xuất feature |

## WORKFLOW

```
Tiếp nhận → Phân loại → Xử lý → Giải quyết → Đóng
    ↓           ↓          ↓          ↓         ↓
  Auto-reply  Priority   Agent     Confirm   CSAT survey
              + Assign   handles   với KH
```

## ESCALATION

```
Level 1: Agent CSKH (15 phút đầu)
  ↓ Không giải quyết được
Level 2: Team Lead (escalate + context)
  ↓ Không giải quyết được
Level 3: Manager / Tech Lead
  ↓ Nghiêm trọng
Level 4: CEO (P0 only)
```

## METRICS

```yaml
cskh_metrics:
  daily_volume: 0
  avg_response_time: "phút"
  avg_resolution_time: "giờ"
  sla_compliance: "%" # target > 95%
  first_contact_resolution: "%" # target > 70%
  csat_score: 0 # target > 4.0/5
  backlog: 0 # open tickets
```

## QUY TẮC

1. P0 = **DROP EVERYTHING** tập trung fix
2. Response time **< SLA** LUÔN LUÔN
3. Close ticket chỉ khi KH **confirm** giải quyết
4. CSAT survey sau mỗi ticket closed
