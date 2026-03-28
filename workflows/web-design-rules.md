---
description: 🚨 SUPREME RULES - Quy tắc tối thượng cho thiết kế web (v3.0) — Bao gồm Design Dial System, AI Anti-Slop Rules, Creative Arsenal 50+ patterns, Redesign Workflow
auto_trigger: true
priority: supreme
triggers: [design, UI, UX, web, website, landing page, dashboard, frontend, giao diện, thiết kế, component, button, card, modal, form, navigation, layout, responsive, tailwind, css, html]
---

# 🚨 WEB DESIGN SUPREME RULES v3.0

> **LUẬT TỐI CAO** - Mọi tác vụ thiết kế web PHẢI tuân thủ framework này. Không có ngoại lệ.

---

# PHẦN I: IRON DISCIPLINE - 5 QUY TẮC THÉP

## WD-1: DESIGN SYSTEM FIRST - HỆ THỐNG TRƯỚC
```
❌ FORBIDDEN: Code UI ngay khi chưa có design tokens
✅ REQUIRED: Phải định nghĩa Color/Typography/Spacing TRƯỚC
```
**Quy trình bắt buộc:**
1. Xác định màu chủ đạo (Primary, Secondary, Accent)
2. Chọn font từ `/ui-ux-pro-max` hoặc Google Fonts
3. Dùng 8px grid system cho spacing

---

## WD-2: MOBILE-FIRST ALWAYS - DI ĐỘNG TRƯỚC
```
❌ FORBIDDEN: Thiết kế desktop rồi mới responsive
✅ REQUIRED: BẮT ĐẦU từ mobile (320px) → tablet → desktop
```
**Breakpoints chuẩn:**
- Mobile: 320-767px (default)
- Tablet: 768-1023px (`md:`)
- Desktop: 1024-1439px (`lg:`)
- Large: 1440px+ (`xl:`)

---

## WD-3: ACCESSIBILITY MANDATORY - WCAG AA BẮT BUỘC
```
❌ FORBIDDEN: Bỏ qua accessibility
✅ REQUIRED: Tuân thủ WCAG 2.1 Level AA
```
**Checklist bắt buộc:**
- [ ] Contrast ratio ≥ 4.5:1 cho text nhỏ
- [ ] Contrast ratio ≥ 3:1 cho text lớn (18px+)
- [ ] Tất cả img có alt text
- [ ] Form inputs có labels
- [ ] Focus states rõ ràng
- [ ] Keyboard navigation hoạt động

---

## WD-4: PERFORMANCE CRITICAL - HIỆU SUẤT QUAN TRỌNG
```
❌ FORBIDDEN: UI gây layout shift, LCP > 2.5s
✅ REQUIRED: Core Web Vitals > 90 điểm
```
**Quy tắc:**
- Images phải có width/height cố định (tránh CLS)
- Lazy load cho images below-the-fold
- Font loading không gây FOUT/FOIT
- CSS critical path inline

---

## WD-5: NO PLACEHOLDERS - KHÔNG PLACEHOLDER
```
❌ FORBIDDEN: Lorem ipsum, placeholder images, "Coming soon"
✅ REQUIRED: Dữ liệu thực hoặc realistic mockup
```
**Nếu chưa có data:**
- Dùng generate_image tạo ảnh thật
- Text phải có ý nghĩa, đúng ngữ cảnh
- Số liệu phải hợp lý (không "123", "xxx")

---

# PHẦN II: AESTHETIC STANDARDS - TIÊU CHUẨN THẨM MỸ

## AS-1: COLOR HARMONY - HÀI HÒA MÀU SẮC

### Palette Structure
| Token | Mục đích | Ví dụ |
|-------|----------|-------|
| `--primary` | Brand color chính | #6366F1 (Indigo) |
| `--secondary` | Phụ trợ, ít quan trọng | #64748B (Slate) |
| `--accent` | CTA, hành động chính | #F59E0B (Amber) |
| `--background` | Nền trang | #FFFFFF / #0F172A |
| `--surface` | Nền card, modal | #F8FAFC / #1E293B |
| `--text` | Text chính | #0F172A / #F8FAFC |
| `--muted` | Text phụ | #64748B / #94A3B8 |
| `--border` | Viền | #E2E8F0 / #334155 |

