---
description: Giao việc tạo tài liệu cho Jarvis — proposal, SOP, minutes, memo
---

// turbo-all

# 📄 Document Pipeline — Quick Start

## Bước 1: Load Jarvis
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow activation steps 1-4

## Bước 2: Auto-route tới Document Pipeline
- Set task_type = "docs"
- Load skill-routing: office-documents, brainstorming
- Load agent-routing: office-manager
- Load workflow: `{project-root}/_abm/bmm/workflows/0-orchestration/document-pipeline/workflow.yaml`

## Bước 3: Hỏi Requirements
Hỏi user:
1. Loại document? (Proposal / SOP / Meeting Minutes / Decision Matrix / Memo / Plan)
2. Nội dung chính?
3. Audience?

Sau đó chạy pipeline theo workflow.
