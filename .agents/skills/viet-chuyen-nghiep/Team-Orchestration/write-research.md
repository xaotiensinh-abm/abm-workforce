# Pipeline: Viết Tài Liệu Nghiên Cứu (write-research) — v3.2

## Khi nào kích hoạt
- User yêu cầu viết tài liệu nghiên cứu, phân tích chuyên sâu
- Tín hiệu: "viết luận", "viết nghiên cứu", "báo cáo phân tích", "white paper",
  "literature review", "policy brief", "case analysis", "viết report chuyên sâu"

## Pipeline

```
content/ (deep research) → style/ (technical) → research-writer-worker → quality/ (fact-check) → platform/ (docs) → Output
   │                              │                        │                       │                     │
   │                              │                        │                       │                     └─ Format tài liệu
   │                              │                        │                       └─ Citation verify + fact-check
   │                              │                        └─ Templates + citation format
   │                              └─ Academic tone + structure
   └─ Research question + source collection + analysis
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — Deep Research Mode
1. `lead-content.md` nhận brief → xác định:
   - Research question / thesis
   - Scope (thời gian, địa lý, domain)
   - Document type (lit review / white paper / policy brief / case analysis / report)
   - Target audience (academic / executive / general)
2. `research.md` thu thập chuyên sâu:
   - Web search cho sources mới nhất
   - Source evaluation (5-tier: peer-reviewed > official > expert > media > user)
   - Thu thập data points, statistics, case studies
3. `analysis.md` phân tích:
   - Compare & contrast sources
   - Identify themes, patterns, gaps
   - Synthesis findings
4. Output: **Research Package YAML** (findings + sources + analysis) → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến `technical.md`
2. **research-writer-worker.md** bổ sung:
   - Document template theo type
   - Academic writing patterns
   - Citation formatting (APA/Harvard)
3. Rules:
   - CLAIM = EVIDENCE: mọi claim phải có citation
   - BALANCED: multiple perspectives
   - PRECISE: ngôn ngữ chính xác
   - STRUCTURED: heading hierarchy rõ ràng
4. Output: **Research Draft** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra nâng cao:
   - **fact-check** (verify mọi claim có source)
   - **citation-check** (format đúng, source tồn tại)
   - consistency (thuật ngữ, referencing style)
   - natural (academic nhưng không khô cứng)
   - anti-ai (burstiness + human fingerprint — academic flavor)
2. Bonus check: **Source diversity** (không over-rely 1 source)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. Format:
   - PDF/DOCX: cover + abstract + ToC + sections + references + appendix
   - Notion: linked references, embedded tables
   - Web: structured HTML, citation hover

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/content/research.md` — research methodology
- `Ban/content/analysis.md` — analysis framework
- `Ban/style/technical.md` — technical editing rules
- `Ban/quality/fact-check.md` — verification protocols
- `Ban/platform/docs.md` — document formatting
- `Workers/research-writer-worker.md` — templates, citation, academic patterns ★
