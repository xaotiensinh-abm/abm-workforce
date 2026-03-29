---
name: "web-design-guidelines"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "100+ quy tắc audit UI từ Vercel — accessibility, forms, animation, typography, performance, dark mode, touch, i18n. Guidelines inline, không phụ thuộc external URL."
---

# 🌐 Web Design Guidelines — 100+ Rules Audit UI

Skill chính thức từ **Vercel** — audit UI code theo **100+ rules** covering 15 categories. Guidelines **inline** — không cần fetch external.

## Sử dụng khi

- "Review UI code của tôi"
- "Check accessibility"
- "Audit design / UX"
- "Check best practices web"

## KHÔNG sử dụng khi

- Cần tạo design mới từ đầu → dùng `frontend-design`
- Cần tối ưu React performance → dùng `vercel-react-best-practices`
- Cần tra cứu palette/font → dùng `ui-ux-pro-max`
- Cần viết code frontend → dùng `frontend-developer`

---

## VÍ DỤ NHANH

```
Input:  "Review file Button.tsx cho tôi"
Output:
  ## src/Button.tsx
  src/Button.tsx:42 — icon button thiếu aria-label
  src/Button.tsx:18 — input không có label
  src/Button.tsx:55 — animation thiếu prefers-reduced-motion
  src/Button.tsx:67 — transition: all → liệt kê properties cụ thể
```

---

## 15 CATEGORIES — INLINE GUIDELINES

### 1. Focus States
- Interactive elements cần visible focus: `focus-visible:ring-*`
- KHÔNG BAO GIỜ `outline-none` / `outline: none` mà không có focus replacement
- Dùng `:focus-visible` thay `:focus` (tránh focus ring khi click)
- Group focus với `:focus-within` cho compound controls

### 2. Forms
- Inputs cần `autocomplete` và `name` có ý nghĩa
- Dùng đúng `type` (`email`, `tel`, `url`, `number`) và `inputmode`
- KHÔNG bao giờ block paste (`onPaste` + `preventDefault`)
- Labels clickable (`htmlFor` hoặc wrapping control)
- Disable spellcheck trên emails, codes, usernames (`spellCheck={false}`)
- Checkbox/radio: label + control share single hit target (no dead zones)
- Submit button enabled đến khi request bắt đầu; spinner trong request
- Errors inline cạnh fields; focus first error khi submit
- Placeholders kết thúc `…` và hiện example pattern
- Warn trước navigation với unsaved changes (`beforeunload` hoặc router guard)

### 3. Animation
- Check `prefers-reduced-motion` (provide reduced variant hoặc disable)
- CHỈ animate `transform`/`opacity` (compositor-friendly)
- KHÔNG BAO GIỜ `transition: all` — liệt kê properties cụ thể
- Set `transform-origin` chính xác
- SVG: transforms trên wrapper với `transform-box: fill-box; transform-origin: center`
- Animations interruptible — phản hồi user input mid-animation

### 4. Typography
- `…` KHÔNG dùng `...`
- Curly quotes `"` `"` KHÔNG straight `"`
- Non-breaking spaces: `10 MB`, `⌘ K`, brand names
- Loading states kết thúc `…`: "Loading…", "Saving…"
- `font-variant-numeric: tabular-nums` cho number columns
- `text-wrap: balance` hoặc `text-pretty` cho headings

### 5. Content Handling
- Text containers handle long content: `truncate`, `line-clamp-*`, hoặc `break-words`
- Flex children cần `min-w-0` để text truncation hoạt động
- Handle empty states — không render broken UI cho empty strings/arrays
- User-generated content: anticipate short, average, very long inputs

### 6. Images
- `<img>` cần explicit `width` và `height` (tránh CLS)
- Below-fold: `loading="lazy"`
- Above-fold critical: `priority` hoặc `fetchpriority="high"`

