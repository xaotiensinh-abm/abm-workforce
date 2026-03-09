# Blueprint dự án web app AI phân tích chứng khoán

## 1) Tầm nhìn sản phẩm
Xây dựng một nền tảng web fullstack chuyên về:
- Cung cấp dữ liệu chứng khoán theo thời gian thực hoặc gần thời gian thực
- Phân tích thị trường đa lớp: price action, volume, dòng tiền, ngành, vĩ mô, tin tức, sentiment
- Phân tích kỹ thuật chuyên sâu với biểu đồ tương tác mạnh
- Tạo insight và gợi ý đầu tư bằng AI theo hướng **giải thích được**, **có kiểm soát rủi ro**, và **không biến thành hộp đen**
- Hỗ trợ cả nhà đầu tư mới lẫn trader/người phân tích nâng cao

### Định vị tối ưu
Thay vì chỉ là “website xem giá + chatbot AI”, sản phẩm nên được định vị là:

**Nền tảng Research Copilot cho nhà đầu tư**
- Xem dữ liệu nhanh
- Phân tích kỹ thuật sâu
- AI tóm tắt, phát hiện tín hiệu, giải thích bối cảnh
- Hỗ trợ ra quyết định, không thay người dùng quyết định

## 2) Mục tiêu chiến lược

### Mục tiêu kinh doanh
- Thu hút traffic organic từ nhu cầu tra cứu mã cổ phiếu và phân tích thị trường
- Tăng retention bằng watchlist, cảnh báo, AI brief hằng ngày
- Chuyển đổi sang gói trả phí bằng các tính năng cao cấp: AI Pro, screener nâng cao, portfolio intelligence, signal lab, alert thông minh

### Mục tiêu sản phẩm
- Tốc độ tải trang rất nhanh
- UX cao cấp, tạo cảm giác đáng tin cậy như một terminal mini nhưng dễ dùng
- Dữ liệu rõ ràng, AI có căn cứ, biểu đồ mạnh
- Có thể mở rộng từ thị trường Việt Nam sang US/crypto/ETF về sau

## 3) Chân dung người dùng

### Persona 1: Nhà đầu tư mới
Nhu cầu:
- Hiểu nhanh một mã cổ phiếu
- Xem xu hướng, hỗ trợ/kháng cự, dòng tiền, chỉ báo dễ hiểu
- Cần AI giải thích bằng ngôn ngữ đơn giản

### Persona 2: Trader chủ động
Nhu cầu:
- Biểu đồ mượt
- Indicator, multi-timeframe, volume profile cơ bản, breakout/breakdown alerts
- Cần AI phân tích xác suất kịch bản

### Persona 3: Nhà đầu tư trung hạn
Nhu cầu:
- Theo dõi ngành, sức mạnh tương đối, earnings, tin tức, sentiment
- Tìm cơ hội theo theme/sector
- Muốn AI tổng hợp bối cảnh thị trường mỗi ngày

### Persona 4: Power user / analyst
Nhu cầu:
- Screener mạnh
- Backtest logic cơ bản
- Dashboard sâu
- Báo cáo AI có cấu trúc và xuất bản nội bộ

## 4) Giá trị khác biệt cốt lõi

### Không chỉ hiển thị dữ liệu, mà tạo insight hành động
- AI không chỉ trả lời câu hỏi
- AI chủ động tạo “market brief”, “stock brief”, “risk brief”, “scenario analysis”

### AI giải thích được
Mỗi insight AI phải gắn với:
- Dữ liệu giá/khối lượng
- Indicator liên quan
- Tin tức hoặc sentiment nếu có
- Mức độ tin cậy
- Cảnh báo giới hạn mô hình

### Trải nghiệm đẹp và khác biệt
- Dark theme cao cấp là chủ đạo
- Chuyển động tinh tế
- Hero section ấn tượng, cảm giác công nghệ + tài chính + AI
- Chart là trung tâm, không phải phần phụ

## 5) Đề xuất tên sản phẩm
- StockPilot AI
- QuantVista
- SignalFlow
- AlphaLens
- MarketNexus AI
- TradeWhisper
- PulseAlpha
- VinaAlpha AI

**Khuyến nghị:** chọn tên ngắn, dễ brand, dễ mua domain, có thể dùng quốc tế.

---

# 6) Cấu trúc tính năng toàn hệ thống

## 6.1 Public features

### Trang chủ
Mục tiêu:
- Truyền tải định vị sản phẩm trong 5 giây
- Dẫn người dùng vào tra cứu mã, market overview, AI brief, pricing
- Tạo ấn tượng “high-end fintech + AI-native”

### Trang thị trường tổng quan
Nội dung:
- Chỉ số chính
- Heatmap ngành
- Top tăng/giảm
- Thanh khoản nổi bật
- Breadth market
- Tin tức nổi bật
- AI market summary

### Trang tra cứu mã cổ phiếu
Nội dung:
- Giá hiện tại
- OHLCV
- Chart nâng cao
- Indicator panels
- Key levels
- Dòng tiền / volume anomalies
- Tin tức liên quan
- AI stock brief
- Luận điểm bullish/bearish
- Rủi ro ngắn hạn / trung hạn

### Trang phân tích kỹ thuật
Nội dung:
- Danh sách chỉ báo
- Mô hình giá
- Breakout scanner
- Relative strength
- Multi-timeframe trend map
- AI technical interpretation

### Trang screener
Nội dung:
- Filter theo giá, volume, market cap, sector, RSI, MACD, EMA cross, breakout, gap, earnings, sentiment
- Preset scanner: Momentum, Swing setup, Oversold reversal, Trend continuation, High volume breakout

