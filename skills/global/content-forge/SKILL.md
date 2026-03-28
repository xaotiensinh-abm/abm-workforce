---
name: "Goal"
description: "Sinh nội dung chuyên nghiệp đạt enterprise-grade từ lần xuất bản đầu tiên"
---

﻿---
name: content-forge
description: Enterprise content engine: Intake > Draft > 12-agent Audit > Fix > Loop until >90/100. All content types.
---
---

# Goal

> **Use this skill when:** content production pipeline or multi-format content creation

Sinh nội dung chuyên nghiệp đạt enterprise-grade từ lần xuất bản đầu tiên
thông qua quy trình chuẩn hóa **Intake → Draft → Multi-Agent Audit → Fix → Loop**.
Apply cho MỌI thể loại nội dung. Mục tiêu: score >90/100 qua hệ thống audit thích ứng.

---

# Instructions

## 🧭 PHASE 0: INTAKE — Thu thập & Phân loại

### 0.1 Xác định thể loại nội dung

Khi user yêu cầu viết, PHẢI xác định **Content Type** trước:

| Type ID | Thể loại | Đặc trưng | Audit Profile |
|---|---|---|---|
| `VO` | Voice-over / E-learning Script | Thời lượng, slides, SFX, breath marks, Gagné | `TRAINING` |
| `RPT` | Báo cáo / Report / Whitepaper | Dữ liệu, biểu đồ, executive summary, citations | `ANALYTICAL` |
| `SOP` | Quy trình / SOP / Hướng dẫn | Steps, checklist, diagrams, compliance | `PROCEDURAL` |
| `PROP` | Đề án / Proposal / Business Case | ROI, timeline, risk, stakeholder, budget | `PERSUASIVE` |
| `EMAIL` | Email / Communication | Tone, brevity, CTA, recipient context | `COMMUNICATION` |
| `SLIDE` | Slide / Presentation | Visual cues, speaker notes, flow, timing | `PRESENTATION` |
| `TRAIN` | Training Material (non-VO) | Learning objectives, exercises, assessment | `TRAINING` |
| `MKT` | Marketing / Content Marketing | Hook, CTA, SEO, brand voice, audience | `PERSUASIVE` |
| `SOCIAL` | Social Media / Short-form | Platform rules, hashtags, visual, virality | `ENGAGEMENT` |
| `TECH` | Technical Documentation | Accuracy, API refs, code samples, versioning | `TECHNICAL` |
| `LEGAL` | Hợp đồng / Legal / Compliance | Clauses, regulatory refs, precision | `COMPLIANCE` |
| `CUSTOM` | Khác | User tự define audit agents | `CUSTOM` |

Nếu không rõ type → HỎI: *"Nội dung này thuộc thể loại nào? (báo cáo, SOP, email, slide, marketing...)"*

### 0.2 Thu thập thông tin bắt buộc

Sau khi xác định type, thu thập **INTAKE CARD**:

| # | Thông tin | Bắt buộc | Ví dụ |
|---|---|---|---|
| 1 | **Content Type** | ✅ | `RPT` — Báo cáo |
| 2 | **Tiêu đề / Chủ đề** | ✅ | "Báo cáo hiệu quả CDU Q3/2025" |
| 3 | **Đối tượng đọc/nghe** | ✅ | "HĐQT BSR" |
| 4 | **Mục đích sử dụng** | ✅ | "Trình ĐHĐCĐ thường niên" |
| 5 | **Ngữ cảnh tổ chức** | ✅ | "BSR, 1.600 CBCNV, dầu khí" |
| 6 | **Yêu cầu format** | ✅ | "10 trang, tiếng Việt, có bảng số liệu" |
| 7 | **Dữ liệu đầu vào** | 🟡 | Số liệu, tài liệu tham khảo |
| 8 | **Yêu cầu đặc biệt** | 🟡 | "Có so sánh với PVN, giọng trang trọng" |

Nếu thiếu mục ✅ → HỎI, không đoán. Nếu thiếu mục 🟡 → ghi nhận, bổ sung sau.

---

## ✍️ PHASE 1: DRAFT — Viết bản nháp

### 1.1 Áp dụng quy tắc theo Content Type

