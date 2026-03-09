# Starter kit triển khai dự án Stock AI Platform

Tài liệu này là bộ khởi tạo thực chiến để bạn bắt đầu repo ngay với:
- Next.js App Router
- TypeScript
- Tailwind CSS
- shadcn/ui
- Drizzle ORM
- PostgreSQL
- Redis
- BullMQ
- Auth.js
- OpenAI API

---

# 1) Cách khởi tạo repo

## 1.1 Tạo monorepo

```bash
mkdir stock-ai-platform
cd stock-ai-platform
pnpm init
```

## 1.2 Tạo cấu trúc workspace

### `pnpm-workspace.yaml`
```yaml
packages:
  - apps/*
  - packages/*
```

### `package.json`
```json
{
  "name": "stock-ai-platform",
  "private": true,
  "packageManager": "pnpm@10.0.0",
  "scripts": {
    "dev": "turbo dev",
    "build": "turbo build",
    "lint": "turbo lint",
    "typecheck": "turbo typecheck",
    "db:generate": "pnpm --filter @repo/db db:generate",
    "db:migrate": "pnpm --filter @repo/db db:migrate"
  },
  "devDependencies": {
    "turbo": "latest",
    "typescript": "latest"
  }
}
```

### `turbo.json`
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {},
    "typecheck": {}
  }
}
```

---

# 2) Tạo app web bằng Next.js

Theo tài liệu Next.js, App Router là router hiện đại hỗ trợ Server Components, Suspense và full-stack patterns. Tailwind cũng có hướng dẫn cài trực tiếp cho Next.js App Router. shadcn/ui hiện hỗ trợ khởi tạo trực tiếp cho dự án Next.js hoặc monorepo. Auth.js có tích hợp chính thức cho Next.js. Drizzle có guide chính thức cho PostgreSQL. [Tài liệu tham chiếu dùng ở cuối tài liệu]

## 2.1 Tạo app web
```bash
pnpm create next-app@latest apps/web --typescript --eslint --app --src-dir false --import-alias "@/*"
```

## 2.2 Cài dependencies chính cho web
```bash
cd apps/web
pnpm add framer-motion lightweight-charts @tanstack/react-query zustand zod openai next-auth
pnpm add @radix-ui/react-slot lucide-react clsx tailwind-merge class-variance-authority
pnpm add drizzle-orm pg postgres
pnpm add bullmq ioredis
pnpm add -D @tailwindcss/postcss tailwindcss drizzle-kit
```

## 2.3 Khởi tạo shadcn/ui
```bash
pnpm dlx shadcn@latest init
```

## 2.4 Thêm các component nền
```bash
pnpm dlx shadcn@latest add button card input badge tabs dialog sheet skeleton tooltip table command dropdown-menu separator avatar
```

---

# 3) Cấu trúc thư mục gợi ý

```txt
stock-ai-platform/
├─ apps/
│  ├─ web/
│  │  ├─ app/
│  │  │  ├─ (marketing)/
│  │  │  │  ├─ page.tsx
│  │  │  │  ├─ pricing/page.tsx
│  │  │  │  └─ layout.tsx
│  │  │  ├─ (app)/
│  │  │  │  ├─ dashboard/page.tsx
│  │  │  │  ├─ watchlist/page.tsx
│  │  │  │  ├─ portfolio/page.tsx
│  │  │  │  ├─ alerts/page.tsx
│  │  │  │  └─ copilot/page.tsx
│  │  │  ├─ markets/page.tsx
│  │  │  ├─ stocks/[symbol]/page.tsx
│  │  │  ├─ api/
│  │  │  │  ├─ market/route.ts
│  │  │  │  ├─ stocks/[symbol]/route.ts
│  │  │  │  ├─ stocks/[symbol]/candles/route.ts
│  │  │  │  ├─ stocks/[symbol]/technical/route.ts
│  │  │  │  ├─ stocks/[symbol]/brief/route.ts
│  │  │  │  ├─ ai/copilot/route.ts
│  │  │  │  └─ auth/[...nextauth]/route.ts
│  │  │  ├─ globals.css
│  │  │  ├─ layout.tsx
│  │  │  └─ not-found.tsx
│  │  ├─ components/
│  │  │  ├─ layout/
│  │  │  ├─ chart/
│  │  │  ├─ market/
│  │  │  ├─ stock/
│  │  │  └─ ai/
│  │  ├─ features/
│  │  │  ├─ market/
│  │  │  ├─ stocks/
│  │  │  ├─ watchlist/
│  │  │  ├─ alerts/
│  │  │  ├─ auth/
│  │  │  └─ copilot/
│  │  ├─ lib/
│  │  │  ├─ utils.ts
│  │  │  ├─ openai.ts
│  │  │  ├─ redis.ts
│  │  │  ├─ auth.ts
│  │  │  └─ env.ts
│  │  ├─ server/
│  │  │  ├─ db/
│  │  │  ├─ repositories/
│  │  │  ├─ services/
│  │  │  ├─ ai/
│  │  │  └─ providers/
│  │  ├─ middleware.ts
│  │  └─ components.json
│  └─ worker/
│     ├─ src/
│     │  ├─ index.ts
│     │  ├─ queues/
│     │  ├─ processors/
│     │  ├─ schedulers/
│     │  └─ indicators/
│     └─ package.json
├─ packages/
│  ├─ db/
│  ├─ types/
│  ├─ ui/
│  ├─ market-core/
│  └─ ai-core/
└─ docs/
```

---

# 4) Bộ file cốt lõi nên tạo ngay

## 4.1 `apps/web/app/layout.tsx`
```tsx
import "./globals.css"
import type { Metadata } from "next"
import { Inter } from "next/font/google"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "AlphaLens AI",
  description: "AI-native stock research platform",
}

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>{children}</body>
    </html>
  )
}
```

## 4.2 `apps/web/app/globals.css`
```css
@import "tailwindcss";

