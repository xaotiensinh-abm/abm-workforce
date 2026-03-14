---
name: "compliance-checker"
description: "Kiểm tra tuân thủ quy định — GDPR, PDPA, Luật An ninh mạng VN, ISO 27001, nội quy công ty. Checklist tự động."
---

# 🛡️ Compliance Checker — Kiểm Tra Tuân Thủ

## Sử dụng khi

- Kiểm tra sản phẩm/dịch vụ có tuân thủ quy định
- Audit nội bộ định kỳ
- Chuẩn bị cho external audit
- Review privacy policy, data handling

## KHÔNG sử dụng khi

- Rà soát hợp đồng → dùng `contract-review`
- Kiểm tra code security → dùng `code-review`
- Đánh giá đa chiều → dùng `multi-dimensional-review`

## FRAMEWORKS HỖ TRỢ

| Framework | Phạm vi | Bắt buộc tại |
|-----------|---------|------------|
| Luật An ninh mạng VN | Dữ liệu cá nhân, lưu trữ VN | Việt Nam |
| PDPA | Bảo vệ dữ liệu cá nhân | ASEAN |
| GDPR | Bảo vệ dữ liệu EU | EU |
| ISO 27001 | An toàn thông tin | Toàn cầu |
| PCI-DSS | Thanh toán thẻ | Nếu xử lý thẻ |

## CHECKLIST TỰ ĐỘNG

### Dữ liệu cá nhân (Luật ATNM VN + PDPA)
- [ ] Có consent form trước khi thu thập?
- [ ] Mục đích thu thập rõ ràng?
- [ ] Dữ liệu lưu trữ tại VN?
- [ ] Có quy trình xóa dữ liệu khi user yêu cầu?
- [ ] Mã hóa dữ liệu nhạy cảm?
- [ ] Access control: ai được xem data nào?

### An toàn thông tin (ISO 27001)
- [ ] Password policy (min 8 chars, special chars)
- [ ] 2FA cho admin accounts
- [ ] Backup định kỳ + test restore
- [ ] Incident response plan
- [ ] Logs retention policy
- [ ] Vendor security assessment

## QUY TẮC

1. Audit compliance **ít nhất 1 lần/quý**
2. Non-compliance critical → CEO biết TRONG NGÀY
3. Lưu kết quả audit vào `_abm-output/legal/compliance/`

---

## Nguồn gốc
- Wave 2 v3.0: Phòng Pháp Chế coverage