**Type `VO` (Voice-over):**
- Dùng pipeline từ skill `enterprise-voiceover-script`
- Tính @140 từ/phút, breath marks, SFX, demo backup, Gagné 9 Events

**Type `RPT` (Báo cáo):**
- Executive Summary trước, detail sau
- Mọi claim có citation (năm + nguồn)
- Bảng/biểu đồ data-driven
- Kết luận + đề xuất actionable

**Type `SOP` (Quy trình):**
- Steps đánh số rõ ràng (1, 2, 3...)
- Mỗi step = 1 hành động cụ thể
- Có checklist cuối
- Ghi rõ: ai làm, khi nào, điều kiện, output mong đợi

**Type `PROP` (Đề án):**
- Problem → Solution → ROI → Timeline → Risk → Ask
- Số liệu tài chính cụ thể
- So sánh phương án
- Call to action rõ ràng

**Type `EMAIL` (Email):**
- Subject line compelling
- Mở đầu: context 1 câu
- Thân: 1-3 ý chính (bullet nếu >1)
- Kết: CTA rõ ràng
- Tổng ≤300 từ (trừ formal proposals)

**Type `SLIDE` (Presentation):**
- 1 ý chính / slide
- Text ≤40 từ / slide (speaker notes riêng)
- Visual cues: [Hình: ...], [Biểu đồ: ...]
- Flow: Hook → Problem → Solution → Evidence → CTA

**Type `MKT` (Marketing):**
- Hook đầu (pain point hoặc aspiration)
- Benefits > Features
- Social proof / case study
- CTA specific + urgent

**Type `TECH` (Technical Doc):**
- Structure: Overview → Prerequisites → Steps → Troubleshooting → Reference
- Code blocks có syntax highlight
- Version + last-updated
- Cross-reference related docs

### 1.2 Quy tắc viết universal

| Rule | Áp dụng mọi type |
|---|---|
| **Clarity first** | Viết rõ ràng > viết hay. Mọi câu phải có 1 ý chính |
| **Active voice** | "Ban KTSX đã hoàn thành" > "Đã được hoàn thành bởi..." |
| **Data-backed** | Mọi claim có bằng chứng. Không bịa số liệu |
| **Audience-aware** | Giọng điệu + chi tiết phù hợp đối tượng |
| **Structured** | Heading hierarchy rõ ràng. Scan-friendly |
| **Actionable** | Kết thúc bằng: người đọc cần LÀM GÌ tiếp? |

---

## 🔬 PHASE 2: AUDIT — Đánh giá đa chiều thích ứng

### 2.1 Audit Profile theo Content Type

Mỗi Content Type kích hoạt 1 **Audit Profile** — bộ agents phù hợp:

#### Profile `TRAINING` (VO, TRAIN)

| # | Agent | Trọng số |
|---|---|---|
| 1 | 🎯 Content Accuracy | 10% |
| 2 | 🎓 Instruction Design (Gagné/Bloom) | 12% |
| 3 | 🎙️ Audio/Production Quality | 8% |
| 4 | 🏭 Domain Expert | 10% |
| 5 | 🧪 QA Consistency | 10% |
| 6 | 🧠 Psychology/Engagement | 8% |
| 7 | 🏢 L&D Director | 10% |
| 8 | 🔄 Change Management | 8% |
| 9 | ⚖️ Legal/Compliance | 6% |
| 10 | 📺 Production Feasibility | 6% |
| 11 | ♿ Accessibility | 6% |
| 12 | 🇻🇳 Localization/Culture | 6% |

#### Profile `ANALYTICAL` (RPT)

| # | Agent | Trọng số |
|---|---|---|
| 1 | 🎯 Data Accuracy | 15% |
| 2 | 📊 Analytical Rigor | 12% |
| 3 | 🏭 Domain Expert | 12% |
| 4 | 🧪 QA Consistency | 10% |
| 5 | 📐 Structure & Flow | 8% |
| 6 | 🏢 Executive Readability | 10% |
| 7 | ⚖️ Legal/Compliance | 8% |
| 8 | 📈 Visualization Quality | 8% |
| 9 | 🔍 Citation/Source Integrity | 8% |
| 10 | 🇻🇳 Localization/Culture | 5% |
| 11 | ♿ Accessibility | 2% |
| 12 | 🎨 Formatting/Polish | 2% |

