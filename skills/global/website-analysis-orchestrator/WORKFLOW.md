---
description: Phân tích website mẫu và tạo design plan tối ưu với code boilerplate
triggers: [website analysis, analyze website, phân tích website, clone design, reverse engineer]
---

# Website Analysis Workflow

Multi-Agent Orchestrator để phân tích website mẫu và tạo design plan với code sẵn sàng implement.

## Prerequisites
- UI/UX Pro Max skill installed
- Browser access enabled

## Workflow Steps

### 1. Collect Input
```
Hỏi user:
- URL website cần phân tích
- Focus areas (design, components, UX, all)
- Output preference (design tokens only / full boilerplate)
```

### 2. Execute Phase 1: Research (Parallel)

#### 2a. @Website_Scout
```
- Navigate to target URL
- Capture full-page screenshots (homepage + 3-4 key pages)
- Build sitemap structure
- Output: screenshots/, sitemap.md
```

#### 2b. @Component_Analyst (after 2a)
```
- Analyze screenshots for UI components
- Catalog all visible elements
- Note variants and states
- Output: component_inventory.md
```

#### 2c. @UX_Pattern_Mapper (parallel with 2b)
```
- Map navigation flows
- Identify CTA patterns
- Document scroll/hover behaviors
- Test responsive breakpoints
- Output: ux_patterns.md
```

#### 2d. @Color_Typography_Extractor (parallel with 2b)
```
- Extract color palette from screenshots
- Identify typography stack
- Measure spacing system
- Document shadows and radius
- Output: design_tokens.md
```

### 3. Execute Phase 2: Intelligence (Sequential)

#### 3a. @Competitor_Benchmarker
```
- Identify industry/niche
- Search for top competitors
- Compare patterns
- Identify gaps and opportunities
- Output: benchmark_report.md
```

#### 3b. @Design_Strategist
```
// turbo
python3 C:/Users/PC/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<style>" --domain style
python3 C:/Users/PC/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<industry>" --domain color
python3 C:/Users/PC/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<component>" --domain ux

- Match with UI/UX Pro Max database
- Generate recommendations
- Propose improvements
- Output: strategy_recommendations.md
```

### 4. Execute Phase 3: Synthesis

#### 4a. @Plan_Compiler
```
- Aggregate all outputs
- Structure final design plan
- Generate CSS custom properties (tokens.css)
- Generate component styles (components.css)
- Generate HTML starter template
- Output: final_design_plan.md, code/
```

### 5. Deliver Results
```
Present to user:
1. final_design_plan.md - Complete design plan
2. code/tokens.css - CSS custom properties
3. code/components.css - Component styles
4. code/index.html - HTML starter template
5. Screenshots and analysis artifacts
```

## Quick Start Command
```
/website-analysis https://example.com
```

## Output Directory Structure
```
artifacts/
├── screenshots/
│   ├── homepage.png
│   ├── features.png
│   └── ...
├── sitemap.md
├── component_inventory.md
├── ux_patterns.md
├── design_tokens.md
├── benchmark_report.md
├── strategy_recommendations.md
├── final_design_plan.md
└── code/
    ├── tokens.css
    ├── components.css
    ├── animations.css
    └── index.html
```

## Estimated Duration
- Simple website: 20-30 minutes
- Complex website: 40-60 minutes

## Notes
- Skill tích hợp UI/UX Pro Max để đưa ra recommendations
- Output là code boilerplate sẵn sàng implement
- Có thể chạy từng agent riêng lẻ nếu cần
