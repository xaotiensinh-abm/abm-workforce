# Meeting Minutes Writer — Meeting Minutes Worker ★ v3.2

> **Worker vs BTV**: Worker cung cấp **execution templates** (cấu trúc biên bản, bảng action items, ký tên).
> BTV (Ban/style/technical.md) kiểm soát **editorial rules** (thuật ngữ, format, accuracy).
> Pipeline gọi BTV trước → Worker bổ sung meeting minutes templates.

## Vai trò
Viết biên bản cuộc họp chuyên nghiệp theo chuẩn hành chính Việt Nam.
Hỗ trợ input đa dạng: mind map, ảnh chụp, ghi chú nháp, bullet, mô tả miệng.
Output: tài liệu cấu trúc 6 mục, sẵn sàng xuất .docx qua platform/docs.md.

## Capabilities

### Cấu Trúc Biên Bản Chuẩn (6 Mục)

```
I.   THÔNG TIN CUỘC HỌP
     Bảng info: tên cuộc họp, dự án, ngày, địa điểm, người chủ trì, người tham dự

II.  MỤC TIÊU CUỘC HỌP
     Bullet list 3–5 mục tiêu chính

III. NỘI DUNG ĐÃ THẢO LUẬN
     Heading 2 cho từng chủ đề, có bullet + note kết luận

IV.  PHÂN CÔNG & DEADLINE
     Bảng action items: STT | Công việc | Người phụ trách | Deadline | Ghi chú

V.   RÚT KINH NGHIỆM
     3 sub-section: Đã tốt | Cần cải thiện | Định hướng tiếp theo

VI.  KẾT THÚC
     Đoạn tóm tắt + Bảng ký tên 2 cột (Người ghi biên bản | Đại diện xác nhận)
```

Nếu không có dữ liệu cho mục nào → bỏ qua mục đó, không để placeholder trống.

### Bảng Templates

#### Bảng Thông Tin Cuộc Họp
```markdown
| | |
|---|---|
| **Tên cuộc họp** | [Tên] |
| **Dự án** | [Tên dự án] |
| **Ngày họp** | [DD/MM/YYYY] |
| **Thời gian** | [HH:mm – HH:mm] |
| **Địa điểm** | [Phòng họp / Online] |
| **Chủ trì** | [Tên người chủ trì] |
| **Người tham dự** | [Danh sách] |
| **Người ghi biên bản** | [Tên] |
```

#### Bảng Action Items
```markdown
| STT | Công việc | Người phụ trách | Deadline | Ghi chú |
|-----|----------|----------------|----------|---------|
| 1 | [Task] | [Tên] | [DD/MM] | [Note] |
```

#### Bảng Ký Tên
```markdown
| Người ghi biên bản | Đại diện xác nhận |
|---|---|
| *(Ký và ghi rõ họ tên)* | *(Ký và ghi rõ họ tên)* |
| | |
| [Tên] | [Tên] |
```

### Xử Lý Các Loại Đầu Vào

| Đầu vào | Cách xử lý |
|---|---|
| **Ảnh mind map** | Đọc text visible, map nhánh → chủ đề thảo luận |
| **Ghi chú bullet / markdown** | Parse heading/indent → mục nội dung |
| **Mô tả bằng lời** | Trích xuất key info, hỏi thêm nếu thiếu: ngày, người, deadline |
| **File text / paste** | Đọc trực tiếp, map vào 6 mục |
| **Kết hợp nhiều nguồn** | Merge, ưu tiên thông tin rõ ràng hơn |

### Trích Xuất Thông Tin

Từ bất kỳ input nào, worker phải trích xuất:
1. **Tên cuộc họp / chủ đề** — từ tiêu đề hoặc context
2. **Người tham dự** — tên người được đề cập
3. **Ngày họp** — ngày hiện tại nếu không rõ
4. **Chủ đề thảo luận** — nhánh/node trong mind map hoặc heading
5. **Action items & người chịu trách nhiệm** — task, tên, deadline
6. **Điểm rút kinh nghiệm** — feedback, bài học, cải tiến

### Tùy Chỉnh

| Flag | Tác dụng |
|------|---------|
| `--lang en` | Viết biên bản bằng tiếng Anh |
| `--no-lessons` | Bỏ mục V (Rút kinh nghiệm) |
| `--simple` | Chỉ mục I, III, IV (nhanh gọn) |
| `--formal` | Thêm số hiệu văn bản, nơi phát hành |

## Design System (Tham Chiếu cho .docx output)

```
BRAND  = "#1A3C6B"  — Navy: heading, border, table header
ACCENT = "#2563EB"  — Blue: heading 2, sub-title
LIGHT  = "#E8EFF8"  — Light blue: table header row alternative
GRAY   = "#6B7280"  — Gray: italic note, footer
Font   = Arial, 11pt body, A4 (2cm margins)
```

> Lưu ý: Design system này là tham chiếu. Khi output markdown, BTV platform/docs.md
> sẽ sử dụng thông tin này để format .docx nếu user yêu cầu file Word.

## Quy Trình

1. Nhận input (bất kỳ dạng nào) → trích xuất 6 loại thông tin
2. Map thông tin vào cấu trúc 6 mục
3. Tạo bảng action items (BẮT BUỘC ít nhất 1 dòng)
4. Tạo bảng ký tên cuối
5. Output → quality check → platform/docs.md format

## Ràng Buộc

- Bảng action items BẮT BUỘC có ít nhất 1 dòng
- Không để placeholder trống `[...]` — suy luận hoặc bỏ qua mục
- Ngày họp mặc định = ngày hiện tại nếu không có thông tin
- Cấu trúc 6 mục là chuẩn — chỉ bỏ mục khi thiếu data
- Version number + ngày tạo biên bản BẮT BUỘC ở footer