:root {
  --background: 222 47% 6%;
  --foreground: 210 40% 98%;
  --card: 222 40% 9%;
  --card-foreground: 210 40% 98%;
  --muted: 217 33% 17%;
  --muted-foreground: 215 20% 72%;
  --border: 217 33% 18%;
  --primary: 199 89% 48%;
  --primary-foreground: 210 40% 98%;
  --accent: 160 84% 39%;
}

body {
  background:
    radial-gradient(circle at top, rgba(56, 189, 248, 0.12), transparent 35%),
    radial-gradient(circle at right, rgba(34, 197, 94, 0.08), transparent 30%),
    hsl(var(--background));
  color: hsl(var(--foreground));
}
```

## 4.3 `apps/web/lib/utils.ts`
```ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

---

# 5) Homepage starter

## `apps/web/app/(marketing)/page.tsx`
```tsx
import { ArrowRight, BarChart3, BrainCircuit, Radar } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Input } from "@/components/ui/input"

const features = [
  {
    icon: BrainCircuit,
    title: "AI Research Copilot",
    desc: "Tóm tắt thị trường, phân tích mã và giải thích tín hiệu kỹ thuật bằng AI có cấu trúc.",
  },
  {
    icon: BarChart3,
    title: "Technical Analysis Engine",
    desc: "Biểu đồ mượt, indicator cốt lõi, phân tích đa khung thời gian và breakout scanner.",
  },
  {
    icon: Radar,
    title: "Market Intelligence",
    desc: "Heatmap ngành, top movers, breadth thị trường và cảnh báo thông minh theo thời gian thực.",
  },
]

export default function HomePage() {
  return (
    <main className="min-h-screen overflow-hidden">
      <section className="relative border-b border-white/10">
        <div className="mx-auto grid max-w-7xl gap-10 px-6 py-24 lg:grid-cols-2 lg:px-8">
          <div className="space-y-8">
            <div className="inline-flex items-center rounded-full border border-cyan-400/20 bg-cyan-400/10 px-3 py-1 text-sm text-cyan-300">
              AI-native stock research platform
            </div>
            <div className="space-y-4">
              <h1 className="max-w-3xl text-5xl font-semibold tracking-tight text-white md:text-6xl">
                Phân tích chứng khoán sâu hơn. Nhanh hơn. Thông minh hơn với AI.
              </h1>
              <p className="max-w-2xl text-lg text-slate-300">
                Theo dõi dữ liệu thị trường, đọc biểu đồ nâng cao, phát hiện tín hiệu kỹ thuật và nhận insight đầu tư được hỗ trợ bởi AI trong một nền tảng duy nhất.
              </p>
            </div>

            <div className="flex flex-col gap-3 sm:flex-row">
              <Button size="lg" className="gap-2">
                Bắt đầu miễn phí <ArrowRight className="h-4 w-4" />
              </Button>
              <Button size="lg" variant="outline">
                Xem demo live
              </Button>
            </div>

            <div className="max-w-xl rounded-2xl border border-white/10 bg-white/5 p-3 backdrop-blur">
              <div className="flex gap-3">
                <Input
                  placeholder="Nhập mã cổ phiếu hoặc câu hỏi như: phân tích HPG hôm nay"
                  className="border-white/10 bg-slate-950/40"
                />
                <Button>Tra cứu</Button>
              </div>
            </div>
          </div>

          <div className="relative">
            <div className="rounded-3xl border border-white/10 bg-slate-950/60 p-5 shadow-2xl backdrop-blur-xl">
              <div className="mb-4 flex items-center justify-between">
                <div>
                  <div className="text-sm text-slate-400">AI Brief</div>
                  <div className="text-xl font-semibold text-white">VN30 Market Pulse</div>
                </div>
                <div className="rounded-full bg-emerald-500/15 px-3 py-1 text-sm text-emerald-300">
                  Bullish bias
                </div>
              </div>

              <div className="grid gap-4 md:grid-cols-2">
                <Card className="border-white/10 bg-white/5">
                  <CardContent className="p-4">
                    <div className="text-sm text-slate-400">Top movers</div>
                    <div className="mt-3 space-y-2 text-sm">
                      <div className="flex justify-between"><span>HPG</span><span className="text-emerald-300">+3.2%</span></div>
                      <div className="flex justify-between"><span>FPT</span><span className="text-emerald-300">+2.1%</span></div>
                      <div className="flex justify-between"><span>SSI</span><span className="text-rose-300">-1.4%</span></div>
                    </div>
                  </CardContent>
                </Card>

                <Card className="border-white/10 bg-white/5">
                  <CardContent className="p-4">
                    <div className="text-sm text-slate-400">AI signal summary</div>
                    <p className="mt-3 text-sm leading-6 text-slate-200">
                      Dòng tiền tập trung nhóm công nghệ và thép. Breadth cải thiện, nhưng RSI nhiều mã vốn hóa lớn đang tiến vào vùng nhạy cảm.
                    </p>
                  </CardContent>
                </Card>
              </div>

              <div className="mt-4 rounded-2xl border border-white/10 bg-gradient-to-br from-cyan-500/10 to-emerald-500/10 p-5">
                <div className="text-sm text-slate-300">Confidence</div>
                <div className="mt-2 text-3xl font-semibold text-white">78%</div>
                <div className="mt-3 text-sm text-slate-300">
                  Key risks: chốt lời ngắn hạn, thanh khoản suy yếu nếu nhóm dẫn dắt hạ nhiệt.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-6 py-20 lg:px-8">
        <div className="grid gap-6 md:grid-cols-3">
          {features.map((item) => {
            const Icon = item.icon
            return (
              <Card key={item.title} className="border-white/10 bg-white/5">
                <CardContent className="space-y-4 p-6">
                  <div className="inline-flex rounded-2xl border border-white/10 bg-white/5 p-3">
                    <Icon className="h-5 w-5 text-cyan-300" />
                  </div>
                  <div className="space-y-2">
                    <h3 className="text-xl font-semibold text-white">{item.title}</h3>
                    <p className="text-sm leading-6 text-slate-300">{item.desc}</p>
                  </div>
                </CardContent>
              </Card>
            )
          })}
        </div>
      </section>
    </main>
  )
}
```

