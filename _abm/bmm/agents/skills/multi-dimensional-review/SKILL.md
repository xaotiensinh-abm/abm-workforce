---
name: multi-dimensional-review
description: "Standardized multi-perspective evaluation framework. Generates 10-dimension scores, 5+ adversarial perspectives, evidence-based findings, and prioritized action plan. Use for system audits, project reviews, and quality gates."
tags: [meta, review, quality, process]
---

## KHONG su dung khi

- Review nhanh 1 chieu -> khong can 8 personas. Can fix bug -> dung systematic-debugging.


# 🔍 Multi-Dimensional Review — Quy trình đánh giá chuẩn

## Overview

Quy trình đánh giá đa chiều, đa luồng, chuyên sâu. Biến review từ "ý kiến cá nhân"
thành "phân tích có hệ thống" với evidence, scoring, và adversarial thinking.

**Dùng khi:** System audit, project review, quality gate, design review, strategy evaluation.

## Quy trình 6 bước

### Bước 1: THU THẬP (Gather Evidence)
```
□ Liệt kê TẤT CẢ files/components cần đánh giá
□ Đọc TỪNG file — ghi chú evidence thật (line numbers, sizes, counts)
□ Inventory: đếm files, lines, tokens, dependencies
□ KHÔNG đánh giá gì ở bước này — chỉ thu thập data
```

### Bước 2: CHẤM ĐIỂM (Score Dimensions)

Chấm 10 chiều chuẩn. Mỗi chiều PHẢI có evidence cụ thể:

| # | Chiều | Câu hỏi đánh giá | Weight |
|---|-------|-------------------|--------|
| 1 | **Kiến trúc** | Separation of concerns? Layers rõ ràng? | 15% |
| 2 | **Thiết kế** | Consistent patterns? DRY? | 10% |
| 3 | **Contracts/API** | Rõ ràng? Đầy đủ fields? | 10% |
| 4 | **Coverage** | Bao phủ tất cả use cases? | 10% |
| 5 | **Enforcement** | Rules được enforce bởi code hay trust? | 15% |
| 6 | **Governance** | Security, permissions, human gates? | 10% |
| 7 | **Observability** | Logging, monitoring, debugging? | 10% |
| 8 | **Ecosystem** | Extensions, plugins, integrations? | 5% |
| 9 | **Readiness** | Production-ready? Can use today? | 10% |
| 10 | **Evolution** | System có thể tự cải thiện? | 5% |

**Scoring rules:**
- 1-3: Thiếu hoàn toàn hoặc broken
- 4-6: Có nhưng chưa đủ, cần cải thiện
- 7-8: Tốt, minor issues
- 9-10: Excellent, best practice

### Bước 3: PHẢN BIỆN ĐA LUỒNG (Adversarial Perspectives)

Đánh giá TỐI THIỂU 5 góc nhìn. Mỗi góc nhìn = 1 persona cụ thể:

| Persona | Câu hỏi chính | Focus |
|---------|--------------|-------|
| **🔓 Hacker** | "Làm sao phá hệ thống?" | Security holes, edge cases, abuse vectors |
| **📋 Auditor** | "Chứng minh nó hoạt động?" | Evidence, compliance, audit trail |
| **🏢 Competitor** | "Có gì unique?" | Competitive edge, differentiation |
| **👨‍💻 Pragmatist** | "Dùng được ngay không?" | Practical value, ROI, learning curve |
| **🏗️ Architect** | "Sustainable 2 năm nữa?" | Tech debt, scalability, maintenance |
| **👔 CEO** | "Kiếm thêm tiền hay mất thời gian?" | Business value, cost/benefit |
| **🔄 Operator** | "Vận hành hàng ngày như nào?" | Ops burden, monitoring, troubleshooting |
| **🆕 New Hire** | "Onboard mất bao lâu?" | Documentation, complexity, learning curve |

**Rules:**
- Mỗi persona PHẢI đưa ra verdict riêng (1-10)
- KHÔNG được thiên vị — nếu persona thấy vấn đề, PHẢI report
- Mỗi finding PHẢI có evidence cụ thể

### Bước 4: PHÁT HIỆN (Findings)

Phân loại findings:

```
🔴 CRITICAL: Broken / missing / security risk → Fix ngay
🟡 IMPORTANT: Incomplete / inconsistent → Fix trong Q này
🔵 OPTIMIZATION: Nice-to-have → Backlog
✅ STRENGTH: Điểm mạnh cần giữ
```

Mỗi finding PHẢI có format:

```markdown
### [🔴/🟡/🔵/✅] [Title]
> **Score: [X/10]**

**Evidence:** [Specific data — file names, line numbers, metrics]
**Impact:** [What happens if not fixed]
**Fix:** [Specific action with effort estimate]
```

### Bước 5: ĐỐI CHIẾU (Cross-Reference)

| Finding | Hacker | Auditor | Pragmatist | Architect | CEO |
|---------|--------|---------|------------|-----------|-----|
| [Finding 1] | ? | ? | ? | ? | ? |
| [Finding 2] | ? | ? | ? | ? | ? |

**Rules:**
- Nếu ≥3 perspectives đồng ý = HIGH CONFIDENCE finding
- Nếu perspectives conflict = NEED MORE DATA
- Nếu chỉ 1 perspective thấy = MONITOR

### Bước 6: HÀNH ĐỘNG (Action Plan)

Ưu tiên theo Impact × Confidence:

| Priority | Finding | Impact | Confidence | Effort | Action |
|----------|---------|--------|-----------|--------|--------|
| P0 | | ★★★★★ | ≥3 agree | | |
| P1 | | ★★★★ | ≥2 agree | | |
| P2 | | ★★★ | 1 only | | |

## Output Template

```markdown
# 🔍 Multi-Dimensional Review — [Subject]

## Tổng điểm: [X.XX/10]

## Bảng chấm điểm 10 chiều
| # | Chiều | Điểm | Evidence |
|---|-------|------|----------|

## Phản biện đa luồng
### [Persona 1]
| Concern | Verdict |

## Findings
### 🔴 Critical
### 🟡 Important
### 🔵 Optimization
### ✅ Strengths

## Cross-Reference Matrix
| Finding | P1 | P2 | P3 | P4 | P5 | Confidence |

## Action Plan
| Priority | Finding | Effort | Owner |
```

## Integration
- **capability-evolver** — Feeds review findings into evolution cycle
- **knowledge-crystallizer** — Extracts lessons from review findings
- **prompt-sentinel** — Review chuyên sâu từng prompt riêng lẻ (SOUL.md, workflow step, skill) — dùng khi multi-dimensional-review phát hiện vấn đề ở tầng prompt
- **HEARTBEAT** — Schedule periodic reviews (monthly or every 20 tasks)
