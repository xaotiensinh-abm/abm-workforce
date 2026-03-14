---
name: "cash-flow-forecast"
description: "Dự báo dòng tiền — thu chi 13 tuần, scenario planning, runway calculation."
---

# 💵 Cash Flow Forecast — Dự Báo Dòng Tiền

## Sử dụng khi

- Dự báo thu chi 13 tuần (rolling forecast)
- Tính runway (còn bao lâu hết tiền)
- Scenario planning (best/base/worst)
- Quyết định đầu tư/cắt giảm

## KHÔNG sử dụng khi

- Chi phí ngắn hạn → dùng `expense-management`
- Thuế → dùng `tax-compliance`
- Báo cáo tài chính → dùng `xlsx`

## MÔ HÌNH 13 TUẦN

```yaml
cash_flow:
  opening_balance: 0
  weeks:
    - week: 1
      inflows:
        - revenue: 0
        - other_income: 0
      outflows:
        - payroll: 0
        - rent: 0
        - marketing: 0
        - operations: 0
        - other: 0
      net_cash_flow: 0
      closing_balance: 0
```

## RUNWAY CALCULATION

```
Runway (tháng) = Tiền mặt hiện tại / Burn rate trung bình

Burn rate = Tổng chi phí tháng - Doanh thu tháng

Cảnh báo:
  > 12 tháng = An toàn (xanh)
  6-12 tháng = Cẩn thận (vàng)
  < 6 tháng  = NGUY HIỂM (đỏ)
  < 3 tháng  = KHẨN CẤP → CEO action ngay
```

## SCENARIO PLANNING

| Scenario | Revenue | Expenses | Runway |
|----------|:-------:|:--------:|:------:|
| **Best** | +20% | -5% | |
| **Base** | = | = | |
| **Worst** | -30% | +10% | |

## QUY TẮC

1. Update **hàng tuần** — không để stale
2. Runway < 6 tháng → **báo CEO ngay**
3. Luôn có scenario worst-case
4. Tách rõ recurring vs one-time