#### Profile `PROCEDURAL` (SOP)

| # | Agent | Trọng số |
|---|---|---|
| 1 | 🎯 Technical Accuracy | 15% |
| 2 | 📋 Step Clarity | 15% |
| 3 | 🏭 Domain Expert | 12% |
| 4 | 🧪 QA Completeness | 10% |
| 5 | ⚠️ Safety/Risk Coverage | 10% |
| 6 | ⚖️ Compliance | 10% |
| 7 | 🔄 Change Management | 8% |
| 8 | ♿ Accessibility (language level) | 5% |
| 9 | 📐 Format Consistency | 5% |
| 10 | 🏢 Approver Readiness | 5% |
| 11 | 🇻🇳 Localization | 3% |
| 12 | 🎨 Formatting/Polish | 2% |

#### Profile `PERSUASIVE` (PROP, MKT)

| # | Agent | Trọng số |
|---|---|---|
| 1 | 🎯 Claim Accuracy | 12% |
| 2 | 🧠 Persuasion Psychology | 12% |
| 3 | 🏭 Domain Expert | 10% |
| 4 | 📊 Data/Evidence Quality | 10% |
| 5 | 🎪 Hook & Narrative Arc | 10% |
| 6 | 💰 ROI / Business Case Logic | 10% |
| 7 | 🧪 QA Consistency | 8% |
| 8 | 🏢 Decision-Maker Alignment | 8% |
| 9 | ⚖️ Legal/Ethics | 6% |
| 10 | 📐 Structure & Flow | 6% |
| 11 | 🇻🇳 Localization/Culture | 4% |
| 12 | 🎨 Formatting/Polish | 4% |

#### Profile `COMMUNICATION` (EMAIL)

| # | Agent | Trọng số |
|---|---|---|
| 1 | 🎯 Message Clarity | 15% |
| 2 | 👤 Audience Appropriateness | 15% |
| 3 | ✉️ Tone & Register | 12% |
| 4 | 📏 Brevity & Conciseness | 12% |
| 5 | 🎯 CTA Effectiveness | 10% |
| 6 | 🧪 QA (grammar, typo) | 10% |
| 7 | ⚖️ Compliance/Sensitivity | 8% |
| 8 | 📐 Format/Structure | 6% |
| 9 | 🇻🇳 Localization | 6% |
| 10 | 🏭 Domain Context | 4% |
| 11 | ♿ Accessibility | 1% |
| 12 | 🎨 Polish | 1% |

#### Profile `CUSTOM`

User tự chọn 8-12 agents + trọng số. AI suggest mặc định, user confirm.

### 2.2 Scoring & Grading

Mỗi agent chấm 1-10. Weighted average = Final Score.

| Score | Grade | Action |
|---|---|---|
| ≥ 9.0 | ✅ PASS | Ship. Nice-to-have optional |
| 8.0–8.9 | ⚠️ CONDITIONAL | Fix priority items → Re-audit |
| 7.0–7.9 | 🔴 REVISE | Major rewrite sections |
| < 7.0 | ❌ REJECT | Restart from outline |

### 2.3 Audit Output Format

```markdown
# 🔬 CONTENT FORGE AUDIT — [Tiêu đề] v[X] Round [R]
## Type: [TYPE ID] | Profile: [PROFILE] | Score: **[X.X]/10**

## SCORECARD
| Agent | Score | Key Finding |

## PRIORITY ACTION ITEMS
| # | Severity | Issue | Location | Fix |
| 🔴 Critical | ... |
| 🟡 High | ... |
| 🟢 Low | ... |

## STRENGTHS
1. ...
```

---

## 🔧 PHASE 3: FIX — Chỉnh sửa

1. Fix ALL 🔴 Critical trước
2. Fix 🟡 High/Medium tiếp
3. 🟢 Low = nice-to-have
4. KHÔNG thay đổi nội dung không liên quan (minimal impact)
5. Version bump: v1.0 → v1.1 → v1.2...

---

## 🔄 PHASE 4: LOOP — Re-audit đến khi PASS

```
┌──────────────────────────────────────────────┐
│       DRAFT → AUDIT → FIX → RE-AUDIT         │
│       ↑                         │             │
│       └── < 9.0 ── SCORE ── ≥ 9.0 → ✅ PASS  │
└──────────────────────────────────────────────┘
```