---

# 6) Stock detail page starter

## `apps/web/app/stocks/[symbol]/page.tsx`
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default async function StockDetailPage({
  params,
}: {
  params: Promise<{ symbol: string }>
}) {
  const { symbol } = await params

  return (
    <main className="mx-auto min-h-screen max-w-7xl px-6 py-10 lg:px-8">
      <div className="mb-8 flex flex-wrap items-start justify-between gap-4">
        <div>
          <div className="text-sm text-slate-400">Stocks / {symbol.toUpperCase()}</div>
          <h1 className="mt-2 text-4xl font-semibold text-white">{symbol.toUpperCase()}</h1>
          <p className="mt-2 text-slate-300">Công ty mẫu - snapshot dữ liệu, chart và AI brief.</p>
        </div>

        <div className="flex gap-3">
          <Button variant="outline">Add watchlist</Button>
          <Button variant="outline">Set alert</Button>
          <Button>Ask AI</Button>
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-12">
        <div className="space-y-6 lg:col-span-8">
          <Card className="border-white/10 bg-white/5">
            <CardHeader>
              <CardTitle>Chart</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="h-[420px] rounded-2xl border border-dashed border-white/10 bg-slate-950/40" />
            </CardContent>
          </Card>

          <Card className="border-white/10 bg-white/5">
            <CardHeader>
              <CardTitle>AI Brief</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4 text-sm text-slate-200">
              <p>
                Xu hướng hiện tại nghiêng tích cực trên khung ngày, với EMA20 duy trì trên EMA50 và động lượng giá được hỗ trợ bởi thanh khoản tăng.
              </p>
              <div className="grid gap-4 md:grid-cols-2">
                <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 p-4">
                  <div className="font-medium text-emerald-300">Bull case</div>
                  <p className="mt-2 text-slate-200">Nếu giá giữ trên vùng hỗ trợ gần nhất và volume tiếp tục cải thiện, xác suất mở rộng xu hướng tăng sẽ cao hơn.</p>
                </div>
                <div className="rounded-xl border border-rose-500/20 bg-rose-500/10 p-4">
                  <div className="font-medium text-rose-300">Bear case</div>
                  <p className="mt-2 text-slate-200">Nếu thủng hỗ trợ ngắn hạn và MACD suy yếu, áp lực điều chỉnh ngắn hạn có thể tăng nhanh.</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="space-y-6 lg:col-span-4">
          <Card className="border-white/10 bg-white/5">
            <CardHeader>
              <CardTitle>Snapshot</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3 text-sm">
              <div className="flex justify-between"><span className="text-slate-400">Price</span><span>32.45</span></div>
              <div className="flex justify-between"><span className="text-slate-400">Change</span><span className="text-emerald-300">+2.51%</span></div>
              <div className="flex justify-between"><span className="text-slate-400">Volume</span><span>21.4M</span></div>
              <div className="flex justify-between"><span className="text-slate-400">RSI(14)</span><span>63.2</span></div>
              <div className="flex justify-between"><span className="text-slate-400">MACD</span><span>Positive</span></div>
            </CardContent>
          </Card>

          <Card className="border-white/10 bg-white/5">
            <CardHeader>
              <CardTitle>Key levels</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3 text-sm">
              <div className="flex justify-between"><span className="text-slate-400">Support 1</span><span>31.20</span></div>
              <div className="flex justify-between"><span className="text-slate-400">Support 2</span><span>30.60</span></div>
              <div className="flex justify-between"><span className="text-slate-400">Resistance 1</span><span>33.10</span></div>
              <div className="flex justify-between"><span className="text-slate-400">Resistance 2</span><span>34.00</span></div>
            </CardContent>
          </Card>
        </div>
      </div>
    </main>
  )
}
```

---

# 7) Chart component starter

Lightweight Charts là thư viện chính thức của TradingView cho chart tài chính tương tác. Tài liệu hướng dẫn tạo chart bằng `createChart`, và trang giới thiệu nhấn mạnh hiệu năng cao cùng kích thước gọn. [Tài liệu tham chiếu dùng ở cuối tài liệu]

## `apps/web/components/chart/candles-chart.tsx`
```tsx
"use client"

