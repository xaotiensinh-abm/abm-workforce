---
name: "startup-financial-modeling"
description: "Mô hình tài chính startup — dự báo doanh thu cohort-based, cấu trúc chi phí, cash flow, headcount planning, scenario analysis 3 kịch bản."
---

# Mô Hình Tài Chính Startup

Tạo mô hình tài chính 3-5 năm cho startup với doanh thu, chi phí, dòng tiền, và phân tích kịch bản.

## Sử dụng skill này khi

- Cần tạo financial projections cho startup
- Xây dựng mô hình doanh thu (SaaS, marketplace, e-commerce)
- Tính toán burn rate, runway, unit economics
- Chuẩn bị tài liệu gọi vốn
- Lập kế hoạch headcount và chi phí

## KHÔNG sử dụng khi

- Cần phân tích quy mô thị trường → dùng `market-sizing-analysis`
- Cần phân tích startup toàn diện → dùng `startup-analyst`
- Cần phân tích dữ liệu → dùng `data-analysis`

## Thành Phần Cốt Lõi

### 1. Mô Hình Doanh Thu (Cohort-Based)

```
MRR = Σ (Quy mô Cohort × Tỷ lệ Giữ chân × ARPU)
ARR = MRR × 12
```

**Inputs chính:**
- Số khách hàng mới/tháng
- Tỷ lệ giữ chân theo tháng
- ARPU (Average Revenue Per User)
- Pricing tiers và cấu trúc
- Expansion revenue (upsell, cross-sell)

**Retention curve mẫu (SaaS):**
- Tháng 1: 100% → Tháng 3: 90% → Tháng 6: 85% → Tháng 12: 75% → Tháng 24: 70%

### 2. Cấu Trúc Chi Phí

| Hạng mục | Loại | Thành phần |
|----------|------|-----------|
| **COGS** | Biến đổi | Hosting, payment processing, support |
| **S&M** | Bán biến đổi | CAC, marketing spend, sales team |
| **R&D** | Cố định | Engineering, product, design |
| **G&A** | Cố định | Admin, legal, HR, office |

**Tỷ lệ phân bổ nhân sự (Early-stage SaaS):**
- Engineering: 40-50%
- Sales & Marketing: 25-35%
- G&A: 10-15%
- Customer Success: 5-10%

### 3. Dòng Tiền (Cash Flow)

```
Tiền đầu kỳ
+ Doanh thu thu được (tính payment terms)
- Chi phí hoạt động đã trả
- CapEx
= Tiền cuối kỳ

Runway = Tiền cuối kỳ / Burn rate trung bình/tháng
Burn rate = Doanh thu/tháng - Chi phí/tháng
```

### 4. Key Metrics Theo Giai Đoạn

**Revenue Metrics:**
- MRR / ARR
- Growth rate (MoM, YoY)

**Unit Economics:**
- CAC (Chi phí thu khách)
- LTV (Giá trị vòng đời khách hàng)
- CAC Payback Period
- LTV / CAC Ratio (mục tiêu: ≥3x)

**Efficiency Metrics:**
- Burn Multiple = Net Burn / Net New ARR
- Magic Number = Net New ARR / S&M Spend
- Rule of 40 = Growth % + Profit Margin %

## Framework 3 Kịch Bản

| Biến | Lạc quan (+) | Cơ sở | Bi quan (-) |
|------|-------------|-------|------------|
| Tốc độ thu khách | +30% | baseline | -30% |
| Churn rate | -20% | baseline | +20% |
| Giá trị hợp đồng | +15% | baseline | -15% |
| CAC | -25% | baseline | +25% |

**Giữ cố định:** Pricing structure, chi phí core, vai trò thuê (điều chỉnh timing, không phải roles)

## Templates Theo Mô Hình

### SaaS
- Subscription pricing tiers
- Annual vs monthly contracts
- Free trial / freemium
- Expansion revenue

### Marketplace
- GMV projections
- Take rate (% giao dịch)
- Buyer & seller economics
- Transaction frequency

### E-Commerce
- Giá trị đơn hàng trung bình (AOV)
- Tần suất mua lại
- Margin theo dòng sản phẩm
- Chi phí vận chuyển & hoàn hàng

## Quy Trình 7 Bước

1. **Xác định mô hình kinh doanh** — SaaS/Marketplace/E-Commerce
2. **Xây dựng dự báo doanh thu** — Cohort-based
3. **Mô hình chi phí** — Fixed vs Variable
4. **Lập kế hoạch nhân sự** — By department
5. **Dự báo dòng tiền** — Monthly cash position
6. **Tính key metrics** — CAC, LTV, burn rate, runway
7. **Phân tích kịch bản** — 3 scenarios

## Output Format

```
# Mô Hình Tài Chính: [Tên Startup]

## Tóm tắt (≤200 từ)

## 1. Giả định chính
| Giả định | Giá trị | Nguồn |
|----------|---------|-------|

## 2. Dự báo doanh thu (3 năm)
| Chỉ số | Năm 1 | Năm 2 | Năm 3 |
|--------|--------|--------|--------|
| MRR cuối năm | | | |
| ARR | | | |
| Growth MoM | | | |

## 3. Cấu trúc chi phí
## 4. Dòng tiền & Runway
## 5. Unit Economics
## 6. 3 Kịch bản
## 7. Nhu cầu vốn (nếu có)
```

## Sai Lầm Phổ Biến

- ❌ Hockey stick revenue không có lý do
- ❌ Quên chi phí ẩn (tax, compliance, insurance)
- ❌ Giả định churn = 0
- ❌ CAC không tăng theo quy mô
- ❌ Không tính dilution khi gọi vốn

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) (community)
- Adapter: ABM Workforce v2.0 — Jarvis Orchestrator
