---
description: "Hệ thống viết content đa năng tiếng Việt. Auto-kích hoạt khi user yêu cầu viết bất kỳ loại content nào: truyện fiction, tài liệu học tập, slide bài giảng, nghiên cứu, blog, social media đa nền tảng. Pipeline multi-agent + Anti-AI Engine + Vietnamese Emotional Writing. Trigger: /novel, /write, viết truyện, viết bài, tạo slide, tài liệu, content."
---

# ✍️ Viet-Pro Writer — Universal Vietnamese Content Studio

> **Version**: 3.0 — Powered by Viet-Pro Engine
> **Architecture**: Adaptive Multi-Agent Pipeline + Anti-AI Humanization
> **Đặc biệt**: Viết content KHÔNG THỂ nhận diện là AI, đa format, đa nền tảng

---

## 🎯 TỰ ĐỘNG KÍCH HOẠT KHI

### Nhận diện ý định viết content (Auto-detect)
Skill này **TỰ ĐỘNG kích hoạt** khi phát hiện user yêu cầu bất kỳ nội dung nào dưới đây — KHÔNG cần user gõ lệnh:

| Trigger | Ví dụ user request |
|---------|-------------------|
| **Viết truyện** | "viết chapter", "tạo outline", "viết truyện", "tiếp chapter" |
| **Viết bài / content** | "viết bài về...", "viết content cho...", "tạo bài đăng..." |
| **Tài liệu học tập** | "soạn giáo trình", "tạo tài liệu", "viết bài giảng" |
| **Slide / Presentation** | "tạo slide", "soạn bài thuyết trình", "presentation về..." |
| **Nghiên cứu** | "viết luận", "tổng hợp nghiên cứu", "phân tích chủ đề..." |
| **Social media** | "đăng Facebook", "viết post LinkedIn", "caption TikTok", "thread Twitter" |
| **Email / Newsletter** | "viết email marketing", "soạn newsletter", "email B2B" |
| **SEO / Blog** | "viết bài SEO", "blog post về...", "long-form article" |

### Lệnh trực tiếp
| Lệnh | Mô tả |
|-------|--------|
| `/novel` hoặc `/write` | Kích hoạt thủ công |
| `/novel init` | Tạo world-bible mẫu cho truyện fiction |
| `/novel chapter [N]` | Viết chapter N (full pipeline) |
| `/write [loại]` | Viết content theo loại chỉ định |

---

## 🧠 ADAPTIVE DISPATCH — PHÂN LOẠI TỰ ĐỘNG

### Bước 1: Nhận diện loại content

```
User Request
    ↓
┌──────────────────────────────────────────────────────────┐
│                 CONTENT TYPE ROUTER                       │
│                                                          │
│  📖 FICTION        → Pipeline A: Novel Writer (7 agent)   │
│  📝 ARTICLE/BLOG   → Pipeline B: Viet-Pro (Swarm)        │
│  📚 LEARNING       → Pipeline C: EduWriter (NEW)         │
│  🎤 PRESENTATION   → Pipeline D: SlideWriter (NEW)       │
│  🔬 RESEARCH       → Pipeline E: ResearchWriter (NEW)    │
│  📱 SOCIAL MEDIA   → Pipeline F: SocialWriter (NEW)      │
│  📧 EMAIL          → Pipeline B + Email Module            │
└──────────────────────────────────────────────────────────┘
```

### Bước 2: Thu thập thông tin (THÔNG MINH)

Hỏi user TỐI THIỂU — chỉ những gì chưa biết. Nếu user đã cung cấp đủ, KHÔNG hỏi:

```
1. CHỦ ĐỀ: Viết về gì? (auto-detect từ request)
2. LOẠI CONTENT: Fiction / Article / Learning / Slide / Research / Social? (auto-detect)
3. ĐỐI TƯỢNG: Viết cho ai? (Gen Z / Millennials / Chuyên gia / Học sinh-SV / Đại chúng)
4. PLATFORM/FORMAT: Output ở đâu? (Facebook / LinkedIn / Blog / Slide / Word / PDF)
5. GIỌNG VĂN: (Thân thiện / Chuyên gia / Storytelling / Học thuật / Hóm hỉnh)
6. ĐỘ DÀI: (Ngắn / Vừa / Dài / Để tôi quyết định)
```

---

