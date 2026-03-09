---
name: "vercel-react-best-practices"
description: "40+ quy tắc tối ưu React/Next.js từ Vercel Engineering — 8 categories priority-based: waterfall, bundle, server, client, re-render, rendering, JS perf, advanced. Nguồn chính thức."
---

# ⚡ Vercel React Best Practices — 40+ Rules

Skill chính thức từ **Vercel Engineering** — 40+ quy tắc tối ưu hiệu năng React/Next.js, phân loại theo **8 priority categories**.

## Sử dụng khi

- Viết React components hoặc Next.js pages mới
- Implementing data fetching (client/server)
- Review code cho performance issues
- Tối ưu bundle size hoặc load times

---

## QUY TẮC THEO PRIORITY

### 1. 🔴 Eliminating Waterfalls (CRITICAL)
- `async-defer-await` — Di chuyển `await` vào branch thực sự dùng
- `async-parallel` — `Promise.all()` cho operations độc lập
- `async-dependencies` — `better-all` cho partial dependencies
- `async-api-routes` — Start promises sớm, await muộn trong API routes
- `async-suspense-boundaries` — `Suspense` để stream content

### 2. 🔴 Bundle Size Optimization (CRITICAL)
- `bundle-barrel-imports` — Import trực tiếp, tránh barrel files
- `bundle-dynamic-imports` — `next/dynamic` cho heavy components
- `bundle-defer-third-party` — Load analytics SAU hydration
- `bundle-conditional` — Load modules chỉ khi feature active
- `bundle-preload` — Preload on hover/focus cho perceived speed

### 3. 🟡 Server-Side Performance (HIGH)
- `server-auth-actions` — Authenticate server actions như API routes
- `server-cache-react` — `React.cache()` cho per-request dedup
- `server-cache-lru` — LRU cache cho cross-request caching
- `server-dedup-props` — Tránh duplicate serialization trong RSC props
- `server-hoist-static-io` — Hoist static I/O (fonts, logos) lên module level
- `server-serialization` — Minimize data passed to client components
- `server-parallel-fetching` — Restructure components để parallelize fetches
- `server-after-nonblocking` — `after()` cho non-blocking operations

### 4. 🟡 Client-Side Data Fetching (MEDIUM-HIGH)
- `client-swr-dedup` — SWR cho automatic request deduplication
- `client-event-listeners` — Deduplicate global event listeners
- `client-passive-event-listeners` — Passive listeners cho scroll
- `client-localstorage-schema` — Version + minimize localStorage data

### 5. 🟢 Re-render Optimization (MEDIUM)
- `rerender-defer-reads` — Không subscribe state chỉ dùng trong callbacks
- `rerender-memo` — Extract expensive work thành memoized components
- `rerender-dependencies` — Primitive dependencies trong effects
- `rerender-derived-state` — Subscribe derived booleans, không raw values
- `rerender-functional-setstate` — Functional setState cho stable callbacks
- `rerender-lazy-state-init` — Pass function cho `useState` (expensive values)
- `rerender-transitions` — `startTransition` cho non-urgent updates
- `rerender-use-ref-transient-values` — Refs cho transient frequent values

### 6. 🟢 Rendering Performance (MEDIUM)
- `rendering-content-visibility` — `content-visibility` cho long lists
- `rendering-hoist-jsx` — Extract static JSX outside components
- `rendering-hydration-no-flicker` — Inline script cho client-only data
- `rendering-activity` — Activity component cho show/hide
- `rendering-conditional-render` — Ternary, KHÔNG `&&` cho conditionals
- `rendering-usetransition-loading` — `useTransition` cho loading state

### 7. ⚪ JavaScript Performance (LOW-MEDIUM)
- `js-batch-dom-css` — Group CSS changes qua classes hoặc `cssText`
- `js-index-maps` — Build Map cho repeated lookups
- `js-cache-property-access` — Cache object properties trong loops
- `js-combine-iterations` — Combine filter/map thành 1 loop
- `js-set-map-lookups` — Set/Map cho O(1) lookups
- `js-early-exit` — Return early từ functions

### 8. ⚪ Advanced Patterns (LOW)
- `advanced-event-handler-refs` — Store event handlers trong refs
- `advanced-init-once` — Initialize app 1 lần per load
- `advanced-use-latest` — `useLatest` cho stable callback refs

---

## CÁCH SỬ DỤNG

Khi review code:
```
1. Check CRITICAL rules trước (Waterfalls + Bundle)
2. Sau đó HIGH (Server)
3. Rồi MEDIUM (Client + Re-render + Rendering)
4. Cuối cùng LOW nếu cần tối ưu thêm
```

Khi viết code mới:
```
1. Server Components by default
2. Parallel data fetching
3. Direct imports (no barrels)
4. Dynamic imports cho heavy components
5. Suspense boundaries cho streaming
```

---

## Nguồn gốc
- **Chính thức**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — Vercel Engineering
- 455K+ installs trên skills.sh (#1 trong leaderboard)
- Adapt bởi: ABM Workforce v2.2 — Jarvis Orchestrator
