---
name: "competitor-intelligence"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Thu thập thông tin đối thủ — phân tích chiến lược, nội dung, giá cả, quảng cáo, và định vị thị trường qua nhiều kênh (web, social, review)."
---

# Thu Thập Thông Tin Đối Thủ (Competitor Intelligence)

Phân tích chiến lược, nội dung, giá cả, quảng cáo, và định vị thị trường của đối thủ trên nhiều kênh.

## Sử dụng skill này khi

- Cần thu thập dữ liệu chi tiết về đối thủ cạnh tranh
- Phân tích chiến lược marketing/content của đối thủ
- So sánh pricing và positioning trên nhiều platform
- Theo dõi hoạt động quảng cáo và social media đối thủ
- Chuẩn bị competitive intelligence report

## KHÔNG sử dụng khi

- Cần **framework phân tích chiến lược** (Porter's, SWOT, positioning) → dùng `competitive-landscape`
- Cần phân tích nội bộ startup → dùng `startup-analyst`

## ⚡ Phân Biệt Với competitive-landscape

| | competitor-intelligence | competitive-landscape |
|---|---|---|
| **Vai trò** | Thu thập & báo cáo dữ liệu thực | Framework & chiến lược |
| **Focus** | Web research, digital presence, pricing data | Porter's 5 Forces, SWOT, positioning map |
| **Khi dùng** | "Tìm hiểu đối thủ X đang làm gì" | "Phân tích chiến lược cạnh tranh" |
| **Thứ tự** | Chạy TRƯỚC → cung cấp dữ liệu | Chạy SAU → phân tích dữ liệu |

## Loại Phân Tích

### 1. Phân tích Digital Presence
- Website: traffic ước lượng, tech stack, UX/UI
- SEO: từ khóa xếp hạng, backlink profile, content strategy
- Social media: follower count, engagement rate, posting frequency
- Review & ratings: Google, App Store, G2, Capterra

### 2. Phân tích Pricing & Positioning
- So sánh pricing tiers
- Feature matrix (tính năng theo tier)
- Value proposition messaging
- Target audience positioning

### 3. Phân tích Content Strategy
- Loại nội dung đang publish (blog, video, podcast)
- Tần suất publish
- Chủ đề chính và secondary topics
- Lead magnets và content upgrades

### 4. Phân tích Sales & Marketing
- Kênh quảng cáo chính (Google Ads, Facebook, LinkedIn)
- Messaging và creative patterns
- Landing page structure
- Email marketing strategy (nếu subscribe được)

## Quy Trình Thu Thập

### Bước 1: Xác định đối thủ
- Đối thủ trực tiếp (cùng sản phẩm, cùng thị trường)
- Đối thủ gián tiếp (khác sản phẩm, cùng vấn đề)
- Đối thủ tiềm ẩn (có thể mở rộng vào thị trường)

### Bước 2: Thu thập dữ liệu qua web research
- Truy cập website và đọc pricing, features, about
- Tìm kiếm reviews trên G2, Capterra, TrustPilot
- Kiểm tra social media profiles
- Đọc blog/content marketing

### Bước 3: Phân tích và so sánh
- Tạo ma trận so sánh chi tiết
- Xác định điểm mạnh/yếu từng đối thủ
- Tìm patterns chung và khác biệt
- Xác định cơ hội chưa khai thác

### Bước 4: Tổng hợp báo cáo

## Output Format

```
# Báo Cáo Competitive Intelligence

## Tóm tắt (≤200 từ)

## Ma trận So sánh
| Tiêu chí | Chúng ta | Đối thủ A | Đối thủ B |
|----------|----------|-----------|-----------|

## Phân tích Chi tiết Từng Đối thủ
### [Đối thủ A]
- Positioning:
- Pricing:
- Điểm mạnh:
- Điểm yếu:
- Chiến lược content:
- Kênh marketing:

## Cơ hội & Đề xuất

## Hành động tiếp theo
```

## Lưu Ý
- Chỉ dùng dữ liệu công khai — KHÔNG truy cập trái phép
- Ghi rõ nguồn mọi dữ liệu thu thập
- Đánh dấu rõ: DỮ KIỆN vs. ƯỚC LƯỢNG

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) — `apify-competitor-intelligence` (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
- Lưu ý: Phiên bản gốc dùng Apify API. Phiên bản ABM sử dụng web research tích hợp của agent.
