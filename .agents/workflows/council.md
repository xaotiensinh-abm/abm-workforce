---
description: Lập hội đồng đánh giá sau planning — multi-agent consolidate + ranking
---
// turbo-all

## Workflow: /council — Hội Đồng Đánh Giá

1. Đọc file `.agents/workflows/jarvis.md` để hiểu quy trình Jarvis
2. Xác định context: đang đánh giá cái gì? (plan, architecture, skill gap, PRD...)
3. Jarvis triệu tập **Hội đồng 3-5 agents** liên quan:
   - Architect → đánh giá kiến trúc
   - Pragmatist → đánh giá tính khả thi
   - Hacker → tìm lỗ hổng
   - CEO → đánh giá ROI/business value
   - Creative → đề xuất alternatives
4. Mỗi agent đánh giá **độc lập** theo scoring rubric:
   - Chấm 1-10 theo criteria riêng
   - Liệt kê gaps (thiếu skill/workflow/agent nào)
   - Đề xuất bổ sung
5. Jarvis **consolidate** kết quả:
   - Tổng hợp scores → weighted average
   - Cross-reference gaps → ưu tiên
   - Ranking đề xuất → CEO quyết định
6. Load template scoring: `_abm/Context-Layer/Second-Brain/standards/council-scoring.yaml`
7. Output: Bảng đánh giá + Gap list + Action plan
8. ⚠️ CEO quyết định cuối cùng — hội đồng chỉ tư vấn
