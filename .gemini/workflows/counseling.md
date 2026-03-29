---
description: Giao việc tư vấn tâm lý học đường cho Jarvis — sàng lọc, tư vấn, can thiệp khủng hoảng, giáo dục kỹ năng sống, phòng chống bắt nạt
---

# 🧠 Workflow Tư Vấn Tâm Lý Học Đường

Agent: `school-psychologist`

## Bước 1: Xác định yêu cầu
Hỏi CEO/user:
- Đối tượng: Học sinh / Phụ huynh / Giáo viên / Toàn trường?
- Cấp học: Tiểu học (1-5) / THCS (6-9) / THPT (10-12)?
- Loại yêu cầu: Sàng lọc / Tư vấn / Can thiệp khủng hoảng / Giáo dục tâm lý / Phòng chống bắt nạt / Kế hoạch can thiệp?

## Bước 2: Đánh giá rủi ro nhanh
⚠️ **BẮT BUỘC** — Trước khi làm bất cứ gì:
- Có dấu hiệu tự hại/tự tử không?
- Có nguy hiểm vật lý ngay lập tức không?
- Nếu CÓ → **Chuyển ngay sang skill `crisis-intervention`**

## Bước 3: Phân loại & chọn skill
| Yêu cầu | Skill | Output |
|----------|-------|--------|
| Sàng lọc tâm lý | `mental-health-screening` | Báo cáo sàng lọc |
| Tư vấn học sinh | `student-counseling` | Ghi chú tư vấn |
| Khủng hoảng | `crisis-intervention` | Kế hoạch an toàn |
| Giáo dục kỹ năng sống | `psychoeducation` | Kế hoạch bài giảng |
| Hướng dẫn PH/GV | `parent-teacher-guidance` | Thư/Phiếu hướng dẫn |
| Kế hoạch can thiệp | `iep-mental-health` | Hồ sơ IEP |
| Phòng chống bắt nạt | `anti-bullying` | Kế hoạch phòng ngừa |

## Bước 4: Thực hiện
1. Load skill tương ứng (max 3 cùng lúc)
2. Follow instructions trong skill
3. Tạo output theo template

## Bước 5: Output & theo dõi
1. Lưu output vào `_abm-output/school-psychology/`
2. Ghi attestation
3. Đề xuất bước tiếp theo
4. Lên lịch theo dõi nếu cần

## Hotline tham khảo
- Bảo vệ trẻ em: **111**
- Sức khỏe tâm thần: **1800 599 920**
- Tư vấn tâm lý: **1800 599 199**
