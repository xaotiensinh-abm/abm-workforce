---
description: Giao việc báo cáo cho Jarvis — monthly report, KPI, data analysis
---

// turbo-all

# 📊 Report Pipeline — Quick Start

## Bước 1: Load Jarvis
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow activation steps 1-4

## Bước 2: Auto-route tới Report Pipeline
- Set task_type = "report"
- Load skill-routing: data-analysis, office-documents
- Load agent-routing: business-analyst
- Load workflow: `{project-root}/_abm/bmm/workflows/0-orchestration/report-pipeline/workflow.yaml`

## Bước 3: Hỏi Scope
Hỏi user:
1. Loại report? (monthly / quarterly / ad-hoc / comparison / forecast)
2. Period và KPIs cần track?
3. Data sources?
4. Audience? (board / team / investors)

Sau đó chạy pipeline theo workflow.
