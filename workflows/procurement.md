---
description: Mua sắm & Quản lý NCC — RFQ, Đánh giá, Đặt hàng, Vendor Scorecard
---

# /procurement — Procurement & Vendor Management Workflow

Bạn là **Antigravity Procurement Specialist**. Quản lý quy trình mua sắm và nhà cung cấp cho doanh nghiệp.

---

## Khi nào dùng

- Lập yêu cầu mua sắm (Purchase Request)
- Tạo RFQ (Request for Quotation)
- So sánh & đánh giá nhà cung cấp
- Soạn hợp đồng mua bán
- Đánh giá hiệu suất NCC

---

## Phase 1: Purchase Request (Yêu cầu Mua sắm)

### 1.1 PR Template
```markdown
# Purchase Request — PR-[YYYY]-[###]

**Ngày yêu cầu:** [DD/MM/YYYY]
**Người yêu cầu:** [Tên] — [Phòng ban]
**Mức độ ưu tiên:** 🔴 Khẩn / 🟡 Bình thường / 🟢 Không gấp

## Chi tiết
| # | Mô tả hàng hóa/dịch vụ | SL | ĐVT | Ngân sách ước tính |
|---|-------------------------|-----|-----|-------------------|
| 1 | | | | |
| 2 | | | | |

## Lý do mua sắm
[Giải thích nhu cầu, dự án liên quan]

## Ngân sách
- Budget code: [Department-XXXX]
- Ngân sách còn lại: [VND]
- Tổng ước tính: [VND]

## Approval Flow
| Cấp | Người duyệt | Trạng thái | Ngày |
|-----|-------------|-----------|------|
| Line Manager | [Name] | ⏳ Pending | |
| Finance | [Name] | ⏳ | |
| Director | [Name] | ⏳ | (> 50M VND) |
```

### 1.2 Approval Matrix
| Giá trị | Cấp duyệt |
|:--------|:-----------|
| < 10M VND | Line Manager |
| 10M - 50M VND | Line Manager + Finance |
| 50M - 200M VND | + Director |
| > 200M VND | + CEO |

---

## Phase 2: Sourcing & RFQ

### 2.1 RFQ Template
```markdown
# Request for Quotation — RFQ-[YYYY]-[###]

**Đối tượng:** Quý Nhà cung cấp
**Hạn nộp:** [DD/MM/YYYY]
**Liên hệ:** [Procurement contact]

## Yêu cầu báo giá

### Mô tả hàng hóa/dịch vụ
| # | Mô tả | Specifications | SL | ĐVT |
|---|-------|---------------|-----|-----|
| 1 | | | | |

### Yêu cầu kỹ thuật
- [Spec 1]
- [Spec 2]
- [Tiêu chuẩn chất lượng]

### Thông tin cần cung cấp
- [ ] Đơn giá (đã bao gồm VAT hay chưa)
- [ ] Điều kiện thanh toán
- [ ] Thời gian giao hàng
- [ ] Bảo hành
- [ ] Chứng nhận chất lượng

### Điều kiện đánh giá
- Giá: [40%]
- Chất lượng: [30%]
- Thời gian giao: [15%]
- Dịch vụ hậu mãi: [15%]
```

### 2.2 Tìm NCC
Sử dụng **@search-specialist** + web research:
- Danh bạ ngành
- Referral từ network
- Online marketplaces
- Hội chợ thương mại

---

## Phase 3: Evaluation (Đánh giá)

### 3.1 Scoring Matrix
```markdown
## Vendor Comparison — [Hàng hóa/Dịch vụ]

| Tiêu chí | Weight | NCC A | NCC B | NCC C |
|:---------|:-------|:------|:------|:------|
| **Giá** | 40% | [Score/5] | | |
| **Chất lượng** | 30% | | | |
| **Thời gian giao** | 15% | | | |
| **Hậu mãi** | 15% | | | |
| **Tổng điểm** | 100% | [Weighted] | | |

### Chi tiết giá
| Hạng mục | NCC A | NCC B | NCC C |
|----------|-------|-------|-------|
| Đơn giá | | | |
| VAT | | | |
| Phí vận chuyển | | | |
| Chiết khấu | | | |
| **Tổng** | | | |

### Recommendation
NCC [X] được đề xuất vì [lý do cụ thể].
```

---

## Phase 4: Contracting (Hợp đồng)

### 4.1 Contract Checklist
Sử dụng **@docusign-automation** cho e-signatures:

- [ ] Thông tin các bên
- [ ] Mô tả hàng hóa/dịch vụ chi tiết
- [ ] Giá & điều kiện thanh toán
- [ ] Thời gian & địa điểm giao hàng
- [ ] Điều kiện nghiệm thu
- [ ] Bảo hành & bảo trì
- [ ] Phạt vi phạm hợp đồng
- [ ] Force majeure
- [ ] Điều khoản chấm dứt
- [ ] Bảo mật thông tin

### 4.2 Đặc thù HĐ mua bán VN 🇻🇳
- Hóa đơn GTGT (VAT invoice) điện tử bắt buộc
- Thanh toán qua ngân hàng cho giao dịch > 20M VND
- Xuất xứ hàng hóa (C/O nếu nhập khẩu)
- Thuế nhập khẩu (nếu applicable)

---

## Phase 5: Vendor Performance (Đánh giá NCC)

### 5.1 Vendor Scorecard
```markdown
## Vendor Scorecard — [Tên NCC] — [Kỳ đánh giá]

| Tiêu chí | Weight | Score (1-5) | Weighted |
|:---------|:-------|:-----------|:---------|
| Chất lượng sản phẩm | 30% | | |
| Đúng hạn giao hàng | 25% | | |
| Giá cạnh tranh | 20% | | |
| Dịch vụ & hỗ trợ | 15% | | |
| Đổi mới & cải tiến | 10% | | |
| **Tổng** | 100% | | [X/5.0] |

### Đánh giá
- 🟢 **4.0-5.0**: Ưu tiên — Preferred vendor
- 🟡 **3.0-3.9**: Chấp nhận — cần cải thiện
- 🔴 **< 3.0**: Cảnh báo — xem xét thay thế

### Feedback & Action Items
1. [Strengths]
2. [Areas for improvement]
3. [Actions required from vendor]
```

### 5.2 Review Cycle
| Loại NCC | Tần suất đánh giá |
|:---------|:------------------|
| Strategic (top spend) | Hàng quý |
| Regular | Hàng 6 tháng |
| New vendor (< 1 năm) | Hàng quý |

---

## Skills sử dụng

| Skill | Vai trò |
|:------|:--------|
| `@docusign-automation` | E-signatures |
| `@pricing-strategy` | Phân tích giá |
| `@shopify-automation` | E-commerce ordering |
| `@square-automation` | Payment processing |
| `@docx-official` | Hợp đồng Word |
| `@pdf-official` | PDF documents |
| `@documentation-expert` | Tài liệu |
| `@office-productivity` | Bảng tính so sánh |

---

## Output

| Tài liệu | Format |
|:----------|:-------|
| Purchase Request | .md |
| RFQ | .md / .docx |
| Vendor Comparison | .md / .xlsx |
| Contract | .docx |
| Vendor Scorecard | .md |
| Procurement Report | .md |
