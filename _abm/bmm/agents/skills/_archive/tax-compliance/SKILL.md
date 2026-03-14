---
name: "tax-compliance"
description: "Tuân thủ thuế VN — TNCN, GTGT, TNDN. Lịch nộp, tính toán, chứng từ."
---

# 🏛️ Tax Compliance — Tuân Thủ Thuế

## Sử dụng khi

- Tính thuế TNCN cho nhân viên
- Kê khai thuế GTGT hàng tháng/quý
- Tính thuế TNDN hàng quý/năm
- Kiểm tra deadline nộp thuế

## KHÔNG sử dụng khi

- Quản lý chi phí → dùng `expense-management`
- Dòng tiền → dùng `cash-flow-forecast`
- Hợp đồng → dùng `contract-review`

## LỊCH NỘP THUẾ VN

| Loại | Kỳ | Deadline | Mẫu |
|------|-----|----------|------|
| GTGT | Tháng/Quý | Ngày 20 tháng sau / ngày 30 quý sau | 01/GTGT |
| TNCN | Tháng/Quý | Cùng GTGT | 05/KK-TNCN |
| TNDN | Quý | Ngày 30 quý sau | 01A/TNDN |
| TNDN | Năm | Ngày 31/03 năm sau | 03/TNDN |

## THUẾ TNCN

### Biểu thuế lũy tiến (2024)
```
Bậc 1:  ≤ 5 triệu       →  5%
Bậc 2:  5-10 triệu      → 10%
Bậc 3:  10-18 triệu     → 15%
Bậc 4:  18-32 triệu     → 20%
Bậc 5:  32-52 triệu     → 25%
Bậc 6:  52-80 triệu     → 30%
Bậc 7:  > 80 triệu      → 35%

Giảm trừ bản thân: 11 triệu/tháng
Giảm trừ người phụ thuộc: 4.4 triệu/người/tháng
```

## THUẾ GTGT

```
Thuế GTGT phải nộp = Thuế GTGT đầu ra - Thuế GTGT đầu vào

Thuế suất phổ biến:
  10% — hàng hóa, dịch vụ thông thường
   8% — giảm thuế (nếu có chính sách)
   5% — nông sản, y tế, giáo dục
   0% — xuất khẩu
```

## CHECKLIST

- [ ] Hóa đơn đầu vào hợp lệ (tên, MST, ngày)
- [ ] Kê khai đúng hạn
- [ ] Nộp thuế đúng hạn (phạt chậm: 0.03%/ngày)
- [ ] Lưu trữ chứng từ 10 năm
- [ ] Quyết toán TNCN hàng năm

## QUY TẮC

1. **Nộp trước deadline** ít nhất 3 ngày
2. Kiểm tra hóa đơn **trước khi** kê khai
3. Chậm nộp = phạt 0.03%/ngày — **không chấp nhận**
4. Lưu trữ 10 năm theo quy định
