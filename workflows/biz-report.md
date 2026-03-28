---
description: Báo cáo quản trị — KPIs, Dashboard, Reports tuần/tháng/quý
---

# /biz-report — Business Reporting Workflow

Bạn là **Antigravity Business Analyst**. Tạo báo cáo kinh doanh chuyên nghiệp với data-driven insights.

---

## Khi nào dùng

- Tạo báo cáo KPI tuần/tháng/quý
- Thiết kế dashboard metrics
- Phân tích xu hướng và so sánh kỳ trước
- Executive summary cho leadership
- Board report cho investors

---

## Phase 1: KPI Definition

### 1.1 Chọn KPIs theo ngành
Sử dụng **@kpi-dashboard-design** + **@startup-metrics-framework**:

#### SaaS
| KPI | Formula | Target |
|:----|:--------|:-------|
| MRR | Recurring revenue/tháng | Growth >10%/tháng |
| Churn Rate | Lost customers / Total | < 5%/tháng |
| LTV/CAC | Lifetime Value / Acquisition Cost | > 3x |
| NRR | (MRR + Expansion - Churn) / Beginning MRR | > 110% |

#### E-commerce
| KPI | Formula | Target |
|:----|:--------|:-------|
| GMV | Gross Merchandise Value | Growth YoY |
| AOV | Revenue / Orders | Tăng dần |
| Conversion Rate | Orders / Visitors | > 2% |
| Repeat Purchase Rate | Returning / Total customers | > 30% |

#### Service Business
| KPI | Formula | Target |
|:----|:--------|:-------|
| Revenue per Employee | Revenue / Headcount | Tăng dần |
| Utilization Rate | Billable hours / Total hours | > 75% |
| Client Retention | Retained clients / Total | > 85% |
| Project Margin | (Revenue - Cost) / Revenue | > 30% |

---

## Phase 2: Report Templates

### 2.1 Weekly Flash Report (CEO Dashboard)
```markdown
# Weekly Flash — Tuần [X], [Tháng/Năm]

## 📊 Tổng quan
| Metric | Tuần này | Tuần trước | Δ | YTD |
|--------|----------|-----------|---|-----|
| Revenue | | | | |
| New Customers | | | | |
| Active Users | | | | |
| NPS | | | | |

## 🟢 Wins
- [Thành tựu 1]
- [Thành tựu 2]

## 🔴 Concerns
- [Vấn đề 1] → [Action đang thực hiện]

## 📌 Focus tuần tới
1. [Priority 1]
2. [Priority 2]
```

### 2.2 Monthly Business Report
```markdown
# Monthly Business Report — [Tháng/Năm]

## Executive Summary
[2-3 câu tóm tắt tháng: highlights, challenges, outlook]

## Financial Performance
| Metric | Actual | Budget | Δ% | YoY |
|--------|--------|--------|-----|-----|
| Revenue | | | | |
| Gross Profit | | | | |
| EBITDA | | | | |
| Cash Balance | | | | |

## Sales & Marketing
| Metric | Actual | Target | Status |
|--------|--------|--------|--------|
| New Leads | | | 🟢/🔴 |
| Conversion Rate | | | |
| Pipeline Value | | | |
| CAC | | | |

## Product & Operations
- Feature releases: [...]
- Uptime: [X%]
- Bug resolution: [X/Y resolved]

## Team & HR
- Headcount: [X] (Hired: [Y], Left: [Z])
- Employee satisfaction: [Score]

## Risks & Challenges
| Risk | Impact | Status | Mitigation |
|------|--------|--------|-----------|

## Outlook & Next Month Plan
1. [Key initiative 1]
2. [Key initiative 2]
```

### 2.3 Quarterly Board Report
```markdown
# Q[X] 20XX — Board Report

## 1. Financial Overview
[Charts: Revenue trend, P&L summary, Cash position]

## 2. Strategic Progress
| OKR | Target | Actual | Status |
|-----|--------|--------|--------|

## 3. Market & Competition
[Key market changes, competitive moves]

## 4. Team & Organization
[Org changes, culture initiatives]

## 5. Fundraising & Runway
[If applicable]

## 6. Decisions Required
1. [Decision cần Board approve]
```

---

## Phase 3: Analytics Integration

Kết nối analytics tools:

| Tool | Skill | Data |
|:-----|:------|:-----|
| Mixpanel | `@mixpanel-automation` | Product analytics |
| PostHog | `@posthog-automation` | User behavior |
| HubSpot | `@hubspot-automation` | Sales metrics |
| Notion | `@notion-automation` | OKRs, docs |

---

## Phase 4: Insight & Recommendations

### Phân tích xu hướng
- **MoM** (Month over Month): So sánh tháng này vs tháng trước
- **QoQ** (Quarter over Quarter): So quý
- **YoY** (Year over Year): So năm
- **Trailing 12 months**: Moving average 12 tháng

### Action Items format
```markdown
## Recommendations

### 🟢 Tiếp tục (Keep Doing)
- [Điều đang hiệu quả]

### 🟡 Cải thiện (Improve)
- [Metric dưới target] → [Specific action] — Owner: [Name] — Due: [Date]

### 🔴 Dừng lại (Stop)
- [Hoạt động không hiệu quả] → [Lý do]

### 🆕 Bắt đầu (Start)
- [Initiative mới] → [Expected impact]
```

---

## Skills sử dụng

| Skill | Vai trò |
|:------|:--------|
| `@kpi-dashboard-design` | Dashboard design |
| `@startup-metrics-framework` | Metrics selection |
| `@mixpanel-automation` | Product analytics |
| `@posthog-automation` | User analytics |
| `@content-research-writer` | Report writing |
| `@pptx-official` | Slide presentations |
| `@office-productivity` | Spreadsheets |

---

## Output

| Tài liệu | Format |
|:----------|:-------|
| Weekly Flash | .md |
| Monthly Report | .md / .pptx |
| Quarterly Board Report | .md / .pptx |
| KPI Dashboard | .md |
| Trend Analysis | .md |
