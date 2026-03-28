---
description: ✨ Tạo dự án mới
---

# WORKFLOW: /init - The Project Bootstrapper (Complete Setup)

Bạn là **Antigravity Project Initializer**. User muốn bắt đầu dự án từ con số 0, KHÔNG BIẾT các thứ kỹ thuật như package manager, environment variables, git.

**Nhiệm vụ:** Dựng lên "Bộ xương" hoàn chỉnh và hướng dẫn từng bước.

---

## Giai đoạn 1: Vision Capture (Hiểu ý tưởng)

### 1.1. Loại App
*   "Anh muốn làm loại app gì?"
    *   A) **Website đơn giản** (Landing page, Blog, Portfolio)
    *   B) **Web App** (Có đăng nhập, Dashboard, quản lý data)
    *   C) **API Backend** (Chỉ có Server, không giao diện)
    *   D) **Full-stack** (Frontend + Backend + Database)
    *   E) **Mobile App** (Ứng dụng điện thoại)

### 1.2. Tên Project
*   "Tên dự án là gì? (Viết liền không dấu, VD: my-cool-app)"

### 1.3. Thư mục
*   "Anh muốn tạo project ở thư mục nào?"
*   Hoặc tự động tạo trong thư mục hiện tại.

---

## Giai đoạn 2: Tech Stack Selection (AI tự quyết)

AI tự chọn công nghệ phù hợp nhất (User không cần biết):

*   **Website đơn giản:** Next.js + TailwindCSS
*   **Web App:** Next.js + TailwindCSS + PostgreSQL + Prisma + NextAuth
*   **API Backend:** Node.js + Fastify + PostgreSQL + Prisma
*   **Full-stack:** Next.js Full-stack + PostgreSQL
*   **Mobile:** React Native hoặc Expo

---

## Giai đoạn 3: Hidden Setup (Những thứ User không biết)

AI TỰ ĐỘNG thiết lập những thứ quan trọng mà User thường quên:

### 3.1. Environment Variables
*   Tạo file `.env.example` với tất cả các biến môi trường cần thiết.
*   Tạo file `.env.local` để User điền giá trị thật.
*   **Giải thích từng biến:**
    ```
    # Database connection
    DATABASE_URL=postgresql://user:password@localhost:5432/mydb
    
    # Authentication secret (Random string, keep secret!)
    NEXTAUTH_SECRET=your-secret-here
    
    # App URL
    NEXT_PUBLIC_APP_URL=http://localhost:3000
    ```

### 3.2. Git Setup
*   Khởi tạo Git repository.
*   Tạo `.gitignore` chuẩn (ignore node_modules, .env, etc.).
*   Tạo commit đầu tiên: "Initial project setup".

### 3.3. Code Quality Tools
*   Cài ESLint (Kiểm tra lỗi code).
*   Cài Prettier (Format code đẹp).
*   Tạo config files.

### 3.4. Folder Structure
*   Tạo cấu trúc thư mục chuẩn Enterprise:
    ```
    /src
      /app (hoặc /pages)
      /components
      /lib
      /services
      /types
      /utils
    /docs
      /specs
      /architecture
    /scripts
    /public
    ```

### 3.5. README.md
*   Tạo README với hướng dẫn:
    *   Cách cài đặt
    *   Cách chạy dev server
    *   Cách build production
    *   Cấu trúc thư mục

---

## Giai đoạn 4: Dependencies Installation

### 4.1. Core Dependencies
*   Chạy `npm install` (hoặc yarn/pnpm).
*   Cài các thư viện cần thiết theo loại app.

### 4.2. Dev Dependencies
*   TypeScript
*   ESLint, Prettier
*   Testing tools (Jest, Playwright)

---

## Giai đoạn 5: Database Setup (Nếu cần)

### 5.1. Chọn Database
*   **SQLite:** Đơn giản, không cần cài gì thêm.
*   **PostgreSQL:** Chuyên nghiệp, cần cài riêng.

### 5.2. Hướng dẫn cài Database (Nếu PostgreSQL)
*   "Anh đã cài PostgreSQL chưa?"
    *   **Chưa:** Hướng dẫn cài (link download, bước cài).
    *   **Rồi:** "Username và password database là gì?"

### 5.3. Initial Schema
*   Tạo file migration cơ bản (Users table nếu có Auth).

---

## Giai đoạn 6: First Run Test

1.  Chạy `npm run dev` để kiểm tra.
2.  Mở browser tại `http://localhost:3000`.
3.  Xác nhận app hoạt động.

---

## Giai đoạn 7: Documentation Bootstrap

1.  Tạo `docs/architecture/system_overview.md` sơ khai.
2.  Chạy `/save-brain` để lưu cấu trúc ban đầu.

---

## Giai đoạn 8: Handover

1.  Báo User: "Dự án đã sẵn sàng!"
2.  Tóm tắt:
    *   "Tech stack: [Danh sách]"
    *   "Chạy dev: `npm run dev`"
    *   "Mở browser: `http://localhost:3000`"
3.  Next steps:
    *   "Gõ `/plan` để bắt đầu thiết kế tính năng đầu tiên."
    *   "Gõ `/visualize` nếu muốn làm giao diện trước."

---

## ⚠️ NEXT STEPS (Menu số):
```
1️⃣ Bắt đầu tính năng đầu tiên? /plan
2️⃣ Thiết kế UI trước? /visualize
3️⃣ Chạy thử app? /run
```
