---
name: context7-docs
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: |
  Tra cứu documentation và code examples cập nhật từ source chính thức
  của bất kỳ thư viện, framework, SDK. Dùng CLI `npx ctx7` để lấy docs
  real-time, chống hallucination API. Dùng khi cần: tra cứu cách dùng
  thư viện, tìm API reference, xem code examples, kiểm tra cú pháp
  mới nhất, setup/configuration steps, migration guide, hoặc khi không
  chắc API có tồn tại hay không. Cũng kích hoạt khi user nói "use context7",
  "tra docs", "docs của X", "API reference", "cách dùng thư viện Y",
  "hướng dẫn setup Z", hoặc đơn giản "check docs".
---

# Goal

Tra cứu documentation cập nhật từ source chính thức trong 10 giây, thay
vì dựa vào training data cũ có thể gây hallucination API. Đảm bảo mọi
code generation trong ABM Workforce sử dụng API **thực sự tồn tại** và
**đúng phiên bản**.

# Instructions

## Khi nào kích hoạt

Tự động kích hoạt khi task yêu cầu:
- Viết code dùng thư viện/framework/SDK bên ngoài
- Tra cứu API reference hoặc configuration
- Setup, migration, hoặc integration guide
- Không chắc API/method có tồn tại trong version hiện tại

**Không kích hoạt** khi: logic thuần (không dùng thư viện), viết content/marketing,
hoặc user đã cung cấp đầy đủ code reference.

## Workflow 2 bước

### Bước 1: Tìm Library ID

Chạy lệnh để tìm ID chính xác của thư viện trên Context7:

```bash
npx ctx7 library "<tên thư viện>" "<câu hỏi hoặc keyword>"
```

**Ví dụ:**
```bash
npx ctx7 library react "how to use hooks"
npx ctx7 library prisma "one-to-many relation"
npx ctx7 library nextjs "middleware setup"
```

**Output:** Danh sách libraries khớp, mỗi library có ID dạng `/org/project`.
Chọn library ID phù hợp nhất (thường là kết quả đầu tiên).

**Nếu biết sẵn Library ID** (dạng `/org/project`), bỏ qua bước này và
đi thẳng Bước 2. Các ID phổ biến:
- React: `/facebook/react`
- Next.js: `/vercel/next.js`
- Prisma: `/prisma/prisma`
- Supabase: `/supabase/supabase`
- Express: `/expressjs/express`

### Bước 2: Lấy Documentation

Dùng Library ID từ Bước 1 để lấy docs cụ thể:

```bash
npx ctx7 docs <libraryId> "<câu hỏi chi tiết>"
```

**Ví dụ:**
```bash
npx ctx7 docs /facebook/react "useEffect cleanup with async"
npx ctx7 docs /vercel/next.js "app router middleware authentication"
npx ctx7 docs /prisma/prisma "cascade delete one-to-many"
```

**Tips tối ưu query:**
- Dùng câu hỏi chi tiết thay vì keyword đơn: `"how to handle auth"` tốt hơn `"auth"`
- Chỉ định version nếu cần: `npx ctx7 docs /vercel/next.js/v14 "middleware"`
- Output dạng JSON cho scripting: thêm `--json`

### Bước 3: Áp dụng vào code

Sau khi nhận docs từ Context7:
1. Đọc kỹ code examples và API signatures
2. Kiểm tra version compatibility với dự án hiện tại
3. Áp dụng vào code — ưu tiên patterns từ official docs
4. Nếu docs không đủ chi tiết → chạy query khác với câu hỏi cụ thể hơn

## Decision Tree

```
Cần dùng thư viện/framework?
├── KHÔNG → Không kích hoạt skill
└── CÓ → Đã biết chính xác API?
    ├── CÓ (confident 90%+) → Viết code trực tiếp
    └── KHÔNG hoặc KHÔNG CHẮC → Bước 1: ctx7 library
        └── Tìm được Library ID?
            ├── CÓ → Bước 2: ctx7 docs
            └── KHÔNG → Thư viện chưa có trên Context7
                └── Fallback: dùng kiến thức training data
                    + cảnh báo user "docs chưa verify"
```

# Examples

## Ví dụ 1: Setup Supabase Auth (Happy path)

**Tình huống:** User yêu cầu "setup đăng ký bằng email/password với Supabase"

**Bước 1:**
```bash
npx ctx7 library supabase "email password sign up authentication"
```
→ Output: `/supabase/supabase` (ID)

**Bước 2:**
```bash
npx ctx7 docs /supabase/supabase "email password sign up authentication setup"
```
→ Output: Documentation chính thức với code examples cập nhật

**Kết quả:** Viết code auth dựa trên docs real-time, không dùng API cũ/hallucinated.

## Ví dụ 2: Tra cứu specific version

**Tình huống:** User đang dùng Next.js 14, cần middleware

**Bước 1:** Bỏ qua (đã biết ID)

**Bước 2:**
```bash
npx ctx7 docs /vercel/next.js "middleware redirect unauthenticated users app router"
```
→ Output: Middleware docs cho Next.js version mới nhất

## Ví dụ 3: Thư viện không phổ biến

**Tình huống:** User hỏi "cách dùng Drizzle ORM để tạo migration"

**Bước 1:**
```bash
npx ctx7 library drizzle "migration schema"
```
→ Output: `/drizzle-team/drizzle-orm` (ID)

**Bước 2:**
```bash
npx ctx7 docs /drizzle-team/drizzle-orm "create migration push schema changes"
```
→ Output: Official migration guide

# Constraints

- **Luôn dùng `npx ctx7`** — không cần cài global, nhờ đó skill hoạt
  động trên mọi máy mà không cần setup trước
- **Không cache kết quả** — mỗi lần cần docs, chạy lại lệnh để đảm bảo
  thông tin mới nhất. Documentation thay đổi liên tục theo version
- **Query chi tiết > keyword đơn** — câu hỏi cụ thể cho kết quả chính
  xác hơn. "How to setup JWT middleware in Express" > "express middleware"
- **Không thay thế đọc docs** — Context7 trả về snippets liên quan, nếu
  cần hiểu sâu hơn → gợi ý user đọc full docs tại source
- **Fallback gracefully** — nếu `ctx7` trả lỗi hoặc thư viện chưa có
  trên Context7, dùng training data + gắn cảnh báo "⚠️ Docs chưa verify
  từ source chính thức"
- **Không dùng cho thư viện nội bộ/private** — Context7 chỉ index thư
  viện public. Thư viện internal → dùng codebase search thay thế

<!-- Generated by ABM Skill Generator v1.0 | ABM Workforce -->
