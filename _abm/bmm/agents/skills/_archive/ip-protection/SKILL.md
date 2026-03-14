---
name: "ip-protection"
description: "Bảo vệ sở hữu trí tuệ — đăng ký nhãn hiệu, bản quyền, patent, trade secrets, NDA."
---

# 🛡️ IP Protection — Bảo Vệ Sở Hữu Trí Tuệ

## Sử dụng khi

- Đăng ký nhãn hiệu (trademark)
- Bảo vệ bản quyền (copyright) content, phần mềm
- Đánh giá patent filing
- Soạn NDA / Non-compete
- Xử lý vi phạm SHTT

## KHÔNG sử dụng khi

- Hợp đồng kinh doanh → dùng `contract-review`
- Compliance → dùng `compliance-checker`
- Luật lao động → dùng `labor-law`

## LOẠI SHTT

| Loại | Bảo vệ cái gì | Thời hạn VN |
|------|---------------|:-----------:|
| Nhãn hiệu | Logo, tên, slogan | 10 năm (gia hạn) |
| Bản quyền | Văn bản, code, design | 50 năm |
| Patent | Sáng chế, giải pháp hữu ích | 20/10 năm |
| Trade secret | Công thức, quy trình, data | Vô hạn (nếu bảo mật) |
| Kiểu dáng CN | Hình dáng sản phẩm | 5 năm × 2 lần |

## CHECKLIST NHÃN HIỆU

- [ ] Tra cứu trùng: [NOIP](https://www.noip.gov.vn)
- [ ] Phân lớp Nice (lớp 9, 35, 41, 42 cho tech)
- [ ] Nộp đơn: Cục SHTT hoặc đại diện
- [ ] Thời gian xử lý: 12-18 tháng
- [ ] Chi phí: ~3-5 triệu/lớp (VN)
- [ ] Madrid Protocol cho đăng ký quốc tế

## NDA TEMPLATE

```yaml
nda:
  parties: ["Bên A (Discloser)", "Bên B (Receiver)"]
  scope: "Thông tin kinh doanh, kỹ thuật, khách hàng"
  duration: "2 năm sau khi kết thúc hợp tác"
  exclusions: ["Thông tin đã public", "Độc lập phát triển"]
  penalties: "Bồi thường thiệt hại + phạt vi phạm"
  jurisdiction: "Tòa án TP.HCM / Hà Nội"
```

## QUY TẮC

1. **Đăng ký TRƯỚC khi public** — không để lộ rồi mới đăng ký
2. NDA cho MỌI đối tác, freelancer, nhân viên mới
3. Monitor vi phạm SHTT hàng tháng
4. Lưu bằng chứng sáng tạo (git log, email, timestamp)
