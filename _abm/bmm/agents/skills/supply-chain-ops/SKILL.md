---
name: "supply-chain-ops"
description: "Quản lý chuỗi cung ứng toàn diện — logistics, kho bãi, chất lượng, nhà cung cấp. KPI dashboard, cost optimization."
tags: [operations]
---

> Skill này thay thế: `supply-chain`, `logistics-optimization`, `inventory-management`, `quality-management`

# 🏭 Supply Chain Ops — Quản Lý Chuỗi Cung Ứng

## Sử dụng khi
- Tối ưu chi phí vận chuyển / kho bãi
- Quản lý nhà cung cấp và đánh giá hiệu suất
- Theo dõi tồn kho, đặt hàng, EOQ
- Kiểm soát chất lượng (QC/QA)
- Phân tích bottleneck và cải tiến liên tục

## Quy Trình Chuỗi Cung Ứng

```
Nhà cung cấp → Mua hàng → Kho → Sản xuất → Phân phối → Khách hàng
      ↑                                                      |
      └──── Forecast + Demand Planning ←────────────────────┘
```

---

## A. Quản Lý Nhà Cung Cấp

### Đánh giá nhà cung cấp (Supplier Scorecard):
| Tiêu chí | Trọng số | Thang điểm |
|----------|---------|------------|
| Chất lượng (tỷ lệ lỗi) | 30% | 1-5 |
| Giao hàng đúng hẹn | 25% | 1-5 |
| Giá cạnh tranh | 20% | 1-5 |
| Khả năng đáp ứng | 15% | 1-5 |
| Tài chính ổn định | 10% | 1-5 |

### Chiến lược nguồn cung:
- **Single source**: Rủi ro cao, thương lượng yếu → chỉ cho unique items
- **Dual source**: Cân bằng rủi ro + cạnh tranh → recommended
- **Multi source**: Phức tạp quản lý → cho commodity items

---

## B. Quản Lý Tồn Kho

### Công thức EOQ (Economic Order Quantity):
```
EOQ = √(2 × D × S / H)

D = Nhu cầu hàng năm (đơn vị)
S = Chi phí đặt hàng (VND/lần)
H = Chi phí lưu kho (VND/đơn vị/năm)
```

### Phân loại ABC:
| Loại | % SKU | % Giá trị | Chiến lược |
|------|-------|-----------|------------|
| A | 10-20% | 70-80% | Kiểm soát chặt, đếm tuần, safety stock thấp |
| B | 20-30% | 15-20% | Kiểm soát vừa, đếm tháng |
| C | 50-70% | 5-10% | Kiểm soát lỏng, đếm quý, order lớn |

### KPI Kho:
| KPI | Công thức | Target |
|-----|-----------|--------|
| Inventory Turnover | COGS / Avg Inventory | > 8 lần/năm |
| Days Sales of Inventory | 365 / Turnover | < 45 ngày |
| Stock-out Rate | # Stock-outs / # Orders | < 2% |
| Carrying Cost | Total Inv. Cost / Avg Inv. Value | < 25% |
| Order Accuracy | Correct Orders / Total Orders | > 99% |

---

## C. Logistics & Vận Chuyển

### Tối ưu chi phí vận chuyển:
```
1. Consolidate shipments — gộp đơn, giảm trips
2. Route optimization — thuật toán TSP/VRP
3. Mode selection — so sánh đường bộ/biển/hàng không
4. Warehouse location — gần cluster khách hàng lớn nhất
5. Milk-run delivery — 1 xe, nhiều điểm giao
```

### Bảng so sánh phương thức:
| Phương thức | Chi phí | Tốc độ | Phù hợp |
|-------------|---------|--------|---------|
| Đường bộ | TB | 1-3 ngày | < 500km, linh hoạt |
| Đường biển | Thấp | 7-30 ngày | Hàng nặng, bulk, quốc tế |
| Hàng không | Cao | 1-2 ngày | Urgent, giá trị cao, nhẹ |
| Đường sắt | Thấp-TB | 3-7 ngày | Bulk, khoảng cách xa |

---

## D. Quản Lý Chất Lượng

### Công cụ QC:
| Công cụ | Mục đích | Khi nào dùng |
|---------|---------|-------------|
| Pareto (80/20) | Xác định lỗi chủ yếu | Phân tích lỗi |
| Ishikawa (Fishbone) | Tìm nguyên nhân gốc | Root cause analysis |
| Control Chart | Giám sát quy trình | Theo dõi SPC |
| FMEA | Đánh giá rủi ro | Phòng ngừa lỗi |
| Checklist | Kiểm tra hàng ngày | QC incoming/outgoing |

### Quy trình xử lý lỗi:
```
1. PHÁT HIỆN → Ghi nhận (NCR — Non-Conformance Report)
2. CÁCH LY → Tách hàng lỗi, ngăn xuất kho
3. PHÂN TÍCH → Root cause (5 Whys / Fishbone)
4. SỬA LỖI → Hành động khắc phục + phòng ngừa
5. XÁC MINH → Verify fix, update SOP
```

---

## Dashboard KPI Tổng Hợp

| Nhóm | KPI | Target |
|------|-----|--------|
| Supplier | On-time delivery | > 95% |
| Supplier | Quality rate | > 98% |
| Inventory | Turnover | > 8x/năm |
| Inventory | Stock-out | < 2% |
| Logistics | Cost/revenue ratio | < 8% |
| Logistics | On-time shipment | > 95% |
| Quality | First-pass yield | > 97% |
| Quality | Customer complaint | < 1% |

## Related Skills
- kaizen, facility-management, data-analysis, expense-management