### Trang tin tức & AI digest
Nội dung:
- News feed theo mã/ngành/thị trường
- Sentiment score
- AI summary 1 câu / 1 phút / chuyên sâu
- Tin nóng có ảnh hưởng cao

### Trang pricing
Các gói:
- Free
- Pro
- Elite

## 6.2 Logged-in features

### Dashboard cá nhân
- Watchlist
- AI recap buổi sáng / cuối ngày
- Alert gần nhất
- Danh sách mã đang theo dõi
- Các cơ hội nổi bật theo khẩu vị

### Portfolio intelligence
- Nhập danh mục thủ công hoặc đồng bộ broker về sau
- Phân tích phân bổ
- Rủi ro tập trung
- Lãi/lỗ
- Exposure theo ngành
- AI portfolio review

### Alert center
- Giá chạm ngưỡng
- Breakout volume
- RSI vào vùng quá mua/quá bán
- MACD cross
- Tin tức bất thường
- AI alert: phát hiện sự kiện đáng chú ý

### AI Copilot
Các mode:
- Ask Market
- Ask Stock
- Compare Stocks
- Explain Chart
- Build Watchlist
- Risk Review
- Scenario Planning

### Notebook / saved insights
- Lưu báo cáo AI
- Gắn tag
- Chia sẻ link nội bộ

## 6.3 Admin / internal
- Quản trị user
- Quản trị gói trả phí
- Quản trị nội dung landing page/blog
- Theo dõi API/data ingestion health
- Theo dõi queue jobs
- Moderation cho AI generated content nếu cần

---

# 7) Information Architecture tối ưu

## Public routes
- /
- /markets
- /stocks
- /stocks/[symbol]
- /technical-analysis
- /screeners
- /news
- /pricing
- /about
- /blog

## Authenticated routes
- /dashboard
- /watchlist
- /portfolio
- /alerts
- /copilot
- /notebook
- /settings
- /billing

## Admin routes
- /admin
- /admin/users
- /admin/content
- /admin/data-health
- /admin/queues
- /admin/analytics

---

# 8) Trang chủ: cấu trúc nội dung chi tiết

## 8.1 Hero section
### Mục tiêu
- Nói rõ sản phẩm làm gì
- Cho cảm giác premium
- Có search ngay lập tức
- Có demo panel trực quan

### Headline đề xuất
**Phân tích chứng khoán sâu hơn. Nhanh hơn. Thông minh hơn với AI.**

### Subheadline
Theo dõi dữ liệu thị trường, đọc biểu đồ nâng cao, nhận insight kỹ thuật và tóm tắt đầu tư được hỗ trợ bởi AI — tất cả trong một nền tảng research hiện đại.

### CTA
- Bắt đầu miễn phí
- Xem demo live
- Tra cứu mã ngay

### Thành phần thị giác trong hero
- Nền gradient tối + grid tài chính tinh tế
- Một mockup dashboard nổi lớn ở giữa
- Floating cards:
  - AI Signal Summary
  - Market Breadth
  - Top Movers
  - RSI / MACD snapshot
- Hiệu ứng chuyển động nhẹ theo scroll

### Search thông minh trong hero
Placeholder:
- Nhập mã cổ phiếu, ngành hoặc câu hỏi như “phân tích HPG hôm nay”

## 8.2 Social proof / credibility bar
- Theo dõi dữ liệu đa nguồn
- Hàng ngàn tín hiệu được xử lý mỗi ngày
- Phân tích AI theo thời gian thực
- Tối ưu cho trader và nhà đầu tư

## 8.3 Feature pillars section
### Cột 1: Market Intelligence
- Tổng quan thị trường
- Heatmap ngành
- Dòng tiền và breadth
- AI daily brief

### Cột 2: Technical Analysis Engine
- Chart mượt
- Chỉ báo mạnh
- Multi-timeframe
- Breakout / reversal scanner

### Cột 3: AI Research Copilot
- Tóm tắt dữ liệu
- So sánh mã
- Giải thích chart
- Gợi ý kịch bản và rủi ro

## 8.4 Interactive demo section
- Tabs: Market / Stock / AI / Alerts
- User có thể bấm xem demo như app thật
- Hiển thị chart, panel chỉ báo, AI summary card

## 8.5 Deep feature showcase
Các block zig-zag:
1. Theo dõi thị trường toàn cảnh
2. Phân tích từng mã chuyên sâu
3. Xây watchlist thông minh
4. Nhận cảnh báo đúng thời điểm
5. Quản lý danh mục với AI

## 8.6 Explainable AI section
Tiêu đề:
**AI không chỉ trả lời. AI giải thích vì sao.**
Nội dung:
- Mỗi insight gắn với dữ liệu
- Có confidence score
- Có luận điểm bullish / bearish
- Có cảnh báo “không phải khuyến nghị đầu tư cá nhân hóa”

## 8.7 Pricing preview
- Free: tra cứu cơ bản, market overview, AI giới hạn
- Pro: AI full, screener nâng cao, alerts, watchlist mạnh
- Elite: portfolio intelligence, signal lab, báo cáo sâu, xuất file

## 8.8 FAQ
- Dữ liệu có realtime không?
- AI tạo gợi ý như thế nào?
- Có dùng cho người mới không?
- Có hỗ trợ thị trường Việt Nam không?
- Có thay thế tư vấn tài chính không?

## 8.9 Final CTA
**Bắt đầu nghiên cứu thị trường theo cách hiện đại hơn.**
- Tạo tài khoản miễn phí
- Xem AI market brief ngay

---

# 9) Design direction tối ưu

## Phong cách thương hiệu
- Hiện đại
- Cao cấp
- Tin cậy
- Công nghệ nhưng không lạnh lẽo
- Fintech + AI + phân tích dữ liệu