import { useEffect, useRef } from "react"
import { createChart, ColorType, CandlestickData } from "lightweight-charts"

const sampleData: CandlestickData[] = [
  { time: "2026-03-02", open: 31.1, high: 32.4, low: 30.9, close: 32.1 },
  { time: "2026-03-03", open: 32.1, high: 32.9, low: 31.8, close: 32.7 },
  { time: "2026-03-04", open: 32.7, high: 33.0, low: 32.0, close: 32.2 },
  { time: "2026-03-05", open: 32.2, high: 33.2, low: 32.1, close: 33.0 },
  { time: "2026-03-06", open: 33.0, high: 33.5, low: 32.6, close: 33.2 },
]

export function CandlesChart() {
  const containerRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    if (!containerRef.current) return

    const chart = createChart(containerRef.current, {
      layout: {
        background: { type: ColorType.Solid, color: "#020617" },
        textColor: "#cbd5e1",
      },
      grid: {
        vertLines: { color: "rgba(148, 163, 184, 0.08)" },
        horzLines: { color: "rgba(148, 163, 184, 0.08)" },
      },
      width: containerRef.current.clientWidth,
      height: 420,
      rightPriceScale: {
        borderColor: "rgba(148, 163, 184, 0.18)",
      },
      timeScale: {
        borderColor: "rgba(148, 163, 184, 0.18)",
      },
    })

    const series = chart.addCandlestickSeries()
    series.setData(sampleData)
    chart.timeScale().fitContent()

    const resizeObserver = new ResizeObserver(() => {
      if (!containerRef.current) return
      chart.applyOptions({ width: containerRef.current.clientWidth })
    })

    resizeObserver.observe(containerRef.current)

    return () => {
      resizeObserver.disconnect()
      chart.remove()
    }
  }, [])

  return <div ref={containerRef} className="w-full" />
}
```

---

# 8) Database package starter với Drizzle

## `packages/db/package.json`
```json
{
  "name": "@repo/db",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "db:generate": "drizzle-kit generate",
    "db:migrate": "drizzle-kit migrate"
  },
  "dependencies": {
    "drizzle-orm": "latest",
    "pg": "latest"
  },
  "devDependencies": {
    "drizzle-kit": "latest",
    "typescript": "latest"
  }
}
```

## `packages/db/drizzle.config.ts`
```ts
import { defineConfig } from "drizzle-kit"

