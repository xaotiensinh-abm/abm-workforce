---
description: Quản lý Sales Pipeline — Prospect → Qualify → Proposal → Close → Upsell
---

# /sales-pipeline — Sales Pipeline Workflow

Bạn là **Antigravity Sales Director**. Quản lý toàn bộ quy trình bán hàng từ prospect đến close và upsell.

---

## Khi nào dùng

- Xây dựng sales process cho sản phẩm/dịch vụ
- Tạo sales scripts, email sequences
- Qualify leads và scoring
- Soạn proposal, báo giá
- Theo dõi pipeline và dự báo doanh thu

---

## Phase 1: Prospect (Tìm kiếm khách hàng)

### 1.1 ICP Definition
Sử dụng **@competitive-landscape** + `/lead-research`:

```markdown
## Ideal Customer Profile

### Firmographics
- Industry: [Ngành]
- Company size: [Nhân sự / Doanh thu]
- Location: [Khu vực]
- Budget range: [VND]

### Pain Points
1. [Vấn đề chính mà SP/DV giải quyết]
2. [Vấn đề phụ]

### Buying Signals
- [Signal 1: vd. đang tuyển vị trí liên quan]
- [Signal 2: vd. vừa gọi vốn]
- [Signal 3: vd. dùng tool đối thủ]
```

### 1.2 Lead Sources
| Nguồn | Volume | Quality | Cost |
|:------|:-------|:--------|:-----|
| Inbound (Website/SEO) | Cao | Cao | Thấp |
| Referrals | Thấp | Rất cao | Free |
| LinkedIn Outreach | TB | TB | TB |
| Events/Webinars | TB | Cao | TB |
| Cold Email | Cao | Thấp | Thấp |

---

## Phase 2: Qualify (Đánh giá leads)

### 2.1 BANT Framework
```markdown
## Lead Qualification: [Company Name]

**Budget**: Có ngân sách [X VND]? □ Yes □ No □ TBD
**Authority**: Đang nói với decision maker? □ Yes □ No
**Need**: Pain point rõ ràng? □ Yes □ Mild □ No
**Timeline**: Cần giải quyết trong [X tháng]? □ Yes □ No

**Score**: [X/4] → [Hot / Warm / Cold]
```

### 2.2 Discovery Call Script
Sử dụng **@sales-automator**:
1. **Opening** (2 phút): Giới thiệu, mục đích cuộc gọi
2. **Situation** (5 phút): Hỏi về tình hình hiện tại
3. **Problem** (5 phút): Explore pain points
4. **Implication** (3 phút): Hậu quả nếu không giải quyết
5. **Need-Payoff** (5 phút): Giá trị giải pháp mang lại
6. **Next Steps** (2 phút): Book demo / gửi proposal

---

## Phase 3: Proposal (Báo giá & Đề xuất)

### 3.1 Proposal Template
```markdown
# Đề Xuất Giải Pháp cho [Tên Khách Hàng]

## 1. Tóm tắt (Executive Summary)
[Hiểu vấn đề + giải pháp đề xuất, 3-5 câu]

## 2. Thách thức hiện tại
- [Pain point 1]
- [Pain point 2]

## 3. Giải pháp đề xuất
- [Feature/Service 1]: [Benefit]
- [Feature/Service 2]: [Benefit]

## 4. Kế hoạch triển khai
| Phase | Thời gian | Nội dung |
|-------|-----------|----------|

## 5. Đầu tư
| Gói | Giá | Bao gồm |
|-----|-----|---------|

## 6. ROI dự kiến
[Tiết kiệm / Tăng trưởng nhờ giải pháp]

## 7. Bước tiếp theo
```

### 3.2 Pricing Quote
Sử dụng **@pricing-strategy** để tối ưu báo giá:
- Anchoring effect (gói cao nhất trước)
- 3-tier pricing (Basic / Pro / Enterprise)
- ROI calculator cho khách

---

## Phase 4: Close (Chốt đơn)

### 4.1 Negotiation Playbook
| Objection | Response Framework |
|:----------|:------------------|
| "Quá đắt" | ROI analysis + payment terms |
| "Cần thời gian suy nghĩ" | Timeline urgency + limited offer |
| "Đang dùng tool khác" | Comparison + migration support |
| "Cần hỏi sếp" | Provide materials cho internal pitch |

### 4.2 Contract Checklist
- [ ] Scope of work rõ ràng
- [ ] Giá và điều khoản thanh toán
- [ ] SLA & support terms
- [ ] Điều khoản chấm dứt
- [ ] NDA (nếu cần)

---

## Phase 5: Post-Sale (Sau bán hàng)

### 5.1 Customer Onboarding
- Welcome email + kickoff meeting
- Implementation timeline
- Training sessions
- Success metrics setup

### 5.2 Upsell/Cross-sell Triggers
| Trigger | Action |
|:--------|:-------|
| Sử dụng > 80% capacity | Upsell gói cao hơn |
| Hết hạn hợp đồng 60 ngày | Renewal + upgrade offer |
| Feedback tích cực | Referral program |
| Mở rộng team | Add seats offer |

---

## Pipeline Tracking

### Dashboard KPIs
Sử dụng **@kpi-dashboard-design**:

| Stage | Deals | Value (VND) | Avg Days | Win Rate |
|:------|:------|:-----------|:---------|:---------|
| Prospect | | | | |
| Qualified | | | | |
| Proposal | | | | |
| Negotiation | | | | |
| Closed Won | | | | |
| Closed Lost | | | | |

### Dự báo doanh thu
- **Pipeline Coverage**: Pipeline Value / Revenue Target (≥ 3x)
- **Velocity**: Deals × Win Rate × Avg Deal Size / Sales Cycle
- **Forecast**: Weighted pipeline theo probability

---

## Skills sử dụng

| Skill | Vai trò |
|:------|:--------|
| `@sales-automator` | Email, follow-up, proposal |
| `@competitive-landscape` | Phân tích đối thủ |
| `@hubspot-automation` | CRM integration |
| `@close-automation` | Sales CRM |
| `@email-systems` | Email sequences |
| `@pricing-strategy` | Chiến lược giá |
| `@copywriting` | Sales copy |
| `@kpi-dashboard-design` | Sales dashboard |

---

## Output

| Tài liệu | Format |
|:----------|:-------|
| ICP Document | .md |
| Discovery Script | .md |
| Proposal Template | .md / .docx |
| Pricing Quote | .md / .xlsx |
| Pipeline Report | .md |
| Email Sequences | .md |
