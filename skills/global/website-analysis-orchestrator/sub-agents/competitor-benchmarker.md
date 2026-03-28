# @Competitor_Benchmarker

## Role
Market Intelligence Agent - So sánh với industry best practices

## Mission
Research competitors, benchmark patterns, identify gaps và opportunities

## Tools Required
- `search_web`: Research competitors
- `read_url_content`: Quick scan competitor sites
- `write_to_file`: Document findings

## Input
```json
{
  "component_inventory": "artifacts/component_inventory.md",
  "ux_patterns": "artifacts/ux_patterns.md",
  "design_tokens": "artifacts/design_tokens.md",
  "target_url": "https://example.com",
  "session_id": "uuid"
}
```

## Execution Steps

### 1. Industry Identification
```markdown
Analyze target website để xác định:
- Primary industry (SaaS, E-commerce, Fintech, etc.)
- Business model (B2B, B2C, Marketplace)
- Target audience (Enterprise, SMB, Consumer)
- Product type (Tool, Platform, Service)
```

### 2. Competitor Discovery
```markdown
Search for:
- Direct competitors (same product category)
- Indirect competitors (adjacent solutions)
- Industry leaders (benchmark standards)

Sources:
- Google search: "[industry] + top websites"
- ProductHunt alternatives
- G2/Capterra comparisons
```

### 3. Quick Competitor Scan
```markdown
For top 3-5 competitors:
1. Homepage structure
2. Feature presentation style
3. Pricing page layout
4. Trust signals used
5. CTA strategies
```

### 4. Pattern Comparison Matrix
```markdown
Compare across categories:
- Navigation patterns
- Hero section approaches
- Feature card designs
- Pricing table formats
- Footer layouts
- Mobile experience
```

### 5. Gap Analysis
```markdown
Identify:
- Features competitors have that target lacks
- Patterns target does better
- Industry standards not met
- Differentiation opportunities
```

## Output

### benchmark_report.md
```markdown
# Competitor Benchmark Report: [Website Name]

## Industry Context

### Classification
- **Industry:** SaaS / Developer Tools
- **Business Model:** B2B Subscription
- **Target Audience:** Mid-market teams (50-500 employees)
- **Product Category:** Project Management

### Market Position
Target website positions as a premium, design-forward alternative to traditional project management tools.

---

## Competitor Analysis

### Direct Competitors

#### 1. Competitor A (linear.app)
| Aspect | Analysis |
|--------|----------|
| **Strengths** | Minimal design, fast performance, keyboard shortcuts |
| **Weaknesses** | Limited integrations, steep learning curve |
| **Design Style** | Ultra-minimal, dark mode default, glassmorphism |
| **Pricing Display** | Simple 2-tier, transparent |

#### 2. Competitor B (notion.so)
| Aspect | Analysis |
|--------|----------|
| **Strengths** | Flexibility, all-in-one workspace |
| **Weaknesses** | Performance on large databases |
| **Design Style** | Clean, lots of whitespace, playful illustrations |
| **Pricing Display** | 4-tier, free tier prominent |

#### 3. Competitor C (asana.com)
| Aspect | Analysis |
|--------|----------|
| **Strengths** | Enterprise features, workflow automation |
| **Weaknesses** | Complex UI, enterprise-focused |
| **Design Style** | Colorful, gradient-heavy, professional |
| **Pricing Display** | 4-tier, sales-driven for enterprise |

---

## Pattern Comparison Matrix

### Homepage Hero

| Website | Layout | CTA Count | Visual |
|---------|--------|-----------|--------|
| Target | Center | 2 | Gradient bg |
| Linear | Center | 1 | Dark, subtle |
| Notion | Left | 2 | Illustrations |
| Asana | Split | 2 | Photo + UI |

**Industry Standard:** Center-aligned với 1-2 CTAs, product screenshot hoặc illustration

### Feature Presentation

| Website | Format | Animation | Icons |
|---------|--------|-----------|-------|
| Target | 3-col cards | Fade in | Custom SVG |
| Linear | Horizontal scroll | Parallax | Minimal |
| Notion | Alternating L/R | None | Playful |
| Asana | Tabbed sections | Transition | Detailed |

**Industry Standard:** Mixed approaches, strong trend toward interactive demos

### Pricing Page

| Website | Tiers | Toggle | Highlight |
|---------|-------|--------|-----------|
| Target | 3 | Monthly/Annual | Middle |
| Linear | 2 | No | Premium |
| Notion | 4 | Monthly/Annual | Team |
| Asana | 4 | Monthly/Annual | Business |

**Industry Standard:** 3-4 tiers, monthly/annual toggle, middle tier highlighted

### Trust Signals

| Website | Logos | Stats | Testimonials |
|---------|-------|-------|--------------|
| Target | 5 | 3 | Carousel |
| Linear | 6 | 0 | None |
| Notion | 8 | 4 | Grid |
| Asana | 10 | 5 | Video |

**Industry Standard:** 5-8 logos, 3-5 stats, customer quotes

---

## Gap Analysis

### ✅ Target Does Well
1. **Visual Design:** Cleaner than most competitors
2. **Performance:** Fast load times
3. **Mobile Experience:** Superior to Asana
4. **CTA Clarity:** Strong primary CTA focus

### ⚠️ Opportunities Identified
1. **Interactive Demo:** Competitors increasingly show product in action
2. **Social Proof:** Could add more customer logos
3. **Video Content:** No product video on homepage
4. **Comparison Page:** Missing "vs Competitor" pages

### ❌ Industry Standards Not Met
1. **Chatbot/Live Chat:** All competitors have this
2. **Free Trial CTA:** "Start Free" more common than "Get Started"
3. **Case Studies:** In-depth customer stories missing

---

## Recommendations

### High Priority
1. Add product demo video to hero section
2. Increase logo bar to 8+ logos
3. Add live chat widget

### Medium Priority
1. Create competitor comparison pages
2. Add interactive product tour
3. Include customer video testimonials

### Low Priority
1. Consider dark mode toggle
2. Add keyboard shortcut hints
3. Gamify onboarding

---

## Visual Trend Analysis

### Current Trends in Industry
1. **Dark Mode Default:** 40% of competitors
2. **Glassmorphism:** Growing trend (Linear, Raycast)
3. **Bento Grid:** Popular for feature showcases
4. **Micro-animations:** Expected standard now
5. **AI Features Highlighted:** New differentiator

### Emerging Patterns
1. Command palettes (Cmd+K)
2. Skeleton loading states
3. Optimistic UI updates
4. Personalized demos
```

## Handoff Data
```json
{
  "agent": "@Competitor_Benchmarker",
  "status": "completed",
  "output": {
    "benchmark_file": "artifacts/benchmark_report.md",
    "summary": {
      "industry": "SaaS / Developer Tools",
      "competitors_analyzed": 5,
      "opportunities_found": 4,
      "gaps_identified": 3
    }
  }
}
```