export default defineConfig({
  schema: "./src/schema.ts",
  out: "./drizzle",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
})
```

## `packages/db/src/schema.ts`
```ts
import {
  pgTable,
  text,
  timestamp,
  uuid,
  integer,
  numeric,
  boolean,
  jsonb,
} from "drizzle-orm/pg-core"

export const users = pgTable("users", {
  id: uuid("id").defaultRandom().primaryKey(),
  email: text("email").notNull().unique(),
  name: text("name"),
  image: text("image"),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
})

export const symbols = pgTable("symbols", {
  id: uuid("id").defaultRandom().primaryKey(),
  symbol: text("symbol").notNull().unique(),
  companyName: text("company_name").notNull(),
  exchange: text("exchange").notNull(),
  sector: text("sector"),
  industry: text("industry"),
  currency: text("currency").default("VND").notNull(),
  isActive: boolean("is_active").default(true).notNull(),
})

export const quotesLatest = pgTable("quotes_latest", {
  symbolId: uuid("symbol_id").primaryKey().references(() => symbols.id),
  lastPrice: numeric("last_price", { precision: 18, scale: 4 }).notNull(),
  priceChange: numeric("price_change", { precision: 18, scale: 4 }).notNull(),
  percentChange: numeric("percent_change", { precision: 10, scale: 4 }).notNull(),
  open: numeric("open", { precision: 18, scale: 4 }).notNull(),
  high: numeric("high", { precision: 18, scale: 4 }).notNull(),
  low: numeric("low", { precision: 18, scale: 4 }).notNull(),
  previousClose: numeric("previous_close", { precision: 18, scale: 4 }).notNull(),
  volume: numeric("volume", { precision: 20, scale: 0 }).notNull(),
  updatedAt: timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
})

