---
description: Giao việc HR cho Jarvis — viết JD, onboarding, review, training
---

// turbo-all

# 👥 HR Pipeline — Quick Start

## Bước 1: Load Jarvis
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow activation steps 1-4

## Bước 2: Auto-route tới HR Pipeline
- Set task_type = "hr"
- Load skill-routing: hr-operations, internal-comms
- Load agent-routing: hr-specialist
- Load workflow: `{project-root}/_abm/bmm/workflows/0-orchestration/hr-pipeline/workflow.yaml`

## Bước 3: Hỏi Requirements
Hỏi user:
1. Loại HR task? (JD / Onboarding / Review / Training / Exit / Comms)
2. Vị trí/phòng ban liên quan?
3. Yêu cầu đặc biệt?

Sau đó chạy pipeline theo workflow.
