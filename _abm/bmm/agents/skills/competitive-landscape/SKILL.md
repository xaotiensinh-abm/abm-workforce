---
name: "competitive-landscape"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Phân tích bối cảnh cạnh tranh — Porter's Five Forces, đánh giá đối thủ, xác định lợi thế khác biệt, chiến lược định vị thị trường."
---

# Phân Tích Bối Cảnh Cạnh Tranh

Framework toàn diện để phân tích cạnh tranh, xác định cơ hội khác biệt hóa, và phát triển chiến lược định vị thị trường.

## Sử dụng skill này khi

- User yêu cầu "phân tích đối thủ", "đánh giá cạnh tranh", "xác định khác biệt hóa"
- Cần đánh giá định vị thị trường hoặc áp dụng Porter's Five Forces
- Lập chiến lược cạnh tranh cho sản phẩm/dịch vụ
- So sánh sản phẩm với đối thủ

## KHÔNG sử dụng khi

- Task không liên quan đến phân tích cạnh tranh
- Cần **thu thập dữ liệu thực tế** về đối thủ (website, social, pricing cụ thể) → dùng `competitor-intelligence`
- Cần phân tích tài chính chi tiết → dùng `startup-analyst`
- Cần tính toán quy mô thị trường → dùng `market-sizing-analysis`

## ⚡ Phân Biệt Với competitor-intelligence

| | competitive-landscape | competitor-intelligence |
|---|---|---|
| **Vai trò** | Framework & chiến lược | Thu thập & báo cáo dữ liệu |
| **Input** | Thông tin đã có hoặc tổng quan | Web research trực tiếp |
| **Output** | Porter's 5 Forces, SWOT, positioning map | Ma trận so sánh chi tiết, data profiles |
| **Khi dùng** | Lập chiến lược, ra quyết định | Điều tra thực địa, thu thập bằng chứng |
| **Kết hợp** | Dùng SAU competitor-intelligence | Dùng TRƯỚC competitive-landscape |

## Hướng Dẫn Thực Hiện

### Bước 1: Thu thập thông tin
- Xác định 3-7 đối thủ trực tiếp và 2-3 đối thủ gián tiếp
- Thu thập: website, pricing, features, reviews, social media
- Lưu ý: CẦN bằng chứng cụ thể, KHÔNG suy đoán

### Bước 2: Phân tích theo Framework

#### Porter's Five Forces
| Lực lượng | Câu hỏi chính | Mức đánh giá |
|-----------|---------------|--------------|
| Quyền lực nhà cung cấp | Có bao nhiêu nhà cung cấp? Chi phí chuyển đổi? | Cao / Trung bình / Thấp |
| Quyền lực khách hàng | Khách hàng có nhiều lựa chọn? Nhạy cảm giá? | Cao / Trung bình / Thấp |
| Đe dọa sản phẩm thay thế | Có giải pháp thay thế nào? Chi phí chuyển đổi? | Cao / Trung bình / Thấp |
| Đe dọa đối thủ mới | Rào cản gia nhập? Vốn yêu cầu? | Cao / Trung bình / Thấp |
| Mức độ cạnh tranh | Bao nhiêu đối thủ? Tốc độ tăng trưởng ngành? | Cao / Trung bình / Thấp |

#### Ma trận so sánh đối thủ
```
| Tiêu chí     | Chúng ta | Đối thủ A | Đối thủ B | Đối thủ C |
|--------------|----------|-----------|-----------|-----------|
| Giá          |          |           |           |           |
| Tính năng    |          |           |           |           |
| UX/UI        |          |           |           |           |
| Hỗ trợ      |          |           |           |           |
| Thương hiệu |          |           |           |           |
| Tốc độ      |          |           |           |           |
```

#### Bản đồ định vị (Positioning Map)
- Trục X: Tiêu chí 1 (ví dụ: giá - thấp đến cao)
- Trục Y: Tiêu chí 2 (ví dụ: chất lượng - cơ bản đến cao cấp)
- Đặt mỗi đối thủ vào vị trí tương ứng
- Xác định khoảng trống trên bản đồ = CƠ HỘI

### Bước 3: Phân tích SWOT cạnh tranh
- **Strengths**: Điểm mạnh so với đối thủ
- **Weaknesses**: Điểm yếu cần cải thiện
- **Opportunities**: Cơ hội từ lỗ hổng đối thủ
- **Threats**: Mối đe dọa từ đối thủ mạnh

### Bước 4: Xác định chiến lược khác biệt hóa
1. Khác biệt sản phẩm (tính năng độc quyền)
2. Khác biệt giá (cost leadership hoặc premium)
3. Khác biệt dịch vụ (hỗ trợ, trải nghiệm)
4. Khác biệt thương hiệu (câu chuyện, giá trị)
5. Khác biệt kênh phân phối

### Bước 5: Output
Trả về báo cáo gồm:
1. **Tóm tắt thị trường** (≤200 từ)
2. **Bảng so sánh đối thủ** (bảng chi tiết)
3. **Porter's Five Forces** (đánh giá 5 lực lượng)
4. **Bản đồ định vị** (mô tả vị trí)
5. **SWOT cạnh tranh**
6. **Chiến lược khác biệt hóa đề xuất** (ưu tiên 1-3 chiến lược)
7. **Hành động tiếp theo** (cụ thể, có deadline)

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
