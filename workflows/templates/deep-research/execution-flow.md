# Execution Flow

Mô tả chi tiết luồng thực thi của Deep-Research-Team.

---

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER QUERY                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   🎯 DIRECTOR (OpenDeepResearch)                 │
│                   Khởi tạo session, orchestrate                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 1: QueryClarifier-Worker                      │
│              → clarified_query.md                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 2: Planning-Worker                            │
│              → research_plan.md                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │         PHASE 3 PARALLEL       │
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│  SearchSpecialist       │     │  TechnicalResearcher    │
│  → search_results.md    │     │  → technical_findings   │
└─────────────────────────┘     └─────────────────────────┘
              │                               │
              └───────────────┬───────────────┘
                              │ (wait_all)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 4: FactChecker-Worker                         │
│              → verified_facts.md                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              PHASE 5: ReportGenerator-Worker                     │
│              → final_report.md                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      📄 FINAL OUTPUT                             │
│                      Delivered to User                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase Dependencies

| Phase | Depends On | Outputs |
|-------|-----------|---------|
| 1 | User Query | clarified_query.md |
| 2 | Phase 1 | research_plan.md |
| 3a | Phase 2 | search_results.md |
| 3b | Phase 2 | technical_findings.md |
| 4 | Phase 3a + 3b | verified_facts.md |
| 5 | Phase 1 + 2 + 4 | final_report.md |

---

## Error Handling

- **Phase fails**: Director logs error, attempts retry (max 2)
- **Timeout**: Phase 3 parallel has 5-minute timeout
- **Partial results**: If one Phase 3 worker fails, continue with available data
