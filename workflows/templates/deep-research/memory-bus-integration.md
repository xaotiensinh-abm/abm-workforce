# Memory Bus Integration

Tài liệu về shared memory context giữa các workers trong Deep-Research-Team.

---

## Concept

Memory Bus là cơ chế chia sẻ context giữa các workers:
- Workers có thể đọc/ghi vào shared context
- Director quản lý state transitions
- Ensures consistency across phases

---

## Shared Context Structure

```json
{
  "session": {
    "id": "uuid-v4",
    "created_at": "ISO-8601",
    "status": "running|completed|failed"
  },
  "query": {
    "original": "User's original query",
    "clarified": "Refined query from Phase 1",
    "scope": ["topic1", "topic2"],
    "constraints": {
      "time_range": "2024-2025",
      "languages": ["en", "vi"],
      "sources": ["web", "papers"]
    }
  },
  "research": {
    "plan": {
      "topics": [],
      "assignments": {}
    },
    "findings": {
      "search": [],
      "technical": []
    },
    "verified": {
      "facts": [],
      "warnings": [],
      "rejected": []
    }
  },
  "citations": [
    {
      "id": 1,
      "title": "Source title",
      "url": "https://...",
      "accessed": "date",
      "used_in": ["section1", "section2"]
    }
  ],
  "meta": {
    "total_sources": 0,
    "verified_facts": 0,
    "execution_time_ms": 0
  }
}
```

---

## Worker Access Patterns

| Worker | Read | Write |
|--------|------|-------|
| Director | All | session, meta |
| QueryClarifier | query.original | query.clarified, query.scope |
| Planning | query.* | research.plan |
| SearchSpecialist | research.plan | research.findings.search, citations |
| TechnicalResearcher | research.plan | research.findings.technical, citations |
| FactChecker | research.findings.* | research.verified |
| ReportGenerator | All | meta.execution_time |

---

## Concurrency Control

- **Phase 3 parallel**: Both workers can write to `citations[]` concurrently
- **Append-only**: Workers append to arrays, don't overwrite
- **Director merge**: Director merges results after Phase 3 completes

---

## Memory Persistence

- Session context lưu trong `Output/memory-state.json`
- Cho phép resume interrupted sessions
- Cleanup after 7 days
