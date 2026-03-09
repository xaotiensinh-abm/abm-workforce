---
name: "web-design-guidelines"
description: "100+ quy tắc audit UI từ Vercel — accessibility, forms, animation, typography, images, performance, navigation, dark mode, touch, i18n. Nguồn chính thức."
---

# 🌐 Web Design Guidelines — 100+ Rules Audit UI

Skill chính thức từ **Vercel** — audit UI code theo **100+ rules** covering accessibility, performance, UX. Fetch guidelines từ source mỗi lần review.

## Sử dụng khi

- "Review UI code của tôi"
- "Check accessibility"
- "Audit design"
- "Review UX"
- "Check best practices"

## KHÔNG sử dụng khi

- Cần tạo design từ đầu → dùng `frontend-design`
- Cần optimization React → dùng `vercel-react-best-practices`

---

## CATEGORIES

### 1. Accessibility (CRITICAL)
- `aria-labels` — Semantic HTML, ARIA labels đầy đủ
- `keyboard-handlers` — Keyboard navigation hoạt động
- `focus-visible` — Focus indicators rõ ràng
- `color-contrast` — WCAG contrast ratios

### 2. Focus States
- Visible focus rings
- `focus-visible` patterns
- Tab order logic

### 3. Forms
- `autocomplete` attributes
- Validation UX
- Error handling rõ ràng
- Label associations

### 4. Animation
- `prefers-reduced-motion` check
- Compositor-friendly transforms
- Duration guidelines

### 5. Typography
- Curly quotes (`"` thay `"`)
- Ellipsis character (`…` thay `...`)
- `tabular-nums` cho số liệu
- Số với font-variant-numeric

### 6. Images
- `width`/`height` attributes (tránh CLS)
- Lazy loading
- Alt text
- Responsive `srcset`

### 7. Performance
- Virtualization cho long lists
- Tránh layout thrashing
- `preconnect` cho external domains
- Font loading strategy

### 8. Navigation & State
- URL reflects app state
- Deep-linking support
- Browser back/forward hoạt động
- Scroll position restore

### 9. Dark Mode & Theming
- `color-scheme` meta
- `theme-color` meta tag
- CSS custom properties
- System preference detection

### 10. Touch & Interaction
- `touch-action` control
- Tap highlight customization
- Gesture handling
- Mobile-specific patterns

### 11. Locale & i18n
- `Intl.DateTimeFormat` cho dates
- `Intl.NumberFormat` cho numbers
- RTL layout support
- Language-specific typography

---

## QUY TRÌNH REVIEW

```
Bước 1: Fetch guidelines mới nhất từ source
Bước 2: Đọc files cần review
Bước 3: Check TỪNG rule trong guidelines
Bước 4: Output format:
   file:line — [rule-name] — mô tả issue
```

### Ví dụ output
```
src/components/Button.tsx:12 — aria-labels — Missing aria-label on icon button
src/pages/Home.tsx:45 — image-dimensions — Image missing width/height attributes
src/styles/theme.css:8 — color-contrast — Text contrast ratio 3.2:1 < 4.5:1 required
```

---

## Guidelines Source

Fetch fresh mỗi lần review:
```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

---

## Nguồn gốc
- **Chính thức**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — Vercel
- 455K+ installs trên skills.sh (#1 toàn bộ leaderboard)
- Adapt bởi: ABM Workforce v2.2 — Jarvis Orchestrator
