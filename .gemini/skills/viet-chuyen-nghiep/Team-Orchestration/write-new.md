# Pipeline: Viết Mới (write-new) — v3.0

## Khi nào kích hoạt
- User yêu cầu viết ebook, tài liệu, handbook, content social, kịch bản video

## Pipeline

```
content/ → style/ → quality/ → platform/ → Output
   │         │         │          │
   │         │         │          └─ Tối ưu cho nền tảng
   │         │         └─ 6 kiểm tra → PASS/REVISE/REJECT
   │         └─ 6 BTV biên tập phong cách
   └─ Nghiên cứu + phân tích + bóc brief
```

## Bước chi tiết

### 1. Ban Thu Thập (content/)
1. `lead-content.md` nhận brief → phân loại task
2. `research.md` thu thập nguồn 5 lớp, cross-verify
3. `analysis.md` phân tích audience, chọn angle, đề xuất outline
4. Output: **Gói nguyên liệu** (YAML) → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` đánh giá nhanh bản thảo → phân công BTV
2. BTV chuyên biệt biên tập: storytelling, rhythm, narrative, presentation, technical
3. Output: **Bản thảo đã biên tập** → chuyển Ban Kiểm Duyệt

### 3. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy 6 kiểm tra song song:
   - punctuation, capitalization, natural, anti-ai, fact-check, consistency
2. Quyết định:
   - **PASS** → chuyển Ban Xuất Bản
   - **REVISE** → trả Ban Biên Tập + ghi chú (tối đa 2 vòng)
   - **REJECT** → trả Ban Thu Thập (nghiên cứu lại)

### 4. Ban Xuất Bản (platform/)
1. `lead-platform.md` xác định platform mục tiêu
2. BTV platform tương ứng tối ưu (facebook, tiktok, linkedin, video)
3. Output: **Content sẵn sàng publish**

## Tham chiếu Knowledge
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
- `Context-Layer/CoreModules/anti-ai-global.md`
- `Context-Layer/CoreModules/chinh-ta-viet-hoa.md`
