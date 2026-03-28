# Output Contract: Design Domain

> Áp dụng cho tất cả skill thuộc category `design` (W4:DesignAgent)
> Version: 1.0 | Last Updated: 2026-03-28

---

## Required Sections

Mọi design output PHẢI có:

- [ ] **Visual specifications** — colors, typography, spacing rõ ràng
- [ ] **Responsive considerations** — mobile-first hoặc adaptive
- [ ] **Accessibility** — WCAG 2.1 AA minimum
- [ ] **Design rationale** — giải thích WHY cho design decisions
- [ ] **Interactive states** — hover, active, focus, disabled
- [ ] **Assets list** — icons, images, fonts cần thiết

## Format Standards

| Tiêu chí | Yêu cầu |
|----------|---------|
| Colors | HSL/HEX + semantic naming (--color-primary, --color-surface) |
| Typography | Google Fonts (Inter, Outfit, Roboto), không dùng system defaults |
| Spacing | 4px/8px grid system |
| Breakpoints | mobile: 375px, tablet: 768px, desktop: 1280px, wide: 1440px |
| Animations | ≤300ms cho micro-interactions, ease-out preferred |
| Icons | Lucide, Phosphor, hoặc Heroicons (consistent set) |

## Design Quality Standards

| Tiêu chí | Minimum | Preferred |
|----------|:-------:|:---------:|
| Color palette | 3 colors | 5-7 harmonious colors |
| Contrast ratio | 4.5:1 (AA) | 7:1 (AAA) |
| Touch targets | 44×44px | 48×48px |
| Loading states | Spinner | Skeleton + shimmer |
| Empty states | Text message | Illustration + CTA |
| Error states | Red text | Contextual + recovery action |

## Self-Check Rubric (0-10)

| Dimension | Weight | Mô tả |
|-----------|:------:|-------|
| **Visual Appeal** | 25% | Premium feel, modern aesthetics, WOW factor |
| **Usability** | 25% | Intuitive navigation, clear hierarchy, easy to use |
| **Consistency** | 20% | Design system adherence, uniform spacing/colors |
| **Accessibility** | 15% | WCAG AA, keyboard nav, screen reader friendly |
| **Performance** | 15% | Optimized assets, smooth animations, fast load |

### Grading Scale

| Score | Grade | Action |
|:-----:|:-----:|--------|
| 9-10 | S | Ship — premium quality |
| 7-8 | A | Minor polish → ship |
| 5-6 | B | Design review → iterate |
| 3-4 | C | Major redesign needed |
| 0-2 | F | Start from scratch with references |

**Minimum threshold**: Grade A (7/10) — design PHẢI WOW user.

## CSS Architecture

```css
/* Required structure */
:root {
  /* Colors — HSL for easy theming */
  --color-primary: hsl(220, 90%, 56%);
  --color-surface: hsl(0, 0%, 100%);
  --color-text: hsl(220, 15%, 15%);
  
  /* Spacing — 4px grid */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  
  /* Typography */
  --font-family: 'Inter', 'Segoe UI', sans-serif;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  
  /* Borders & Shadows */
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.1);
  
  /* Transitions */
  --transition-fast: 150ms ease-out;
  --transition-base: 250ms ease-out;
}
```

## Anti-Patterns

```
❌ Plain red/blue/green colors
   → Curated HSL palette, dark mode support

❌ Browser default fonts (Times, Arial)
   → Google Fonts: Inter, Outfit, Roboto

❌ No hover/focus states
   → Interactive elements MUST have state feedback

❌ Fixed pixel widths for layout
   → Responsive: flex/grid, min/max-width, clamp()

❌ Generic "loading..." text
   → Skeleton screens, shimmer effects, progress indicators

❌ Ignoring dark mode
   → Design for both light and dark from the start
```
