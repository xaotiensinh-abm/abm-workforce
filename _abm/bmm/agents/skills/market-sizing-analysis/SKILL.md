---
name: "market-sizing-analysis"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Phân tích quy mô thị trường — tính TAM/SAM/SOM bằng 3 phương pháp: top-down, bottom-up, value theory."
---

# Phân Tích Quy Mô Thị Trường

Phương pháp luận toàn diện để tính Total Addressable Market (TAM), Serviceable Available Market (SAM), và Serviceable Obtainable Market (SOM) cho các cơ hội kinh doanh.

## Sử dụng skill này khi

- User yêu cầu "tính TAM", "xác định SAM", "ước lượng SOM", "quy mô thị trường"
- Cần đánh giá cơ hội thị trường cho sản phẩm/dịch vụ mới
- Chuẩn bị pitch cho nhà đầu tư
- Lập kế hoạch kinh doanh dài hạn

## KHÔNG sử dụng khi

- Task không liên quan đến định lượng thị trường
- Cần phân tích đối thủ chi tiết → dùng `competitive-landscape`

## Khái Niệm Cốt Lõi

### Framework 3 tầng thị trường

**TAM (Total Addressable Market)**
- Tổng cơ hội doanh thu nếu đạt 100% thị phần
- Dùng để: xác nhận tầm nhìn dài hạn, validation thị trường
- Ví dụ: Tổng doanh thu phần mềm email marketing toàn cầu

**SAM (Serviceable Available Market)**
- Phần TAM có thể nhắm đến với sản phẩm/dịch vụ hiện tại
- Tính đến: giới hạn địa lý, phân khúc, năng lực
- Ví dụ: Email marketing AI cho e-commerce tại Đông Nam Á

**SOM (Serviceable Obtainable Market)**
- Thị phần thực tế có thể đạt được trong 3-5 năm
- Tính đến: cạnh tranh, nguồn lực, động lực thị trường
- Ví dụ: 2-5% SAM dựa trên phân tích cạnh tranh

## 3 Phương Pháp Tính

### Phương pháp 1: Top-Down (Từ trên xuống)
```
TAM = Tổng quy mô ngành (từ báo cáo nghiên cứu)
SAM = TAM × % Địa lý × % Phân khúc
SOM = SAM × Tỷ lệ chiếm lĩnh thực tế (2-5%)
```
- **Khi dùng**: Thị trường đã có, có báo cáo nghiên cứu
- **Ưu**: Nhanh, dùng dữ liệu uy tín
- **Nhược**: Có thể ước lượng quá cao cho ngành mới

### Phương pháp 2: Bottom-Up (Từ dưới lên)
```
TAM = Σ (Quy mô phân khúc × Doanh thu/khách hàng/năm)
SAM = TAM × (Phân khúc phục vụ được / Tổng phân khúc)
SOM = SAM × Tỷ lệ thâm nhập thực tế (Năm 3-5)
```
- **Khi dùng**: B2B, thị trường ngách, phân khúc cụ thể
- **Ưu**: Uy tín nhất với nhà đầu tư, chi tiết, có bằng chứng
- **Nhược**: Cần nghiên cứu khách hàng kỹ

### Phương pháp 3: Value Theory (Lý thuyết giá trị)
```
Giá trị/KH = Chi phí vấn đề × % Giải quyết
Giá/KH = Giá trị × Sẵn sàng chi trả (10-30%)
TAM = Tổng KH tiềm năng × Giá/KH
SAM = TAM × % Đủ điều kiện mua
SOM = SAM × Tỷ lệ áp dụng thực tế
```
- **Khi dùng**: Tạo ngành mới, đổi mới đột phá
- **Ưu**: Cho thấy giá trị tạo ra, hiệu quả cho thị trường mới
- **Nhược**: Nhiều giả định, khó xác nhận

## Quy Trình 6 Bước

1. **Định nghĩa thị trường** — Mô tả rõ ràng thị trường mục tiêu
2. **Thu thập nguồn dữ liệu** — Báo cáo ngành, dữ liệu chính phủ, khảo sát
3. **Tính TAM** — Dùng ít nhất 2/3 phương pháp
4. **Tính SAM** — Áp dụng bộ lọc địa lý và phân khúc
5. **Tính SOM** — Ước lượng thị phần thực tế 3-5 năm
6. **Xác nhận & tam giác hóa** — So sánh kết quả 3 phương pháp

## Output

Báo cáo gồm:
1. Bảng TAM/SAM/SOM (3 phương pháp)
2. Giả định và nguồn dữ liệu
3. Biểu đồ phễu thị trường
4. Khuyến nghị phương pháp phù hợp nhất
5. Cảnh báo rủi ro / giới hạn phân tích

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
