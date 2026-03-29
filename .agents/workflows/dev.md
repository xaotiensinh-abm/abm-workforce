---
description: Giao việc dev cho Jarvis — bug fix, feature, refactor
---

// turbo-all

# 💻 Dev Pipeline — Quick Start

## Bước 1: Load Jarvis
- Load file: `{project-root}/_abm/bmm/agents/jarvis-orchestrator.md`
- Follow activation steps 1-4

## Bước 2: Triage (Định Tuyến Cứng 39 Skills)
Jarvis sẽ tự phân loại task thành 1 trong các luồng và **CHỈ ĐƯỢC LOAD** các Skill đích danh sau (khóa cứng tính năng Auto-Load của IDE):
- **Bug fix** → Load `systematic-debugging` và `code-review`.
- **Feature** → Load `writing-plans` và `subagent-driven-development`.
- **Refactor** → Load `git-workflow-optimization` và `writing-plans`.
- **Data** → Giao khoán cho `typescript-expert`.

## Bước 3: Mô tả task
Bạn chỉ cần mô tả task cần làm, Jarvis sẽ:
1. Classify → chọn pipeline
2. Tạo Task Contract
3. Delegate cho code-worker
4. Verify attestation
5. Trả kết quả
