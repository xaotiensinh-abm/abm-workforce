---
name: "frontend-design"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Phương pháp luận thiết kế frontend cao cấp — DFII scoring, Design Thinking bắt buộc, Aesthetic Rules, Anti-Patterns. Tạo giao diện memorable, không generic."
---

# 🎯 Frontend Design — Thiết Kế Frontend Cao Cấp

Skill phương pháp luận cho **frontend designer-engineer**. Mục tiêu: tạo giao diện **memorable, high-craft** — không phải generic "AI UI".

## Sử dụng khi

- Thiết kế giao diện mới cần "WOW factor"
- Cần phân biệt sản phẩm với đối thủ
- Review thiết kế để nâng cấp aesthetic
- Xây dựng design system riêng biệt

## KHÔNG sử dụng khi

- Cần tra cứu palette/font → dùng `ui-ux-pro-max`
- Cần code React/Next.js → dùng `frontend-developer`
- Chỉ cần fix bugs → dùng `systematic-debugging`

---

## VÍ DỤ NHANH

```
Input:  "Thiết kế landing page cho AI startup"
Output:
  DFII: 4.2/5.0 (xuất sắc)
  Tone: Editorial
  Differentiation: Gradient mesh animation on hero section
  Font: Sora (heading) + DM Sans (body)
  Color: #0A0A0A, #6D28D9, #06B6D4 (Neon Cyber palette)
  → "Giao diện này khác biệt vì: gradient mesh tạo depth động, 
     không dùng flat cards như mọi AI product page"
```

## 1. CORE DESIGN MANDATE

Mọi giao diện PHẢI:
- ❌ Tránh generic "AI UI" patterns (Tailwind mặc định, unstyled shadcn)
- ✅ Thể hiện **aesthetic point of view** rõ ràng
- ✅ Fully functional + production-ready
- ✅ Dịch design intent trực tiếp thành code

---

## 2. DFII — Design Feasibility & Impact Index

Chấm điểm **trước khi bắt đầu** thiết kế:

### 5 Chiều Đánh Giá (1-5)

| Chiều | Câu hỏi |
|-------|---------|
| **Visual Distinction** | Có nhận ra ngay sản phẩm này khác biệt không? |
| **Craft Quality** | Chi tiết typography, spacing, color có tinh tế không? |
| **Functional Elegance** | UX có trôi chảy, tự nhiên không? |
| **Technical Feasibility** | Có thể implement được trong budget không? |
| **Brand Coherence** | Có nhất quán với brand identity không? |

### Công thức
```
DFII = (VD × 0.25) + (CQ × 0.25) + (FE × 0.20) + (TF × 0.15) + (BC × 0.15)
```

### Diễn giải
| Điểm | Ý nghĩa |
|------|---------|
| **4.0-5.0** | Xuất sắc — triển khai ngay |
| **3.0-3.9** | Tốt — cải thiện chi tiết |
| **2.0-2.9** | Cần sửa — thiếu distinction hoặc craft |
| **< 2.0** | Reject — thiết kế lại từ đầu |

---

## 3. DESIGN THINKING PHASE (BẮT BUỘC)

TRƯỚC khi viết BẤT KỲ code nào, PHẢI trả lời 3 câu:

### 1. Purpose (Mục đích)
> "Giao diện này phục vụ MỤC ĐÍCH gì cho người dùng?"

### 2. Tone (Chọn 1 hướng chủ đạo)
| Tone | Mô tả | Ví dụ |
|------|-------|-------|
| **Minimal** | Ít nhất, tinh tế nhất | Linear, Notion |
| **Expressive** | Đậm nét, personality | Spotify, Discord |
| **Brutalist** | Raw, chân thực | Craigslist, Terminal |
| **Editorial** | Magazine-like, premium | Apple, Medium |
| **Playful** | Vui vẻ, sáng tạo | Figma, Duolingo |

### 3. Differentiation Anchor
> "1 yếu tố khiến người dùng NHỚ giao diện này?"
> Ví dụ: micro-animation đặc biệt, typography sáng tạo, color signature

---

## 4. AESTHETIC EXECUTION RULES (Non-Negotiable)

### Typography
- ❌ KHÔNG dùng system fonts hoặc browser defaults
- ✅ Custom fonts (Inter, Satoshi, General Sans, Space Grotesk...)
- ✅ Tối thiểu 3 size levels: heading, body, caption
- ✅ Letter-spacing, line-height tinh chỉnh cho từng cấp

### Color & Theme
- ❌ KHÔNG dùng pure black (#000) hoặc pure white (#fff)
- ✅ Off-black, off-white tự nhiên hơn
- ✅ Accent color có ý nghĩa (không random)
- ✅ Dark mode PHẢI có — không phải afterthought

### Spatial Composition
- ✅ Breathing room — đừng chật
- ✅ Consistent spacing scale (4, 8, 12, 16, 24, 32, 48)
- ✅ Visual hierarchy qua size + weight + space

### Motion
- ✅ Micro-interactions cho feedback (hover, click, transition)
- ✅ 150-300ms cho UI, 300-500ms cho page transitions
- ✅ `prefers-reduced-motion` luôn check

### Texture & Depth
- ✅ Subtle shadows, gradients, hoặc borders cho depth
- ❌ KHÔNG flat hoàn toàn (trừ khi chủ đích)

---

## 5. OUTPUT STRUCTURE (BẮT BUỘC)

Mọi output design PHẢI có 4 phần:

### 1. Design Direction Summary
```
Tone: [Minimal/Expressive/etc]
Differentiation: [1 yếu tố khác biệt]
DFII Score: [x.x/5.0]
```

### 2. Design System Snapshot
```
Colors: [palette]
Typography: [font pairing + scale]
Spacing: [base unit + scale]
Shadows: [elevation system]
```

### 3. Implementation
```
Code thực tế — HTML/CSS/JS hoặc React components
```

### 4. Differentiation Callout
```
"Giao diện này khác biệt vì: [giải thích]"
```

---

## 6. ANTI-PATTERNS — LỖI PHẢI TRÁNH

| # | Anti-Pattern | Hậu quả |
|---|-------------|---------|
| 1 | Dùng default Tailwind colors | Generic, giống mọi AI UI |
| 2 | Shadcn unstyled | Trông "chưa xong" |
| 3 | No custom typography | Thiếu personality |
| 4 | Accordion everywhere | Lazy UX pattern |
| 5 | Modal cho mọi thứ | Bad mobile UX |
| 6 | No dark mode | Thiếu professional |
| 7 | Random border-radius | Inconsistent |
| 8 | Over-animated | Distracting |
| 9 | No whitespace | Chật, overwhelming |
| 10 | Stock photos | Fake, unauthentic |

---

## Nguồn gốc
- Gốc: `frontend-design` từ antigravity-awesome-skills (community)
- Việt hóa + adapt bởi: ABM Workforce v2.3 — Jarvis Orchestrator
