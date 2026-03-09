---
name: "ui-ux-pro-max"
description: "Kho tàng design intelligence cho web/mobile — 50+ styles, 97 palettes, 57 font pairings, 99 UX guidelines, 25 chart types. 9 stacks. Pre-delivery checklist. Giao tiếp tiếng Việt."
---

# 🎨 UI/UX Pro Max — Design Intelligence

Skill tra cứu design toàn diện cho web và mobile. Chứa **50+ styles, 97 palettes, 57 font pairings, 99 UX rules, 25 chart types** trên **9 technology stacks**.

## Sử dụng khi

- Thiết kế UI components hoặc trang mới
- Chọn color palette và typography
- Review code cho UX issues
- Xây landing pages hoặc dashboards
- Kiểm tra accessibility requirements

## KHÔNG sử dụng khi

- Cần code implementation cụ thể → dùng `frontend-developer`
- Cần methodology design thinking → dùng `frontend-design`
- Cần React/Next.js optimization → dùng `vercel-react-best-practices`

---

## VÍ DỤ NHANH

```
Input:  "Thiết kế dashboard SaaS"
Output:
  Palette: Midnight Pro (#0F172A, #3B82F6, #F1F5F9)
  Font: Space Grotesk (heading) + Inter (body)
  Spacing: 4px base unit, scale ×2/×3/×4/×6/×8
  Shadows: 3 levels (sm, md, lg)
  → Check pre-delivery checklist trước khi ship
```

## QUY TẮC THEO MỨC ĐỘ ƯU TIÊN

| Ưu tiên | Category | Mức ảnh hưởng | Domain |
|---------|----------|--------------|--------|
| 1 | **Accessibility** | 🔴 CRITICAL | `ux` |
| 2 | **Touch & Interaction** | 🔴 CRITICAL | `ux` |
| 3 | **Performance** | 🟡 HIGH | `ux` |
| 4 | **Layout & Responsive** | 🟡 HIGH | `ux` |
| 5 | **Typography & Color** | 🟢 MEDIUM | `typography`, `color` |
| 6 | **Animation** | 🟢 MEDIUM | `ux` |
| 7 | **Style Selection** | 🟢 MEDIUM | `style` |
| 8 | **Charts & Data** | ⚪ LOW | `chart` |

---

## TRA CỨU NHANH — 8 CATEGORY

### 1. Accessibility (CRITICAL)
- `color-contrast` — Tỷ lệ contrast tối thiểu **4.5:1** cho text thường
- `focus-states` — Focus rings rõ ràng trên các interactive elements
- `alt-text` — Alt text mô tả cho ảnh có ý nghĩa
- `aria-labels` — `aria-label` cho icon-only buttons
- `keyboard-nav` — Tab order khớp visual order
- `form-labels` — Dùng `<label>` với thuộc tính `for`

### 2. Touch & Interaction (CRITICAL)
- `touch-target-size` — Touch target tối thiểu **44x44px**
- `hover-vs-tap` — Dùng click/tap cho tương tác chính
- `loading-buttons` — Disable button khi đang async
- `error-feedback` — Error messages rõ ràng gần vấn đề
- `cursor-pointer` — `cursor: pointer` cho clickable elements

### 3. Performance (HIGH)
- `image-optimization` — WebP, `srcset`, lazy loading
- `reduced-motion` — Check `prefers-reduced-motion`
- `content-jumping` — Reserve space cho async content

### 4. Layout & Responsive (HIGH)
- `viewport-meta` — `width=device-width initial-scale=1`
- `readable-font-size` — Tối thiểu **16px** body text trên mobile
- `horizontal-scroll` — Content fit viewport width
- `z-index-management` — Z-index scale: 10, 20, 30, 50

### 5. Typography & Color (MEDIUM)
- `line-height` — Dùng **1.5-1.75** cho body text
- `line-length` — Giới hạn **65-75 ký tự** mỗi dòng
- `font-pairing` — Match heading/body font personalities

### 6. Animation (MEDIUM)
- `duration-timing` — **150-300ms** cho micro-interactions
- `transform-performance` — Dùng `transform`/`opacity`, KHÔNG dùng `width`/`height`
- `loading-states` — Skeleton screens hoặc spinners

### 7. Style Selection (MEDIUM)
- `style-match` — Style phải match loại sản phẩm
- `consistency` — Cùng style xuyên suốt tất cả pages
- `no-emoji-icons` — Dùng SVG icons, KHÔNG dùng emoji

### 8. Charts & Data (LOW)
- `chart-type` — Chart type phải match data type
- `color-guidance` — Accessible color palettes
- `data-table` — Cung cấp table thay thế cho accessible

---

## 10 PALETTES NỔI BẬT

