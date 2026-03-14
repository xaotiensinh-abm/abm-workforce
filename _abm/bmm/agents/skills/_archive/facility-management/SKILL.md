---
name: "facility-management"
description: "Quản lý cơ sở vật chất — văn phòng, thiết bị, bảo trì, an toàn lao động, mua sắm."
---

# 🏢 Facility Management — Quản Lý Cơ Sở

## Sử dụng khi

- Quản lý văn phòng, trang thiết bị
- Lập kế hoạch bảo trì định kỳ
- Mua sắm tài sản cố định
- An toàn lao động + PCCC
- Quản lý hợp đồng thuê mặt bằng

## KHÔNG sử dụng khi

- Kho hàng sản phẩm → dùng `inventory-management`
- Vận chuyển → dùng `logistics-optimization`
- Chi phí → dùng `expense-management`

## QUẢN LÝ TÀI SẢN

```yaml
asset:
  id: "ASSET-001"
  name: ""
  category: "IT/Furniture/Vehicle/Equipment"
  purchase_date: ""
  cost: 0
  depreciation: "straight-line / 3-5 năm"
  current_value: 0
  location: ""
  assigned_to: ""
  maintenance_schedule: "quarterly"
  next_maintenance: ""
```

## BẢO TRÌ ĐỊNH KỲ

| Hạng mục | Tần suất | Checklist |
|----------|:--------:|-----------|
| Điều hòa | 3 tháng | Vệ sinh filter, gas, tiếng ồn |
| Máy in | 1 tháng | Toner, paper jam, quality |
| Điện | 6 tháng | Ổ cắm, dây, tủ điện |
| PCCC | 6 tháng | Bình chữa cháy, exit sign |
| IT infra | 1 tháng | Server, network, backup |

## AN TOÀN LĐ + PCCC

- [ ] Sơ đồ thoát hiểm cập nhật
- [ ] Bình chữa cháy còn hạn
- [ ] Diễn tập PCCC 2 lần/năm
- [ ] Tủ thuốc y tế đầy đủ
- [ ] Đào tạo ATLĐ cho nhân viên mới

## QUY TẮC

1. Bảo trì **phòng ngừa > sửa chữa** — preventive > reactive
2. Tài sản > 10 triệu → **CEO duyệt** mua sắm
3. PCCC + ATLĐ = **bắt buộc**, không ngoại lệ
4. Kiểm kê tài sản 2 lần/năm