export const ohlcv1d = pgTable("ohlcv_1d", {
  id: uuid("id").defaultRandom().primaryKey(),
  symbolId: uuid("symbol_id").notNull().references(() => symbols.id),
  ts: timestamp("ts", { withTimezone: true }).notNull(),
  open: numeric("open", { precision: 18, scale: 4 }).notNull(),
  high: numeric("high", { precision: 18, scale: 4 }).notNull(),
  low: numeric("low", { precision: 18, scale: 4 }).notNull(),
  close: numeric("close", { precision: 18, scale: 4 }).notNull(),
  volume: numeric("volume", { precision: 20, scale: 0 }).notNull(),
})

export const technicalSnapshots = pgTable("technical_snapshots", {
  id: uuid("id").defaultRandom().primaryKey(),
  symbolId: uuid("symbol_id").notNull().references(() => symbols.id),
  timeframe: text("timeframe").notNull(),
  rsi14: numeric("rsi_14", { precision: 8, scale: 2 }),
  macd: numeric("macd", { precision: 12, scale: 4 }),
  macdSignal: numeric("macd_signal", { precision: 12, scale: 4 }),
  ema20: numeric("ema_20", { precision: 18, scale: 4 }),
  ema50: numeric("ema_50", { precision: 18, scale: 4 }),
  ema200: numeric("ema_200", { precision: 18, scale: 4 }),
  atr14: numeric("atr_14", { precision: 12, scale: 4 }),
  calculatedAt: timestamp("calculated_at", { withTimezone: true }).defaultNow().notNull(),
})

export const watchlists = pgTable("watchlists", {
  id: uuid("id").defaultRandom().primaryKey(),
  userId: uuid("user_id").notNull().references(() => users.id),
  name: text("name").notNull(),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
})

export const watchlistItems = pgTable("watchlist_items", {
  id: uuid("id").defaultRandom().primaryKey(),
  watchlistId: uuid("watchlist_id").notNull().references(() => watchlists.id),
  symbolId: uuid("symbol_id").notNull().references(() => symbols.id),
  note: text("note"),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
})

export const aiStockBriefs = pgTable("ai_stock_briefs", {
  id: uuid("id").defaultRandom().primaryKey(),
  symbolId: uuid("symbol_id").notNull().references(() => symbols.id),
  timeframe: text("timeframe").notNull(),
  summary: text("summary").notNull(),
  bullishCase: text("bullish_case").notNull(),
  bearishCase: text("bearish_case").notNull(),
  keyLevels: jsonb("key_levels").$type<number[]>().notNull(),
  triggers: jsonb("triggers").$type<string[]>().notNull(),
  riskFlags: jsonb("risk_flags").$type<string[]>().notNull(),
  confidenceScore: integer("confidence_score").notNull(),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
})
```

## `packages/db/src/client.ts`
```ts
import { drizzle } from "drizzle-orm/node-postgres"
import { Pool } from "pg"
import * as schema from "./schema"

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
})

export const db = drizzle(pool, { schema })
```

---

# 9) Auth.js starter

Auth.js có tích hợp chính thức cho Next.js và tài liệu hiện tại mô tả pattern `NextAuth({...})` trả về `auth`, `handlers`, `signIn`, `signOut`. [Tài liệu tham chiếu dùng ở cuối tài liệu]

## `apps/web/lib/auth.ts`
```ts
import NextAuth from "next-auth"
import GitHub from "next-auth/providers/github"

export const { auth, handlers, signIn, signOut } = NextAuth({
  providers: [GitHub],
})
```

## `apps/web/app/api/auth/[...nextauth]/route.ts`
```ts
import { handlers } from "@/lib/auth"

export const { GET, POST } = handlers
```

## `apps/web/middleware.ts`
```ts
export { auth as middleware } from "@/lib/auth"

export const config = {
  matcher: ["/dashboard/:path*", "/watchlist/:path*", "/portfolio/:path*", "/alerts/:path*", "/copilot/:path*"],
}
```

---

# 10) OpenAI starter cho stock brief

OpenAI hiện khuyến nghị dùng Responses API; tài liệu Structured Outputs cho biết model có thể bám chặt JSON Schema bạn định nghĩa. Đây là cách phù hợp nhất để sinh `stock_brief` có cấu trúc cố định. [Tài liệu tham chiếu dùng ở cuối tài liệu]

## `apps/web/lib/openai.ts`
```ts
import OpenAI from "openai"

