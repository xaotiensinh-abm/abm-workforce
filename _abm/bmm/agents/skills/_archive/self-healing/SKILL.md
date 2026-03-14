---
name: "self-healing"
description: "Fallback chain khi skill fail — tự retry với strategy khác, escalate nếu vẫn fail. Giảm gián đoạn cho CEO."
---

# 🔄 Self-Healing — Retry Chain & Fallback

Khi skill hoặc workflow fail, Jarvis tự xử lý thay vì report fail ngay.

## Sử dụng khi

- Skill trả về lỗi hoặc output không hợp lệ
- Worker bị chặn (blocked) bởi dependency
- Tool call fail (network, timeout, permission)
- Output không đạt acceptance criteria

## KHÔNG sử dụng khi

- CEO yêu cầu dừng → PHẢI dừng
- Lỗi bảo mật → KHÔNG retry, report ngay
- Budget đã hết → KHÔNG retry

## RETRY CHAIN (3 cấp)

```
Cấp 1: RETRY — Thử lại cùng skill
  ├── Giảm scope (chia nhỏ task)
  ├── Thay đổi prompt/approach
  └── Max 2 retries

Cấp 2: FALLBACK — Chuyển sang skill khác
  ├── Xem KHÔNG sử dụng khi → tìm alternative
  ├── Load skill thay thế từ routing
  └── Max 1 fallback

Cấp 3: ESCALATE — Báo CEO
  ├── Tóm tắt: đã thử gì, fail vì sao
  ├── Đề xuất 2-3 phương án
  └── CEO quyết định
```

## FALLBACK MAP

| Skill gốc fail | Fallback 1 | Fallback 2 |
|----------------|-----------|-----------|
| `writing-plans` | `task-planning` | `brainstorming` |
| `sprint-planning` | `task-planning` | `project-hierarchy` |
| `data-analysis` | `xlsx` | `deep-research` |
| `code-review` | `systematic-debugging` | escalate |
| `copywriting` | `content-strategy` | `social-content` |
| `email-marketing` | `cold-email` | `agent-email-cli` |
| `docx` | `pdf` | `office-documents` |
| `knowledge-graph` | `knowledge-crystallizer` | `deep-research` |

## LOG FORMAT

```yaml
self_healing_log:
  - timestamp: "2026-03-10T22:00:00"
    original_skill: "writing-plans"
    error: "Output incomplete"
    retry_1: { skill: "writing-plans", result: "fail", reason: "timeout" }
    fallback: { skill: "task-planning", result: "success" }
    total_attempts: 3
    resolution: "fallback_success"
```

## QUY TẮC SẮT

1. **Max 3 attempts tổng** (2 retry + 1 fallback) trước khi escalate
2. **Log MỌI attempt** vào self-healing log
3. **Lỗi bảo mật** → KHÔNG retry, escalate ngay
4. **CEO nói dừng** → DỪNG, không retry

---

## Nguồn gốc
- Wave 1 v2.7: Self-healing fallback
- ABM Workforce Roadmap