## Visual language
- Dark mode mặc định
- Nền charcoal / navy rất đậm
- Accent: electric blue + emerald + violet
- Glow vừa phải, không quá cyberpunk
- Glassmorphism dùng tiết chế
- Grid, lines, micro chart, data cards

## Typography
- Heading: mạnh, rõ, hiện đại
- Body: tối ưu readability
- Dùng contrast cao, spacing rộng

## Animation
- Motion tinh tế bằng Framer Motion
- Number ticker animation
- Hover states sắc nét
- Scroll reveal nhẹ
- Skeleton loading đẹp cho dữ liệu thị trường

## Components quan trọng
- Navbar sticky cao cấp
- Mega search command palette
- Card dashboard
- Chart toolbar
- Heatmap panels
- AI insight card
- Confidence badge
- Scenario card bullish/bearish/neutral
- Pricing card nổi bật

---

# 10) Stack công nghệ tối ưu

## Frontend
- Next.js App Router
- TypeScript
- Tailwind CSS
- shadcn/ui cho base components
- Framer Motion cho animation
- TradingView Lightweight Charts hoặc charting layer chuyên biệt cho tài chính
- TanStack Query cho client-side server state khi cần
- Zustand chỉ cho UI state nhẹ

## Backend
### Giai đoạn 1 tối ưu
- Next.js Route Handlers + Server Actions cho phần lớn nghiệp vụ
- Tách background workers riêng cho jobs nặng: ingest dữ liệu, tính indicator, AI batch summary, alert scheduler

### Giai đoạn 2 khi scale
- Tách thành:
  - Web app (Next.js)
  - Data ingestion service
  - AI orchestration service
  - Worker/queue service

## Database
### Lựa chọn khuyến nghị
- PostgreSQL làm core database
- Mở rộng time-series strategy cho bảng OHLCV và ticks
- Redis cho cache, pub/sub, rate limiting, queue support
- Object storage cho ảnh, exports, snapshots, reports

## ORM / query layer
### Khuyến nghị
- Drizzle ORM nếu ưu tiên performance, SQL control, type safety sát DB
- Prisma nếu ưu tiên onboarding dev nhanh và hệ sinh thái dễ học

**Khuyến nghị cuối cùng cho dự án này:**
- Dùng **Drizzle ORM** cho phần dữ liệu thị trường và analytics
- Có thể dùng raw SQL/materialized views cho truy vấn nặng

## Realtime / jobs
- BullMQ cho queue jobs
- Redis để xử lý queue + cache
- Cron jobs để cập nhật dữ liệu định kỳ
- WebSocket hoặc SSE cho realtime watchlist/alerts/market updates

## Auth & billing
- Auth.js
- OAuth + email magic link
- Stripe cho billing quốc tế
- Nếu tập trung Việt Nam có thể thêm cổng thanh toán nội địa ở giai đoạn sau

## AI layer
- OpenAI API cho:
  - Tóm tắt thị trường
  - Tóm tắt mã cổ phiếu
  - So sánh nhiều mã
  - Giải thích kỹ thuật
  - Sinh báo cáo structured output
- RAG nhẹ trên news, filings, notes, user portfolio context
- Rule engine kết hợp AI để tránh hallucination

---

# 11) Kiến trúc dữ liệu và AI tối ưu

## Luồng dữ liệu chuẩn
1. Lấy dữ liệu từ provider market data
2. Đưa vào ingestion pipeline
3. Chuẩn hóa symbol, timeframe, timezone
4. Ghi vào PostgreSQL/time-series tables
5. Tính indicator batch hoặc incremental
6. Cache snapshot nóng ở Redis
7. API/route phục vụ frontend
8. AI lấy dữ liệu đã chuẩn hóa + news + context user
9. Trả insight có cấu trúc

## Nguyên tắc AI bắt buộc
- Không để model tự đoán dữ liệu giá
- Luôn truyền dữ liệu thật đã chuẩn hóa vào prompt/tool
- Tách phần “facts” và phần “interpretation”
- Bắt model trả JSON schema cố định
- Gắn confidence + assumptions + risk flags

## Các loại AI output
### 1. Market Brief
- Tóm tắt 5–10 ý chính
- Xu hướng chung
- Ngành mạnh/yếu
- Rủi ro cần theo dõi

### 2. Stock Brief
- Snapshot
- Trend
- Momentum
- Key levels
- Bull case
- Bear case
- Neutral trigger

### 3. Technical Explain
- Giải thích RSI/MACD/EMA/price action
- Kịch bản tiếp diễn / đảo chiều

### 4. Portfolio Review
- Rủi ro tập trung
- Mã chiếm tỷ trọng cao
- Độ tương quan
- AI note cần chú ý

### 5. Smart Alerts
- Mã có volume spike
- Break cấu trúc kỹ thuật
- News + price reaction bất thường

---

# 12) Data model cốt lõi

## Bảng người dùng
- users
- accounts
- sessions
- subscriptions
- billing_events

## Bảng domain thị trường
- symbols
- exchanges
- sectors
- industries
- companies
- market_indices

## Dữ liệu giá
- ohlcv_1m
- ohlcv_5m
- ohlcv_1h
- ohlcv_1d
- quotes_latest
- volume_profile_snapshots

## Indicator / analytics
- technical_indicators
- trend_snapshots
- support_resistance_levels
- breakout_events
- relative_strength_scores
- sentiment_scores

## Tin tức / research
- news_articles
- symbol_news_map
- ai_market_briefs
- ai_stock_briefs
- ai_reports

## User feature tables
- watchlists
- watchlist_items
- portfolios
- portfolio_holdings
- alerts
- notebooks
- saved_reports

## Hệ thống / jobs
- ingestion_logs
- ai_jobs
- alert_events
- webhook_events

