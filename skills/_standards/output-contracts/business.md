# Output Contract: Business Domain

> Áp dụng cho tất cả skill thuộc category `business` (W3:BusinessAgent)
> Version: 1.0 | Last Updated: 2026-03-28

---

## Required Sections

Mọi business output PHẢI có:

- [ ] **Executive Summary** — tóm tắt kết luận chính trong 3-5 câu
- [ ] **Data-driven analysis** — số liệu, chart reference, so sánh
- [ ] **Actionable recommendations** — ≥3 đề xuất cụ thể, có priority
- [ ] **Risk assessment** — rủi ro chính và mitigation
- [ ] **Next steps** — timeline và responsible party
- [ ] **VN context** — localization cho thị trường Việt Nam (nếu applicable)

## Format Standards

| Tiêu chí | Yêu cầu |
|----------|---------|
| Structure | Executive Summary → Analysis → Recommendations → Risks → Next Steps |
| Data | Bảng so sánh, biểu đồ mô tả, benchmark |
| Numbers | VND cho finance VN, % cho tỷ lệ, source cho mọi thống kê |
| Language | Vietnamese cho report nội bộ, English cho investor-facing |
| Length | Report: 3-10 trang, Brief: 1-2 trang |
| Visuals | Mermaid diagram cho flow, table cho comparison |

## Vietnam-Specific Requirements

| Lĩnh vực | Yêu cầu |
|----------|---------|
| Pháp lý | Trích dẫn Luật Doanh nghiệp, Luật Đầu tư, Nghị định liên quan |
| Thuế | VAT 10%, CIT 20%, PIT bậc thang (theo Luật Thuế hiện hành) |
| Ngân hàng | Lãi suất tham chiếu SBV, quy định cho vay |
| HR | Luật Lao động 2019, BHXH/BHYT/BHTN, lương tối thiểu vùng |
| FDI | Luật Đầu tư 2020, ngành nghề cấm/hạn chế |

## Self-Check Rubric (0-10)

| Dimension | Weight | Mô tả |
|-----------|:------:|-------|
| **Data Quality** | 25% | Số liệu chính xác, có nguồn, cập nhật |
| **Analysis Depth** | 25% | Phân tích SWOT/Porter/BCG đúng cách |
| **Actionability** | 20% | Recommendations cụ thể, có thể implement ngay |
| **VN Relevance** | 15% | Phù hợp bối cảnh VN, pháp lý đúng |
| **Presentation** | 15% | Format chuyên nghiệp, dễ đọc, dễ trình bày |

### Grading Scale

| Score | Grade | Action |
|:-----:|:-----:|--------|
| 9-10 | S | Present to stakeholders |
| 7-8 | A | Minor revision → present |
| 5-6 | B | Needs more data/analysis |
| 3-4 | C | Major revision required |
| 0-2 | F | Re-research from scratch |

**Minimum threshold**: Grade B (5/10) cho internal reports, Grade A (7/10) cho external-facing.

## Analysis Frameworks Required

| Loại Report | Framework bắt buộc |
|-------------|-------------------|
| Market Analysis | TAM/SAM/SOM + Competitive Matrix |
| Business Plan | BMC + Financial Projections + Break-even |
| Strategy | SWOT + Porter's 5 Forces |
| Financial | P&L + Cash Flow + Key Ratios |
| Sales | Pipeline + Conversion Rates + CAC/LTV |
| HR | Headcount Plan + Org Chart + Budget |

## Anti-Patterns

```
❌ "Thị trường rất tiềm năng" mà không có số liệu
   → TAM/SAM/SOM cụ thể, source year

❌ Recommendations chung chung "cần cải thiện marketing"
   → Cụ thể: kênh nào, budget bao nhiêu, KPI gì, timeline

❌ Financial projections không có assumptions
   → List rõ assumptions, sensitivity analysis

❌ Copy framework nước ngoài 1:1 cho VN
   → Adapt theo legal, cultural, market VN

❌ Ignore competition
   → ≥3 competitor analysis, differentiation rõ
```