- Tối đa 3 rounds
- Round 2+ format: "Post-Fix Verification" với RESOLUTION STATUS table
- Round 3 vẫn < 9.0 → escalate cho user review

---

# Examples

## Ví dụ 1: Voice-over script (Type VO)

```
User: "Viết bài giảng Prompt Engineering cho BSR, 90 phút"
→ Type: VO | Profile: TRAINING
→ Phase 0: Intake 8 items
→ Phase 1: Draft 25 slides, ~7.000 từ
→ Phase 2: Audit 12 agents → 8.9/10
→ Phase 3: Fix 7 issues → v1.1
→ Phase 4: Re-audit → 9.2/10 ✅ PASS
```

## Ví dụ 2: Báo cáo HĐQT (Type RPT)

```
User: "Viết báo cáo hiệu quả vận hành CDU quý 3 cho HĐQT"
→ Type: RPT | Profile: ANALYTICAL
→ Intake: đối tượng=HĐQT, data=CDU KPI, format=5 trang
→ Draft: Exec Summary + 4 sections + Đề xuất
→ Audit: Data Accuracy 9.5, Analytical Rigor 8.5, Visualization 7.5...
→ Fix: thêm benchmark chart, citation sources
→ Re-audit: 9.1 ✅ PASS
```

## Ví dụ 3: SOP (Type SOP)

```
User: "Viết SOP khởi động CDU sau bảo dưỡng"
→ Type: SOP | Profile: PROCEDURAL
→ Intake: scope=CDU startup, audience=operators, safety=critical
→ Draft: 12 steps + checklist + safety warnings
→ Audit: Step Clarity 9.0, Safety Coverage 8.0, Compliance 9.5...
→ Fix: add interlock check step, clarify valve positions
→ Re-audit: 9.3 ✅ PASS
```

## Ví dụ 4: Email (Type EMAIL)

```
User: "Soạn email mời thầu cho đợt TA6"
→ Type: EMAIL | Profile: COMMUNICATION
→ Intake: recipient=vendors, tone=formal EN, purpose=RFQ
→ Draft: 250 từ, subject + 3 sections + CTA
→ Audit: Clarity 9.5, Tone 9.0, CTA 8.5, Brevity 9.0...
→ Score: 9.1 ✅ PASS (first round!)
```

## Ví dụ 5: Chỉ audit (không viết mới)

```
User: "Audit báo cáo này giúp tôi" + [paste nội dung]
→ Xác định type → Chọn profile → Chạy Phase 2-4 (skip Draft)
```

---

# Constraints

## Hard constraints — không thỏa hiệp

- 🚫 KHÔNG viết mà không có Intake (Phase 0). Intake = foundation
- 🚫 KHÔNG ship nội dung < 9.0/10. Loop bắt buộc
- 🚫 KHÔNG bịa dữ liệu. Mọi số liệu phải có source hoặc ghi rõ "ước tính"
- 🚫 KHÔNG dùng audit profile sai type. RPT ≠ EMAIL ≠ VO
- 🚫 KHÔNG fix mù — mỗi fix phải trace về audit finding cụ thể

## Smart defaults

- Nội dung ngắn (email, social) → audit 1 round thường đủ
- Nội dung dài (report 10+ trang, VO 60+ phút) → expect 2-3 rounds
- Nội dung phức tạp (đề án, legal) → luôn 2+ rounds
- User nói "nhanh" / "draft" → vẫn audit nhưng chấp nhận 8.5+

## Scope

- Skill này viết + audit TEXT content (markdown output)
- KHÔNG tạo visual assets (image, video, slide design)
- KHÔNG upload/publish lên LMS/CMS/platform
- CÓ THỂ suggest visual cues: [Hình: ...], [Biểu đồ: ...]

## Integration với skills khác

- Type `VO` → route chi tiết qua `enterprise-voiceover-script` skill
- Visuals → suggest dùng `generate_image` tool hoặc `visualize` workflow
- PDF output → suggest dùng `md-to-pdf` skill
- DOCX output → suggest dùng `office-design-toolkit` skill

---

<!-- Generated by Skill Creator Ultra v2.0 — Content Forge Engine -->