---

# 13) API/domain modules nên xây

## market module
- market overview
- top movers
- sector heatmap
- breadth data

## stocks module
- symbol profile
- quote snapshot
- OHLCV history
- technical indicators
- stock AI brief

## screener module
- filter builder
- preset screens
- result ranking

## news module
- ingest news
- tag symbol
- sentiment scoring
- AI summarization

## alerts module
- user-defined alerts
- system-generated alerts
- delivery: email / push / in-app

## portfolio module
- holdings
- pnl
- allocation
- risk analytics
- AI review

## copilot module
- prompt templates
- tool calling
- structured responses
- answer provenance

## admin module
- user management
- content blocks
- model usage monitoring
- prompt experiments

---

# 14) Cấu trúc codebase đề xuất

## Monorepo khuyến nghị
- apps/web
- apps/worker
- packages/ui
- packages/config
- packages/db
- packages/market-core
- packages/ai-core
- packages/types

## apps/web
- app/
- components/
- features/
- hooks/
- lib/
- server/
- styles/

## app/ gợi ý
- (marketing)/
- (dashboard)/
- api/
- stocks/[symbol]/
- markets/
- screeners/
- news/
- pricing/

## features/ gợi ý
- auth/
- market/
- stocks/
- chart/
- technical/
- screener/
- ai/
- alerts/
- portfolio/
- billing/

## server/
- db/
- services/
- repositories/
- jobs/
- cache/
- ai/
- providers/

---

# 15) Kiến trúc trang chi tiết mã cổ phiếu

## Layout tối ưu
### Khu 1: Header snapshot
- Symbol
- Company name
- Giá hiện tại
- % thay đổi
- Volume
- Market cap
- Sector
- Buttons: Add watchlist / Compare / Ask AI

### Khu 2: Main chart area
- Candlestick chart
- Timeframes
- Drawing tools cơ bản
- Overlays: EMA, VWAP, Bollinger, volume
- Indicator tabs: RSI, MACD, ATR

### Khu 3: AI summary panel
- Xu hướng hiện tại
- Key support / resistance
- Tín hiệu đáng chú ý
- Kịch bản bullish
- Kịch bản bearish
- Confidence

### Khu 4: Fundamentals / snapshot
- PE/PB (nếu có)
- Earnings date
- Sector rank
- Relative performance

### Khu 5: News & sentiment
- Tin mới nhất
- AI summary news
- Sentiment score

### Khu 6: Related stocks / compare
- Mã cùng ngành
- Mã mạnh hơn/yếu hơn

---

# 16) AI Prompt/Product strategy

## Các nguyên tắc prompt
- Cấu trúc role rõ ràng
- Facts block riêng
- User context riêng
- Output schema cố định
- Không cho phép AI dự đoán số liệu không có nguồn

## Các tool AI nội bộ
- get_market_overview()
- get_stock_snapshot(symbol)
- get_technical_state(symbol, timeframe)
- get_news_context(symbol)
- get_portfolio_context(userId)
- compare_symbols(symbols[])

## Structured response schema mẫu cho stock brief
- symbol
- market_regime
- summary
- trend
- momentum
- volatility
- support_levels[]
- resistance_levels[]
- bull_case
- bear_case
- triggers_to_watch[]
- risk_flags[]
- confidence
- disclaimer

---

# 17) Lộ trình triển khai theo phase

## Phase 0: Discovery + design system
2–3 tuần
- Chốt brand
- Chốt market focus
- Chốt data provider
- Wireframe các màn chính
- Design system + homepage concept

## Phase 1: MVP có thể ra mắt
4–8 tuần
- Trang chủ
- Auth
- Market overview
- Trang chi tiết mã
- Chart cơ bản
- AI stock brief
- Watchlist
- Alerts cơ bản

## Phase 2: Pro features
4–6 tuần
- Screener nâng cao
- AI market brief
- News sentiment
- Portfolio intelligence
- Pricing/billing

## Phase 3: Advanced intelligence
6–10 tuần
- Smart alerts
- Compare symbols AI
- Scenario engine
- Backtest lite
- Notebook / saved reports

## Phase 4: Scale
- Tách worker/service
- Tối ưu ingestion
- Mở app mobile/web hybrid
- Mở rộng nhiều thị trường

---

# 18) KPI sản phẩm nên đo
- Landing page conversion rate
- Search-to-stock-page conversion
- Signup conversion
- D1 / D7 / D30 retention
- Watchlist creation rate
- Alerts enabled rate
- AI feature usage per user
- Paid conversion
- Report open rate
- Time spent trên stock detail page

---

# 19) Monetization strategy

## Free
- Market overview cơ bản
- Stock page cơ bản
- AI usage giới hạn
- 1 watchlist

## Pro
- AI briefs đầy đủ
- Advanced chart indicators
- 10+ alerts
- Screener nâng cao
- News sentiment

## Elite
- Portfolio intelligence
- Premium AI reports
- Advanced signal lab
- Priority alerts
- Export/reporting

---

# 20) Rủi ro chính và cách giảm rủi ro

## Rủi ro 1: AI hallucination
Giải pháp:
- Chỉ cho AI dựa trên facts block
- Structured outputs
- Cấm tự bịa dữ liệu

## Rủi ro 2: Data provider cost
Giải pháp:
- Thiết kế abstraction layer ngay từ đầu
- Cache mạnh
- Tách hot/cold paths

## Rủi ro 3: Trang chậm vì chart + dữ liệu nặng
Giải pháp:
- SSR/streaming hợp lý
- Lazy load chart nặng
- Cache theo timeframe

