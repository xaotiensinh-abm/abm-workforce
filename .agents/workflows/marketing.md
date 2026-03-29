---
description: Giao việc marketing cho Jarvis — viết content, email, social, SEO
---

// turbo-all

# 📢 Marketing Pipeline — Quick Start

## Bước 1: Load Jarvis
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow activation steps 1-4

## Bước 2: Auto-route tới Marketing Pipeline
- Set task_type = "marketing"
- Load skill-routing: content-strategy, copywriting, marketing-psychology
- Load agent-routing: marketing-specialist
- Load workflow: `{project-root}/_abm/bmm/workflows/0-orchestration/marketing-pipeline/workflow.yaml`

## Bước 3: Hỏi Brief
Hỏi user:
1. Mục tiêu marketing? (brand awareness / lead gen / sales / engagement)
2. Kênh? (social / email / landing page / blog / SEO)
3. Đối tượng mục tiêu?
4. Deadline?

Sau đó chạy pipeline theo workflow.
