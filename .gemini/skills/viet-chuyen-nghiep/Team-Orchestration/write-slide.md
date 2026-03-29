# Pipeline: Tạo Slide Thuyết Trình (write-slide) — v3.2

## Khi nào kích hoạt
- User yêu cầu tạo slide, presentation, bài thuyết trình
- Tín hiệu: "tạo slide", "làm PowerPoint", "soạn presentation", "bài thuyết trình",
  "keynote", "slide deck", "pitch deck", "tạo bài giảng slide"

## Pipeline

```
content/ → style/ (presentation) → slide-worker → quality/ → platform/ (docs) → Output
   │              │                      │              │              │
   │              │                      │              │              └─ Format slide
   │              │                      │              └─ Quality + readability
   │              │                      └─ Storyboard + speaker notes
   │              └─ Visual hierarchy + tone
   └─ Audience analysis + key message research
```

## Bước chi tiết

### 1. Ban Thu Thập (content/)
1. `lead-content.md` nhận brief → xác định:
   - Audience (ai sẽ xem slide?)
   - Thời lượng presentation (→ tính số slide)
   - Key message / thesis (1 câu)
   - Call-to-action (muốn audience làm gì sau?)
   - Context: meeting, conference, workshop, class?
2. `research.md` thu thập:
   - Data points, statistics, quotes để minh hoạ
   - Benchmark slide từ domain tương tự
3. Output: **Slide Brief YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến `presentation.md`
2. **slide-worker.md** bổ sung execution framework:
   - Tính số slide theo thời lượng
   - Thiết kế narrative arc (Hook → Problem → Solution → Evidence → Action)
   - Viết content per slide + speaker notes
   - Gợi ý visual layout cho mỗi slide
3. Rules:
   - ≤7 từ per title
   - ≤6 bullets per slide, mỗi bullet ≤10 từ
   - Speaker notes = what to SAY (50-100 từ)
   - Mỗi 3-4 slides = 1 visual break
4. Output: **Slide Deck Outline** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - consistency (thuật ngữ, tone xuyên suốt)
   - fact-check (data points, quotes)
   - natural (speaker notes phải đọc tự nhiên)
   - anti-ai (speaker notes phải có personality)
2. Bonus check: **Slide density** (quá nhiều text per slide?)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. Format:
   - Markdown slide outline (default)
   - PowerPoint-ready structure (title + bullets + notes per slide)
   - Notion/Google Slides: copy-paste ready

## Slide Count Guide
| Thời lượng | Số slide | Ghi chú |
|-----------|---------|---------|
| 5-10 phút | 8-12 | Pitch, lightning talk |
| 15-20 phút | 15-20 | Conference talk |
| 30-45 phút | 25-35 | Lecture, workshop |
| 60+ phút | 35-50+ | Workshop + activity slides |

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/style/presentation.md` — visual hierarchy rules
- `Ban/platform/docs.md` — document formatting
- `Workers/slide-worker.md` — narrative arc, templates, visual rules ★
