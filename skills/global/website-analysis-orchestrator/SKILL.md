---
name: "Goal"
description: "Điều phối 10 sub-agents phân tích website mẫu TOÀN DIỆN — UI/UX, Design Tokens, Animations, Database Schema, Tech Stack — để tạo Design Plan hoàn chỉnh sẵn sàng implement."
---

﻿---
name: Website Analysis Orchestrator Pro
version: 2.0.0
description: Multi-Agent system phân tích website mẫu và tạo design plan TOÀN DIỆN (UI/UX, Database, Animations, Full-stack)
author: Antigravity
tags: [website-analysis, ui-ux, multi-agent, design-system, reverse-engineering, database-design, full-stack]
triggers: [website analysis, analyze website, clone design, research website, phân tích website]
dependencies:
  - ui-ux-pro-max
---

# Goal

Điều phối 10 sub-agents phân tích website mẫu TOÀN DIỆN — UI/UX, Design Tokens, Animations, Database Schema, Tech Stack — để tạo Design Plan hoàn chỉnh sẵn sàng implement.

# Instructions


# Website Analysis Orchestrator Pro

## Mục đích
Điều phối **10 sub-agents** để phân tích website mẫu TOÀN DIỆN:
- UI/UX Design System
- Database Structure đề xuất
- Animation & Interactions
- Tech Stack Detection
- Full-stack Implementation Plan

## Khi nào kích hoạt
- User yêu cầu phân tích/nghiên cứu một website
- User muốn "clone" hoặc lấy cảm hứng từ website mẫu
- User cần design plan HOÀN CHỈNH cho dự án mới

## Multi-Agent Coordination Matrix (Extended)

### Agent Roster (10 Agents)

| Agent | Role | Tools | Output |
|-------|------|-------|--------|
| `@Website_Scout` | Reconnaissance | `browser_subagent` | `site_map`, `screenshots` |
| `@Component_Analyst` | UI Inventory | Image analysis | `component_inventory` |
| `@UX_Pattern_Mapper` | UX Research | `browser_subagent` | `ux_patterns` |
| `@Color_Typography_Extractor` | Design Tokens | Color/font extraction | `design_tokens` |
| `@Animation_Inspector` | **Animations** | Browser DevTools | `animation_specs` |
| `@Tech_Stack_Detector` | **Tech Detection** | Source analysis | `tech_stack_report` |
| `@Database_Architect` | **Database Design** | Entity analysis | `database_schema` |
| `@Competitor_Benchmarker` | Market Intel | `search_web` | `benchmark_report` |
| `@Design_Strategist` | Recommendations | UI/UX Pro Max search | `strategy_recommendations` |
| `@Plan_Compiler` | Synthesis | Template rendering | `final_design_plan` |

### Extended Coordination Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                      PHASE 1: RESEARCH                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT: target_url                                               │
│           │                                                      │
│           ▼                                                      │
│  ┌─────────────────┐                                             │
│  │ @Website_Scout  │ ──► screenshots[], sitemap                  │
│  └────────┬────────┘                                             │
│           │                                                      │
│     ┌─────┼─────┬──────────────┬──────────────┐                  │
│     ▼     ▼     ▼              ▼              ▼                  │
│  ┌──────┐┌──────┐┌────────────┐┌─────────────┐┌───────────────┐ │
│  │Comp. ││UX    ││Color/Typo  ││Animation    ││Tech Stack     │ │
│  │Analys││Mapper││Extractor   ││Inspector    ││Detector       │ │
│  └──┬───┘└──┬───┘└─────┬──────┘└──────┬──────┘└───────┬───────┘ │
│     │       │          │              │               │          │
│     ▼       ▼          ▼              ▼               ▼          │
│  compo-  ux_      design_       animation_       tech_stack     │
│  nents   patterns tokens        specs            report         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 2: INTELLIGENCE                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────┐  ┌───────────────────────┐           │
│  │ @Competitor_Benchmarker│  │ @Database_Architect   │           │
│  └───────────┬───────────┘  └───────────┬───────────┘           │
│              │                          │                        │
│              ▼                          ▼                        │
│       benchmark_report           database_schema                 │
│              │                          │                        │
│              └──────────┬───────────────┘                        │
│                         ▼                                        │
│            ┌───────────────────────┐                             │
│            │ @Design_Strategist    │                             │
│            └───────────┬───────────┘                             │
│                        ▼                                         │
│             strategy_recommendations                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 3: SYNTHESIS                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐                                             │
│  │ @Plan_Compiler  │ ◄── ALL previous outputs                    │
│  └────────┬────────┘                                             │
│           │                                                      │
│           ▼                                                      │
│    ┌──────────────────────────────────────┐                     │
│    │       COMPREHENSIVE DESIGN PLAN      │                     │
│    │  • Design System (tokens)            │                     │
│    │  • Component Library                 │                     │
│    │  • Animation Specifications          │                     │
│    │  • Database Schema (SQL ready)       │                     │
│    │  • Tech Stack Recommendations        │                     │
│    │  • Implementation Roadmap            │                     │
│    │  • Code Boilerplate                  │                     │
│    └──────────────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## NEW AGENTS DEFINITIONS

