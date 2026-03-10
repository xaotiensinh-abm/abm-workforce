---
name: "inventory-management"
description: "Quản lý kho hàng — theo dõi tồn kho, min/max levels, reorder alerts, ABC analysis, kiểm kê. Dành cho phòng Vận Hành."
---

# 📦 Inventory Management — Quản Lý Kho Hàng

## Sử dụng khi

- Theo dõi tồn kho realtime
- Thiết lập min/max stock levels
- Phân tích ABC (80/15/5)
- Kiểm kê định kỳ
- Dự báo nhu cầu nhập hàng

## KHÔNG sử dụng khi

- Quản lý chuỗi cung ứng tổng thể → dùng `supply-chain`
- Phân tích dữ liệu business → dùng `data-analysis`
- Tạo báo cáo Excel → dùng `xlsx`

## CHECKLIST KHO HÀNG

### Thiết lập
- [ ] Danh mục sản phẩm/vật tư (SKU, tên, đơn vị)
- [ ] Vị trí lưu kho (kệ, khu, nhà kho)
- [ ] Min/Max stock levels cho từng SKU
- [ ] Reorder point = Lead time × Daily usage + Safety stock
- [ ] Phương pháp: FIFO / LIFO / Weighted Average

### ABC Analysis
```
Nhóm A: 20% SKU → 80% giá trị → Kiểm soát chặt, kiểm kê tuần
Nhóm B: 30% SKU → 15% giá trị → Kiểm soát trung bình, kiểm kê tháng
Nhóm C: 50% SKU → 5% giá trị → Kiểm soát nhẹ, kiểm kê quý
```

### Template YAML
```yaml
inventory:
  - sku: "SKU-001"
    name: ""
    unit: "cái"
    location: "Kho A - Kệ 1"
    current_qty: 0
    min_level: 10
    max_level: 100
    reorder_point: 20
    abc_class: "A"
    last_count: "2026-03-10"
```

### Kiểm kê
- [ ] Đếm thực tế vs hệ thống
- [ ] Chênh lệch > 5% → điều tra
- [ ] Cập nhật số liệu
- [ ] Báo cáo CEO nếu mất mát

## QUY TẮC

1. Kiểm kê nhóm A **hàng tuần**
2. Chênh lệch > 5% → **báo CEO ngay**
3. Reorder alert → CEO duyệt PO
4. FIFO bắt buộc cho hàng có hạn sử dụng

---

## Nguồn gốc
- Review v2.7 P2: Cân bằng skills Vận Hành
