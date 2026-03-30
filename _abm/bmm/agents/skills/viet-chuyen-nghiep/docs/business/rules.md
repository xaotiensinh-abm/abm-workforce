# Business Rules — Viết Chuyên Nghiệp v3.0

## Quy tắc Pipeline

| # | Rule | Enforcement |
|---|------|-------------|
| 1 | Luôn research trước viết | Pipeline `write-new` bắt buộc bước content/ |
| 2 | Brief mơ hồ → hỏi lại | 3+ unknowns = BLOCK, escalate hỏi user |
| 3 | Mọi output qua quality gate | `Ban/quality/` 6 kiểm tra song song |
| 4 | Anti-AI audit bắt buộc | Score > 60% = CRITICAL → rewrite |
| 5 | REVISE tối đa 2 vòng | Quá 2 → REJECT → escalate Tổng BT |
| 6 | Claims phải có nguồn | fact-check.md: 5 tier, tier-1/2 ưu tiên |

## Quy tắc Viết Hoa Tiếng Việt

| Loại | Ví dụ |
|------|-------|
| Đầu câu | `Hà Nội là thủ đô.` |
| Tên riêng người | `Nguyễn Văn An` (viết hoa chữ cái đầu mỗi tiếng) |
| Địa danh | `Thành phố Hồ Chí Minh`, `Đà Nẵng` |
| Tổ chức | `Bộ Giáo dục và Đào tạo` (viết hoa tiếng đầu) |
| Tiêu đề | `Hướng dẫn sử dụng hệ thống` (viết hoa chữ cái đầu) |
| Thuật ngữ nước ngoài giữ nguyên | `AI`, `CEO`, `Google Workspace` |

## Quy tắc Dấu Câu Tiếng Việt

- Dấu phẩy, chấm, chấm hỏi: **không** có khoảng trắng trước, **có** sau
- Ngoặc kép `""` cho trích dẫn, ngoặc đơn `()` cho bổ sung
- Dấu gạch ngang `—` (em dash): có khoảng trắng 2 bên
- Không dùng Oxford comma trong tiếng Việt

## Quy tắc Anti-AI

| Grade | Score | Hành động |
|-------|-------|----------|
| A | ≤ 20% | PASS |
| B | 21-40% | PASS (khuyến nghị cải thiện) |
| C | 41-60% | REVISE bắt buộc |
| D | 61-80% | REJECT → rewrite |
| F | > 80% | CRITICAL → escalate |

## Quy tắc Chấm Bài

Rubric 100 điểm, 6 tiêu chí:
- Nội dung & độ sâu: 25 điểm
- Cấu trúc & logic: 20 điểm
- Phong cách viết: 20 điểm
- Chính xác thông tin: 15 điểm
- Anti-AI: 10 điểm
- Format & trình bày: 10 điểm

## Quy tắc Platform

| Platform | Max length | CTA | Hashtags |
|----------|-----------|-----|----------|
| Facebook | 63,206 ký tự | Cuối bài | 3-5 |
| TikTok | 2,200 ký tự | Trong 3s đầu | 3-5 trending |
| LinkedIn | 3,000 ký tự | Cuối bài | 3-5 B2B |
| Video (short) | 60s script | Hook đầu | N/A |
