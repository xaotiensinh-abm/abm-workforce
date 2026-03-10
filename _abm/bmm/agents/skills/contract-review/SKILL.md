---
name: "contract-review"
description: "Rà soát hợp đồng pháp lý — phát hiện rủi ro, điều khoản bất lợi, compliance check. Dành cho phòng Pháp Chế."
---

# ⚖️ Contract Review — Rà Soát Hợp Đồng

## Sử dụng khi

- Receive hợp đồng mới cần review
- Kiểm tra compliance với quy định
- So sánh điều khoản với template chuẩn
- Phát hiện rủi ro pháp lý

## KHÔNG sử dụng khi

- Cần soạn hợp đồng mới → dùng `docx` + template pháp lý
- Phân tích tài chính trong HĐ → dùng `data-analysis`
- Review code → dùng `code-review`

## CHECKLIST RÀ SOÁT

### Thông tin cơ bản
- [ ] Tên các bên chính xác (đúng pháp nhân)
- [ ] Ngày ký, ngày hiệu lực, thời hạn
- [ ] Phạm vi công việc / sản phẩm
- [ ] Giá trị hợp đồng + phương thức thanh toán

### Điều khoản rủi ro cao
- [ ] **Phạt vi phạm**: tỷ lệ hợp lý? (< 8%/năm)
- [ ] **Bồi thường**: giới hạn trách nhiệm có không?
- [ ] **Chấm dứt**: điều kiện đơn phương chấm dứt
- [ ] **Bất khả kháng**: force majeure clause
- [ ] **Bảo mật**: NDA / confidentiality scope
- [ ] **Quyền sở hữu trí tuệ**: IP ownership rõ ràng
- [ ] **Luật áp dụng**: luật VN hay nước ngoài?
- [ ] **Giải quyết tranh chấp**: tòa án hay trọng tài?

### Red Flags 🚩

```
🚩 Không giới hạn trách nhiệm bồi thường
🚩 Tự động gia hạn mà không thông báo
🚩 Phạt vi phạm > 10% giá trị HĐ
🚩 Chuyển nhượng quyền mà không cần đồng ý
🚩 Luật áp dụng nước ngoài mà không có lý do
🚩 Thiếu điều khoản bảo mật
```

## OUTPUT FORMAT

```yaml
contract_review:
  contract_name: ""
  parties: ["Bên A", "Bên B"]
  value: ""
  risk_level: "low/medium/high/critical"
  red_flags: []
  recommendations: []
  approval: "pending/approved/rejected"
  reviewer: "Jarvis Legal Review"
```

## QUY TẮC

1. HĐ > 50 triệu → review ĐẦY ĐỦ checklist
2. HĐ có red flags → CEO PHẢI biết trước khi ký
3. Lưu bản review vào `_abm-output/legal/`

---

## Nguồn gốc
- Wave 2 v3.0: Phòng Pháp Chế coverage
