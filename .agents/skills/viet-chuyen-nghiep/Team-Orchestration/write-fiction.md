# Pipeline: Viết Truyện Fiction (write-fiction) — v3.2

## Khi nào kích hoạt
- User yêu cầu viết truyện, viết chapter, viết fiction
- User yêu cầu viết tiên hiệp, đô thị, ngôn tình, kiếm hiệp, thriller, sci-fi, kinh dị, LitRPG
- Tín hiệu: "viết truyện", "viết chapter", "tạo outline truyện", "viết tiểu thuyết",
  "viết fiction", "tiếp chapter", "viết tiên hiệp", "viết ngôn tình"

## Pipeline

```
content/ (deep) → style/ (storytelling+rhythm+narrative) → quality/ (130đ) → platform/ → Output
   │                         │                                  │              │
   │                         │                                  │              └─ Format ebook/web
   │                         │                                  └─ QA 130 điểm + Anti-AI
   │                         └─ 12-layer humanization
   └─ World building + plot research
```

## Kiến trúc 7+1 Agent

```
┌─────────────────────────────────────────────────┐
│          ORCHESTRATOR (Tổng Biên Tập)            │
└──┬──────┬──────┬──────┬──────┬──────┬──────┬────┘
   │      │      │      │      │      │      │
   │   World  Plotter Writer Human- QA    Editor
   │   Builder              izer  Scorer
   └──── 🔒 VIET-PRO ENGINE (Always Active)
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — Deep Mode
1. `lead-content.md` nhận brief → xác định:
   - Thể loại (8 genres supported)
   - Thế giới quan (world-bible nếu cần)
   - Nhân vật chính + hệ thống sức mạnh
   - Tông giọng + target audience
2. `research.md` thu thập:
   - Genre conventions + thị trường truyện VN
   - Benchmark từ tác phẩm nổi bật cùng thể loại
3. `analysis.md` đề xuất:
   - Plot outline (3-act hoặc serial)
   - Character arc + power system progression
4. Output: **Story Blueprint YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến 3 BTV:
   - `storytelling.md` — show don't tell, dialogue, scene craft
   - `rhythm.md` — sentence variation, burstiness, pacing
   - `narrative.md` — POV consistency, timeline, plot logic
2. **12-Layer Humanization**:
   - Layer 1-5: Core (cắt thuyết minh → neo đời → nội tâm → xấu câu → cliff)
   - Layer 6-12: Viet-Pro (burstiness → emotion → tu từ → voice → idiom → rhythm → anti-AI)
3. Output: **Fiction Draft** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/) — 130 điểm
1. `lead-quality.md` chạy QA scoring:
   - 8 trụ gốc (100đ): POV/Sensory, Urban Texture, Emotional Logic, Rhythm, Dialogue, System, Progress, Noise
   - 3 trụ Anti-AI (30đ): Burstiness, Human Fingerprint, Vietnamese Authenticity
2. Quality Gates:
   - ≥100 → PASS
   - 85-99 → REVISION
   - <85 → REWRITE
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. Format:
   - Ebook: chapter structure, page breaks, ToC
   - Web serial: chapter title, cliff ending, navigation
   - Wattpad/Webnovel: format theo platform requirements

## 8 Thể loại hỗ trợ
Tiên Hiệp · Đô Thị · Hệ Thống/LitRPG · Ngôn Tình · Kiếm Hiệp · Thriller · Sci-Fi · Kinh Dị

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/anti-ai-humanization.md`
- `Context-Layer/CoreModules/emotional-writing-vn.md`
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/style/storytelling.md` — show don't tell rules
- `Ban/style/rhythm.md` — burstiness patterns
- `Ban/style/narrative.md` — POV/timeline rules
- `Ban/quality/anti-ai.md` — 25 AI tells blacklist
