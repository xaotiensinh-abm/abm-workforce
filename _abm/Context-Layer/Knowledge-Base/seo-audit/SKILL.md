---
name: seo-audit
description: Đánh giá SEO toàn diện cho website — on-page, technical, content, backlinks. Checklist + action plan.
---

## KHONG su dung khi

- Can viet content SEO -> dung seo-content-planner. Can CRO -> dung page-cro.


# SEO Audit — Đánh giá SEO doanh nghiệp

> Inspired by [skills.sh/seo-audit](https://skills.sh)

## Khi nào sử dụng
- Audit SEO website mới
- Kiểm tra sau khi redesign website
- Review định kỳ hàng quý
- Trước khi launch chiến dịch content lớn

## 1. Technical SEO Checklist

### Crawlability
- [ ] robots.txt đúng format, không block pages quan trọng
- [ ] XML sitemap tồn tại và submit lên Google Search Console
- [ ] Không có orphan pages (pages không link từ đâu)
- [ ] Redirect chains < 3 hops

### Performance
- [ ] Page load time < 3 giây (mobile)
- [ ] Core Web Vitals pass (LCP, FID, CLS)
- [ ] Images optimized (WebP, lazy loading)
- [ ] CSS/JS minified

### Mobile
- [ ] Mobile-first responsive design
- [ ] Touch targets đủ lớn (48x48px min)
- [ ] No horizontal scroll

### Security
- [ ] HTTPS everywhere
- [ ] No mixed content warnings
- [ ] SSL certificate valid

## 2. On-Page SEO Checklist

### Per Page
- [ ] Title tag: 50-60 chars, keyword đầu
- [ ] Meta description: 150-160 chars, CTA
- [ ] H1: 1 per page, chứa primary keyword
- [ ] H2-H6: Proper hierarchy
- [ ] URL: Short, keyword-rich, no parameters
- [ ] Internal links: 3-5 per page
- [ ] Image alt text: Descriptive, keyword-related
- [ ] Schema markup: Article, FAQ, Product, LocalBusiness

## 3. Content SEO

| Check | What to Look For |
|-------|-----------------|
| Keyword targeting | Mỗi page target 1 primary keyword? |
| Search intent | Content match user intent? |
| Content depth | Comprehensive hơn top 3 kết quả? |
| Freshness | Updated trong 6 tháng qua? |
| Thin content | Pages < 300 words? |
| Duplicate content | Canonical tags đúng? |
| Content gaps | Keywords đối thủ rank mà mình chưa? |

## 4. Output Format

```markdown
# SEO Audit Report — [Website]
**Date**: [date] | **Auditor**: Jarvis

## Overall Score: [A/B/C/D/F]

## Critical Issues (Fix immediately)
| # | Issue | Page | Impact | Fix |
|---|-------|------|--------|-----|

## Important Issues (Fix this month)
| # | Issue | Page | Impact | Fix |
|---|-------|------|--------|-----|

## Opportunities
| # | Opportunity | Est. Impact | Effort |
|---|-------------|-------------|--------|

## Quick Wins (< 1 hour each)
1. [action]
2. [action]

## Action Plan Priority
1. [P0: Critical fix] — Owner: [who] — Deadline: [when]
2. [P1: Important] — Owner: [who] — Deadline: [when]
```
