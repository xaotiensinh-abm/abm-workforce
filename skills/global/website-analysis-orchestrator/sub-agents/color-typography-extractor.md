# @Color_Typography_Extractor

## Role
Design Token Agent - Extract và document visual design system

## Mission
Extract colors, typography, spacing từ screenshots để build design tokens

## Tools Required
- `view_file`: Analyze screenshots
- Image color extraction
- `write_to_file`: Document tokens

## Input
```json
{
  "screenshots": ["path/to/homepage.png", "..."],
  "session_id": "uuid",
  "artifacts_dir": "/path/to/session/artifacts"
}
```

## Execution Steps

### 1. Color Palette Extraction
```markdown
Identify từ screenshots:

Brand Colors:
- Primary (most prominent brand color)
- Secondary (supporting brand color)
- Accent (highlights, CTAs)

Neutral Colors:
- Gray scale (typically 9 shades)
- Background colors
- Text colors

Semantic Colors:
- Success (green)
- Warning (yellow/orange)
- Error (red)
- Info (blue)
```

### 2. Typography Analysis
```markdown
Identify fonts:
1. Check page source hoặc guess từ visual
2. Common combinations:
   - Inter + System UI
   - Poppins + Roboto
   - DM Sans + DM Serif

Font scale:
- H1: ~48-64px
- H2: ~36-48px
- H3: ~24-30px
- H4: ~20-24px
- Body: ~16-18px
- Small: ~14px
- Caption: ~12px

Font weights:
- Bold (700) for headings
- Semibold (600) for subheadings
- Regular (400) for body
- Medium (500) for emphasis
```

### 3. Spacing System Analysis
```markdown
Measure consistent spacing:

Base unit detection:
- 4px system (4, 8, 12, 16, 24, 32, 48, 64)
- 8px system (8, 16, 24, 32, 48, 64, 96)

Spacing uses:
- Component padding
- Section margins
- Grid gaps
- Line heights
```

### 4. Border & Shadow Analysis
```markdown
Border radius:
- None (0px) - sharp corners
- Small (4px) - subtle rounding
- Medium (8px) - standard cards
- Large (12-16px) - prominent elements
- Full (9999px) - pills, avatars

Shadows:
- Subtle: 0 1px 3px rgba(0,0,0,0.1)
- Medium: 0 4px 6px rgba(0,0,0,0.1)
- Large: 0 10px 25px rgba(0,0,0,0.15)
- Colored: 0 4px 14px rgba(primary, 0.25)
```

## Output

### design_tokens.md
```markdown
# Design Tokens: [Website Name]

## Color Palette

### Brand Colors
| Token | Hex | RGB | Usage |
|-------|-----|-----|-------|
| `--color-primary` | #6366F1 | 99, 102, 241 | CTAs, links, active states |
| `--color-primary-dark` | #4F46E5 | 79, 70, 229 | Hover states |
| `--color-primary-light` | #A5B4FC | 165, 180, 252 | Backgrounds, badges |
| `--color-secondary` | #EC4899 | 236, 72, 153 | Accents, highlights |

### Neutral Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-gray-50` | #F9FAFB | Page background |
| `--color-gray-100` | #F3F4F6 | Card background |
| `--color-gray-200` | #E5E7EB | Borders, dividers |
| `--color-gray-300` | #D1D5DB | Disabled text |
| `--color-gray-400` | #9CA3AF | Placeholder text |
| `--color-gray-500` | #6B7280 | Secondary text |
| `--color-gray-600` | #4B5563 | Body text |
| `--color-gray-700` | #374151 | Headings |
| `--color-gray-800` | #1F2937 | Dark text |
| `--color-gray-900` | #111827 | Darkest text |

### Semantic Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-success` | #10B981 | Success states |
| `--color-warning` | #F59E0B | Warning states |
| `--color-error` | #EF4444 | Error states |
| `--color-info` | #3B82F6 | Info states |

---

## Typography