## 📖 PIPELINE A: NOVEL WRITER — Viết Truyện Fiction

### Kiến trúc 7+1 Agent

```
┌─────────────────────────────────────────────────┐
│          ORCHESTRATOR (Tổng Biên Tập)            │
└──┬──────┬──────┬──────┬──────┬──────┬──────┬────┘
   │      │      │      │      │      │      │
   │   World  Plotter Writer Human- QA    Editor
   │   Builder              izer  Scorer
   └──── 🔒 VIET-PRO ENGINE (Always Active)
```

**Flow:** Orchestrator → WorldBuilder → Plotter → Writer → Humanizer (12-layer) → QA (130đ) → Editor

### 12-Layer Humanization
```
Layer 1-5:  Core (cắt thuyết minh → neo đời → nội tâm → xấu câu → cliff)
Layer 6-12: Viet-Pro (burstiness → emotion → tu từ → voice → idiom → rhythm → anti-AI)
```

### QA Scoring — 130 điểm
- 8 trụ gốc (100đ): POV/Sensory, Urban Texture, Emotional Logic, Rhythm, Dialogue, System, Progress, Noise
- 3 trụ Anti-AI (30đ): Burstiness, Human Fingerprint, Vietnamese Authenticity
- Quality Gates: ≥100 PASS / 85-99 REVISION / <85 REWRITE

### 8 Thể loại hỗ trợ
Tiên Hiệp · Đô Thị · Hệ Thống/LitRPG · Ngôn Tình · Kiếm Hiệp · Thriller · Sci-Fi · Kinh Dị

---

## 📝 PIPELINE B: VIET-PRO SWARM — Viết Content/Article/Email

### Swarm Orchestrator (11 Modules)

```
┌─────────────────┐
│  LUÔN LOAD (3)  │  Q1 Punctuation · Q2 Natural · R1 Anti-AI
└────────┬────────┘
         ↓
┌────────────────────────────────────────────┐
│           DISPATCH THEO INPUT              │
│  Giọng thân thiện    → V1 Emotional       │
│  Giọng chuyên gia    → V2 Advanced        │
│  Kỹ thuật/howto      → V3 Technical       │
│  Facebook            → H1 Facebook        │
│  LinkedIn            → H2 LinkedIn (NEW)  │
│  TikTok              → H3 TikTok (NEW)    │
│  Có số liệu/claim   → Q3 Fact-check      │
│  Cần research        → N1 Research        │
│  Long-form           → N2 Analysis        │
│  Email marketing     → H4 Email (NEW)     │
└────────────────────────────────────────────┘
```