## Rủi ro 4: Người dùng hiểu nhầm là tư vấn đầu tư cá nhân
Giải pháp:
- Hiển thị disclaimer rõ
- Định vị là research & education platform
- Có confidence/risk explanation

---

# 21) Stack đề xuất cuối cùng để bắt đầu ngay

## Phiên bản tối ưu để launch nhanh nhưng vẫn có đường scale
- Next.js App Router
- TypeScript
- Tailwind CSS
- shadcn/ui
- Framer Motion
- TradingView Lightweight Charts
- TanStack Query
- Drizzle ORM
- PostgreSQL
- Redis
- BullMQ
- Auth.js
- Stripe
- OpenAI API
- Vercel cho web
- Worker riêng cho jobs nặng

---

# 22) MVP scope nên build đầu tiên

## Must-have
- Landing page cực đẹp
- Search stock
- Stock detail page
- Candlestick chart + 3–5 indicators cốt lõi
- AI stock brief
- Watchlist
- User auth

## Nice-to-have ngay sau đó
- Market overview
- Alerts
- AI market brief
- Screener preset

## Chưa cần ở giai đoạn đầu
- Backtest phức tạp
- Social community
- Broker sync phức tạp
- Tùy biến chart quá sâu như terminal lớn

---

# 23) Kết luận chiến lược
Dự án nên được xây như một **AI-native stock research platform** với ba trụ:
1. **Data đáng tin**
2. **Chart và technical analysis mạnh**
3. **AI insight có cấu trúc, có giải thích, có cảnh báo rủi ro**

Về mặt thực thi, lựa chọn tối ưu là:
- Bắt đầu bằng **Next.js fullstack monolith có worker riêng**
- Dùng **PostgreSQL + Redis + Drizzle**
- Dùng **OpenAI cho AI briefs/coplaying/report generation**
- Tập trung làm **homepage + stock detail page + AI brief** thật khác biệt và thật đẹp trước

Nếu làm đúng, đây không chỉ là một web app xem giá, mà là một sản phẩm có thể phát triển thành terminal research thông minh cho nhà đầu tư hiện đại.


---

# 24) Cấu trúc monorepo triển khai thực chiến

```txt
stock-ai-platform/
├─ apps/
│  ├─ web/                         # Next.js app
│  │  ├─ app/
│  │  │  ├─ (marketing)/
│  │  │  │  ├─ page.tsx
│  │  │  │  ├─ pricing/page.tsx
│  │  │  │  ├─ about/page.tsx
│  │  │  │  └─ blog/page.tsx
│  │  │  ├─ (app)/
│  │  │  │  ├─ dashboard/page.tsx
│  │  │  │  ├─ watchlist/page.tsx
│  │  │  │  ├─ portfolio/page.tsx
│  │  │  │  ├─ alerts/page.tsx
│  │  │  │  ├─ copilot/page.tsx
│  │  │  │  └─ settings/page.tsx
│  │  │  ├─ markets/page.tsx
│  │  │  ├─ stocks/[symbol]/page.tsx
│  │  │  ├─ technical-analysis/page.tsx
│  │  │  ├─ screeners/page.tsx
│  │  │  ├─ news/page.tsx
│  │  │  ├─ api/
│  │  │  │  ├─ market/route.ts
│  │  │  │  ├─ stocks/[symbol]/route.ts
│  │  │  │  ├─ stocks/[symbol]/technical/route.ts
│  │  │  │  ├─ stocks/[symbol]/brief/route.ts
│  │  │  │  ├─ screeners/route.ts
│  │  │  │  ├─ alerts/route.ts
│  │  │  │  ├─ ai/copilot/route.ts
│  │  │  │  └─ webhook/stripe/route.ts
│  │  │  ├─ layout.tsx
│  │  │  ├─ globals.css
│  │  │  └─ not-found.tsx
│  │  ├─ components/
│  │  │  ├─ ui/
│  │  │  ├─ layout/
│  │  │  ├─ chart/
│  │  │  ├─ market/
│  │  │  ├─ stock/
│  │  │  ├─ ai/
│  │  │  └─ pricing/
│  │  ├─ features/
│  │  │  ├─ auth/
│  │  │  ├─ market/
│  │  │  ├─ stocks/
│  │  │  ├─ technical/
│  │  │  ├─ screener/
│  │  │  ├─ alerts/
│  │  │  ├─ portfolio/
│  │  │  ├─ copilot/
│  │  │  └─ billing/
│  │  ├─ lib/
│  │  │  ├─ env.ts
│  │  │  ├─ utils.ts
│  │  │  ├─ auth.ts
│  │  │  ├─ redis.ts
│  │  │  ├─ openai.ts
│  │  │  └─ rate-limit.ts
│  │  ├─ server/
│  │  │  ├─ db/
│  │  │  ├─ repositories/
│  │  │  ├─ services/
│  │  │  ├─ ai/
│  │  │  ├─ cache/
│  │  │  └─ providers/
│  │  └─ middleware.ts
│  │
│  └─ worker/                      # Jobs nền
│     ├─ src/
│     │  ├─ queues/
│     │  ├─ processors/
│     │  ├─ schedulers/
│     │  ├─ providers/
│     │  ├─ indicators/
│     │  ├─ alerts/
│     │  └─ ai/
│     └─ package.json
│
├─ packages/
│  ├─ ui/                          # Design system chung
│  ├─ db/                          # Drizzle schema + migrations
│  ├─ types/                       # Domain types
│  ├─ market-core/                 # Logic xử lý giá, indicator, scanner
│  ├─ ai-core/                     # Prompt builders, schema, parsers
│  ├─ config/                      # ESLint, TSConfig, Tailwind config
│  └─ analytics/                   # Tracking helpers
│
├─ docs/
│  ├─ product/
│  ├─ architecture/
│  ├─ prompts/
│  └─ runbooks/
│
├─ turbo.json
├─ package.json
├─ pnpm-workspace.yaml
└─ README.md
```

