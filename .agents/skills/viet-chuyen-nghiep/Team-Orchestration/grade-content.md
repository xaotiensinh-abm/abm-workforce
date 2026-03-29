# Pipeline: Chấm Bài (grade-content) — v3.0

## Khi nào kích hoạt
- User gửi bài viết → muốn đánh giá, chấm điểm thang 100

## Pipeline

```
content/ (light) → quality/ (rubric mode) → Output
     │                    │
     │                    └─ Rubric 100 điểm + nhận xét
     └─ Đọc bài + xác định context
```

## Bước chi tiết

### 1. Ban Thu Thập (content/) — CHẾ ĐỘ NHẸ
1. `lead-content.md` đọc bài cần chấm
2. Xác định: loại bài, audience, mục đích
3. `research.md` nhanh: check facts/claims nếu cần
4. Output: **Brief đánh giá** (loại bài, context)

### 2. Ban Kiểm Duyệt (quality/) — CHẾ ĐỘ RUBRIC
1. Chạy 6 kiểm tra vẫn bình thường
2. **Thêm:** Chấm theo rubric 100 điểm (`Context-Layer/CoreModules/rubric-100.md`)
3. Output: **Báo cáo điểm** từng tiêu chí + nhận xét + đề xuất cải thiện

## Rubric 100 điểm (tham chiếu)

| Tiêu chí | Trọng số |
|----------|---------|
| Nội dung & độ sâu | 25 |
| Cấu trúc & logic | 20 |
| Phong cách & văn phong | 20 |
| Chính xác & chính tả | 15 |
| Anti-AI & tự nhiên | 10 |
| Format & trình bày | 10 |
| **Tổng** | **100** |
