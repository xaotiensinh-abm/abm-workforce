---
name: data-analysis
description: Phân tích dữ liệu kinh doanh — KPI dashboard, trend analysis, báo cáo định kỳ, insight extraction. Biến data thành quyết định.
---

# Data Analysis — Phân tích dữ liệu kinh doanh

## Khi nào sử dụng
- Phân tích sales / revenue data
- Tạo KPI dashboard
- Nghiên cứu thị trường
- Phân tích customer data
- Benchmark với đối thủ
- Forecasting

## Framework phân tích

### 1. Define the Question
```
- Business question cần trả lời là gì?
- Decision nào sẽ dựa trên analysis này?
- Ai là audience? (CEO vs team lead → mức detail khác nhau)
```

### 2. Gather Data
```
- Data sources: CRM, Analytics, Finance, HR
- Time period: Q? Year? All-time?
- Data quality check: missing values? outliers?
```

### 3. Analyze
```
- Descriptive: Chuyện gì đã xảy ra? (metrics, trends)
- Diagnostic: Tại sao? (root cause, correlations)
- Predictive: Sẽ xảy ra gì? (forecasting, modeling)
- Prescriptive: Nên làm gì? (recommendations)
```

### 4. Present
```
- Executive summary (3 bullets max)
- Key visualizations (chart types matter)
- Actionable recommendations
- Next steps with owners
```

## KPI Dashboard Template

```markdown
# KPI Dashboard — [Period]

## 🎯 Top-Line Metrics
| Metric | Target | Actual | vs Target | vs Last Period |
|--------|--------|--------|-----------|----------------|
| Revenue | 1B₫ | 1.2B₫ | +20% ✅ | +15% ↑ |
| Customers | 500 | 480 | -4% ⚠️ | +8% ↑ |
| Churn Rate | <5% | 3.2% | ✅ | -0.5% ↓ |

## 📊 Trend (6 tháng)
| Month | Revenue | Customers | NPS |
|-------|---------|-----------|-----|

## 🔍 Deep Dive
### Revenue Breakdown
| Source | Amount | % Total | Trend |
|--------|--------|---------|-------|

### Customer Segments
| Segment | Count | Revenue | LTV | Churn |
|---------|-------|---------|-----|-------|

## 💡 Key Insights
1. [Insight + data] → [Recommendation]
2. [Insight + data] → [Recommendation]

## ⚠️ Risks
| Risk | Indicator | Action |
|------|-----------|--------|
```

## Chart Type Selection

| Mục đích | Chart Type |
|---------|-----------|
| Trend theo thời gian | Line chart |
| So sánh categories | Bar chart |
| Tỷ lệ % | Pie chart (< 5 items) |
| Distribution | Histogram |
| Correlation | Scatter plot |
| Part-to-whole over time | Stacked area |
| Geographics | Map/Heatmap |

## Storytelling with Data

```
1. Context: "Doanh thu Q3 tăng 20%"
2. Complication: "Nhưng customer acquisition cost tăng 40%"
3. Resolution: "Cần optimize marketing spend theo channel ROI"
4. Next steps: "Shift budget from Facebook → Google (ROI 3x higher)"
```

## Common Pitfalls
- ❌ Vanity metrics (pageviews mà không conversion)
- ❌ Correlation ≠ Causation
- ❌ Too many KPIs (focus 5-7 max)
- ❌ No benchmark (số liệu không context)
- ❌ Pretty charts mà không insight
