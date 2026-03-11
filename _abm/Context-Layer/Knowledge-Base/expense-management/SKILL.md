---
name: "expense-management"
description: "Quản lý chi phí — duyệt GĐ, phân loại, budget tracking, cost reduction."
---

# 💰 Expense Management — Quản Lý Chi Phí

## Sử dụng khi

- Phê duyệt chi phí hàng ngày
- Phân loại chi phí theo danh mục
- Tracking budget vs actual
- Đề xuất cost reduction

## KHÔNG sử dụng khi

- Dự báo dòng tiền → dùng `cash-flow-forecast`
- Thuế → dùng `tax-compliance`
- Phân tích dữ liệu → dùng `data-analysis`

## QUY TRÌNH PHÊ DUYỆT

```
< 2 triệu   → Trưởng phòng duyệt
2-10 triệu  → Kế toán trưởng duyệt
> 10 triệu  → CEO duyệt
> 50 triệu  → CEO + Hội đồng duyệt
```

## PHÂN LOẠI CHI PHÍ

```yaml
expense_categories:
  fixed: # Chi phí cố định
    - rent: "Thuê văn phòng"
    - salary: "Lương + bảo hiểm"
    - subscriptions: "Phần mềm, tools"
  variable: # Chi phí biến đổi
    - marketing: "Ads, content, events"
    - travel: "Công tác, đi lại"
    - supplies: "Văn phòng phẩm"
  capex: # Chi phí đầu tư
    - equipment: "Thiết bị, máy móc"
    - software: "License dài hạn"
```

## BUDGET TRACKING

| Danh mục | Budget | Actual | Variance | % Used |
|----------|:------:|:------:|:--------:|:------:|
| Marketing | | | | |
| HR | | | | |
| IT | | | | |
| Operations | | | | |
| **Tổng** | | | | |

## QUY TẮC

1. Mọi chi phí **phải có hóa đơn/chứng từ**
2. Over-budget > 10% → **CEO approval bắt buộc**
3. Review chi phí **hàng tuần**
4. Cost reduction report hàng quý
