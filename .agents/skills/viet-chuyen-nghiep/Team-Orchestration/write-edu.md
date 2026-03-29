# Pipeline: Viết Tài Liệu Học Tập (write-edu) — v3.2

## Khi nào kích hoạt
- User yêu cầu viết tài liệu học tập đơn lẻ (không phải full giáo trình)
- User yêu cầu tạo handout, workbook, quiz, lesson plan, case study
- Tín hiệu: "viết tài liệu học tập", "tạo handout", "làm workbook", "viết quiz",
  "soạn lesson plan", "viết case study", "tạo bài tập"

> **So với write-curriculum**: `write-curriculum` dùng cho toàn bộ khóa học (multi-module).
> `write-edu` dùng cho từng tài liệu đơn lẻ (handout, quiz, 1 lesson plan).

## Pipeline

```
content/ (deep) → style/ (curriculum) → quality/ → platform/ (docs) → Output
   │                    │                   │              │
   │                    │                   │              └─ Format tài liệu
   │                    │                   └─ Bloom alignment + fact-check
   │                    └─ Pedagogical design + engagement layer
   └─ Audience analysis + learning needs
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — Deep Mode
1. `lead-content.md` nhận brief → xác định:
   - Loại tài liệu (handout / workbook / quiz / lesson plan / case study)
   - Đối tượng học viên (level, background)
   - Learning objectives (1-3 objectives cụ thể)
   - Thời lượng hoặc độ dài mong muốn
2. `research.md` thu thập:
   - Best practices trong domain
   - Ví dụ thực tế bối cảnh VN
3. Output: **Edu Brief YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến `curriculum.md`
2. **edu-worker.md** bổ sung execution framework:
   - Bloom's Taxonomy mapping
   - Document type template
   - Engagement layer (exercises, quiz, mnemonics)
3. Rules:
   - CONCRETE FIRST: ví dụ trước → lý thuyết sau
   - Mỗi 500 từ = 1 điểm tương tác
   - VN CONTEXT: ví dụ BẮT BUỘC từ bối cảnh Việt Nam
4. Output: **Edu Draft** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - fact-check (claims, số liệu, citations)
   - natural (ngôn ngữ giáo dục, không hàn lâm quá)
   - anti-ai (burstiness, human fingerprint)
2. Bonus check: **Bloom alignment** (objectives match content?)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. Format theo document type:
   - Handout: 1-2 trang, visual summary
   - Workbook: step-by-step, answer key
   - Quiz: câu hỏi + rubric
   - Lesson Plan: template chuẩn

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/curriculum-framework.md`
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Ban/style/curriculum.md` — editorial rules
- `Ban/platform/docs.md` — document formatting
- `Workers/edu-worker.md` — execution frameworks (Bloom, templates) ★
- `Workers/curriculum-worker.md` — ADDIE framework (nếu cần full course context)