export const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
})
```

## `apps/web/server/ai/stock-brief.ts`
```ts
import { openai } from "@/lib/openai"

export async function generateStockBrief(input: {
  symbol: string
  timeframe: "15m" | "1h" | "1d"
  price: number
  changePercent: number
  rsi14?: number
  ema20?: number
  ema50?: number
  supportLevels: number[]
  resistanceLevels: number[]
  newsSummary?: string
}) {
  const response = await openai.responses.create({
    model: "gpt-5.4",
    input: [
      {
        role: "system",
        content: [
          {
            type: "input_text",
            text:
              "You are an explainable stock analysis assistant. Use only the facts provided. Do not invent prices, indicators, or unsupported claims. Return concise, professional analysis.",
          },
        ],
      },
      {
        role: "user",
        content: [
          {
            type: "input_text",
            text: JSON.stringify(input),
          },
        ],
      },
    ],
    text: {
      format: {
        type: "json_schema",
        name: "stock_brief",
        schema: {
          type: "object",
          additionalProperties: false,
          properties: {
            symbol: { type: "string" },
            timeframe: { type: "string", enum: ["15m", "1h", "1d"] },
            summary: { type: "string" },
            marketRegime: { type: "string", enum: ["bullish", "neutral", "bearish"] },
            trend: { type: "string" },
            momentum: { type: "string" },
            supportLevels: { type: "array", items: { type: "number" } },
            resistanceLevels: { type: "array", items: { type: "number" } },
            bullCase: { type: "string" },
            bearCase: { type: "string" },
            triggersToWatch: { type: "array", items: { type: "string" } },
            riskFlags: { type: "array", items: { type: "string" } },
            confidence: { type: "number" },
            disclaimer: { type: "string" }
          },
          required: [
            "symbol",
            "timeframe",
            "summary",
            "marketRegime",
            "trend",
            "momentum",
            "supportLevels",
            "resistanceLevels",
            "bullCase",
            "bearCase",
            "triggersToWatch",
            "riskFlags",
            "confidence",
            "disclaimer"
          ]
        },
        strict: true
      }
    }
  })

  return JSON.parse(response.output_text)
}
```

---

# 11) API route starter cho AI brief

## `apps/web/app/api/stocks/[symbol]/brief/route.ts`
```ts
import { NextRequest, NextResponse } from "next/server"
import { generateStockBrief } from "@/server/ai/stock-brief"

export async function POST(
  _request: NextRequest,
  { params }: { params: Promise<{ symbol: string }> },
) {
  const { symbol } = await params

  const brief = await generateStockBrief({
    symbol: symbol.toUpperCase(),
    timeframe: "1d",
    price: 32.45,
    changePercent: 2.51,
    rsi14: 63.2,
    ema20: 31.9,
    ema50: 30.8,
    supportLevels: [31.2, 30.6],
    resistanceLevels: [33.1, 34.0],
    newsSummary: "Dòng tiền quay lại nhóm cổ phiếu dẫn dắt, tâm lý thị trường được cải thiện.",
  })

  return NextResponse.json(brief)
}
```

---

# 12) Market API starter

## `apps/web/app/api/market/route.ts`
```ts
import { NextResponse } from "next/server"

export async function GET() {
  return NextResponse.json({
    indices: [
      { symbol: "VNINDEX", value: 1284.2, changePercent: 0.82 },
      { symbol: "VN30", value: 1301.7, changePercent: 1.13 },
      { symbol: "HNX", value: 245.4, changePercent: 0.34 },
    ],
    topMovers: [
      { symbol: "HPG", changePercent: 3.2 },
      { symbol: "FPT", changePercent: 2.1 },
      { symbol: "MWG", changePercent: 1.9 },
    ],
    breadth: {
      advancers: 244,
      decliners: 181,
      unchanged: 75,
    },
  })
}
```

---

# 13) Worker starter với BullMQ

BullMQ là thư viện queue chạy trên Redis với các class chính như Queue, Worker, QueueEvents và FlowProducer. Nó phù hợp để tách jobs như sync market data, tính indicator và sinh AI brief ra khỏi request cycle của Next.js. [Tài liệu tham chiếu dùng ở cuối tài liệu]

## `apps/worker/package.json`
```json
{
  "name": "worker",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "tsx src/index.ts"
  },
  "dependencies": {
    "bullmq": "latest",
    "ioredis": "latest"
  },
  "devDependencies": {
    "tsx": "latest",
    "typescript": "latest"
  }
}
```

## `apps/worker/src/index.ts`
```ts
import { Queue, Worker } from "bullmq"
import IORedis from "ioredis"