### 7. Performance
- Large lists (>50 items): virtualize (`virtua`, `content-visibility: auto`)
- Không layout reads trong render (`getBoundingClientRect`, `offsetHeight`)
- Batch DOM reads/writes; tránh interleaving
- Prefer uncontrolled inputs; controlled inputs phải cheap per keystroke
- `<link rel="preconnect">` cho CDN/asset domains
- Critical fonts: `<link rel="preload">` với `font-display: swap`

### 8. Navigation & State
- URL phản ánh state — filters, tabs, pagination trong query params
- Links dùng `<a>`/`<Link>` (Cmd/Ctrl+click support)
- Deep-link mọi stateful UI (nếu dùng `useState`, consider URL sync)
- Destructive actions cần confirmation hoặc undo window

### 9. Touch & Interaction
- `touch-action: manipulation` (tránh double-tap zoom delay)
- `-webkit-tap-highlight-color` set intentionally
- `overscroll-behavior: contain` trong modals/drawers
- Khi drag: disable text selection, `inert` trên dragged elements

### 10. Safe Areas & Layout
- Full-bleed layouts cần `env(safe-area-inset-*)` cho notches
- Tránh scrollbars không mong muốn: `overflow-x-hidden`
- Flex/grid thay JS measurement cho layout

### 11. Dark Mode & Theming
- `color-scheme: dark` trên `<html>` (fix scrollbar, inputs)
- `<meta name="theme-color">` match page background
- Native `<select>`: explicit `background-color` và `color`

### 12. Locale & i18n
- Dates/times: `Intl.DateTimeFormat` không hardcode formats
- Numbers/currency: `Intl.NumberFormat` không hardcode formats
- Detect language via `Accept-Language` / `navigator.languages`, không IP

### 13. Hydration Safety
- Inputs với `value` cần `onChange` (hoặc dùng `defaultValue`)
- Date/time rendering: guard hydration mismatch (server vs client)
- `suppressHydrationWarning` chỉ khi truly needed

### 14. Hover & Interactive States
- Buttons/links cần `hover:` state (visual feedback)
- Interactive states tăng contrast: hover/active/focus nổi bật hơn rest

### 15. Content & Copy
- Active voice: "Cài đặt CLI" không "CLI sẽ được cài đặt"
- Numerals cho counts: "8 deployments" không "eight"
- Button labels cụ thể: "Lưu API Key" không "Tiếp tục"
- Error messages kèm fix/next step, không chỉ describe problem

---

## ANTI-PATTERNS — FLAG NGAY

| Anti-Pattern | Tại sao sai |
|-------------|------------|
| `user-scalable=no` / `maximum-scale=1` | Disable zoom = violate accessibility |
| `onPaste` + `preventDefault` | Block paste = bad UX |
| `transition: all` | Performance hit, unexpected transitions |
| `outline-none` không có focus replacement | Keyboard users mất focus |
| Inline `onClick` navigation không `<a>` | Mất Cmd+click, middle-click |
| `<div>`/`<span>` với click handlers | Nên dùng `<button>` |
| Images không dimensions | Gây CLS |
| Large arrays `.map()` không virtualization | Performance death |
| Form inputs không labels | Accessibility violation |
| Icon buttons không `aria-label` | Screen readers không đọc được |
| Hardcoded date/number formats | i18n failure |
| `autoFocus` không justification | Mobile UX issue |

---

## OUTPUT FORMAT

Group theo file. Dùng `file:line` format. Ngắn gọn.

```text
## src/Button.tsx
src/Button.tsx:42 — icon button thiếu aria-label
src/Button.tsx:18 — input không có label

## src/Modal.tsx
src/Modal.tsx:12 — thiếu overscroll-behavior: contain
src/Modal.tsx:34 — "..." → "…"

## src/Card.tsx
✓ pass
```

Nêu issue + location. Skip giải thích trừ khi fix non-obvious. Không preamble.

---

## Nguồn gốc
- **Chính thức**: [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) — Vercel
- Guidelines inline — không phụ thuộc external fetch
- Adapt bởi: ABM Workforce v2.3 — Jarvis Orchestrator
