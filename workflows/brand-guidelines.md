---
description: Áp dụng brand colors và typography (Anthropic style) cho artifacts
---

Workflow áp dụng Anthropic brand identity cho các artifacts: presentations, documents, UI.

---

## Brand Colors

### Main Colors
| Color | Hex | RGB | Dùng cho |
|-------|-----|-----|----------|
| **Dark** | `#141413` | 20,20,19 | Primary text, dark backgrounds |
| **Light** | `#faf9f5` | 250,249,245 | Light backgrounds, text on dark |
| **Mid Gray** | `#b0aea5` | 176,174,165 | Secondary elements |
| **Light Gray** | `#e8e6dc` | 232,230,220 | Subtle backgrounds |

### Accent Colors
| Color | Hex | RGB |
|-------|-----|-----|
| **Orange** | `#d97757` | 217,119,87 |
| **Blue** | `#6a9bcc` | 106,155,204 |
| **Green** | `#788c5d` | 120,140,93 |

---

## Typography

| Element | Font | Fallback |
|---------|------|----------|
| **Headings** (24pt+) | Poppins | Arial |
| **Body Text** | Lora | Georgia |

---

## Smart Styling Rules

1. **Text Styling**:
   - Headings (24pt+): Poppins font
   - Body text: Lora font
   - Smart color selection based on background

2. **Shape & Accent Colors**:
   - Non-text shapes use accent colors
   - Cycle through: orange → blue → green
   - Maintains visual interest

---

## Python Implementation (pptx)

```python
from pptx.util import Pt
from pptx.dml.color import RGBColor

# Colors
DARK = RGBColor(20, 20, 19)
LIGHT = RGBColor(250, 249, 245)
ORANGE = RGBColor(217, 119, 87)
BLUE = RGBColor(106, 155, 204)
GREEN = RGBColor(120, 140, 93)

# Apply to heading
run.font.name = 'Poppins'
run.font.size = Pt(24)
run.font.color.rgb = DARK

# Apply to body
run.font.name = 'Lora'
run.font.size = Pt(12)
```

---

## CSS Implementation

```css
:root {
  --brand-dark: #141413;
  --brand-light: #faf9f5;
  --brand-orange: #d97757;
  --brand-blue: #6a9bcc;
  --brand-green: #788c5d;
}

h1, h2, h3 {
  font-family: 'Poppins', Arial, sans-serif;
  color: var(--brand-dark);
}

body {
  font-family: 'Lora', Georgia, serif;
  background: var(--brand-light);
}

.accent-1 { color: var(--brand-orange); }
.accent-2 { color: var(--brand-blue); }
.accent-3 { color: var(--brand-green); }
```

---

## Keywords

branding, corporate identity, visual identity, styling, brand colors, typography, Anthropic brand, visual formatting
