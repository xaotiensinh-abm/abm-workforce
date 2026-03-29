# Bộ Phân loại Tác vụ Tự động

## Mục đích

Engine phân loại **yêu cầu người dùng** thành task type + complexity level,
quyết định pipeline nào sẽ được kích hoạt.

## Ma trận Phân loại

```
User Request
    │
    ├─ Có keyword viết mới? ──→ "write-new"
    │   ├─ ebook/sách/tài liệu/handbook ──→ longform pipeline
    │   ├─ social/Facebook/Threads/LinkedIn ──→ social pipeline
    │   └─ video/script/kịch bản ──→ video pipeline
    │
    ├─ Có keyword sửa? ──→ "edit-draft"
    │   └─ sửa/edit/rewrite/refine/polish
    │
    ├─ Có keyword chấm? ──→ "grade-content"
    │   └─ chấm/đánh giá/grade/score/thang 100
    │
    ├─ Có keyword phản biện? ──→ "critique-content"
    │   └─ phản biện/critique/review/chỉ lỗi/phân tích
    │
    ├─ Có keyword research thuần? ──→ "deep-research"
    │   └─ nghiên cứu/research/tìm hiểu/phân tích thị trường
    │
    └─ Có keyword xuất bản? ──→ "publish-ready"
        └─ xuất bản/publish/finalize/kiểm duyệt cuối
```

## Chấm điểm Độ phức tạp

| Factor | Score 1 | Score 2 | Score 3 |
|--------|---------|---------|---------|
| **Output length** | < 500 từ | 500-3000 | > 3000 |
| **Platforms** | 1 | 2-3 | 4+ |
| **Research depth** | Surface | Standard | Deep |
| **Domain risk** | None | Low-Medium | High |
| **Multi-output** | Single | 2-3 outputs | 4+ |

**Total (5-15):**
- 5-7 = **Light** → fast-track, skip optional steps
- 8-11 = **Standard** → full pipeline
- 12-15 = **Heavy** → full pipeline + extra review rounds

## Định dạng đầu ra

```yaml
classification:
  task_type: "[write-new/edit-draft/grade-content/critique-content/deep-research/publish-ready]"
  pipeline: "[pipeline name]"
  content_type: "[ebook/document/social/video/etc]"
  complexity: "[light/standard/heavy]"
  complexity_score: [5-15]
  workers_needed: ["intake", "research", "..."]
  estimated_output: "[mô tả output dự kiến]"
```

## Trường hợp đặc biệt

- User nói "viết rồi chấm" → 2 pipelines tuần tự: write-new → grade-content
- User nói "sửa bài rồi xuất bản" → edit-draft → publish-ready
- Ambiguous → hỏi user xác nhận trước khi chạy