const connection = new IORedis(process.env.REDIS_URL!, {
  maxRetriesPerRequest: null,
})

export const marketSyncQueue = new Queue("market-sync", { connection })

new Worker(
  "market-sync",
  async (job) => {
    console.log("Processing market sync job:", job.name, job.data)
    // TODO: pull data provider -> normalize -> save DB -> queue technical calc
  },
  { connection },
)

async function bootstrap() {
  await marketSyncQueue.add("seed-market-sync", {
    source: "demo-provider",
  })
  console.log("Worker started")
}

bootstrap().catch(console.error)
```

---

# 14) Redis helper starter

## `apps/web/lib/redis.ts`
```ts
import Redis from "ioredis"

export const redis = new Redis(process.env.REDIS_URL!, {
  maxRetriesPerRequest: null,
})
```

---

# 15) Environment variables

## `.env.local`
```bash
DATABASE_URL=postgres://postgres:postgres@localhost:5432/stock_ai
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=your_openai_api_key
AUTH_SECRET=replace_me
AUTH_GITHUB_ID=replace_me
AUTH_GITHUB_SECRET=replace_me
```

---

# 16) Các package nên tách dần sau khi MVP chạy được

## `packages/types`
- shared domain types
- API response types
- AI output types

## `packages/market-core`
- indicator calculators
- screener logic
- trend scoring
- support/resistance logic

## `packages/ai-core`
- JSON schemas
- prompt builders
- AI output validators
- explainability rules

## `packages/ui`
- shared design tokens
- chart wrappers
- cards, badges, metrics components

---

# 17) Thứ tự build thực tế sau khi tạo repo

## Step 1
Chạy web app và dựng homepage cho đẹp trước.

## Step 2
Tạo database schema và migrate.

## Step 3
Tạo stock detail page với chart thật.

## Step 4
Kết nối API brief và render AI card.

## Step 5
Thêm auth + watchlist.

## Step 6
Bật worker để sync data và tính snapshot.

---

# 18) Danh sách việc phải làm ngay sau starter

- Gắn provider market data thật
- Viết adapter chuẩn hóa symbol/timeframe
- Viết indicator engine: RSI, EMA, MACD, ATR
- Viết repository layer cho symbols, quotes, candles
- Viết cache keys và invalidation
- Tạo skeleton loading và error states
- Thêm pricing page và billing hooks
- Thêm alert builder UI

---

# 19) Tài liệu tham chiếu chính thức đã dùng

- Next.js App Router và create-next-app: Next.js docs
- Tailwind CSS với Next.js: Tailwind framework guide
- shadcn/ui cho Next.js: shadcn docs
- Auth.js cho Next.js: Auth.js docs
- Drizzle với PostgreSQL: Drizzle docs
- Structured Outputs và Responses API: OpenAI docs
- BullMQ: BullMQ docs
- Lightweight Charts: TradingView docs

---

# 20) Kết luận áp dụng

Đây là bộ khởi tạo đủ tốt để bạn bắt đầu một bản MVP nghiêm túc:
- Có kiến trúc scale được
- Có AI layer đúng hướng
- Có worker để xử lý job nặng
- Có DB schema đủ cho stock detail, watchlist, AI brief
- Có homepage và stock page mẫu

Sau bước này, nên chuyển ngay sang:
1. Tạo repo thật
2. Chạy UI homepage
3. Dựng stock page thật
4. Gắn data provider thật
5. Gắn AI brief thật

