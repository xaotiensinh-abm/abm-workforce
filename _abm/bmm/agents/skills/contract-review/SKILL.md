---
name: "contract-review"
description: "Rà soát hợp đồng pháp lý — phát hiện rủi ro, điều khoản bất lợi, compliance check. Red flags, negotiation points, output template chuẩn."
---

# ⚖️ Contract Review — Rà Soát Hợp Đồng

## Sử dụng khi

- Nhận hợp đồng mới cần review (mua/bán, dịch vụ, lao động, thuê)
- Kiểm tra compliance với quy định pháp luật Việt Nam
- So sánh điều khoản với template chuẩn
- Phát hiện rủi ro pháp lý trước khi ký
- Chuẩn bị negotiation points

## KHÔNG sử dụng khi

- Cần soạn hợp đồng mới → dùng `docx-official` + template pháp lý
- Phân tích tài chính trong HĐ → dùng `data-analysis`
- Review code → dùng `code-review`

## QUY TRÌNH RÀ SOÁT 5 BƯỚC

```
Bước 1: Đọc tổng quan      → Xác định loại HĐ, các bên, giá trị
Bước 2: Check thông tin     → Pháp nhân, ngày, phạm vi
Bước 3: Scan điều khoản     → Checklist rủi ro cao
Bước 4: So sánh benchmark   → So với template chuẩn ngành
Bước 5: Tạo báo cáo review  → Output format chuẩn
```

## CHECKLIST RÀ SOÁT CHI TIẾT

### 📋 1. Thông tin cơ bản
- [ ] Tên các bên chính xác (đúng pháp nhân, đúng MST)
- [ ] Người đại diện có thẩm quyền ký
- [ ] Ngày ký, ngày hiệu lực, thời hạn hợp đồng
- [ ] Phạm vi công việc / sản phẩm / dịch vụ rõ ràng
- [ ] Giá trị hợp đồng + phương thức thanh toán (đợt, %)
- [ ] Đồng tiền thanh toán (VND / USD / khác)

### ⚠️ 2. Điều khoản rủi ro CAO
| Điều khoản | Tiêu chuẩn | Câu hỏi kiểm tra |
|-----------|-----------|-----------------|
| Phạt vi phạm | < 8%/năm giá trị HĐ | Tỷ lệ có hợp lý không? Có giới hạn tối đa? |
| Bồi thường | Có giới hạn trách nhiệm | Liability cap = bao nhiêu lần giá trị HĐ? |
| Chấm dứt | 30 ngày thông báo | Các bên có quyền chấm dứt ngang nhau? |
| Bất khả kháng | Có clause | Danh sách events có đủ? Có COVID/pandemic? |
| Bảo mật (NDA) | Có clause + thời hạn | Scope bảo mật rõ ràng? Thời hạn hợp lý (2-5 năm)? |
| Sở hữu trí tuệ | IP ownership rõ ràng | Ai sở hữu output? Work-for-hire hay license? |
| Luật áp dụng | Luật Việt Nam | Nếu luật nước ngoài — CEO phải biết. |
| Tranh chấp | Trọng tài hoặc tòa án VN | VIAC hay tòa kinh tế? Chi phí ai chịu? |
| Tự động gia hạn | Phải thông báo trước | Bao nhiêu ngày trước? Có quyền chọn không gia hạn? |
| Chuyển nhượng | Cần sự đồng ý 2 bên | Bên nào có quyền chuyển nhượng? |

### 🚩 3. Red Flags — DỪNG ngay khi thấy

```
🔴 CRITICAL (phải sửa trước khi ký):
🚩 Không giới hạn trách nhiệm bồi thường (unlimited liability)
🚩 Phạt vi phạm > 10% giá trị HĐ
🚩 Chỉ 1 bên có quyền chấm dứt đơn phương
🚩 Luật áp dụng nước ngoài mà không có lý do business

🟡 WARNING (nên sửa):
⚠️ Tự động gia hạn mà không báo trước
⚠️ Chuyển nhượng quyền mà không cần đồng ý
⚠️ Thiếu điều khoản bảo mật
⚠️ Phạm vi công việc mơ hồ ("và các dịch vụ liên quan")
⚠️ Thanh toán 100% trước khi nghiệm thu

🔵 INFO (nên lưu ý):
ℹ️ HĐ chỉ tiếng Anh — yêu cầu bản song ngữ
ℹ️ Không có điều khoản bảo hành
ℹ️ Không quy định quy trình nghiệm thu
```

### 🔍 4. Negotiation Points — Gợi ý đàm phán

| Tình huống | Đề xuất đàm phán |
|------------|------------------|
| Thanh toán 100% trước | Đề xuất: 30% đặt cọc + 70% nghiệm thu |
| Phạt quá cao | Đề xuất: giảm xuống 5-8%/năm, có cap |
| Không có warranty | Đề xuất: bảo hành 12 tháng cho sản phẩm/dịch vụ |
| IP không rõ | Đề xuất: work-for-hire clause rõ ràng |
| Chấm dứt bất đối xứng | Đề xuất: 30 ngày notice cho cả 2 bên |

## OUTPUT FORMAT

```yaml
contract_review:
  contract_name: "[Tên hợp đồng]"
  contract_type: "mua_ban / dich_vu / lao_dong / thue / hop_tac"
  parties:
    - name: "Bên A — [Tên pháp nhân]"
      mst: "[Mã số thuế]"
    - name: "Bên B — [Tên pháp nhân]"
      mst: "[Mã số thuế]"
  value: "[Giá trị + đơn vị]"
  duration: "[Thời hạn]"
  risk_level: "low / medium / high / critical"

  checklist_results:
    basic_info: "pass / fail"
    high_risk_clauses: "pass / fail_with_details"
    red_flags_count: 0
    red_flags: []

  negotiation_points: []
  recommendations: []

  approval: "pending / approved / approved_with_conditions / rejected"
  reviewer: "Jarvis Legal Review"
  review_date: "[YYYY-MM-DD]"
```

## QUY TẮC SẮT

1. HĐ > 50 triệu → review ĐẦY ĐỦ checklist
2. HĐ có red flags 🔴 → **CEO PHẢI biết** trước khi ký
3. Lưu bản review vào `_abm-output/legal/`
4. KHÔNG BAO GIỜ khuyên "ký được" nếu chưa rà hết checklist
5. Mọi review phải có evidence — trích dẫn điều khoản cụ thể

## Related Skills
- compliance-checker, labor-law, ip-protection, docx-official
