---
description: Quy trình bán hàng đa tác nhân theo DISC
---

# Hệ Thống Bán Hàng Đa Tác Nhân Theo DISC

Phân tích khách hàng theo DISC và tạo kế hoạch bán khóa học AI giá cao của ABM.

---

## Khởi động

Khi user gọi `/disc-sales`, hỏi:
- **Thông tin khách hàng**: Tên, chức vụ, công ty, ngành nghề
- **Nguồn tiếp cận**: LinkedIn, Zalo, giới thiệu, sự kiện
- **Dữ liệu DISC** (nếu có): Kết quả khảo sát hoặc quan sát hành vi

---

## Kiến Trúc 7 Tác Nhân

| Tác nhân | Vai trò | Output |
|----------|---------|--------|
| survey_builder | Xây dựng khảo sát | Bộ câu hỏi DISC |
| high_ticket_designer | Thiết kế sản phẩm giá cao | Đề xuất sản phẩm |
| disc_profiler | Phân tích DISC | Hồ sơ DISC chi tiết |
| customer_insight | Phân tích nhu cầu | Insight khách hàng |
| touchpoint_planner | Lập kế hoạch 7 điểm chạm | Lịch trình tiếp cận |
| sales_strategist | Chiến lược bán hàng | Thẻ chiến thuật |
| content_generator | Tạo nội dung | Mẫu thư, kịch bản |

---

## Workflow

### Step 1: Thu thập & Phân tích
- Chạy song song: `disc_profiler` + `customer_insight`
- Output: Hồ sơ DISC + Nhu cầu khách hàng

### Step 2: Lập Kế Hoạch
- `touchpoint_planner` tạo lịch trình 7 điểm chạm
- Kết hợp DISC profile để cá nhân hóa

### Step 3: Chiến Lược
- `sales_strategist` tạo thẻ chiến thuật bán hàng
- Xử lý phản đối theo nhóm DISC

### Step 4: Nội Dung
- `content_generator` tạo mẫu thư, kịch bản Zalo, kịch bản gọi điện

---

## Ma Trận DISC

| Nhóm | Từ khóa | Cách tiếp cận | Nên tránh |
|------|---------|---------------|-----------|
| **D** | Kết quả, Nhanh, Kiểm soát | Trực tiếp, Ngắn gọn, Lợi nhuận | Nói chuyện phiếm, Chi tiết |
| **I** | Vui vẻ, Mạng lưới, Câu chuyện | Ấm áp, Bằng chứng xã hội | Nặng dữ liệu, Trang trọng |
| **S** | Ổn định, Hỗ trợ, Đội nhóm | Kiên nhẫn, Trấn an | Áp lực, Vội vàng |
| **C** | Dữ liệu, Chất lượng, Logic | Chi tiết, Chính xác | Mơ hồ, Cảm xúc |

---

## Sản Phẩm ABM

| Sản phẩm | Giá | Đối tượng |
|----------|-----|-----------|
| Coaching nhóm 10 người | 25 triệu/người | Giám đốc, Nhà sáng lập |
| Câu lạc bộ VIP 6 người | 50 triệu/người | Giám đốc cấp cao |
| Coaching 1-1 cấp điều hành | 100 triệu/3 tháng | Giám đốc cấp cao |
| Đào tạo doanh nghiệp | 150-500 triệu | Doanh nghiệp vừa và nhỏ |

---

## Checklist Đầu Ra

- [ ] Hồ sơ DISC với phần trăm chi tiết
- [ ] Đề xuất sản phẩm với lý do
- [ ] Lịch trình 7 điểm chạm với ngày cụ thể
- [ ] Thẻ chiến thuật bán hàng hoàn chỉnh
- [ ] Mẫu thư (ít nhất 3)
- [ ] Kịch bản Zalo (mở đầu + theo dõi)
- [ ] Kịch bản gọi điện (mở đầu + chốt)
- [ ] Xử lý phản đối cho 4 phản đối phổ biến

---

## Full Skill Reference

Xem chi tiết agents tại:
- [README.md](file:///D:/Antigravity/.agent/skills/abm-sales-agents/abm-sales-agents/README.md)
