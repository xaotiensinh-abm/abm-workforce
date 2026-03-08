---
description: Giao việc dev cho Jarvis — bug fix, feature, refactor
---

// turbo-all

# 💻 Dev Pipeline — Quick Start

## Bước 1: Load Jarvis
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow activation steps 1-4

## Bước 2: Triage
Jarvis sẽ tự phân loại task thành 1 trong:
- **Bug fix** → bug-fix-pipeline (Code → Test → Browser QA → Synthesis)
- **Feature** → feature-pipeline (Plan → Code∥ → Test → Browser QA → Docs)
- **Refactor** → refactor-pipeline (Impact → Code → Static → Risk Eval)
- **Data** → data-pipeline (MCP/Data → Code → Integration Verify)

## Bước 3: Mô tả task
Bạn chỉ cần mô tả task cần làm, Jarvis sẽ:
1. Classify → chọn pipeline
2. Tạo Task Contract
3. Delegate cho code-worker
4. Verify attestation
5. Trả kết quả
