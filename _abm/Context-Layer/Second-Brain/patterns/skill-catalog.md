# 📚 Skill Catalog — ABM Workforce Knowledge Base

> **Phiên bản**: v2.1 | **Cập nhật**: 2026-03-09 | **Tổng**: 48 Skills

## Mục đích

Tài liệu knowledge chính thức cho hệ thống Second Brain — catalog toàn bộ 48 skills, phân loại theo domain, maturity level, dependencies, và cross-references.

---

## Tổng Quan Hệ Thống

| Chỉ số | Giá trị |
|--------|---------|
| Tổng skills | **48** |
| Categories | 8 (meta, dev, marketing, phân tích, văn phòng, HR, bán hàng, tự động hóa) |
| Tổng dòng code | ~5,100 dòng SKILL.md |
| Skill nhỏ nhất | sales-enablement (56 dòng) |
| Skill lớn nhất | skill-creator (198 dòng) |
| Trung bình | 106 dòng/skill |

---

## 📋 CATALOG ĐẦY ĐỦ

### 🧠 Hệ thống / Meta (8 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| context-engineering | 169 | ⭐⭐⭐ | Lắp ráp ngữ cảnh 5 lớp + kiểm soát token | Core — mandatory |
| delegation-chain | 111 | ⭐⭐⭐ | Hợp đồng → Chứng nhận → Xác minh | Core — mandatory |
| verification-before-completion | 90 | ⭐⭐⭐ | Bằng chứng trước khẳng định | Core — mandatory |
| capability-evolver | 131 | ⭐⭐⭐ | Tự tiến hóa khả năng agent | Core |
| knowledge-crystallizer | 149 | ⭐⭐⭐ | Kết tinh knowledge từ tasks | memory-keeper |
| memory-keeper | 109 | ⭐⭐⭐ | Quản lý bộ nhớ dài hạn | Core |
| skill-creator | 198 | ⭐⭐⭐ | Tạo skill mới theo chuẩn | capability-evolver |
| dispatching-parallel-agents | 105 | ⭐⭐⭐ | Điều phối agents song song | delegation-chain |

### 💻 Phát triển (7 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| writing-plans | 100 | ⭐⭐⭐ | Lập kế hoạch triển khai | — |
| code-review | 102 | ⭐⭐⭐ | Review code đa chiều | — |
| systematic-debugging | 113 | ⭐⭐⭐ | Debug hệ thống có phương pháp | code-review |
| subagent-driven-development | 136 | ⭐⭐⭐ | Phát triển qua subagents | dispatching-parallel-agents |
| git-worktrees | 87 | ⭐⭐⭐ | Quản lý git worktrees | — |
| finishing-a-development-branch | 86 | ⭐⭐⭐ | Hoàn thiện và merge branch | git-worktrees |
| brainstorming | 107 | ⭐⭐⭐ | Brainstorming ý tưởng có cấu trúc | — |

### 📢 Marketing — Content & Copy (6 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| content-strategy | 96 | ⭐⭐⭐ | Chiến lược nội dung tổng thể | — |
| copywriting | 68 | ⭐⭐⭐ | Viết copy chuyển đổi | marketing-psychology |
| social-content | 93 | ⭐⭐⭐ | Nội dung social media | content-strategy |
| email-marketing | 93 | ⭐⭐⭐ | Email campaigns | copywriting |
| content-creator | 124 | ⭐⭐ | Brand voice + blog SEO + social | content-strategy, seo-content-planner |
| seo-content-planner | 105 | ⭐⭐ | Topic clusters, content calendar | seo-audit |

### 📢 Marketing — CRO & SEO (4 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| seo-audit | 91 | ⭐⭐⭐ | Kiểm tra SEO kỹ thuật | — |
| page-cro | 87 | ⭐⭐⭐ | Tối ưu chuyển đổi trang | ab-test-setup |
| ab-test-setup | 71 | ⭐⭐⭐ | Thiết lập A/B test | — |
| marketing-psychology | 65 | ⭐⭐⭐ | Tâm lý marketing & thuyết phục | — |

### 📢 Marketing — Sales & Strategy (4 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| launch-strategy | 64 | ⭐⭐⭐ | Chiến lược ra mắt sản phẩm | content-strategy |
| pricing-strategy | 78 | ⭐⭐⭐ | Chiến lược giá | — |
| product-marketing-context | 88 | ⭐⭐⭐ | Bối cảnh marketing sản phẩm | — |
| sales-enablement | 56 | ⭐⭐⭐ | Hỗ trợ đội sales | — |

### 📢 Marketing — Retention & Revenue (3 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| churn-prevention | 64 | ⭐⭐⭐ | Ngăn chặn churn | data-analysis |
| cold-email | 68 | ⭐⭐⭐ | Cold email outreach | — |
| revops | 67 | ⭐⭐⭐ | Revenue operations | data-analysis |

### 📢 Sales Automation (1 skill)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| sales-automator | 105 | ⭐⭐ | Cold email sequences, objection handling | cold-email |