### @Animation_Inspector

```markdown
Mission: Phân tích và document tất cả animations, transitions, micro-interactions

Actions:
1. Observe hover effects trên buttons, cards, links
2. Document scroll-triggered animations
3. Identify page transition styles
4. Note loading states và skeleton screens
5. Capture modal open/close animations
6. Measure timing functions và durations
7. Check for parallax effects

Output → animation_specs.md

Template:
```css
/* Hover Effects */
.btn:hover {
  transform: translateY(-2px);
  transition: transform 200ms ease;
}

/* Scroll Reveal */
.fade-in-up {
  animation: fadeInUp 0.4s ease forwards;
}

/* Modal Animation */
.modal-enter {
  animation: scaleIn 0.3s ease;
}
```
```

### @Tech_Stack_Detector

```markdown
Mission: Detect công nghệ được sử dụng

Actions:
1. Analyze page source for framework hints:
   - Next.js: __NEXT_DATA__, _next/ paths
   - Nuxt: __NUXT__, _nuxt/ paths
   - React: react-root, data-reactroot
   - Vue: [data-v-*], __VUE__
2. Check meta tags và headers
3. Identify CSS framework (Tailwind, Bootstrap)
4. Detect analytics và tracking scripts
5. Identify hosting provider

Output → tech_stack_report.md

Template:
| Category | Technology | Confidence |
|----------|------------|------------|
| Framework | Next.js 14 | High |
| Styling | Tailwind CSS | High |
| Hosting | Vercel | Medium |
| Analytics | Google Analytics 4 | High |
```

### @Database_Architect

```markdown
Mission: Đề xuất database schema dựa trên features phát hiện được

Actions:
1. Identify entities từ UI:
   - User accounts → users table
   - Products → products table
   - Blog posts → posts table
   - Comments → comments table
2. Infer relationships (1:N, M:N)
3. Suggest data types và constraints
4. Propose indexes cho performance
5. Design for scalability

Output → database_schema.md

Template:
```sql
-- Users
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    name VARCHAR(100),
    role ENUM('user', 'admin'),
    created_at TIMESTAMP
);

-- Products
CREATE TABLE products (
    id UUID PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    price DECIMAL(10,2),
    created_by UUID REFERENCES users(id)
);
```
```

---

## Extended Execution Protocol

### Step 5b: Execute @Animation_Inspector (parallel)
```markdown
Mission: Document animations và transitions

Actions:
1. Hover trên interactive elements, observe:
   - Transform (scale, translate, rotate)
   - Opacity changes
   - Color transitions
   - Shadow animations
2. Scroll page, note:
   - Fade-in effects
   - Slide animations
   - Parallax scrolling
   - Sticky element behavior
3. Open modals/dropdowns, observe:
   - Entry animation
   - Exit animation
   - Backdrop fade
4. Document timing:
   - Duration (ms)
   - Easing function
   - Delay

Output → animation_specs.md
```

### Step 5c: Execute @Tech_Stack_Detector (parallel)
```markdown
Mission: Identify technologies

Actions:
1. View page source:
   - Look for framework signatures
   - Check script sources
   - Analyze build artifacts
2. Check Network tab:
   - API patterns (/api/, /graphql)
   - Static file paths
   - CDN usage
3. Inspect headers:
   - Server header
   - X-Powered-By
   - Cache policies
4. Use Wappalyzer-style detection

Output → tech_stack_report.md
```

