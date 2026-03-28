---
description: Deep Research Team - Multi-Agent System cho nghiên cứu chuyên sâu với 6 workers và 5 phases
---

# Deep Research Team Workflow

Hệ thống Multi-Agent orchestration cho nghiên cứu chuyên sâu. Tự động hóa quy trình từ phân tích query → lập kế hoạch → tìm kiếm → verify → báo cáo.

---

## Khi nào dùng

- Nghiên cứu chuyên sâu về một topic phức tạp
- So sánh nhiều công nghệ/giải pháp
- Tổng hợp thông tin từ nhiều nguồn
- Cần báo cáo có citations và fact-checking

---

## Team Structure

```
Deep-Research-Team/
├── OpenDeepResearch-Worker/    (Director)
├── QueryClarifier-Worker/      (Phase 1)
├── Planning-Worker/            (Phase 2)
├── SearchSpecialist-Worker/    (Phase 3 - Parallel)
├── TechnicalResearcher-Worker/ (Phase 3 - Parallel)
├── FactChecker-Worker/         (Phase 4)
└── ReportGenerator-Worker/     (Phase 5)
```

---

## Phase 1: Query Clarification

**Worker**: `QueryClarifier-Worker`

1. Phân tích query gốc của user
2. Xác định:
   - **Scope**: Phạm vi nghiên cứu
   - **Constraints**: Giới hạn (thời gian, nguồn, ngôn ngữ)
   - **Success criteria**: Kết quả mong đợi
3. Output: `clarified_query.md`

**Template Output:**
```markdown
# Clarified Query

## Original Query
[Query gốc của user]

## Refined Query
[Query đã refine, cụ thể hơn]

## Scope
- Include: [...]
- Exclude: [...]

## Constraints
- Time range: [...]
- Sources: [...]
- Language: [...]

## Success Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

---

## Phase 2: Research Planning

**Worker**: `Planning-Worker`

1. Dựa trên clarified query, tạo research strategy
2. Identify các topics/subtopics cần nghiên cứu
3. Phân chia tasks cho Phase 3 workers
4. Output: `research_plan.md`

**Template Output:**
```markdown
# Research Plan

## Strategy
[Mô tả approach tổng quan]

## Topics to Research

### Topic 1: [Name]
- Assigned to: SearchSpecialist-Worker
- Keywords: [...]
- Expected sources: [...]

### Topic 2: [Name]
- Assigned to: TechnicalResearcher-Worker
- Focus: [...]

## Timeline
- Phase 3 parallel execution: [estimate]
- Phase 4 verification: [estimate]
- Phase 5 report: [estimate]
```

---

## Phase 3: Parallel Research

**Workers**: `SearchSpecialist-Worker` + `TechnicalResearcher-Worker` (chạy đồng thời)

### SearchSpecialist-Worker
- Web search với keywords từ plan
- Tìm articles, papers, documentation
- Output: `search_results.md`

### TechnicalResearcher-Worker
- Deep dive vào technical aspects
- Code examples, benchmarks, comparisons
- Output: `technical_findings.md`

**Template Output (search_results.md):**
```markdown
# Search Results

## Source 1: [Title]
- URL: [...]
- Key findings: [...]
- Relevance: High/Medium/Low

## Source 2: [Title]
...

## Summary
[Tổng hợp key findings]
```

---

## Phase 4: Fact Checking

**Worker**: `FactChecker-Worker`

1. Cross-verify findings từ Phase 3
2. Check citations và sources
3. Flag inconsistencies
4. Output: `verified_facts.md`

**Template Output:**
```markdown
# Verified Facts

## Confirmed Facts
1. ✅ [Fact 1] - Source: [...]
2. ✅ [Fact 2] - Source: [...]

## Needs Clarification
1. ⚠️ [Claim] - Reason: [...]

## Rejected Claims
1. ❌ [Claim] - Reason: [...]

## Fact Matrix
| Claim | Source 1 | Source 2 | Status |
|-------|----------|----------|--------|
| [...] | ✅ | ✅ | Verified |
```

---

## Phase 5: Report Generation

**Worker**: `ReportGenerator-Worker`

1. Synthesize tất cả findings
2. Create structured report với citations
3. Include executive summary
4. Output: `final_report.md`

**Template Output:**
```markdown
# Research Report: [Topic]

## Executive Summary
[2-3 paragraphs tóm tắt key findings]

## Table of Contents
1. Introduction
2. Methodology
3. Findings
4. Analysis
5. Conclusion
6. References

## 1. Introduction
[Background và context]

## 2. Methodology
[Mô tả research approach]

## 3. Findings
### 3.1 [Topic 1]
[Details với citations [1], [2]]

### 3.2 [Topic 2]
[Details]

## 4. Analysis
[So sánh, đánh giá, insights]

## 5. Conclusion
[Key takeaways và recommendations]

## References
[1] Author. Title. URL. Date.
[2] ...
```

---

## Output Artifacts

Mỗi research session tạo folder với structure:

```
Output/
├── orchestration-manifest.md   # Manifest điều phối
├── swarm-router-config.json    # Config parallel execution
├── execution-flow.md           # Log luồng thực thi
├── memory-bus-integration.md   # Shared context
├── clarified_query.md          # Phase 1 output
├── research_plan.md            # Phase 2 output
├── search_results.md           # Phase 3a output
├── technical_findings.md       # Phase 3b output
├── verified_facts.md           # Phase 4 output
└── final_report.md             # Phase 5 output (FINAL)
```

---

## Memory Bus Integration

Shared context giữa các workers:

```json
{
  "session_id": "uuid",
  "query": "original query",
  "clarified_query": "refined query",
  "current_phase": 1-5,
  "findings": [],
  "citations": [],
  "flags": []
}
```

---

## Quickstart

```
/deep-research [your research query]
```

**Ví dụ:**
```
/deep-research So sánh các AI Agent frameworks 2025: LangGraph vs CrewAI vs AutoGen
```

---

## Customization

### Skip phases
```
/deep-research --skip-phase=1 [query đã rõ ràng]
```

### Single worker mode
```
/deep-research --single-worker [query đơn giản]
```

### Specify output format
```
/deep-research --format=academic [query]
/deep-research --format=executive-brief [query]
```

---

## Pro Tips

1. **Be specific**: Query càng cụ thể, kết quả càng tốt
2. **Set constraints**: Thêm giới hạn thời gian, ngôn ngữ nếu cần
3. **Review Phase 2**: Check research plan trước khi parallel execution
4. **Iterate**: Có thể re-run specific phases nếu cần thêm info