**Flow:** Research → Structure (PAS/BAB/AIDA/Hero's Journey) → Write → Quality → Anti-AI → Deliver

---

## 📚 PIPELINE C: EDUWRITER — Tài Liệu Học Tập (MỚI)

### Khi nào kích hoạt
- User yêu cầu: soạn giáo trình, tài liệu học, bài giảng, lesson plan, quiz, handout, workbook

### EduWriter Architecture

```
[1] CURRICULUM ANALYZER
    Phân tích learning objectives, target level, scope
    ↓
[2] STRUCTURE DESIGNER
    Bloom's Taxonomy mapping → Module/Lesson/Topic hierarchy
    ↓
[3] CONTENT WRITER (Viet-Pro Engine)
    Viết nội dung theo pedagogical patterns
    ↓
[4] ENGAGEMENT LAYER
    Thêm: examples, case study VN, exercises, quiz, mnemonics
    ↓
[5] QUALITY CHECK
    Kiểm tra: accuracy, progression, accessibility, anti-AI
    ↓
OUTPUT: Tài liệu học tập hoàn chỉnh
```

### Learning Document Types

| Loại | Format | Đặc thù |
|------|--------|---------|
| **Giáo trình** | Markdown/Word | Chapters → Lessons → Exercises → Summary |
| **Handout** | 1-2 trang | Key points + visual + practice |
| **Workbook** | Bài tập | Instructions → Practice → Self-check |
| **Quiz/Test** | Câu hỏi | MC + True/False + Short answer + Rubric |
| **Lesson Plan** | Template | Objectives → Activities → Assessment → Reflection |
| **Case Study** | Narrative | Scenario VN → Questions → Discussion Guide |

### Pedagogical Frameworks

```
Bloom's Taxonomy Integration:
┌──────────────────────────────────┐
│  6. Sáng tạo    → Dự án, thiết kế  │
│  5. Đánh giá    → Phân tích case   │
│  4. Phân tích   → So sánh, debate  │
│  3. Vận dụng    → Bài tập thực hành │
│  2. Hiểu        → Giải thích, ví dụ │
│  1. Nhớ         → Định nghĩa, list │
└──────────────────────────────────┘

Mỗi lesson PHẢI cover ít nhất 3 tầng Bloom.
```

### EduWriter Rules
```
1. CONCRETE FIRST: Luôn bắt đầu bằng ví dụ/tình huống → rồi mới lý thuyết
2. VN CONTEXT: Ví dụ phải từ bối cảnh Việt Nam (doanh nghiệp VN, pháp luật VN)
3. ACTIVE LEARNING: Mỗi 500 từ phải có 1 điểm tương tác (câu hỏi/bài tập/reflection)
4. PROGRESSIVE: Từ đơn giản → phức tạp, không nhảy cóc
5. VISUAL AIDS: Suggest table/diagram/flowchart ở mọi khái niệm phức tạp
```

---

## 🎤 PIPELINE D: SLIDEWRITER — Slide Bài Giảng (MỚI)

### Khi nào kích hoạt
- User yêu cầu: tạo slide, PowerPoint, presentation, bài thuyết trình, keynote

### SlideWriter Architecture

```
[1] PRESENTATION PLANNER
    Xác định: audience, duration, key message, call-to-action
    ↓
[2] STORYBOARD DESIGNER
    Tạo slide outline theo narrative arc
    ↓
[3] SLIDE CONTENT WRITER
    Viết content per slide (bullet points + speaker notes)
    ↓
[4] VISUAL RECOMMENDER
    Suggest: layout, chart type, image prompts, icons
    ↓
OUTPUT: Slide deck outline + speaker notes
```

### Slide Format Rules

```
MỖI SLIDE:
├── Title: ≤7 từ, action-oriented
├── Body: ≤6 bullets, mỗi bullet ≤10 từ
├── Visual: 1 hình/biểu đồ/icon gợi ý
└── Speaker Note: 50-100 từ (what to SAY)

TỔNG SLIDE:
├── 10-min talk: 8-12 slides
├── 20-min talk: 15-20 slides
├── 45-min lecture: 25-35 slides
└── Workshop: 15-20 slides + 5-10 activity slides
```

### Presentation Narrative Arc

```
Slide 1-2:   HOOK — Tình huống/câu hỏi/số liệu gây shock
Slide 3-4:   PROBLEM — Đào sâu vấn đề, pain point
Slide 5-8:   SOLUTION — Framework/giải pháp, từng bước
Slide 9-10:  EVIDENCE — Case study, data, demo
Slide 11-12: ACTION — CTA, next steps, Q&A
```

### Output Format

```markdown
## Slide [N]: [Tiêu đề]

**Layout:** [Full-image / Title+Bullets / Split / Quote / Chart]

### Content
- Bullet 1
- Bullet 2
- Bullet 3

### Visual
> [Gợi ý hình ảnh/biểu đồ/icon]

### Speaker Notes
> [Nội dung cần nói — 50-100 từ]

---
```

---

## 🔬 PIPELINE E: RESEARCHWRITER — Tài Liệu Nghiên Cứu (MỚI)

### Khi nào kích hoạt
- User yêu cầu: viết luận, nghiên cứu, báo cáo phân tích, white paper, literature review, policy brief

### ResearchWriter Architecture

```
[1] RESEARCH SCOPING
    Define: research question, scope, methodology
    ↓
[2] LITERATURE REVIEW
    Thu thập & tổng hợp nguồn (Perplexity + Web search)
    ↓
[3] ANALYSIS ENGINE
    Phân tích data, so sánh, synthesis
    ↓
[4] WRITER (Academic Viet-Pro)
    Viết theo chuẩn academic + anti-AI
    ↓
[5] CITATION CHECK
    Verify sources, format references
    ↓
OUTPUT: Tài liệu nghiên cứu + References
```

### Research Document Types

| Loại | Cấu trúc | Độ dài |
|------|---------|--------|
| **Literature Review** | Introduction → Themes → Gaps → Conclusion | 2000-5000 từ |
| **White Paper** | Problem → Analysis → Solution → Recommendation | 3000-6000 từ |
| **Policy Brief** | Executive Summary → Context → Options → Recommendation | 1000-2000 từ |
| **Case Analysis** | Background → Methodology → Findings → Implications | 2000-4000 từ |
| **Report** | Executive Summary → Sections → Conclusion → Appendix | 3000-10000 từ |

### Academic Writing Rules
```
1. CLAIM = EVIDENCE: Mọi claim phải có citation hoặc data
2. BALANCED: Trình bày multiple perspectives trước khi kết luận
3. PRECISE: Ngôn ngữ chính xác, không mơ hồ
4. STRUCTURED: Heading hierarchy rõ ràng (H1→H2→H3)
5. VN CONTEXT: Ưu tiên sources và case studies Việt Nam
6. ANTI-AI: Vẫn áp dụng burstiness + human fingerprint (academic flavor)
```

---

## 📱 PIPELINE F: SOCIALWRITER — Content Đa Nền Tảng (MỚI)

### Khi nào kích hoạt
- User yêu cầu content cho bất kỳ social media platform nào

### Platform-Specific Rules

#### 📘 Facebook
```
Format: 150-500 từ · Paragraph 1-3 câu · Emoji 3-5/bài · Hashtag 3-5
Hook: 3 giây đầu (Shock stat / Question / Contrarian / Story open)
CTA: Engagement (Drop emoji) / Save ("Bookmark lại") / Share ("Tag 1 người")
Template: HOOK → CONTEXT → BODY (3-5 đoạn) → CLOSING → CTA → Hashtags
```

#### 💼 LinkedIn
```
Format: 200-800 từ · Professional tone · Data-driven · Storytelling
Hook: Insight/Lesson learned/Contrarian take
Structure: Hook → Context → 3-5 Key Points → Takeaway → Question CTA
Đặc biệt: Dùng "—" thay bullet · Line breaks ngắn · No hashtag spam (≤5)
```

#### 🎵 TikTok / Reels Caption
```
Format: 50-150 từ · Punchy · Gen Z friendly · Emoji OK
Hook: Câu đầu = scroll-stopper
Structure: Hook → 1-2 key points → CTA ("Follow để xem part 2")
Hashtag: 5-10, mix trending + niche
Đặc biệt: Viết như đang nói · Slang OK · Short sentences
```

#### 🐦 Twitter/X Thread
```
Format: Mỗi tweet ≤280 ký tự · Thread 5-15 tweets
Tweet 1: HOOK (compelling opening + "🧵")  
Tweet 2-N: Mỗi tweet = 1 ý hoàn chỉnh
Tweet cuối: Summary + CTA ("Retweet nếu hữu ích")
Đặc biệt: Numbered · Self-contained per tweet · Cliff giữa tweets
```

#### 📧 Email Newsletter
```
Format: 300-800 từ · Subject line ≤50 ký tự · Preview text ≤90 ký tự
Structure: Subject → Preview → Greeting → Body (scannable) → CTA → P.S.
CTA: 1 CTA chính, rõ ràng, action verb
Đặc biệt: Mobile-first · 1 link CTA · Personal tone
```

#### 📝 Blog / SEO Article
```
Format: 1000-3000 từ · H2/H3 structure · Internal/External links
SEO: Target keyword trong title, H1, first 100 words, meta description
Structure: Title → Meta → Intro (hook) → Sections (H2) → Conclusion → CTA
Đặc biệt: Table of Contents · FAQ schema · Featured snippet optimization
```

### Cross-Platform Content Repurposing

```
1 chủ đề → 6 formats:

Blog (2000 từ) 
  ├─→ LinkedIn Post (summary + insight)
  ├─→ Facebook Post (storytelling angle)
  ├─→ Twitter Thread (key points breakdown)
  ├─→ TikTok Caption (hook + 1 tip)
  └─→ Newsletter (curated version)
```

---

## 📦 KNOWLEDGE FILES

### Core (Luôn load — từ Viet-Pro)
| File | Path | Module |
|------|------|--------|
| Anti-AI Humanization | `Viet-Pro/knowledge/anti-ai-humanization.md` | Humanizer + QA |
| Emotional Writing VN | `Viet-Pro/knowledge/emotional-writing-vn.md` | Writer |
| Advanced Writing | `Viet-Pro/knowledge/advanced-writing-techniques.md` | Plotter |
| Natural Language VN | `Viet-Pro/knowledge/natural-language-vn.md` | QA |
| Punctuation VN | `Viet-Pro/knowledge/punctuation-patterns-vn.md` | Editor |
| Fact-Check System | `Viet-Pro/knowledge/fact-check-system.md` | QA |

### Genre (Load theo thể loại fiction)
8 files: `genre-tien-hiep.md`, `genre-do-thi-tu-tien.md`, `genre-he-thong-litrpg.md`, `genre-ngon-tinh.md`, `genre-kiem-hiep.md`, `genre-thriller.md`, `genre-sci-fi.md`, `genre-kinh-di.md`

### Modules (Load theo dispatch)
Existing: `style-emotional.md`, `style-advanced.md`, `style-technical.md`, `content-research.md`, `content-analysis.md`, `platform-facebook.md`, `quality-*.md`
New Platforms: `platform-linkedin.md`, `platform-tiktok.md`, `platform-email.md`, `platform-twitter.md`, `platform-blog-seo.md`
New Pipelines: `edu-writer.md`, `slide-writer.md`, `research-writer.md`, `social-writer.md`

> **Knowledge Resolution Order:**
> 1. Workspace: `.agent/skills/novel-writer/knowledge/`
> 2. Global Skill: `D:\AntigravityWorkspace\Skill\Viet-Pro\knowledge/`
> 3. Global Skill Modules: `D:\AntigravityWorkspace\Skill\Viet-Pro\modules/`

---

## 🔒 RULES BẤT KHẢ XÂM PHẠM (Áp dụng cho MỌI pipeline)

### Rule 1: ZERO AI TELLS
```
Humanizer PHẢI quét 25 AI tells. Nếu phát hiện → fix NGAY.
❌ "Trong bối cảnh hiện nay..." | "Hơn nữa..." | "Điều đáng chú ý..."
✅ Viết như ĐANG NÓI CHUYỆN với người thông minh
```

### Rule 2: BURSTINESS BẮT BUỘC
```
- Ít nhất 1 câu ≤5 từ mỗi 200 từ
- Ít nhất 3 loại câu (hỏi, thán, kể, bỏ lửng)
- Paragraph length KHÔNG đồng đều
```

### Rule 3: VIETNAMESE SOUL
```
MỌI bài viết PHẢI có:
- Ít nhất 1 thành ngữ/tục ngữ/cách nói VN
- Ít nhất 1 ví dụ cụ thể (tên, ngày, con số thật)
- Dấu câu CHUẨN tiếng Việt
```

### Rule 4: HUMAN FINGERPRINT
```
MỌI bài viết PHẢI có:
- Ít nhất 1 anecdote/trải nghiệm
- Quan điểm cá nhân rõ ràng
- Chi tiết cảm xúc cụ thể
```

### Rule 5: SHOW DON'T TELL (Fiction)
```
❌ "Lâm cảm thấy tức giận."
✅ "Hàm Lâm nghiến lại. Mắt hắn đỏ. Móng tay cắm vào lòng bàn tay."
```

### Rule 6: ANTI-AI FINAL CHECK
```
TRƯỚC KHI giao bài, tự chạy 10 câu hỏi:
1. Có câu ≤5 từ?  2. Variation câu?  3. Anecdote?
4. Thành ngữ VN?  5. Paragraph vary?  6. Humor/wit?
7. Kết khác mở?   8. Từ mở đầu vary?  9. Opinion mạnh?
10. Đọc to tự nhiên?
→ <7/10 → REWRITE | ≥7/10 → Deliver
```

---

## 📄 OUTPUT FORMAT CHUNG

```markdown
## 📝 [Tiêu đề]

[Nội dung]

---

### 📊 Thông số
- **Loại**: [Fiction/Article/Learning/Slide/Research/Social]
- **Độ dài**: X từ
- **Framework**: [PAS/BAB/AIDA/Bloom's/Academic/...]
- **Giọng văn**: [Emotional/Advanced/Technical/Academic]
- **Anti-AI Score**: X/10
- **Platform**: [Facebook/LinkedIn/Blog/Slide/...]

### 💡 Gợi ý
- [CTA, hashtag, hình ảnh, cross-platform repurpose]
```

---

*Viet-Pro Writer v3.0 — Universal Vietnamese Content Studio*
*"Viết như người. Nghĩ như người. Chạm như người."*
