---
name: workflow-automation
description: Tự động hóa quy trình công việc — trigger→action mapping, SOP to automation, report scheduling, notification rules.
---

# Workflow Automation — Tự động hóa quy trình doanh nghiệp

## Khi nào sử dụng
- Có quy trình lặp lại > 3 lần/tuần
- Nhiều bước thủ công có thể tự động
- Cần notification/alert tự động
- Báo cáo định kỳ cần auto-generate
- Dữ liệu cần sync giữa các hệ thống

## Framework nhận diện cơ hội automation

### Automation Score
Chấm điểm mỗi process (1-5):
| Criteria | Weight | Score |
|----------|--------|-------|
| Frequency (bao nhiêu lần/tuần) | 30% | |
| Time per execution (phút) | 25% | |
| Error-prone (hay sai) | 20% | |
| Standardized (có SOP rõ) | 15% | |
| Integration ready (API sẵn) | 10% | |

**Score > 3.5 → Automate now | 2.5-3.5 → Plan | < 2.5 → Keep manual**

## Automation Patterns

### 1. Trigger → Action
```yaml
automation:
  name: "New client onboarding"
  trigger: "CRM deal status = 'Won'"
  actions:
    - create_project_folder
    - send_welcome_email_sequence
    - create_onboarding_checklist
    - notify_team_slack
    - schedule_kickoff_meeting
```

### 2. Scheduled Reports
```yaml
automation:
  name: "Weekly KPI report"
  trigger: "Every Monday 8:00 AM"
  actions:
    - pull_data_from_sources
    - generate_kpi_dashboard
    - create_report_document
    - send_to_leadership
```

### 3. Conditional Alerts
```yaml
automation:
  name: "Revenue drop alert"
  trigger: "Daily revenue < 80% of 7-day average"
  conditions:
    - not_weekend
    - not_holiday
  actions:
    - alert_sales_manager
    - generate_diagnostic_report
```

### 4. Multi-Step Approval
```yaml
automation:
  name: "Purchase approval"
  trigger: "New purchase request submitted"
  steps:
    - if amount < 5M: auto_approve
    - if amount 5M-50M: manager_approval
    - if amount > 50M: director_approval + cfo_approval
  on_approved:
    - create_purchase_order
    - notify_accounting
  on_rejected:
    - notify_requester_with_reason
```

## SOP → Automation Blueprint

```markdown
## Converting SOP to Automation

### Input: SOP Steps
1. [Manual step 1]
2. [Manual step 2]
3. [Decision point]
4. [Manual step 3]

### Output: Automation Map
| SOP Step | Can Automate? | Tool/API | Effort |
|----------|--------------|----------|--------|
| Step 1 | ✅ Full | Zapier/n8n | Low |
| Step 2 | ⚠️ Partial | Custom script | Medium |
| Step 3 | ❌ Human needed | Approval gate | — |
| Step 4 | ✅ Full | API call | Low |

### ROI Calculation
- Time saved per execution: [X] minutes
- Frequency: [Y] times per week
- Monthly time saved: X × Y × 4 = [Z] hours
- Monthly cost saved: Z × hourly_rate = [$$]
```

## Enterprise Automation Categories

| Category | Examples | Priority |
|----------|---------|----------|
| **Report generation** | KPI dashboard, financials, project status | High |
| **Notification** | Deadline reminders, escalation alerts | High |
| **Onboarding** | New employee, new client flows | High |
| **Data sync** | CRM → Accounting, HR → Payroll | Medium |
| **Approvals** | Purchase, leave, expense | Medium |
| **Content** | Social media scheduling, newsletter | Medium |
| **Meeting** | Agenda prep, minutes distribution | Low |

## Tool Recommendations

| Need | Tool | Best For |
|------|------|----------|
| No-code automation | Zapier, Make | Simple trigger→action |
| Complex workflows | n8n, Power Automate | Multi-step, conditions |
| Custom scripts | Node.js, Python | API integration |
| AI-powered | Jarvis system | Content generation, analysis |
| Scheduling | Cron jobs | Periodic tasks |
