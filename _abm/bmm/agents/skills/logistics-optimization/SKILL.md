---
name: "logistics-optimization"
description: "Tối ưu logistics — lập kế hoạch vận chuyển, chọn carrier, theo dõi delivery, tối ưu route, cost analysis."
---

# 🚚 Logistics Optimization — Tối Ưu Vận Chuyển

## Sử dụng khi

- Lập kế hoạch vận chuyển hàng hóa
- So sánh và chọn đơn vị vận chuyển
- Theo dõi delivery status
- Tối ưu chi phí logistics
- Phân tích last-mile delivery

## KHÔNG sử dụng khi

- Quản lý kho → dùng `inventory-management`
- Mua hàng/vendor → dùng `supply-chain`
- Phân tích tài chính → dùng `data-analysis`

## CHECKLIST VẬN CHUYỂN

### Lập kế hoạch
- [ ] Xác định: điểm xuất, điểm đến, khối lượng, kích thước
- [ ] Yêu cầu đặc biệt: nhiệt độ, dễ vỡ, nguy hiểm
- [ ] Deadline giao hàng
- [ ] Ngân sách cho phép

### Chọn Carrier

| Tiêu chí | Trọng số | Carrier A | Carrier B |
|----------|:--------:|:---------:|:---------:|
| Giá | 30% | | |
| Thời gian | 25% | | |
| Độ tin cậy | 20% | | |
| Bảo hiểm | 15% | | |
| Theo dõi realtime | 10% | | |

### Cost Optimization
```
Tổng chi phí logistics = Vận chuyển + Lưu kho + Xử lý + Bảo hiểm

Tối ưu:
1. Gom hàng (consolidation) khi có thể
2. Đàm phán giá volume discount
3. Chọn thời điểm off-peak
4. Last-mile: so sánh tự giao vs outsource
```

## QUY TẮC

1. Đơn hàng > 5 triệu → **2 quotes** từ carriers khác nhau
2. Hàng dễ vỡ/nguy hiểm → bảo hiểm **bắt buộc**
3. Delivery trễ > 2 ngày → **escalate CEO**

---

## Nguồn gốc
- Review v2.7 P2: Cân bằng skills Vận Hành
