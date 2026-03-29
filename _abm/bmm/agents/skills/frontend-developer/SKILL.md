---
name: "frontend-developer"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Frontend expert React 19+ / Next.js 15+ — components, RSC, state, styling, testing, accessibility, performance. Build production-grade web apps."
---

# ⚛️ Frontend Developer — React 19 & Next.js 15

Skill chuyên gia frontend cho **React 19+**, **Next.js 15+**, modern web development. Masters server & client rendering, React ecosystem, performance optimization.

## Sử dụng khi

- Xây dựng React/Next.js UI components và pages
- Fix performance, accessibility, hoặc state issues
- Thiết kế client-side data fetching và interaction flows
- Implementing responsive layouts

## KHÔNG sử dụng khi

- Chỉ cần backend API → dùng dev worker
- Cần native mobile → dùng mobile skills
- Cần thiết kế visual → dùng `frontend-design`
- Cần **tối ưu performance** React → dùng `vercel-react-best-practices`
- Cần **refactor component architecture** → dùng `vercel-composition-patterns`

> ⚠️ **Ranh giới**: Skill này dạy **cách xây** (implementation). `vercel-react-best-practices` dạy **cách tối ưu** (optimization). Dùng cả hai khi cần build + optimize.

## VÍ DỤ NHANH

```
Input:  "Xây trang sản phẩm e-commerce"
Output:
  Bước 1: Server Component + getProduct() async
  Bước 2: ProductImage (next/image + lazy)
  Bước 3: AddToCart client component (useState + React Hook Form)
  Bước 4: Suspense boundary cho reviews section
  Bước 5: Lighthouse ≥ 90
```

---

## CAPABILITIES

### 1. Core React Expertise
- React 19+ với Hooks, Context, Suspense, Error Boundaries
- Server Components (RSC) & Client Components
- Concurrent Features: `useTransition`, `useDeferredValue`
- Component composition patterns
- Custom Hooks creation

### 2. Next.js & Full-Stack Integration
- Next.js 15+ App Router
- Server Actions & API Routes
- Middleware & Edge Runtime
- ISR, SSR, SSG strategies
- Image/Font optimization
- Parallel & Intercepting Routes

### 3. State Management & Data Fetching
- React Query / TanStack Query
- Zustand / Jotai cho client state
- SWR cho server state
- Form handling: React Hook Form + Zod
- Real-time: WebSocket, SSE

### 4. Styling & Design Systems
- Tailwind CSS 4
- CSS Modules
- Styled Components / Emotion
- CSS-in-JS vs Utility-first decisions
- Theme systems & design tokens

### 5. Performance & Optimization
- Bundle size analysis & code splitting
- `React.lazy()` & `next/dynamic`
- Image optimization (`next/image`)
- Core Web Vitals (LCP, CLS, INP)
- Lighthouse auditing

### 6. Testing & Quality
- React Testing Library
- Vitest / Jest
- Playwright E2E
- Storybook component testing
- MSW (Mock Service Worker)

### 7. Accessibility (A11y)
- WCAG 2.1 AA compliance
- Semantic HTML
- ARIA attributes
- Keyboard navigation
- Screen reader testing

### 8. Developer Tools
- TypeScript strict mode
- ESLint + Prettier
- Turbopack / Webpack
- Monorepo (Turborepo)
- CI/CD integration

---

## QUY TRÌNH IMPLEMENTATION

### Bước 1: Phân tích yêu cầu
```
1. Yêu cầu UI cụ thể gì?
2. Target devices nào?
3. Performance goals?
4. Data flow như thế nào?
```

### Bước 2: Chọn architecture
```
Server Component vs Client Component?
Static vs Dynamic rendering?
Data fetching strategy?
State management approach?
```

### Bước 3: Implement
```
1. Components (mobile-first, semantic HTML)
2. Styling (design tokens)
3. State & data (hooks, queries)
4. Error handling (boundaries, fallbacks)
```

### Bước 4: Validate
```
1. Lighthouse ≥ 90 tất cả metrics
2. A11y audit pass
3. Responsive check (320px → 1920px)
4. TypeScript strict no errors
```

---

## BEST PRACTICES

### Component Rules
- **1 component = 1 responsibility** (Single Responsibility)
- **Props down, events up** (Unidirectional data flow)
- **Composition over inheritance** (Compound components)
- **Server Components by default** (Client khi cần interactivity)

### Performance Rules
- `use client` CHỈ khi cần useState/useEffect/event handlers
- Lazy load components below fold
- Optimize images: WebP + `next/image` + lazy
- Prefetch links on hover

### Code Style
```typescript
// ✅ Good — typed, readable, server-first
export default async function ProductPage({ params }: Props) {
  const product = await getProduct(params.id)
  return <ProductDetail product={product} />
}

// ❌ Bad — unnecessary client, no types
'use client'
export default function ProductPage({ params }) {
  const [product, setProduct] = useState(null)
  useEffect(() => { fetch(...) }, [])
}
```

---

## Nguồn gốc
- Gốc: `frontend-developer` từ antigravity-awesome-skills (community)
- Việt hóa + adapt bởi: ABM Workforce v2.3 — Jarvis Orchestrator
