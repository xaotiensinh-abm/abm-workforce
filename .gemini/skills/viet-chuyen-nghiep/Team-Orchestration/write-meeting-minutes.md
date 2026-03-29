# Pipeline: Viết Biên Bản Cuộc Họp (write-meeting-minutes) — v3.2 ★

## Khi nào kích hoạt
- User yêu cầu viết biên bản cuộc họp, meeting minutes
- User gửi mind map, ảnh chụp, ghi chú nháp cuộc họp
- Tín hiệu: "biên bản họp", "meeting minutes", "ghi chú họp", "tóm tắt cuộc họp",
  "viết biên bản", "tạo meeting minutes", "ghi lại nội dung cuộc họp",
  "làm biên bản từ mind map / ảnh / ghi chú"

## Pipeline

```
content/ → style/ (technical + presentation) → meeting-minutes-worker
→ quality/ → platform/ (docs, format: docx) → Output
   │                    │                          │              │
   │                    │                          │              └─ .docx / markdown
   │                    │                          └─ Accuracy + completeness
   │                    └─ Technical writing + visual hierarchy
   └─ Trích xuất info từ input đa dạng
```

## Bước chi tiết

### 1. Ban Thu Thập (content/)
1. `lead-content.md` nhận input → phân loại đầu vào:
   - Loại input: mind map, ảnh, ghi chú, bullet, mô tả miệng, file text, kết hợp
   - Xác định: cuộc họp gì, dự án nào, bao nhiêu người
2. `research.md` (light) — không cần deep research, chỉ trích xuất:
   - Tên cuộc họp / chủ đề
   - Người tham dự (danh sách)
   - Ngày họp (mặc định = ngày hiện tại)
   - Các chủ đề thảo luận
   - Action items & người chịu trách nhiệm
   - Điểm rút kinh nghiệm (nếu có)
3. `analysis.md` đề xuất:
   - Cấu trúc mục nào cần giữ / bỏ (dựa trên data có sẵn)
   - Ưu tiên thông tin: action items > nội dung thảo luận > mục tiêu
4. Output: **Meeting Brief YAML** → chuyển Ban Biên Tập

### 2. Ban Biên Tập (style/)
1. `lead-style.md` route đến 2 BTV:
   - `technical.md` — ngôn ngữ chính xác, rõ ràng, không mơ hồ
   - `presentation.md` — visual hierarchy, bảng, numbering
2. Kết hợp xử lý:
   - Bullet points rõ ràng, mỗi point = 1 ý
   - Nội dung thảo luận: heading + bullet + kết luận
   - Action items: verbs mạnh ở đầu (Hoàn thành, Chuẩn bị, Gửi, Review...)
   - Tone: chính thức, khách quan, ngắn gọn
3. Output: **Meeting Draft** → chuyển meeting-minutes-worker

### 3. Meeting Minutes Worker ★
1. `Workers/meeting-minutes-worker.md` đóng vai trò:
   - Map content vào cấu trúc 6 mục chuẩn hành chính VN
   - Tạo bảng thông tin cuộc họp
   - Tạo bảng action items (BẮT BUỘC ≥ 1 dòng)
   - Tạo phần rút kinh nghiệm (3 sub-section)
   - Tạo bảng ký tên cuối
   - Xử lý flags: `--simple`, `--no-lessons`, `--lang en`, `--formal`
2. Output: **Structured Meeting Minutes** → chuyển Ban Kiểm Duyệt

### 4. Ban Kiểm Duyệt (quality/)
1. `lead-quality.md` chạy kiểm tra:
   - `consistency.md` — tên người nhất quán, ngày tháng đúng format
   - `natural.md` — ngôn ngữ rõ ràng, không mơ hồ
   - `punctuation.md` — dấu câu chuẩn
   - `fact-check.md` — action items có đủ: việc + người + deadline
2. Bonus check: **Completeness**
   - Có ít nhất 1 action item
   - Mọi người được đề cập đều có trong danh sách tham dự
   - Deadline hợp lệ (không quá khứ)
3. PASS → Ban Xuất Bản | REVISE → Ban Biên Tập

### 5. Ban Xuất Bản (platform/)
1. `lead-platform.md` route đến `docs.md`
2. BTV Tài Liệu format:
   - Cấu trúc heading I → VI
   - Bảng info, bảng action items, bảng ký tên đúng format
   - Footer: ngày tạo + phiên bản
   - Design system: Navy/Blue, Arial, A4 (tham chiếu từ worker)
3. Output format:
   - **Mặc định:** Markdown có bảng (sẵn copy-paste)
   - **Nếu user yêu cầu .docx:** Hướng dẫn xuất Word theo design system

## Tùy Chỉnh

| Flag | Hành vi |
|------|---------|
| `--simple` | Chỉ mục I, III, IV — nhanh gọn |
| `--no-lessons` | Bỏ mục V (Rút kinh nghiệm) |
| `--lang en` | Biên bản tiếng Anh |
| `--formal` | Thêm số hiệu văn bản, nơi phát hành |

## Tham chiếu Knowledge
- `Workers/meeting-minutes-worker.md` — execution templates (6 mục, bảng, ký tên) ★
- `Ban/style/technical.md` — technical editing
- `Ban/style/presentation.md` — visual structure
- `Ban/platform/docs.md` — document formatting (.docx)
- `Context-Layer/CoreModules/tone-of-voice-guide.md`
