---
name: "abm-agent-evals"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: "Framework Trace Grading: Đánh giá chất lượng hiệu suất tự động của Agent sau khi hoàn thành task. Đo lường tốc độ, tỷ lệ lỗi, và lãng phí Token."
tags: [evaluation, observability, meta, architecture]
---

# 📊 Trace Grading Evaluator (Agent Evals)

## Mục tiêu
Skill này cung cấp phương pháp luận "Trace Grading" từ OpenAI/Anthropic giúp ABM System tự chấm điểm độ chính xác, logic thực thi và sự hao phí nội hàm (Token inefficiency) sau khi một nhiệm vụ lớn kết thúc.

## Trigger (Khi nào sử dụng)
- Tự chạy sau mỗi Sprint/Milestone.
- Khi người dùng (CEO) cảm thấy Agent tốn quá nhiều thời gian/mất phương hướng và gõ lệnh: `/review-trace`.

## Quy trình Trace Grading
1. **Thu thập dữ liệu (Traces)**
   Đọc File Log/Conversation History (`.gemini/antigravity/brain/[id]/.system_generated/logs/overview.txt`).
2. **Deterministic Check (Đánh giá Xác định)**
   - Agent có tạo ra đúng file (Artifacts) mà Contract yêu cầu không? (1/0)
   - Code/Config tạo ra có syntax error không (ví dụ chạy `python -m py_compile`)? (1/0)
3. **Trajectory Critique (Chấm điểm Hành trình)**
   - Số lượng Tool Calls sử dụng: `X` calls.
   - Thất bại liên tiếp: Nếu gọi cùng 1 Tool thất bại quá 2 lần -> `inefficiency = TRUE`.
   - Token Burn: Đánh giá xem Agent có đọc (`read_file` / `ls`) lại những thứ đã đọc rồi không?

## Output (Định dạng JSONL)
Ghi một line JSONL xuống file `.agents/traces/evals_log.jsonl` với cấu trúc chuẩn:

```json
{
  "task_id": "bc83178f-...",
  "status": "success|failed",
  "tool_calls_count": 15,
  "redundant_calls": 3,
  "deterministic_check": "passed",
  "score": 85,
  "critique": "Agent làm tốt phần code nhưng gọi nhầm lệnh bash gây tốn 2 tools call."
}
```

## Các lệnh hỗ trợ
Nếu cần tự động hóa, hãy sử dụng `/eval [conversation_id]` để kích hoạt skill này đánh giá chất lượng của chính các phiên làm việc trong quá khứ.