| # | Tên | Dùng cho | Màu chính |
|:-:|-----|----------|-----------|
| 1 | **Midnight Pro** | SaaS Dashboard | `#0F172A` `#1E293B` `#3B82F6` `#60A5FA` `#F1F5F9` |
| 2 | **Warm Minimal** | Landing Page | `#1C1917` `#78716C` `#F59E0B` `#FFFBEB` `#FAFAF9` |
| 3 | **Ocean Depth** | Fintech | `#0C4A6E` `#0284C7` `#38BDF8` `#E0F2FE` `#F0F9FF` |
| 4 | **Forest Green** | Health/Eco | `#14532D` `#16A34A` `#4ADE80` `#DCFCE7` `#F0FDF4` |
| 5 | **Royal Purple** | Creative/AI | `#3B0764` `#7C3AED` `#A78BFA` `#EDE9FE` `#FAF5FF` |
| 6 | **Coral Sunset** | E-commerce | `#7F1D1D` `#EF4444` `#FB923C` `#FEF3C7` `#FFFBEB` |
| 7 | **Slate Modern** | Portfolio | `#020617` `#334155` `#94A3B8` `#E2E8F0` `#F8FAFC` |
| 8 | **Neon Cyber** | Gaming/Tech | `#0A0A0A` `#6D28D9` `#06B6D4` `#22D3EE` `#F5F3FF` |
| 9 | **Sand Dune** | Luxury | `#1C1917` `#A8A29E` `#D6D3D1` `#F5F5F4` `#FAFAF9` |
| 10 | **Electric Blue** | Startup | `#0C0A09` `#2563EB` `#3B82F6` `#DBEAFE` `#EFF6FF` |

## 10 FONT PAIRINGS

| # | Heading | Body | Vibe |
|:-:|---------|------|------|
| 1 | **Inter** | Inter | Clean, neutral, startup |
| 2 | **Space Grotesk** | Inter | Tech, modern, bold |
| 3 | **Outfit** | DM Sans | Friendly, rounded, SaaS |
| 4 | **Playfair Display** | Source Sans 3 | Editorial, premium, luxury |
| 5 | **Satoshi** | General Sans | Minimal, contemporary |
| 6 | **Cal Sans** | Inter | Product, Vercel-like |
| 7 | **Plus Jakarta Sans** | Plus Jakarta Sans | Geometric, versatile |
| 8 | **Fraunces** | Work Sans | Creative, distinctive |
| 9 | **Sora** | DM Sans | Futuristic, AI vibes |
| 10 | **Libre Baskerville** | Karla | Classic + modern blend |

## QUY TRÌNH SỬ DỤNG

### Bước 1: Phân tích yêu cầu
- Xác định loại project (landing page, dashboard, e-commerce, SaaS...)
- Xác định target audience
- Xác định devices (desktop, mobile, tablet)

### Bước 2: Generate Design System (BẮT BUỘC)
Trước mọi implementation, PHẢI tạo:
```
1. Color Palette — primary, secondary, accent, neutral, semantic
2. Typography Scale — headings, body, captions, labels
3. Spacing System — base unit + scale (4, 8, 12, 16, 24, 32, 48, 64)
4. Border Radius — consistent rounding
5. Shadow System — elevation levels
6. Breakpoints — mobile-first responsive
```

### Bước 3: Stack Guidelines
Áp dụng guidelines theo stack:

| Stack | Áp dụng |
|-------|---------|
| `html-tailwind` | Default — Tailwind utility classes |
| `react` | React components + hooks |
| `next` | Next.js App Router + RSC |
| `vue` | Vue 3 Composition API |
| `svelte` | Svelte 5 runes |
| `react-native` | React Native + Expo |
| `flutter` | Flutter widgets |
| `swiftui` | SwiftUI views |
| `vanilla` | Pure HTML/CSS/JS |

---

## PRE-DELIVERY CHECKLIST

### ✅ Visual Quality
- [ ] Colors có đủ contrast (4.5:1 text, 3:1 UI)
- [ ] Typography hierarchy rõ ràng
- [ ] Spacing nhất quán (dùng design tokens)
- [ ] Icons cùng style và size

### ✅ Interaction
- [ ] Tất cả interactive elements có hover/active states
- [ ] Loading states cho async operations
- [ ] Error states hiển thị rõ ràng
- [ ] Touch targets ≥ 44px

### ✅ Light/Dark Mode
- [ ] Cả hai mode hoạt động
- [ ] Không text nào bị mất trên background
- [ ] Images/icons hiển thị đúng cả hai mode

### ✅ Layout
- [ ] Responsive trên mobile, tablet, desktop
- [ ] Không horizontal scroll trên mobile
- [ ] Content không bị overflow

### ✅ Accessibility
- [ ] ARIA labels đầy đủ
- [ ] Keyboard navigation hoạt động
- [ ] Screen reader compatible
- [ ] Focus indicators rõ ràng

---

## Nguồn gốc
- Gốc: `ui-ux-pro-max` từ antigravity-awesome-skills (community)
- Việt hóa + adapt bởi: ABM Workforce v2.2 — Jarvis Orchestrator