## Vì sao cấu trúc này tối ưu
- `apps/web` giữ toàn bộ phần người dùng thấy và các API phục vụ trực tiếp UI
- `apps/worker` tách jobs nặng ra khỏi request cycle
- `packages/market-core` và `packages/ai-core` giúp logic tái sử dụng, test dễ và không bị dính chặt vào Next.js
- Monorepo giúp scale team tốt hơn khi thêm frontend, backend, data engineer, AI engineer

---

# 25) Kiến trúc module trong app web

## Layout groups

### (marketing)
Chứa landing page và các trang SEO/public.
Mục tiêu:
- Tốc độ cao
- Nội dung giàu visual
- Tối ưu conversion

### (app)
Chứa dashboard, watchlist, portfolio, alerts, copilot.
Mục tiêu:
- Auth-protected
- Dữ liệu cá nhân hóa
- Tối ưu retention

## Domain-first structure
Mỗi domain nên có:
- `components/`
- `server/queries.ts`
- `server/actions.ts`
- `schemas.ts`
- `types.ts`
- `hooks/`
- `utils/`

Ví dụ:
```txt
features/stocks/
├─ components/
│  ├─ stock-header.tsx
│  ├─ stock-chart.tsx
│  ├─ stock-ai-brief.tsx
│  ├─ stock-news-panel.tsx
│  └─ stock-technical-grid.tsx
├─ server/
│  ├─ queries.ts
│  ├─ actions.ts
│  └─ mappers.ts
├─ hooks/
│  ├─ use-stock-detail.ts
│  └─ use-stock-brief.ts
├─ schemas.ts
├─ types.ts
└─ utils.ts
```

---

# 26) Database schema khởi đầu nên có

## auth & billing

### users
- id
- email
- name
- avatar_url
- created_at
- updated_at

### accounts
- id
- user_id
- provider
- provider_account_id
- access_token
- refresh_token
- created_at

### sessions
- id
- user_id
- expires_at

### subscriptions
- id
- user_id
- plan
- status
- current_period_start
- current_period_end
- stripe_customer_id
- stripe_subscription_id

---

## market master data

### exchanges
- id
- code
- name
- country
- timezone

### sectors
- id
- slug
- name

### industries
- id
- sector_id
- slug
- name

### symbols
- id
- symbol
- exchange_id
- company_name
- sector_id
- industry_id
- market_cap
- currency
- is_active
- metadata_json

---

## market price data

### quotes_latest
- symbol_id
- last_price
- price_change
- percent_change
- open
- high
- low
- previous_close
- volume
- value_traded
- updated_at

### ohlcv_1d
- id
- symbol_id
- ts
- open
- high
- low
- close
- volume
- value_traded

### ohlcv_1h
- id
- symbol_id
- ts
- open
- high
- low
- close
- volume

### ohlcv_15m
- id
- symbol_id
- ts
- open
- high
- low
- close
- volume

**Gợi ý:** giai đoạn đầu chỉ cần `1d`, `1h`, `15m`. Không cần tick data ngay.

---

## analytics & technical

### technical_snapshots
- id
- symbol_id
- timeframe
- rsi_14
- macd
- macd_signal
- macd_hist
- ema_20
- ema_50
- ema_200
- atr_14
- bb_upper
- bb_middle
- bb_lower
- adx_14
- calculated_at

### support_resistance_levels
- id
- symbol_id
- timeframe
- level_type            # support | resistance
- price
- strength_score
- created_at

### trend_snapshots
- id
- symbol_id
- timeframe
- trend_label           # bullish | neutral | bearish
- momentum_label
- volatility_label
- structure_label
- calculated_at

### signal_events
- id
- symbol_id
- timeframe
- signal_type           # breakout | breakdown | ema_cross | rsi_extreme...
- signal_score
- payload_json
- created_at

---

## news & AI

### news_articles
- id
- provider
- title
- summary
- url
- source_name
- published_at
- sentiment_score
- impact_score
- raw_json

### symbol_news_map
- id
- symbol_id
- news_article_id

### ai_market_briefs
- id
- market_scope
- summary
- bullets_json
- regime_label
- risk_flags_json
- confidence_score
- created_at

### ai_stock_briefs
- id
- symbol_id
- timeframe
- summary
- bullish_case
- bearish_case
- key_levels_json
- triggers_json
- risk_flags_json
- confidence_score
- created_at

---

## user personalization

### watchlists
- id
- user_id
- name
- created_at

### watchlist_items
- id
- watchlist_id
- symbol_id
- note
- created_at

### alerts
- id
- user_id
- symbol_id
- alert_type
- condition_json
- delivery_channels_json
- is_active
- created_at

### portfolios
- id
- user_id
- name
- base_currency
- created_at

### portfolio_holdings
- id
- portfolio_id
- symbol_id
- quantity
- average_cost
- opened_at

### saved_reports
- id
- user_id
- report_type
- title
- payload_json
- created_at

---

# 27) API routes nên có từ đầu

## Public data routes

### GET `/api/market`
Trả về:
- index snapshots
- top movers
- sector heatmap
- market breadth
- news highlights

### GET `/api/stocks/[symbol]`
Trả về:
- company info
- latest quote
- trend snapshot
- key metrics

### GET `/api/stocks/[symbol]/candles?timeframe=1d&range=6m`
Trả về OHLCV series cho chart.

### GET `/api/stocks/[symbol]/technical?timeframe=1d`
Trả về indicator snapshot + signals.

### GET `/api/stocks/[symbol]/news`
Trả về news + sentiment.

