---
description: Quy trình phát triển sản phẩm tích hợp Marketing — Dev + MKT song song
---
// turbo-all

## Workflow: /product-launch — Dev + Marketing Song Song

1. Đọc thông tin sản phẩm từ CEO
2. Xác định giai đoạn hiện tại:

### Pipeline

| Giai đoạn Dev | Marketing song song | Skills |
|--------------|--------------------|----|
| **PRD** | Market sizing + competitive analysis | `market-sizing-analysis`, `competitive-landscape` |
| **Design** | Landing page draft + brand positioning | `frontend-design`, `product-marketing-context` |
| **MVP** | Beta content + early adopter outreach | `content-strategy`, `cold-email` |
| **Release** | Launch campaign + pricing | `launch-strategy`, `pricing-strategy`, `email-marketing` |
| **Post-launch** | Growth marketing + churn prevention | `seo-content-planner`, `churn-prevention`, `ab-test-setup` |

3. Tại mỗi giai đoạn → tạo hợp đồng cho cả Dev worker VÀ Marketing worker
4. Sprint review → marketing-specialist tham gia đóng góp
5. `/council` đánh giá readiness trước khi chuyển giai đoạn
6. ⚠️ Marketing KHÔNG được publish ra ngoài trước khi CEO duyệt
7. Output: Marketing assets song song với product — sẵn sàng launch ngay khi dev xong