### Step 6b: Execute @Database_Architect (parallel with Competitor_Benchmarker)
```markdown
Mission: Design database schema

Actions:
1. Analyze visible entities:
   - User accounts/profiles
   - Products/items
   - Categories/tags
   - Comments/reviews
   - Orders/transactions
2. Infer relationships:
   - User → Posts (1:N)
   - Posts → Tags (M:N)
   - User → Orders (1:N)
3. Design tables:
   - Primary keys (UUID vs auto-increment)
   - Foreign keys
   - Indexes
   - Timestamps
4. Add security considerations:
   - Password hashing
   - Role-based access
   - Soft deletes

Output → database_schema.md
```

---

## Extended Handoff Data Schema

```json
{
  "session": {
    "id": "uuid",
    "target_url": "https://example.com",
    "timestamp": "ISO8601"
  },
  "phase1_research": {
    "screenshots": ["path/to/screenshot1.png"],
    "sitemap": { "pages": [], "navigation": [] },
    "component_inventory": { "components": [] },
    "ux_patterns": { "patterns": [] },
    "design_tokens": { "colors": {}, "typography": {}, "spacing": {} },
    "animation_specs": { "hovers": [], "scrolls": [], "modals": [] },
    "tech_stack_report": { "framework": "", "styling": "", "hosting": "" }
  },
  "phase2_intelligence": {
    "benchmark_report": { "competitors": [], "gaps": [] },
    "database_schema": { "tables": [], "relationships": [], "sql": "" },
    "strategy_recommendations": { "style": {}, "improvements": [] }
  },
  "phase3_synthesis": {
    "final_design_plan": "markdown_content",
    "code_boilerplate": {
      "tokens_css": "...",
      "components_css": "...",
      "animations_css": "...",
      "database_sql": "...",
      "index_html": "..."
    }
  }
}
```

---

## Extended Output: Final Design Plan

Bao gồm thêm các sections:

### Animation Specifications
```css
/* Entry Animations */
@keyframes fadeInUp { ... }
@keyframes scaleIn { ... }

/* Hover Effects */
.card:hover { ... }
.btn:hover { ... }

/* Page Transitions */
.page-enter { ... }
.page-exit { ... }
```

### Database Schema
```sql
-- Full SQL schema ready for PostgreSQL/MySQL
CREATE TABLE ...
```

### Tech Stack Recommendations
```markdown
| Layer | Recommended | Alternative |
|-------|-------------|-------------|
| Frontend | Next.js 14 | Nuxt 3 |
| Styling | CSS Modules | Tailwind CSS |
| Database | PostgreSQL | MySQL |
| ORM | Prisma | Drizzle |
| Auth | NextAuth.js | Clerk |
| Hosting | Vercel | VPS |
```

---

## Usage Examples

### Full-stack Analysis
```
User: Phân tích stripe.com, tôi muốn clone full-stack với database
Agent: [Activates Website Analysis Orchestrator Pro]
       [Executes 10-agent pipeline]
       [Delivers comprehensive plan với SQL schema]
```

### Focus on Animations
```
User: Phân tích animations của linear.app
Agent: [Emphasizes @Animation_Inspector]
       [Detailed animation_specs.md]
```

### Database-first Analysis
```
User: Phân tích notion.so, focus vào database structure
Agent: [Emphasizes @Database_Architect]
       [Complete ERD và SQL schema]
```

---

## Performance (Updated)

| Phase | Estimated Time |
|-------|----------------|
| Research (6 agents parallel) | 12-18 minutes |
| Intelligence (3 agents) | 10-15 minutes |
| Synthesis | 8-12 minutes |
| **Total** | **30-45 minutes** |


# Examples

## Ví dụ 1: Full-stack analysis Stripe.com

**Input:** `Phân tích stripe.com, clone full-stack với database`n**Output:** Design tokens + 45 components + animation specs + PostgreSQL schema + Next.js boilerplate

## Ví dụ 2: Focus animations Linear.app

**Input:** `Phân tích animations của linear.app`n**Output:** Detailed animation_specs.md: 12 hover effects + 8 scroll animations + 3 page transitions

# Constraints

- KHÔNG ĐƯỢC bỏ qua screenshots — mọi phân tích phải dựa trên visual evidence
- KHÔNG ĐƯỢC đề xuất database schema mà không phân tích entities từ UI
- LUÔN LUÔN chạy 6 agents song song trong Phase 1 (Research)
- LUÔN LUÔN cung cấp SQL ready schema trong output
- LUÔN LUÔN tổng hợp qua @Plan_Compiler trước khi deliver

---

📦 Upgraded by Skill Generator v4.0 Audit