### GET `/api/screeners?preset=breakout`
Trả về danh sách mã phù hợp preset.

---

## AI routes

### POST `/api/stocks/[symbol]/brief`
Input:
- symbol
- timeframe
- user_context optional

Output:
- summary
- trend
- momentum
- support_levels
- resistance_levels
- bull_case
- bear_case
- triggers
- risks
- confidence

### POST `/api/ai/copilot`
Input:
- mode
- question
- symbols[]
- portfolio_id optional

Output:
- structured answer
- references
- follow_up_actions

### POST `/api/market/brief`
Sinh market brief theo ngày/phiên.

---

## User routes

### GET `/api/watchlists`
### POST `/api/watchlists`
### POST `/api/watchlists/[id]/items`
### DELETE `/api/watchlists/[id]/items/[itemId]`

### GET `/api/alerts`
### POST `/api/alerts`
### PATCH `/api/alerts/[id]`
### DELETE `/api/alerts/[id]`

### GET `/api/portfolio`
### POST `/api/portfolio`
### POST `/api/portfolio/[id]/holdings`

---

# 28) Service layer nên chia thế nào

## services/market.service.ts
Phụ trách:
- Market overview
- Top movers
- Sector strength
- Market breadth

## services/stocks.service.ts
Phụ trách:
- Symbol profile
- Quote snapshot
- OHLCV retrieval
- Chart data transform

## services/technical.service.ts
Phụ trách:
- Tính indicator
- Load indicator snapshot
- Build signal events
- Tạo trend labels

## services/news.service.ts
Phụ trách:
- Ingest news
- Deduplicate
- Map news vào symbol
- Tính sentiment/impact

## services/alerts.service.ts
Phụ trách:
- Tạo điều kiện cảnh báo
- Evaluate condition
- Push event vào queue

## services/portfolio.service.ts
Phụ trách:
- Holdings
- PnL
- Allocation
- Sector exposure
- Risk concentration

## services/ai.service.ts
Phụ trách:
- Build prompt context
- Gọi model
- Parse structured output
- Persist AI brief/report

---

# 29) AI layer nên xây theo pattern nào

## Nguyên tắc
AI không được truy cập DB tùy ý trong prompt text.
AI chỉ nhận dữ liệu đã được server gom sẵn theo schema chuẩn.

## Prompt pipeline chuẩn
1. Load facts
2. Validate facts
3. Build instruction by mode
4. Call model với JSON schema
5. Parse output
6. Validate output
7. Persist + return

## Prompt modes nên có
- `stock_brief`
- `market_brief`
- `compare_symbols`
- `explain_technical`
- `portfolio_review`
- `smart_alert_explanation`

## Output contract ví dụ cho stock brief
```ts
export type StockBrief = {
  symbol: string
  timeframe: '15m' | '1h' | '1d'
  summary: string
  marketRegime: 'bullish' | 'neutral' | 'bearish'
  trend: string
  momentum: string
  supportLevels: number[]
  resistanceLevels: number[]
  bullCase: string
  bearCase: string
  triggersToWatch: string[]
  riskFlags: string[]
  confidence: number
  disclaimer: string
}
```

## Rule engine kết hợp AI
Một số tín hiệu không cần AI suy luận ngay:
- RSI > 70
- EMA20 cắt EMA50
- Giá vượt đỉnh 20 phiên với volume tăng
- ATR tăng bất thường

Hãy để code tạo facts/signal trước, AI chỉ giải thích và xâu chuỗi bối cảnh.

---

# 30) Kiến trúc worker jobs

## Các queue chính
- `market-sync`
- `technical-calc`
- `news-ingest`
- `ai-brief-generate`
- `alert-evaluate`
- `alert-delivery`

## Chu kỳ gợi ý
- Quotes latest: 15s–60s tùy data provider và cost
- Intraday candles: 1m–5m
- Daily candles: cuối phiên và đầu ngày
- Technical snapshot: sau mỗi lần cập nhật candle
- AI market brief: đầu phiên, giữa phiên, cuối phiên
- Alert evaluate: mỗi 1–5 phút hoặc event-driven

## Processor ví dụ
### market-sync processor
- Pull market data
- Normalize symbol
- Upsert quotes
- Upsert candles
- Push `technical-calc`

### technical-calc processor
- Load candles mới nhất
- Tính RSI/MACD/EMA/ATR/Bollinger
- Upsert technical snapshots
- Phát signal nếu có
- Push `ai-brief-generate` khi cần

### ai-brief-generate processor
- Load facts
- Call OpenAI
- Validate JSON
- Save brief
- Warm cache

---

# 31) Redis caching strategy

## Cache keys gợi ý
- `market:overview`
- `stock:{symbol}:snapshot`
- `stock:{symbol}:candles:{timeframe}:{range}`
- `stock:{symbol}:technical:{timeframe}`
- `stock:{symbol}:brief:{timeframe}`
- `user:{userId}:dashboard`

## TTL gợi ý
- Market overview: 15–60 giây
- Quote snapshot: 5–15 giây
- Daily technical snapshot: 1–5 phút
- AI brief: 5–30 phút tùy timeframe

## Nguyên tắc
- Cache dữ liệu nóng, không cache mù quáng
- Invalidate khi có candle mới
- Dùng stale-while-revalidate cho trải nghiệm mượt

---

# 32) Homepage wireframe thực chiến

## Section order tối ưu
1. Sticky navbar
2. Hero premium với search + mock terminal/dashboard
3. Social proof / metrics strip
4. 3 trụ giá trị sản phẩm
5. Interactive product demo
6. Feature showcase dạng zig-zag
7. Explainable AI section
8. Market snapshot preview
9. Pricing preview
10. FAQ
11. Final CTA
12. Footer

