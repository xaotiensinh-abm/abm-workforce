---
name: ai-trend-radar
description: "Theo dõi xu thế AI thế giới — papers, releases, conferences, industry moves, weekly/monthly radar"
---

# Radar Xu Thế AI — AI Trend Radar

## Mục đích
Skill này giúp theo dõi và tổng hợp xu hướng AI toàn cầu, giúp ABM luôn bắt kịp và dẫn đầu trong đào tạo AI.

## Nguồn theo dõi (18 kênh)

### Papers & Research
| Nguồn | Tần suất | Cách theo dõi |
|-------|---------|--------------|
| arXiv (cs.AI, cs.CL, cs.CV) | Hàng ngày | RSS feed + AI summary |
| Google Research Blog | Hàng tuần | RSS |
| OpenAI Blog | Khi có bài mới | RSS |
| Papers With Code | Hàng tuần | Top trending |
| Semantic Scholar | Hàng tuần | Alerts theo keywords |

### Industry & Products
| Nguồn | Tần suất | Focus |
|-------|---------|-------|
| Hugging Face (trending models) | Hàng ngày | Models mới, fine-tunes |
| GitHub Trending (AI repos) | Hàng ngày | Tools, frameworks |
| Product Hunt (AI category) | Hàng tuần | Startups, products |
| TechCrunch AI | Hàng ngày | Funding, acquisitions |
| The Verge AI | Hàng ngày | Consumer AI news |

### Community & Events
| Nguồn | Focus |
|-------|-------|
| r/MachineLearning | Thảo luận, hot takes |
| X/Twitter (AI researchers) | Breaking news, debates |
| NeurIPS, ICML, ICLR | Papers accepted, trends |
| Google I/O, WWDC, AWS re:Invent | Product launches |
| AI Vietnam community | Local trends |

## Quy trình Radar hàng tuần

```yaml
weekly_radar:
  monday:
    - "Scan arXiv top papers (cs.AI, cs.CL, cs.CV) 7 ngày qua"
    - "Check Hugging Face trending models"
    - "Review GitHub trending AI repos"
  
  wednesday:
    - "Đọc AI newsletters (The Batch, TLDR AI, Import AI)"
    - "Check industry news (funding, acquisitions, launches)"
  
  friday:
    - "Tổng hợp Weekly Radar Report"
    - "Đánh giá relevance cho ABM curriculum"
    - "Flag items cần action (update course, new workshop, etc.)"

  output:
    format: "weekly-radar-YYYY-WXX.md"
    sections:
      - breakthrough: "🔬 Đột phá (papers/models đáng chú ý)"
      - releases: "🚀 Ra mắt (tools, APIs, platforms mới)"
      - industry: "💼 Industry (funding, M&A, partnerships)"
      - open_source: "🔓 Open Source (repos trending)"
      - vietnam: "🇻🇳 Vietnam AI (local news, regulations)"
      - action_items: "📋 Hành động (cập nhật khóa học, workshop mới)"
```

## Radar hàng tháng (Monthly Deep Dive)

```yaml
monthly_radar:
  content:
    trend_analysis: "Top 5 xu hướng tháng này + dự đoán tháng sau"
    model_landscape: "Bản đồ models (performance, cost, use cases)"
    framework_update: "PyTorch / TF / JAX / LangChain / LlamaIndex changes"
    curriculum_impact: "Modules nào cần cập nhật?"
    competitor_courses: "Đối thủ đào tạo AI đang dạy gì mới?"
  
  deliverable:
    format: "monthly-radar-YYYY-MM.md"
    presentation: "Trình bày CEO + team đào tạo (30 phút)"
    archive: "Lưu vào Second Brain → Knowledge Base"
```

## Hệ thống phân loại xu hướng

```
🔴 HOT — Đang bùng nổ, cần action ngay (< 1 tuần)
   Ví dụ: Model mới phá kỷ lục, regulation mới ban hành

🟡 WARM — Đang phát triển, cần theo dõi (1-4 tuần)
   Ví dụ: Framework mới gaining traction, research direction mới

🟢 WATCH — Mới xuất hiện, ghi nhận (1-3 tháng)
   Ví dụ: Early-stage research, startup mới
   
⚪ ARCHIVE — Đã mature hoặc decline
   Ví dụ: Deprecated tools, outdated approaches
```

## Tích hợp Deep Research Agent

```yaml
deep_research_integration:
  tool: "Gemini Deep Research / Perplexity Pro"
  use_cases:
    weekly_scan:
      prompt: "Tìm top 5 papers AI quan trọng nhất tuần này trên arXiv (cs.AI, cs.CL, cs.CV). Tóm tắt mỗi paper trong 3 câu: What, Why, Impact."
      frequency: "Monday"
    
    tech_deep_dive:
      prompt: "Phân tích [technology X]: architecture, performance benchmarks, adoption rate, competitors, và dự đoán 6 tháng tới."
      frequency: "On-demand (khi có 🔴HOT)"
    
    competitor_scan:
      prompt: "Tìm top 5 khóa đào tạo AI mới ra mắt tháng này. So sánh nội dung, giá, format với ABM."
      frequency: "Monthly"
```

---

## Ví dụ Weekly Radar Hoàn Chỉnh

```markdown
# R&D Weekly Radar — Tuần 11/2026

## 🔴 HOT — Action ngay
- **Gemini 2.5 Flash ra mắt**: Nhanh gấp 3 lần Pro, giá rẻ hơn 80%.
  → Action: Benchmark ngay (benchmark-lab). Cập nhật module LLM nếu tốt hơn.
  → Owner: rd-specialist | Deadline: Thứ 6

## 🟡 WARM — Theo dõi
- **LlamaIndex v0.12**: Workflow engine mới, async-first.
  → Theo dõi adoption. Review lại RAG module nếu stable.
- **EU AI Act enforcement bắt đầu**: Quy định mới cho AI systems.
  → Chuẩn bị workshop "AI Ethics & Compliance" cho Q3.

## 🟢 WATCH — Ghi nhận
- **Apple Intelligence 2.0**: On-device LLM cải tiến.
- **Moshi (Kyutai)**: Open-source voice AI model.

## 📊 Benchmark tuần này
- Gemini 2.5 Pro vs Claude 3.5 Sonnet trên tiếng Việt QA:
  Gemini thắng accuracy (92% vs 89%), Claude thắng reasoning.
  → Giữ cả 2 trong curriculum. Chi tiết: benchmark-llm-2026-03.md

## 📋 Action Items
- [ ] @rd: Benchmark Gemini 2.5 Flash (Thứ 4)
- [ ] @rd: Cập nhật glossary entry "Gemini" (Thứ 5)
- [ ] @training: Review RAG module cho LlamaIndex update (Tuần sau)
- [ ] @ceo: Approve budget workshop AI Ethics Q3

## 🔗 Links
- [Gemini 2.5 Flash blog](https://blog.google/gemini-flash)
- [LlamaIndex v0.12 changelog](https://github.com/run-llama/llama_index)
- [EU AI Act timeline](https://artificialintelligenceact.eu)
```

---

## Output khi được yêu cầu

1. **Weekly Radar** — Tổng hợp 5 mục theo template
2. **Monthly Deep Dive** — Phân tích xu hướng + tác động curriculum
3. **Trend Alert** — Notification khi có đột phá (🔴 HOT)
4. **Landscape Map** — Bản đồ models/tools theo category
5. **Action Items** — Đề xuất cập nhật cho team đào tạo
6. **Deep Research Brief** — Autonomous research results
