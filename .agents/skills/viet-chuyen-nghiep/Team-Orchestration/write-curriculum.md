# Pipeline: Viết Giáo Trình (write-curriculum) — v3.1

## Khi nào kích hoạt
- User yêu cầu viết giáo trình, khóa học, training manual
- User yêu cầu viết slide đào tạo, workshop content, module học
- Tín hiệu: "viết giáo trình", "viết khóa học", "training manual", "thiết kế module",
  "viết tài liệu đào tạo", "slide bài giảng", "curriculum", "course design"

## Pipeline

```
content/ (deep) → style/ (curriculum + technical) → quality/ → platform/ (docs) → Output
   │                         │                          │              │
   │                         │                          │              └─ Format tài liệu
   │                         │                          └─ Quality + fact-check
   │                         └─ Curriculum design + technical editing
   └─ Deep research + learning needs analysis
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — Deep Mode
1. `lead-content.md` nhận brief → xác định:
   - Đối tượng học viên (background, level hiện tại)
   - Mục tiêu đào tạo (sau khóa học làm được gì?)
   - Thời lượng và format (online/offline/hybrid)
   - Kiến thức tiên quyết
2. `research.md` thu thập:
   - Best practices trong domain
   - Benchmark từ khóa học tương tự
   - Case studies và ví dụ thực tế
3. `analysis.md` đề xuất:
   - Learning path (chuỗi module)
   - Bloom's Taxonomy mapping cho mỗi module
   - Assessment strategy
4. Output: **Curriculum Blueprint YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến 2 BTV:
   - `curriculum.md` — thiết kế cấu trúc module, exercises, assessment
   - `technical.md` — biên tập thuật ngữ, số liệu, citation
2. BTV Curriculum xử lý:
   - Module structure theo template chuẩn
   - Learning objectives theo Bloom's
   - Bài tập: guided → independent → capstone
   - Progression logic: module bridge, prerequisite check
3. Output: **Giáo trình Draft** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - fact-check (claims, số liệu, case studies)
   - consistency (thuật ngữ, xưng hô, level progression)
   - natural (ngôn ngữ giáo dục, không hàn lâm) 
   - anti-ai (đặc biệt cho tài liệu đào tạo — phải có personality)
2. Bonus check: **Bloom alignment** (objectives match content?)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. BTV Tài Liệu format:
   - PDF/DOCX: cover, ToC, module structure, page breaks
   - Slide: speaker notes, visual hierarchy
   - Notion/Web: interactive exercises, embedded quiz
3. Output: **Giáo trình sẵn sàng xuất bản**

## Multi-Module Mode
Khi giáo trình có nhiều module:
1. Thiết kế master outline + learning path
2. Viết từng module theo pipeline riêng
3. Module cuối: capstone project design
4. Cross-module consistency check
5. Output: full curriculum package

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/curriculum-framework.md`
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/style/curriculum.md` — editorial rules
- `Ban/style/technical.md` — technical editing
- `Ban/platform/docs.md` — document formatting
- `Workers/curriculum-worker.md` — execution frameworks (ADDIE, Bloom verbs, module templates) ★
