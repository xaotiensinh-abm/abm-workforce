# Pipeline: Viết Content Social Media (write-social) — v3.2

## Khi nào kích hoạt
- User yêu cầu viết content cho social media đa nền tảng
- User yêu cầu repurpose 1 bài sang nhiều platforms
- Tín hiệu: "viết post Facebook", "viết LinkedIn", "caption TikTok", "thread Twitter",
  "viết blog SEO", "newsletter", "content đa nền tảng", "repurpose content"

> **So với write-new**: `write-new` viết 1 bài cho 1 platform.
> `write-social` chuyên **multi-platform** orchestration + cross-platform repurposing.

## Pipeline

```
content/ → style/ (per-platform) → social-writer-worker → quality/ (anti-AI) → platform/ (multi) → Output
   │              │                          │                      │                    │
   │              │                          │                      │                    └─ Multi-platform format
   │              │                          │                      └─ Anti-AI per platform
   │              │                          └─ Platform rules + repurpose
   │              └─ Tone per platform
   └─ Audience + trending topics + hashtag research
```

## Bước chi tiết

### 1. Ban Thu Thập (content/)
1. `lead-content.md` nhận brief → xác định:
   - Platform(s) target: Facebook / LinkedIn / TikTok / Twitter / Blog / Newsletter
   - Multi-platform? (→ chọn bài gốc platform → repurpose)
   - Audience per platform
   - Chủ đề + key message
   - Có data/stats để support?
2. `research.md` thu thập:
   - Trending topics trên platform target
   - Hashtag research (trending + niche + branded)
   - Competitor content benchmarks
3. Output: **Social Brief YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route BTV theo platform:
   - Facebook → `storytelling.md` (narrative hook)
   - LinkedIn → `presentation.md` (professional tone)
   - TikTok → `rhythm.md` (punchy, Gen Z)
   - Blog → `technical.md` hoặc `storytelling.md` (depend on topic)
2. **social-writer-worker.md** bổ sung:
   - Platform-specific rules (format, emoji, hashtag, CTA)
   - Cross-platform repurposing flow
   - Post templates per platform
3. Output: **Social Content Pack** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - **anti-ai** (đặc biệt quan trọng cho social — phải voice tự nhiên)
   - natural (đọc to phải giống người nói)
   - fact-check (data points, statistics)
   - consistency (brand voice xuyên platforms)
2. Bonus check: **Platform compliance** (character limits, hashtag count, CTA phù hợp)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến BTV từng platform:
   - `facebook.md` — FB post format
   - `linkedin.md` — LinkedIn post format
   - `tiktok.md` — TikTok caption format
   - `threads.md` — Threads format
   - `docs.md` — Blog / Newsletter format
2. Output: **Multi-platform content package** sẵn sàng đăng

## Cross-Platform Repurpose Flow
Khi user yêu cầu multi-platform:
1. Chọn "anchor platform" (bài gốc dài nhất)
2. Viết bài gốc → full pipeline
3. Repurpose sang các platform khác (ADAPT, không translate):
   - Blog → LinkedIn (insight angle)
   - Blog → Facebook (story angle)
   - Blog → Twitter thread (breakdown)
   - Blog → TikTok caption (1 hook tip)
   - Blog → Newsletter (curated)
4. Mỗi bản repurpose qua quality check riêng

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/anti-ai-humanization.md`
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/platform/facebook.md` — FB rules
- `Ban/platform/tiktok.md` — TikTok rules
- `Ban/platform/linkedin.md` — LinkedIn rules
- `Ban/platform/threads.md` — Threads rules
- `Ban/platform/docs.md` — Blog/Newsletter format
- `Workers/social-writer-worker.md` — platform rules, templates, repurpose flow ★