## Hero composition chi tiết
### Cột trái
- Heading lớn 2 dòng
- Subheadline 2–3 dòng
- CTA primary + secondary
- Search field thông minh

### Cột phải
- Dashboard mockup lớn
- 3 floating cards:
  - AI Brief
  - Top Movers
  - Signal Alert

## Màu sắc đề xuất
- Background: gần đen + xanh navy
- Primary accent: cyan/electric blue
- Secondary accent: emerald
- Highlight accent: violet nhẹ

## Motion
- Parallax rất nhẹ ở floating cards
- Số liệu animate từ 0 lên
- Chart line auto-draw khi load
- Glow pulse nhẹ ở alert card

---

# 33) Stock detail page wireframe thực chiến

## Above the fold
- Breadcrumb nhỏ
- Symbol + company name
- Price block lớn
- % change + volume + market cap
- Actions: Add watchlist / Set alert / Ask AI / Compare

## Main content grid
### Left column 8 phần
1. Candlestick chart
2. Indicator tabs
3. AI brief card
4. Technical grid
5. Key levels
6. News & sentiment
7. Related stocks
8. Historical mini insights

### Right column 4 phần
1. Trend status card
2. Signal events card
3. Watchlist notes
4. Quick compare widget

---

# 34) Design system và component inventory

## Core primitives
- Button
- Input
- Select
- Tabs
- Tooltip
- Dialog
- Command
- Badge
- Skeleton
- Card
- Drawer

## Domain components
- MarketTickerStrip
- HeroSearch
- StockPriceHeader
- CandleChartPanel
- IndicatorPanel
- SignalBadge
- AIInsightCard
- ConfidenceMeter
- SectorHeatmap
- ScreenerTable
- PortfolioExposureChart
- AlertBuilder

## UX states phải làm kỹ
- loading
- empty state
- error state
- stale data state
- premium locked state

---

# 35) Quy chuẩn coding để team không vỡ kiến trúc

## Quy ước bắt buộc
- Không fetch trực tiếp từ component nếu dữ liệu là domain-critical; đi qua server/service layer
- Không để prompt text rải rác khắp project; tập trung trong `packages/ai-core`
- Không để chart transform logic nằm trong UI component
- Mọi API response cần có schema validate bằng Zod
- Tách `query params parsing` ra helper riêng
- Tách mapping data provider ra adapter layer

## Naming
- Route handlers: `route.ts`
- Services: `*.service.ts`
- Repositories: `*.repo.ts`
- Schemas: `*.schema.ts`
- Validators: `*.validator.ts`
- AI builders: `*.prompt.ts`

---

# 36) Backlog sprint đầu tiên

## Sprint 1
- Khởi tạo monorepo
- Cấu hình Next.js + Tailwind + shadcn/ui
- Tạo design tokens
- Dựng navbar, footer, layout base
- Dựng homepage v1

## Sprint 2
- Setup auth
- Setup DB + Drizzle
- Tạo schema users/symbols/quotes/watchlists
- Xây market overview page
- Xây stock detail page skeleton

## Sprint 3
- Tích hợp candles
- Tạo chart component
- Tính RSI/MACD/EMA cơ bản
- Hiển thị technical snapshot

## Sprint 4
- Xây AI stock brief
- Watchlist CRUD
- Alert CRUD cơ bản
- Dashboard cá nhân v1

---

# 37) Phiên bản MVP tốt nhất để ra mắt

## Public
- Homepage đẹp và khác biệt
- Market overview
- Stock detail page
- Search symbol

## Private
- Sign up / login
- 1 watchlist
- AI stock brief giới hạn
- Alert giá cơ bản

## Chưa cần
- Portfolio sync broker
- Deep backtesting
- Community/social
- Too many indicators

---

# 38) Gợi ý chiến lược launch

## Giai đoạn launch đầu
Tập trung một thị trường duy nhất.
Không nên ôm nhiều loại tài sản quá sớm.

## Chiến thuật hút user
- SEO theo từng mã cổ phiếu
- SEO theo chủ đề “phân tích mã X”, “cổ phiếu ngành Y”, “tín hiệu breakout hôm nay”
- AI market brief hằng ngày
- Email digest + alert nudges

## Tối ưu retention
- Watchlist rất dễ tạo
- Alert dễ bật
- Mỗi lần vào app thấy ngay insight mới

---

# 39) Kế hoạch build đẹp và độc đáo nhất

## Nguyên tắc thẩm mỹ
- Không làm landing page kiểu SaaS template chung chung
- Hero phải có bản sắc terminal tài chính + AI
- Dùng chart thật hoặc mock data đẹp, không dùng illustration rời rạc vô nghĩa
- Giữ data density cao nhưng vẫn có khoảng thở
- Chuyển động ít nhưng tinh tế, cảm giác premium

## Từ khóa design
- cinematic fintech
- AI-native terminal
- premium dark dashboard
- data-rich but elegant
- fast and sharp

---

# 40) Bản chốt để bắt đầu code

## Stack chốt
- Next.js App Router
- TypeScript
- Tailwind CSS
- shadcn/ui
- Framer Motion
- TradingView Lightweight Charts
- Drizzle ORM
- PostgreSQL
- Redis
- BullMQ
- Auth.js
- Stripe
- OpenAI API

## Scope chốt cho bản đầu
- Landing page
- Markets page
- Stock detail page
- Search
- AI stock brief
- Watchlist
- Alert cơ bản

## Tài liệu cần viết tiếp ngay sau blueprint này
1. PRD chi tiết
2. Sitemap + user flows
3. DB schema bằng code Drizzle
4. API contract bằng Zod
5. Prompt specs cho AI outputs
6. Wireframe homepage và stock detail page
```
