---
name: innovation-report
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Báo cáo R&D định kỳ — tổng hợp nghiên cứu, benchmarks, recommendations, curriculum impact cho CEO"
---

# Báo Cáo R&D — Innovation Report

## Mục đích
Skill này giúp tổng hợp và trình bày kết quả nghiên cứu R&D dưới dạng báo cáo dễ hiểu cho CEO và team đào tạo.

## 3 Loại báo cáo

### 1. Weekly R&D Brief (5 phút đọc)

```yaml
weekly_brief:
  format: "rd-weekly-YYYY-WXX.md"
  max_length: "500 từ"
  
  template: |
    # R&D Weekly Brief — Tuần XX/YYYY
    
    ## 🔴 HOT (Action ngay)
    - [Item 1]: [1 câu tóm tắt] → [Action: workshop / update module]
    
    ## 🟡 WARM (Theo dõi)
    - [Item 1]: [1 câu tóm tắt]
    - [Item 2]: [1 câu tóm tắt]
    
    ## 📊 Benchmark tuần này
    - [Đã benchmark X vs Y → Winner: X vì...]
    
    ## 📋 Action Items
    - [ ] [Ai] [Làm gì] [Khi nào]
    
    ## 🔗 Links
    - [Link 1], [Link 2]
```

### 2. Monthly Innovation Report (CEO review)

```yaml
monthly_report:
  format: "rd-monthly-YYYY-MM.md"
  presentation: "30 phút cho CEO + leadership"
  
  sections:
    executive_summary:
      max: "200 từ"
      content: "Top 3 findings + top 3 recommendations"
    
    trend_analysis:
      content:
        - "Top 5 xu hướng AI tháng này"
        - "Ảnh hưởng đến ABM curriculum"
        - "Dự đoán 3 tháng tới"
      visual: "Trend radar chart"
    
    tech_evaluations:
      content:
        - "Công nghệ đã đánh giá (RAPID scores)"
        - "Adopt vs Trial vs Hold"
        - "So sánh với tháng trước"
      visual: "RAPID scorecard table"
    
    benchmarks:
      content:
        - "Kết quả benchmark tháng này"
        - "Model/tool changes"
        - "Cost implications cho ABM"
      visual: "Comparison tables + charts"
    
    curriculum_impact:
      content:
        - "Modules cần cập nhật"
        - "Modules mới đề xuất"
        - "Modules nên retire"
      visual: "Impact matrix"
    
    competitive_landscape:
      content:
        - "Đối thủ đào tạo AI đang dạy gì?"
        - "Gap analysis: ABM vs competitors"
        - "Cơ hội differentiation"
    
    roadmap_update:
      content:
        - "Training roadmap changes"
        - "Next month priorities"
      visual: "Updated roadmap diagram"
    
    budget:
      content:
        - "R&D spend tháng này"
        - "API costs / compute costs"
        - "ROI: research → revenue"
```

### 3. Quarterly Innovation Review (Strategic)

```yaml
quarterly_review:
  format: "rd-quarterly-YYYY-QX.md"
  audience: "CEO + All department heads"
  duration: "60 phút"
  
  sections:
    quarter_highlights: "Top 10 achievements"
    trend_evolution: "Xu hướng đã thay đổi thế nào qua 3 tháng"
    roi_analysis: "Research → Training → Revenue pipeline"
    knowledge_base_growth: "KB entries added, usage stats"
    competitive_position: "ABM vs market — where we stand"
    next_quarter_plan: "Priorities, budget, milestones"
    risk_assessment: "Disruption risks (new platform, regulation)"
```

## KPI Phòng R&D

```yaml
rd_kpis:
  output_metrics:
    - weekly_radars_published: { target: "4/tháng", actual: "?" }
    - tech_evaluations_completed: { target: "3/tháng", actual: "?" }
    - benchmarks_run: { target: "2/tháng", actual: "?" }
    - kb_entries_added: { target: "10/tháng", actual: "?" }
    - modules_proposed: { target: "2/tháng", actual: "?" }
  
  impact_metrics:
    - research_to_training_time: { target: "< 4 tuần", unit: "days" }
    - trend_detection_accuracy: { target: "> 80%", note: "Trend flagged → actually important" }
    - curriculum_freshness: { target: "< 3 tháng", note: "Avg age of newest content" }
    - student_satisfaction_new_modules: { target: "> 4.0/5" }
  
  efficiency:
    - cost_per_evaluation: { target: "< $50" }
    - time_per_benchmark: { target: "< 4 hours" }
```

## Output khi được yêu cầu

1. **Weekly Brief** — 500 từ, HOT/WARM items, action items
2. **Monthly Report** — Full analysis cho CEO, 30 phút presentation
3. **Quarterly Review** — Strategic review, ROI analysis
4. **KPI Dashboard** — R&D performance metrics
5. **Ad-hoc Report** — Báo cáo đặc biệt khi có breakthrough
