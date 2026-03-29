# Pipeline: Phản Biện Nội Dung (critique-content) — v3.0

## Khi nào kích hoạt
- User muốn phản biện, đánh giá logic, kiểm chứng claims

## Pipeline

```
content/ → quality/ (critique mode) → Output
   │            │
   │            ├─ fact-check.md (kiểm chứng)
   │            ├─ consistency.md (mâu thuẫn)
   │            └─ natural.md (liệu có bias?)
   └─ Research xác minh claims
```

## Bước chi tiết

### 1. Ban Thu Thập (content/)
1. `lead-content.md` đọc bài cần phản biện
2. `research.md` tìm nguồn đối chiếu, số liệu xác minh
3. Output: **Dữ kiện đối chiếu** + danh sách claims cần verify

### 2. Ban Kiểm Duyệt (quality/) — CHẾ ĐỘ PHẢN BIỆN
1. `fact-check.md` — xác minh từng claim, ghi kết quả
2. `consistency.md` — phát hiện mâu thuẫn nội bộ
3. `natural.md` — kiểm tra bias, one-sided argument
4. Output: **Báo cáo phản biện** gồm:
   - Claims đúng / sai / chưa verify
   - Logical fallacies (nếu có)
   - Counter-arguments
   - Đề xuất cải thiện luận điểm
