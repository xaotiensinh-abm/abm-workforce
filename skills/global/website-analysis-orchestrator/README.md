# Website Analysis Orchestrator

Skill điều phối đa agent để phân tích website mẫu và tạo design plan tối ưu, tích hợp UI/UX Pro Max.

## Quick Start

```
/website-analysis https://example.com
```

## Features

- 🔍 **Deep Website Analysis**: Crawl và phân tích toàn bộ structure
- 🎨 **Design Token Extraction**: Tự động extract colors, typography, spacing
- 📊 **Component Inventory**: Map tất cả UI components sử dụng
- 🎯 **UX Pattern Recognition**: Nhận diện navigation, CTA, user flows
- 📈 **Competitor Benchmarking**: So sánh với best practices ngành
- 💡 **Smart Recommendations**: Đề xuất từ UI/UX Pro Max database
- 📋 **Actionable Design Plan**: Output sẵn sàng implement

## Architecture

7 Sub-Agents hoạt động qua 3 Phases:

```
Phase 1: Research
├── @Website_Scout → Screenshots + Sitemap
├── @Component_Analyst → UI Components
├── @UX_Pattern_Mapper → User Flows
└── @Color_Typography_Extractor → Design Tokens

Phase 2: Intelligence  
├── @Competitor_Benchmarker → Industry Comparison
└── @Design_Strategist → Optimization Recommendations

Phase 3: Synthesis
└── @Plan_Compiler → Final Design Plan
```

## Output Format

```markdown
# Design Plan: [Website Name]

## 1. Design Tokens
- Colors, Typography, Spacing, Border Radius

## 2. Component Inventory
- Headers, Cards, Forms, CTAs, Footers

## 3. UX Patterns
- Navigation, Interactions, Responsive Behavior

## 4. Recommendations
- UI/UX Pro Max suggestions

## 5. Implementation Roadmap
- Step-by-step build guide
```

## Requirements

- Antigravity/Claude Code với browser access
- UI/UX Pro Max skill installed

## License

MIT