### 👥 Văn phòng & HR (4 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| office-documents | 193 | ⭐⭐⭐ | Tạo tài liệu văn phòng | — |
| hr-operations | 172 | ⭐⭐⭐ | Quản lý HR | — |
| internal-comms | 115 | ⭐⭐⭐ | Truyền thông nội bộ | — |
| workflow-automation | 131 | ⭐⭐⭐ | Tự động hóa workflow | — |

### 📊 Phân tích & Nghiên cứu (7 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| data-analysis | 108 | ⭐⭐⭐ | Phân tích dữ liệu KPI | — |
| multi-dimensional-review | 144 | ⭐⭐⭐ | Đánh giá phản biện đa chiều | — |
| competitive-landscape | 95 | ⭐⭐ | Porter's Five Forces, positioning | competitor-intelligence |
| competitor-intelligence | 112 | ⭐⭐ | Thu thập dữ liệu đối thủ | — |
| market-sizing-analysis | 95 | ⭐⭐ | TAM/SAM/SOM 3 phương pháp | — |
| startup-analyst | 99 | ⭐⭐ | Phân tích startup toàn diện | market-sizing-analysis |
| deep-research | 87 | ⭐⭐ | Nghiên cứu chuyên sâu có trích dẫn | — |

### 💰 Mô hình Tài chính (1 skill)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| startup-financial-modeling | 164 | ⭐⭐ | Financial model 3-5 năm | startup-analyst |

### 🔧 Cải tiến hệ thống (3 skills)

| Skill | Dòng | Maturity | Mô tả | Dependencies |
|-------|------|----------|-------|-------------|
| multi-agent-brainstorming | 117 | ⭐⭐ | Review thiết kế 5 vai trò | brainstorming |
| kaizen | 97 | ⭐⭐ | Cải tiến liên tục 4 trụ cột | — |
| agent-improve | 118 | ⭐⭐ | Tối ưu agent 4 giai đoạn | kaizen |

---

## 🗺️ DEPENDENCY MAP

```
context-engineering ◀── (mandatory — mọi task)
delegation-chain ◀── (mandatory — mọi task)
verification-before-completion ◀── (mandatory — mọi task)

brainstorming ──▶ multi-agent-brainstorming
cold-email ──▶ sales-automator
content-strategy ──▶ content-creator, social-content
seo-audit ──▶ seo-content-planner
competitor-intelligence ──▶ competitive-landscape
market-sizing-analysis ──▶ startup-analyst ──▶ startup-financial-modeling
kaizen ──▶ agent-improve
capability-evolver ──▶ skill-creator
memory-keeper ──▶ knowledge-crystallizer
dispatching-parallel-agents ──▶ subagent-driven-development
git-worktrees ──▶ finishing-a-development-branch
data-analysis ──▶ churn-prevention, revops
copywriting ──▶ email-marketing
marketing-psychology ──▶ copywriting
ab-test-setup ──▶ page-cro
```

---

## 📊 MATURITY LEVELS

- ⭐⭐⭐ **Battle-tested** (36 skills) — Đã dùng trong production, có KB reference
- ⭐⭐ **Integrated** (12 skills) — Mới tích hợp từ antigravity-awesome-skills, đã Việt hóa, chưa test thực tế
- ⭐ **Draft** (0 skills) — Chưa có

---

## 🔄 CROSS-REFERENCES

### Khi CEO nói... → Skills được load

| Yêu cầu | Task Type | Skills |
|----------|-----------|--------|
| "Phân tích đối thủ" | competitive | competitor-intelligence → competitive-landscape → market-sizing-analysis |
| "Nghiên cứu thị trường X" | research | deep-research + data-analysis |
| "Phân tích ý tưởng startup" | startup | startup-analyst + market-sizing-analysis + startup-financial-modeling |
| "Viết content marketing" | marketing | content-strategy + copywriting + marketing-psychology |
| "Lập kế hoạch SEO" | seo-planning | seo-content-planner + seo-audit + content-creator |
| "Cold email cho B2B" | sales | cold-email + sales-automator + sales-enablement |
| "Cải thiện hệ thống" | improvement | kaizen + agent-improve + capability-evolver |
| "Review thiết kế" | — | multi-agent-brainstorming (manual invoke) |

---

## 📏 QUALITY METRICS

| Metric | Min | Max | Avg | Chuẩn |
|--------|-----|-----|-----|-------|
| Dòng/skill | 56 | 198 | 106 | ≥80 |
| Có YAML frontmatter | — | — | 48/48 | Bắt buộc |
| Có "Sử dụng khi" | — | — | 48/48 | Bắt buộc |
| Có "KHÔNG sử dụng khi" | — | — | 48/48 | Bắt buộc |
| Có Output format | — | — | 40/48 | Khuyến nghị |
| Có "Nguồn gốc" | — | — | 12/48 | Chỉ skills mới |

### Skills cần bổ sung (dưới 70 dòng — content mỏng)
1. `sales-enablement` (56) — cần thêm framework/templates
2. `churn-prevention` (64) — cần thêm playbook
3. `launch-strategy` (64) — cần thêm timeline/checklist
4. `marketing-psychology` (65) — cần thêm frameworks
5. `revops` (67) — cần thêm process/metrics
6. `cold-email` (68) — cần thêm templates
7. `copywriting` (68) — cần thêm frameworks
