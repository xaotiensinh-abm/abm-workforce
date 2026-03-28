---
description: Điều phối nghiệp vụ quản trị doanh nghiệp với hệ thống Multi-Agent (HR, Finance, Sales, Project)
---

# Business Operation Orchestrator

Hệ thống điều phối nghiệp vụ doanh nghiệp theo mô hình Multi-Agent, tự động hóa các quy trình quản trị với context Việt Nam.

---

## Khởi động

Khi user gọi `/business-orchestrator`, hỏi:
- **Yêu cầu cụ thể**: Mô tả nghiệp vụ cần giải quyết
- **Scope**: Single agent hay full orchestration
- **Quy mô**: Startup / SME / Enterprise

---

## Kiến Trúc 6 Sub-Agents

| Agent | Vai Trò | Output |
|-------|---------|--------|
| @HR_Manager | Nhân sự, tuyển dụng, đánh giá | JD, Interview Scripts, KPI |
| @Finance_Analyst | Tài chính, kế toán | Financial Report, Forecast |
| @Sales_CRM | Pipeline, leads, conversion | Dashboard, Lead Scores |
| @Project_Tracker | Tasks, timeline, resources | Gantt, Status Report |
| @Quality_Auditor | Kiểm tra, compliance | Audit (PASS/FAIL) |
| @Report_Generator | Tổng hợp cho lãnh đạo | Executive Summary |

---

## Workflow 4 Phases

### Phase 1: Foundation (Parallel)
- @HR_Manager + @Finance_Analyst chạy đồng thời
- Thu thập dữ liệu nhân sự và tài chính

### Phase 2: Operations (Parallel)
- @Sales_CRM + @Project_Tracker chạy đồng thời
- Pipeline tracking và project planning

### Phase 3: Quality Gate
- @Quality_Auditor kiểm tra output từ Phase 1-2
- IF FAIL → Quay lại Phase tương ứng với feedback
- IF PASS → Tiếp tục Phase 4

### Phase 4: Reporting
- @Report_Generator tổng hợp từ tất cả agents
- Format: Executive Summary cho CEO/Board
- Include KPIs, recommendations, next steps

---

## Agent Routing

```
IF scope == "HR related"       → @HR_Manager
IF scope == "Finance related"  → @Finance_Analyst
IF scope == "Sales related"    → @Sales_CRM
IF scope == "Project related"  → @Project_Tracker
IF scope == "Full operation"   → Run all 4 phases
```

---

## Vietnamese Context

### Pháp Lý & Compliance
- Luật Lao động Việt Nam 2019
- BHXH, BHYT, BHTN regulations
- Chuẩn kế toán Việt Nam (VAS)

### Văn Hóa Kinh Doanh
- Relationship-based decisions
- Hierarchical reporting structure
- Holiday calendar (Tết, 30/4, 2/9...)

---

## Full Skill Reference

Xem chi tiết agents và templates tại:
- [SKILL.md](file:///D:/Antigravity/.agent/skills/claude-skills/business-operation-orchestrator/SKILL.md)