### Rules
- **Không dùng màu ngẫu nhiên** - Mọi màu phải trong palette
- **Semantic colors**: Success (#22C55E), Warning (#F59E0B), Error (#EF4444), Info (#3B82F6)
- **Không quá 5 màu** trong một design

---

## AS-2: TYPOGRAPHY SCALE - HỆ THỐNG CHỮ

### Font Pairing
```css
/* Heading: Modern sans-serif */
font-family: 'Inter', 'Plus Jakarta Sans', 'Outfit', sans-serif;

/* Body: Readable, neutral */
font-family: 'Inter', 'DM Sans', system-ui, sans-serif;
```

### Type Scale (1.25 ratio)
| Token | Size | Line Height | Use |
|-------|------|-------------|-----|
| `text-xs` | 12px | 16px | Captions, footnotes |
| `text-sm` | 14px | 20px | Labels, secondary text |
| `text-base` | 16px | 24px | Body text (default) |
| `text-lg` | 18px | 28px | Lead paragraphs |
| `text-xl` | 20px | 28px | H4 |
| `text-2xl` | 24px | 32px | H3 |
| `text-3xl` | 30px | 36px | H2 |
| `text-4xl` | 36px | 40px | H1 |
| `text-5xl` | 48px | 1 | Hero headlines |

---

## AS-3: SPACING SYSTEM - HỆ THỐNG KHOẢNG CÁCH

### 8px Grid
```
4px  → 0.25rem → Micro spacing
8px  → 0.5rem  → Tight spacing
12px → 0.75rem → Default gap
16px → 1rem    → Standard padding
24px → 1.5rem  → Section spacing
32px → 2rem    → Large gaps
48px → 3rem    → Section margins
64px → 4rem    → Hero sections
```

### Rules
- **Padding trong card**: 16-24px
- **Gap giữa items**: 12-16px
- **Margin giữa sections**: 48-64px
- **Container max-width**: 1280px (max-w-7xl)

---

## AS-4: SHADOW HIERARCHY - HỆ THỐNG BÓNG ĐỔ

```css
/* Elevation levels */
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05);           /* Subtle lift */
--shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);       /* Card default */
--shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);     /* Dropdown, popovers */
--shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.1);     /* Modal, dialogs */
```

### Rules
- **Cards**: shadow-md (resting), shadow-lg (hover)
- **Modals**: shadow-xl
- **Buttons**: không shadow hoặc shadow-sm
- **Dark mode**: Giảm opacity shadows, tăng border

---

## AS-5: BORDER RADIUS CONSISTENCY

```css
--radius-sm: 4px;    /* Badges, small inputs */
--radius-md: 8px;    /* Buttons, cards (DEFAULT) */
--radius-lg: 12px;   /* Large cards, modals */
--radius-xl: 16px;   /* Hero sections */
--radius-full: 9999px; /* Pills, avatars */
```

### Rules
- **Nhất quán**: Chọn 1 style (rounded hoặc sharp) cho toàn bộ design
- **Nested elements**: Inner radius = Outer radius - padding

---

# PHẦN III: ANTI-PATTERNS - ❌ CẤM LÀM

## AP-1: ICONS
| ❌ CẤM | ✅ PHẢI |
|--------|---------|
| Dùng emoji làm icon (🎨 🚀 ⚙️) | Dùng SVG icons (Heroicons, Lucide) |
| Mix icon sets khác nhau | Nhất quán 1 icon set |
| Icon sizes ngẫu nhiên | Cố định 20-24px cho UI icons |

---

## AP-2: INTERACTIONS
| ❌ CẤM | ✅ PHẢI |
|--------|---------|
| Scale on hover gây layout shift | Color/opacity transitions |
| Không có cursor:pointer trên clickable | Luôn có cursor-pointer |
| Transitions quá chậm (>500ms) | 150-300ms là chuẩn |
| Không có hover feedback | Luôn có visual feedback |

---

## AP-3: LIGHT/DARK MODE
| ❌ CẤM | ✅ PHẢI |
|--------|---------|
| Glass bg-white/10 trong light mode | bg-white/80+ trong light mode |
| Text gray-400 trong light mode | Text slate-700+ trong light mode |
| Border trắng trong light mode | Border gray-200 trong light mode |
| Chỉ test 1 mode | Test CẢ HAI modes |

---

## AP-4: LAYOUT
| ❌ CẤM | ✅ PHẢI |
|--------|---------|
| Navbar dính sát top-0 | Floating navbar với margin |
| Content bị navbar che | Padding-top đủ cho fixed nav |
| Mix container widths | Nhất quán max-w-6xl/7xl |
| Horizontal scroll trên mobile | Luôn test 320px width |

---

## AP-5: CONTENT
| ❌ CẤM | ✅ PHẢI |
|--------|---------|
| Lorem ipsum | Text có nghĩa |
| Placeholder.com images | generate_image hoặc ảnh thật |
| "Click here" links | Descriptive link text |
| Số "123", "xxx" | Số liệu hợp lý |

---

# PHẦN IV: COMPONENT STANDARDS - TIÊU CHUẨN COMPONENT

## CS-1: BUTTONS

```css
/* Base button */
height: 40px;           /* Touch target minimum */
padding: 0 16px;
border-radius: 8px;
font-weight: 500;
transition: all 150ms;

/* Variants */
Primary:   bg-primary text-white hover:opacity-90
Secondary: bg-surface border hover:bg-muted/10
Ghost:     bg-transparent hover:bg-muted/10
Danger:    bg-red-500 text-white hover:bg-red-600

/* Sizes */
Small:  height 32px, padding 0 12px, text-sm
Medium: height 40px, padding 0 16px, text-base (default)
Large:  height 48px, padding 0 24px, text-lg
```

---

## CS-2: CARDS

```css
/* Standard card */
padding: 24px;
border-radius: 12px;
background: var(--surface);
border: 1px solid var(--border);
box-shadow: var(--shadow-md);

/* Hover (if interactive) */
cursor: pointer;
transition: shadow 200ms, transform 200ms;
&:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}
```

---

## CS-3: INPUTS

```css
/* Text input */
height: 40px;
padding: 0 12px;
border: 1px solid var(--border);
border-radius: 8px;
background: var(--surface);

/* Focus state */
&:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

/* Error state */
&.error {
  border-color: var(--error);
}
```

---

## CS-4: MODALS

```css
/* Overlay */
position: fixed;
inset: 0;
background: rgba(0, 0, 0, 0.5);
backdrop-filter: blur(4px);

/* Modal container */
max-width: 500px;
margin: auto;
padding: 24px;
border-radius: 16px;
background: var(--surface);
box-shadow: var(--shadow-xl);

/* Animation */
animation: fadeIn 200ms ease-out;
```

---

## CS-5: NAVIGATION

```css
/* Sticky navbar */
position: fixed;
top: 16px;
left: 16px;
right: 16px;
height: 64px;
border-radius: 16px;
background: var(--surface)/95;
backdrop-filter: blur(12px);
border: 1px solid var(--border);
box-shadow: var(--shadow-md);
z-index: 50;

/* Content padding-top */
main {
  padding-top: 96px; /* navbar height + gap */
}
```

---

# PHẦN V: STATE MANAGEMENT - QUẢN LÝ TRẠNG THÁI

## SM-1: LOADING STATES

```
Ưu tiên sử dụng:
1. Skeleton (chuyên nghiệp nhất)
2. Spinner với text "Đang tải..."
3. Progress bar (cho long operations)
```

### Skeleton Example
```html
<div class="animate-pulse">
  <div class="h-4 bg-gray-200 rounded w-3/4"></div>
  <div class="h-4 bg-gray-200 rounded w-1/2 mt-2"></div>
</div>
```

---

## SM-2: ERROR STATES

```
Vị trí:
- Form errors: Inline dưới field
- API errors: Toast ở góc phải dưới
- Critical: Modal với CTA retry

Format:
- Icon warning/error
- Thông báo rõ ràng bằng Tiếng Việt
- Hành động khắc phục (nếu có)
```

---

## SM-3: EMPTY STATES

```
Bắt buộc:
- Illustration hoặc icon
- Tiêu đề rõ ràng
- Mô tả ngắn gọn
- CTA để thêm/tạo mới

Ví dụ:
"Chưa có đơn hàng nào"
"Bắt đầu bằng cách tạo đơn hàng đầu tiên"
[Tạo đơn hàng]
```

---

## SM-4: SUCCESS STATES

```
Feedback:
- Toast xanh "Thành công!" (auto-dismiss 3s)
- Checkmark animation
- Redirect sau 1-2s (nếu phù hợp)
```

---

# PHẦN VI: MOTION & ANIMATION

## MO-1: DURATION STANDARDS

| Duration | Use Case |
|----------|----------|
| 100-150ms | Micro-interactions (hover, focus) |
| 200-300ms | Transitions (slide, fade) |
| 300-500ms | Complex animations (modal, drawer) |

---

## MO-2: EASING CURVES

```css
/* Recommended */
--ease-out: cubic-bezier(0, 0, 0.2, 1);      /* Exits */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1); /* Standard */

/* Avoid */
linear        /* Feels robotic */
ease-in       /* Slow start feels laggy */
```

---

## MO-3: REDUCED MOTION

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

# PHẦN VII: QUY TRÌNH LÀM VIỆC

## 7.1. WORKFLOW TỰ ĐỘNG HÓA ⭐⭐⭐

### KHÔNG BAO GIỜ DỪNG GIỮA CHỪNG
- **KHÔNG** xin phép hay xác nhận trong quá trình làm việc
- **KHÔNG** hỏi "Bạn muốn tôi tiếp tục không?"
- **LUÔN** tiếp tục cho đến khi hoàn tất

### TỰ QUYẾT ĐỊNH APPROACH
- Chọn cách tối ưu nhất và thực hiện luôn
- Sử dụng `/ui-ux-pro-max` search cho design intelligence
- Chỉ hỏi khi thiếu business logic quan trọng

### NOTIFY_USER RULES
**CHỈ** notify khi:
- Hoàn tất TOÀN BỘ công việc
- Có vấn đề block nghiêm trọng
- Cần review implementation plan

**LUÔN** set `ShouldAutoProceed = true` trừ khi có breaking changes

---

## 7.2. UI/UX PRO MAX INTEGRATION

Khi thực hiện tác vụ thiết kế, **BẮT BUỘC** search trước:

```bash
# Search order
python3 ~/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain product
python3 ~/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain style
python3 ~/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain color
python3 ~/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain typography
python3 ~/.gemini/antigravity/.shared/ui-ux-pro-max/scripts/search.py "<keyword>" --domain ux
```

**Domains:** style, color, typography, landing, product, chart, ux, prompt
**Stacks:** html-tailwind, react, nextjs, vue, svelte, swiftui, react-native, flutter

---

# PHẦN VIII: PRE-DELIVERY CHECKLIST

Trước khi deliver UI, **PHẢI** verify:

## Visual Quality
- [ ] Không emoji làm icons
- [ ] Icons từ 1 set duy nhất (Heroicons/Lucide)
- [ ] Brand logos chính xác
- [ ] Hover states không gây layout shift
- [ ] Màu sắc nhất quán với palette

## Interaction
- [ ] Tất cả clickable có cursor-pointer
- [ ] Hover states có visual feedback
- [ ] Transitions 150-300ms
- [ ] Focus states cho keyboard navigation

## Light/Dark Mode
- [ ] Light mode text contrast ≥ 4.5:1
- [ ] Glass elements visible trong light mode
- [ ] Borders visible trong cả 2 modes
- [ ] Test CẢ HAI modes

## Responsive
- [ ] Test tại 320px (mobile)
- [ ] Test tại 768px (tablet)
- [ ] Test tại 1024px (desktop)
- [ ] Không horizontal scroll trên mobile

## Accessibility
- [ ] Tất cả images có alt text
- [ ] Form inputs có labels
- [ ] Color không phải indicator duy nhất
- [ ] prefers-reduced-motion được tôn trọng

## Performance
- [ ] Images có width/height cố định
- [ ] Lazy loading cho below-fold content
- [ ] No layout shift (CLS < 0.1)

---

# PHẦN IX: DESIGN DIAL SYSTEM — HỆ THỐNG NÚM CHỈNH

> **Nguồn:** Tích hợp từ [taste-skill](https://github.com/Leonxlnx/taste-skill)

3 biến điều chỉnh cho phép tinh chỉnh output design mà không cần sửa rules. Đặt giá trị (1-10) theo context dự án.

## DS-1: DESIGN_VARIANCE — Mức Độ Thử Nghiệm Layout

| Level | Mô tả | CSS Guidance |
|-------|--------|--------------|
| **1-3** (Chuẩn) | Centered, symmetric grids, equal paddings | `justify-center`, 12-col grid, uniform `gap` |
| **4-7** (Offset) | Overlapping, varied sizes, left-aligned headers | Negative margins, mixed aspect ratios, asymmetric grid |
| **8-10** (Phá cách) | Masonry, fractional grids, massive empty zones | `grid-template-columns: 2fr 1fr 1fr`, `padding-left: 20vw` |

**Mobile Override (levels 4-10):** Mọi layout asymmetric PHẢI fallback về single-column (`width: 100%`, `padding: 0 1rem`) trên viewport < 768px.

## DS-2: MOTION_INTENSITY — Mức Độ Animation

| Level | Mô tả | Implementation |
|-------|--------|----------------|
| **1-3** (Tĩnh) | Chỉ `:hover` và `:active` CSS states | Không animation tự động |
| **4-7** (Mượt) | Fade-ins, smooth scrolling, cascade delays | `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`, `animation-delay` |
| **8-10** (Phức tạp) | Scroll-triggered reveals, parallax, physics-based | Spring animations, Intersection Observer, scroll-linked |

**Performance rules:**
- CHỈ animate `transform` và `opacity` — KHÔNG BAO GIỜ animate `top`, `left`, `width`, `height`
- `will-change: transform` chỉ dùng khi element đang animate
- Grain/noise filters → `position: fixed; pointer-events: none` — KHÔNG đặt trên scrolling container
- Levels 8-10: animation phức tạp PHẢI isolate trong component riêng, tránh re-render parent

## DS-3: VISUAL_DENSITY — Mật Độ Nội Dung

| Level | Mô tả | Spacing |
|-------|--------|---------|
| **1-3** (Gallery) | Nhiều whitespace, từng element một, cảm giác luxury | Section gap ≥ 4rem, padding ≥ 2.5rem |
| **4-7** (Standard) | Spacing chuẩn cho web app thông thường | Section gap 2-3rem, padding 1-1.5rem |
| **8-10** (Cockpit) | Dense, compact, data-heavy | Padding nhỏ, phân cách bằng `border-top` thay vì cards, `font-family: monospace` cho số |

**Cách sử dụng:**
```
Khi cần landing page premium → DESIGN_VARIANCE: 7, MOTION: 6, DENSITY: 3
Khi cần dashboard analytics  → DESIGN_VARIANCE: 2, MOTION: 3, DENSITY: 8
Khi cần SaaS marketing site  → DESIGN_VARIANCE: 5, MOTION: 5, DENSITY: 5
```

---

# PHẦN X: AI ANTI-SLOP RULES — CHỐNG OUTPUT NHÀM CHÁN

> **Mục đích:** LLM có bias thống kê sinh ra UI generic. Các rules dưới đây **chủ động chống** những pattern nhàm chán.

## SLOP-1: Visual & CSS

| ❌ TRÁNH | ✅ THAY BẰNG | Lý do |
|----------|-------------|-------|
| Neon/outer glow (`box-shadow` phát sáng) | Inner borders hoặc tinted shadows | Glow là dấu hiệu AI điển hình |
| Pure black `#000000` | Off-black: `#0a0a0a`, Zinc-950, Charcoal | Pure black quá harsh |
| Oversaturated accents (saturation > 80%) | Desaturate để blend hài hòa với neutrals | Màu quá chói = unprofessional |
| Gradient text cho headings lớn | Solid color hoặc subtle highlight | Gradient text overused bởi AI |
| Purple/blue "AI gradient" aesthetic | Neutral base + singular considered accent | Dấu hiệu "AI-generated" rõ nhất |
| Mix warm + cool grays cùng project | Chọn 1 gray family, tint consistent | Thiếu nhất quán |
| Flat design không texture | Thêm subtle noise, grain, micro-patterns | Pure flat = sterile |

## SLOP-2: Typography

| ❌ TRÁNH (cho premium/creative) | ✅ THAY BẰNG |
|---------------------------------|-------------|
| Inter everywhere (cho landing page premium) | `Geist`, `Outfit`, `Cabinet Grotesk`, `Satoshi`, `Plus Jakarta Sans` |
| Chỉ dùng Regular (400) + Bold (700) | Thêm Medium (500) + SemiBold (600) cho hierarchy tinh tế |
| All-caps subheaders gây spam cảm giác | Lowercase italic, sentence case, small-caps |
| Orphaned words (từ đơn dòng cuối) | `text-wrap: balance` hoặc `text-wrap: pretty` |

> **LƯU Ý:** Inter vẫn tốt cho dashboards, data-heavy interfaces, SaaS apps. Chỉ **discourage** cho premium landing pages, creative portfolios.

## SLOP-3: Layout

| ❌ TRÁNH (khi DESIGN_VARIANCE > 4) | ✅ THAY BẰNG |
|------------------------------------|-------------|
| Centered Hero H1 (quá generic) | Split Screen 50/50, Left-aligned + Right asset, Asymmetric whitespace |
| 3-column equal cards (feature row) | 2-col Zig-Zag, asymmetric grid, horizontal scroll |
| Navbar dính sát `top: 0` | Floating navbar với margin + blur backdrop |
| `h-screen` cho full-height | `min-height: 100dvh` (fix iOS Safari jumping) |
| Complex flexbox math `calc(33%-1rem)` | CSS Grid `grid-template-columns: repeat(3, 1fr)` |

## SLOP-4: Content & Data ("Jane Doe Effect")

| ❌ TRÁNH | ✅ THAY BẰNG |
|----------|-------------|
| Generic names: "John Doe", "Sarah Chan" | Creative, realistic-sounding names |
| Generic avatars (SVG egg, Lucide user icon) | Creative photo placeholders hoặc styled initials |
| Round numbers: `99.99%`, `50%`, `1234567` | Organic data: `47.2%`, `+1 (312) 847-1928` |
| Startup slop: "Acme", "Nexus", "SmartFlow" | Premium, contextual brand names |
| AI clichés: "Elevate", "Seamless", "Unleash" | Concrete, specific verbs |
| Broken Unsplash links | `https://picsum.photos/seed/{name}/W/H` hoặc SVG placeholders |

## SLOP-5: Cursor & Custom UI

| ❌ TRÁNH | Lý do |
|----------|-------|
| Custom mouse cursors | Performance + accessibility harm |
| Z-index spam (`z-50`, `z-[9999]`) | Chỉ dùng cho systemic layers: nav, modal, overlay |
| shadcn/ui default state | PHẢI customize radii, colors, shadows theo project aesthetic |

---

# PHẦN XI: CREATIVE ARSENAL — THƯ VIỆN UI PREMIUM

> **Mục đích:** Thay vì AI chọn generic patterns, kéo từ thư viện này để output ‹ấn tượng và đáng nhớ.

## CA-1: Vibe Archetypes (chọn 1 cho project)

| Archetype | Mô tả | Context |
|-----------|--------|---------|
| **Ethereal Glass** | Deep OLED black, radial mesh gradients, `backdrop-blur` heavy, white/10 hairlines | SaaS, AI, Tech |
| **Editorial Luxury** | Warm creams, muted sage, Variable Serif headings, CSS noise grain `opacity: 0.03` | Lifestyle, Real Estate, Agency |
| **Soft Structuralism** | Silver-grey/white, massive bold Grotesk, ultra-diffused ambient shadows | Consumer, Health, Portfolio |

## CA-2: Layout Archetypes (chọn 1 cho page)

| Archetype | Mô tả | Mobile Collapse |
|-----------|--------|-----------------|
| **Asymmetrical Bento** | CSS Grid masonry, varied `col-span` sizes (Apple Control Center style) | → `grid-cols-1`, reset col-span |
| **Z-Axis Cascade** | Cards stacked, overlapping, slight rotations (-2° to 3°) | → Remove rotation + negative margins |
| **Editorial Split** | 50% massive typography left + 50% interactive right | → Full-width stack, text on top |

## CA-3: Navigation & Menus
- **Mac OS Dock Magnification** — Icons scale fluidly on hover
- **Magnetic Button** — Buttons pull toward cursor
- **Gooey Menu** — Sub-items detach like viscous liquid
- **Dynamic Island** — Pill-shaped UI morphing to show status
- **Floating Speed Dial** — FAB springs into curved line of actions
- **Mega Menu Reveal** — Full-screen stagger-fade dropdowns

## CA-4: Cards & Containers
- **Parallax Tilt Card** — 3D tilt tracking mouse coordinates
- **Spotlight Border Card** — Borders illuminate under cursor
- **Glassmorphism Panel** — True frosted glass + inner refraction borders (`border-white/10` + `shadow: inset 0 1px 0 rgba(255,255,255,0.1)`)
- **Holographic Foil Card** — Iridescent rainbow reflections on hover
- **Morphing Modal** — Button expands into its own full-screen dialog
- **Double-Bezel (Doppelrand)** — Outer shell (`ring-1`, padding, large radius) + Inner core (own bg, inner highlight, smaller radius) → machined hardware aesthetic

## CA-5: Scroll Animations
- **Sticky Scroll Stack** — Cards stick to top and physically stack
- **Horizontal Scroll Hijack** — Vertical scroll → horizontal gallery pan
- **Zoom Parallax** — Central image zooms with scroll
- **Scroll Progress Path** — SVG lines draw as user scrolls
- **Curtain Reveal** — Hero section parts like curtain on scroll

## CA-6: Typography Effects
- **Kinetic Marquee** — Infinite text bands, reverse on scroll
- **Text Mask Reveal** — Typography as transparent window to video
- **Text Scramble** — Matrix-style character decoding on load
- **Gradient Stroke Animation** — Outlined text with running gradient

## CA-7: Micro-Interactions
- **Particle Explosion Button** — CTAs shatter into particles on click
- **Skeleton Shimmer** — Shifting light across placeholder boxes
- **Directional Hover** — Fill enters from the exact side mouse enters
- **Ripple Click Effect** — Waves from click coordinates
- **Mesh Gradient Background** — Organic lava-lamp animated color blobs
- **Perpetual Micro-Interactions** — Mỗi component nên có 1 animation "sống" (pulse, float, shimmer) khi idle

## CA-8: Component Techniques

### Island Buttons
Primary buttons = fully rounded pills (`border-radius: 9999px`, pad `1.5rem 0.75rem`). Trailing icon (→) PHẢI nested trong circular wrapper riêng, flush với button.

### Spatial Rhythm
- Section padding tối thiểu `py: 6rem` cho density 1-3
- Eyebrow tags: pill badges nhỏ (`border-radius: 9999px`, `font-size: 10px`, `letter-spacing: 0.2em`, uppercase) trước H1/H2

### Perpetual Bento Motion (cho SaaS features)
- **Intelligent List** — Auto-sorting items với layout animations
- **Command Input** — Multi-step typewriter effect + blinking cursor
- **Live Status** — "Breathing" indicators + overshoot spring notifications
- **Data Stream** — Infinite horizontal carousel (seamless loop)
- **Focus Mode** — Staggered text highlight + floating action toolbar

---

# PHẦN XII: REDESIGN WORKFLOW — QUY TRÌNH CẢI THIỆN PROJECT CÓ SẴN

> Dùng khi cần nâng cấp UI cho codebase hiện tại, KHÔNG build from scratch.

## RD-1: QUY TRÌNH 3 BƯỚC

1. **SCAN** — Đọc codebase, xác định framework, styling method, design patterns hiện tại
2. **DIAGNOSE** — Chạy qua audit checklist bên dưới, liệt kê MỌI vấn đề
3. **FIX** — Áp dụng targeted upgrades, KHÔNG rewrite from scratch

## RD-2: DESIGN AUDIT CHECKLIST

### Typography
- [ ] Dùng browser default font hoặc chỉ Inter?
- [ ] Headlines thiếu presence (size nhỏ, tracking rộng, line-height cao)?
- [ ] Body text quá rộng (> 65 characters)?
- [ ] Chỉ dùng Regular + Bold, thiếu Medium/SemiBold?
- [ ] Numbers không dùng tabular figures?
- [ ] Orphaned words?

### Color & Surfaces
- [ ] Pure `#000000` background?
- [ ] Oversaturated accents (> 80% saturation)?
- [ ] Nhiều hơn 1 accent color?
- [ ] Mix warm + cool grays?
- [ ] Purple/blue AI gradient aesthetic?
- [ ] Flat design zero texture?
- [ ] Inconsistent shadow light direction?
- [ ] Random dark sections trong light page?

### Layout
- [ ] Centered everything?
- [ ] 3-column equal cards overuse?
- [ ] Navbar dính `top: 0` không floating?
- [ ] Cards bọc mọi thứ (overuse)?
- [ ] Horizontal scroll trên mobile?

### Interactivity
- [ ] Không hover states?
- [ ] Không loading states?
- [ ] Không empty states?
- [ ] Không error states?
- [ ] Transitions instant (0ms)?

### Content
- [ ] Generic placeholder text?
- [ ] Broken image links?
- [ ] Fake round numbers?
- [ ] Generic brand names?

## RD-3: FIX PRIORITY ORDER

Áp dụng theo thứ tự — tác động lớn nhất, rủi ro thấp nhất trước:

| Priority | Fix | Impact | Risk |
|----------|-----|--------|------|
| 1 | **Font swap** | ★★★★★ | Rất thấp |
| 2 | **Color palette cleanup** | ★★★★☆ | Thấp |
| 3 | **Hover + active states** | ★★★★☆ | Thấp |
| 4 | **Layout + spacing** | ★★★★☆ | Trung bình |
| 5 | **Replace generic components** | ★★★☆☆ | Trung bình |
| 6 | **Add loading/empty/error states** | ★★★☆☆ | Trung bình |
| 7 | **Polish typography scale** | ★★☆☆☆ | Thấp |

## RD-4: REDESIGN RULES

- **Work with existing stack** — KHÔNG migrate frameworks/styling libraries
- **Don't break functionality** — Test sau mỗi thay đổi
- **Check dependencies** — Verify `package.json` trước khi import library mới
- **Check Tailwind version** — v3 vs v4 syntax khác nhau
- **Vanilla fallback** — Nếu project không có framework, dùng vanilla CSS
- **Small, focused changes** — Targeted improvements > big rewrites

---

# PHẦN XIII: ENFORCEMENT - CƠ CHẾ CƯỠNG CHẾ

## Khi phát hiện vi phạm:

```
⚠️ VI PHẠM RULE [RULE-ID]: [TÊN RULE]
[Mô tả vi phạm cụ thể]
→ [Hướng dẫn sửa]
```

### Ví dụ:
```
⚠️ VI PHẠM RULE SLOP-1: PURE BLACK
Bạn đang sử dụng #000000 làm background.
→ Thay bằng off-black: #0a0a0a hoặc zinc-950
```

## Cơ chế xử lý:
1. **DỪNG LẠI** - Không tiếp tục thực hiện
2. **CẢNH BÁO** - Thông báo rule bị vi phạm
3. **YÊU CẦU** - Hướng dẫn cách sửa
4. **TỰ SỬA** - Fix ngay nếu có thể

---

*Web Design Supreme Rules v3.0*
*"Excellence in Every Pixel — Anti-Slop Edition"*
*Cập nhật: 2026-03-17*
*Tích hợp: [taste-skill](https://github.com/Leonxlnx/taste-skill) by Leonxlnx*