### Font Families
```css
--font-heading: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### Font Scale
| Token | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| `--text-xs` | 12px | 16px | 400 | Captions, labels |
| `--text-sm` | 14px | 20px | 400 | Secondary text |
| `--text-base` | 16px | 24px | 400 | Body text |
| `--text-lg` | 18px | 28px | 400 | Lead paragraphs |
| `--text-xl` | 20px | 28px | 500 | H4, card titles |
| `--text-2xl` | 24px | 32px | 600 | H3 |
| `--text-3xl` | 30px | 36px | 600 | H2 |
| `--text-4xl` | 36px | 40px | 700 | H1 (mobile) |
| `--text-5xl` | 48px | 48px | 700 | H1 (desktop) |
| `--text-6xl` | 64px | 64px | 800 | Hero headlines |

### Font Weights
```css
--font-regular: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
--font-extrabold: 800;
```

---

## Spacing System

### Base Unit: 4px

| Token | Value | Usage |
|-------|-------|-------|
| `--space-0` | 0 | Reset |
| `--space-1` | 4px | Tight spacing |
| `--space-2` | 8px | Icon gaps |
| `--space-3` | 12px | Small padding |
| `--space-4` | 16px | Standard padding |
| `--space-5` | 20px | |
| `--space-6` | 24px | Card padding |
| `--space-8` | 32px | Section gap |
| `--space-10` | 40px | |
| `--space-12` | 48px | Large gap |
| `--space-16` | 64px | Section padding |
| `--space-20` | 80px | |
| `--space-24` | 96px | Hero padding |
| `--space-32` | 128px | Page sections |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-none` | 0 | Sharp corners |
| `--radius-sm` | 4px | Buttons, inputs |
| `--radius-md` | 8px | Cards |
| `--radius-lg` | 12px | Modals |
| `--radius-xl` | 16px | Featured cards |
| `--radius-2xl` | 24px | Hero elements |
| `--radius-full` | 9999px | Pills, avatars |

---

## Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | 0 1px 2px rgba(0,0,0,0.05) | Subtle elevation |
| `--shadow-md` | 0 4px 6px -1px rgba(0,0,0,0.1) | Cards |
| `--shadow-lg` | 0 10px 15px -3px rgba(0,0,0,0.1) | Dropdowns |
| `--shadow-xl` | 0 20px 25px -5px rgba(0,0,0,0.1) | Modals |
| `--shadow-2xl` | 0 25px 50px -12px rgba(0,0,0,0.25) | Large elements |
| `--shadow-inner` | inset 0 2px 4px rgba(0,0,0,0.06) | Inputs |
| `--shadow-colored` | 0 4px 14px rgba(99,102,241,0.25) | CTA hover |

---

## Transitions

| Token | Value | Usage |
|-------|-------|-------|
| `--transition-fast` | 150ms ease | Hovers, toggles |
| `--transition-base` | 200ms ease | Most interactions |
| `--transition-slow` | 300ms ease | Modals, reveals |
| `--transition-slower` | 500ms ease | Page transitions |

---

## Z-Index Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--z-dropdown` | 10 | Dropdowns |
| `--z-sticky` | 20 | Sticky elements |
| `--z-fixed` | 30 | Fixed nav |
| `--z-modal-backdrop` | 40 | Modal overlay |
| `--z-modal` | 50 | Modals |
| `--z-popover` | 60 | Popovers |
| `--z-tooltip` | 70 | Tooltips |

---

## CSS Custom Properties (Ready to Copy)

```css
:root {
  /* Colors */
  --color-primary: #6366F1;
  --color-primary-dark: #4F46E5;
  --color-primary-light: #A5B4FC;
  --color-secondary: #EC4899;
  
  --color-gray-50: #F9FAFB;
  --color-gray-100: #F3F4F6;
  --color-gray-200: #E5E7EB;
  --color-gray-300: #D1D5DB;
  --color-gray-400: #9CA3AF;
  --color-gray-500: #6B7280;
  --color-gray-600: #4B5563;
  --color-gray-700: #374151;
  --color-gray-800: #1F2937;
  --color-gray-900: #111827;
  
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  --color-info: #3B82F6;
  
  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  /* Spacing */
  --space-unit: 4px;
  
  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
  
  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
}
```
```

## Handoff Data
```json
{
  "agent": "@Color_Typography_Extractor",
  "status": "completed",
  "output": {
    "tokens_file": "artifacts/design_tokens.md",
    "css_variables": "artifacts/tokens.css",
    "summary": {
      "primary_color": "#6366F1",
      "font_family": "Inter",
      "spacing_unit": "4px",
      "total_tokens": 85
    }
  }
}
```
