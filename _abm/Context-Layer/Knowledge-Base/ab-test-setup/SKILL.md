---
name: ab-test-setup
description: "Thiết kế A/B test — hypothesis, variants, sample size, phân tích kết quả. Sử dụng khi: test landing page, test email, test pricing, cần data-driven decision, tối ưu conversion."
tags: [marketing, measurement]
---

## KHONG su dung khi

- Chi can chay A/B test don gian -> self-serve tool. Phan tich ket qua du lieu -> dung data-analysis.


# 🧪 A/B Test Setup — Thí Nghiệm Marketing

> Adapted from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)

## Quy trình 5 bước

### 1. Giả thuyết
```
Nếu [thay đổi cụ thể]
Thì [metric] sẽ [tăng/giảm bao nhiêu %]
Vì [lý do dựa trên insight]
```

**Ví dụ:** "Nếu thay headline từ feature-focused sang outcome-focused, thì click-through rate sẽ tăng 20% vì khách quan tâm kết quả hơn tính năng."

### 2. Thiết kế Variant
- **Control (A)**: Phiên bản hiện tại
- **Variant (B)**: 1 thay đổi DUY NHẤT
- ❌ KHÔNG thay 2+ thứ cùng lúc

### 3. Sample Size
| Baseline CR | Min Lift | Traffic/variant |
|-------------|----------|----------------|
| 1% | 20% | ~25,000 |
| 3% | 20% | ~8,000 |
| 5% | 20% | ~5,000 |
| 10% | 15% | ~3,000 |

**Rule of thumb:** Nếu traffic thấp → test những thay đổi LỚN (>30% lift expected).

### 4. Chạy test
- Traffic chia 50/50
- Chạy đủ 1-2 tuần (capture weekly patterns)
- KHÔNG peek sớm
- KHÔNG dừng khi "thấy kết quả"

### 5. Phân tích
- **Statistical significance ≥ 95%**
- Nếu không significant → inconclusive (KHÔNG phải "A thắng")
- Document kết quả dù thắng hay thua

## Ưu tiên test theo Impact

| Priority | Test | Expected Impact |
|----------|------|----------------|
| 1 | Headline/Value prop | ★★★★★ |
| 2 | CTA copy + placement | ★★★★ |
| 3 | Social proof | ★★★ |
| 4 | Layout/design | ★★ |
| 5 | Minor copy changes | ★ |

## Output Template
```markdown
## A/B Test: [Tên test]
- **Hypothesis**: Nếu... thì... vì...
- **Control**: [mô tả A]
- **Variant**: [mô tả B]
- **Metric**: [primary metric]
- **Duration**: [x ngày]
- **Result**: [Winner + % lift + confidence]
- **Learning**: [Insight rút ra]
```

## Related Skills
- page-cro, data-analysis, marketing-psychology
