---
name: "quality-management"
description: "Quản lý chất lượng — ISO 9001, QC checklist, PDCA, defect tracking, KPI chất lượng."
---

# ✅ Quality Management — Quản Lý Chất Lượng

## Sử dụng khi

- Xây dựng hệ thống quản lý chất lượng ISO 9001
- QC checklist cho sản phẩm/dịch vụ
- PDCA cycles cải tiến liên tục
- Defect tracking & root cause analysis

## KHÔNG sử dụng khi

- Compliance pháp lý → dùng `compliance-checker`
- Quản lý kho → dùng `inventory-management`
- Code review → dùng `code-review`

## PDCA CYCLE

```
Plan → Do → Check → Act → Plan → ...

Plan:  Xác định vấn đề + mục tiêu + kế hoạch
Do:    Thực hiện theo kế hoạch (pilot nhỏ)
Check: Đo kết quả vs mục tiêu
Act:   Chuẩn hóa nếu OK, điều chỉnh nếu chưa OK
```

## QC CHECKLIST

```yaml
qc_checklist:
  product: ""
  version: ""
  inspector: ""
  date: ""
  items:
    - criteria: ""
      standard: ""
      actual: ""
      pass: true/false
      note: ""
  overall: "PASS/FAIL"
  defects: 0
```

## KPI CHẤT LƯỢNG

| KPI | Mục tiêu | Công thức |
|-----|----------|-----------|
| Defect rate | < 2% | Lỗi / Tổng sản phẩm |
| First pass yield | > 95% | Đạt lần 1 / Tổng kiểm |
| Customer complaints | < 5/tháng | Số phàn nàn |
| CSAT | > 4.0/5 | Trung bình đánh giá |
| Rework rate | < 3% | Làm lại / Tổng |

## QUY TẮC

1. **Zero tolerance** cho lỗi ảnh hưởng khách hàng
2. Root cause analysis cho MỌI defect > 2%
3. PDCA review hàng tháng
4. Documentation đầy đủ — không có QC = không ship
