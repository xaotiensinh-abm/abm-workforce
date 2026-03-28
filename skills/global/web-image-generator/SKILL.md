---
name: "Goal"
description: "Sinh ảnh **nhẹ, tối ưu cho web** bằng Gemini 3.1 Flash Image Preview API."
---

﻿---
name: web-image-generator
description: Generate lightweight web-optimized images (WebP) via Gemini API. 10 presets for web assets.
---
---

# Goal

Sinh ảnh **nhẹ, tối ưu cho web** bằng Gemini 3.1 Flash Image Preview API.
Tự động chọn aspect ratio + resolution phù hợp từng vùng layout, xuất WebP
mặc định để đạt Web Performance Budget (<200KB hero, <80KB cover, <40KB thumb).

# Instructions

## Step 0: Environment Setup

⚠️ **SECURITY (CODE-2)**: API key PHẢI dùng environment variable.

```powershell
$env:GEMINI_API_KEY = "<user's key>"
```

## Step 1: Analyze Website Layout

Trước khi sinh ảnh, **đo kích thước thực** của vùng cần ảnh:

```javascript
// Browser console hoặc browser_subagent
const el = document.querySelector('.hero');
const rect = el.getBoundingClientRect();
console.log(`${Math.round(rect.width)}×${Math.round(rect.height)}`);
```

## Step 2: Chọn Preset

### Web-Optimized Presets (mặc định nhẹ)

| Preset | Ratio | Size | Target | Use Case |
|--------|-------|------|--------|----------|
| `hero` | `16:9` | `1K` | <200KB | Hero banner, full-width |
| `cover` | `3:4` | `512` | <80KB | Book/novel cover portrait |
| `card` | `4:3` | `512` | <60KB | Horizontal card |
| `square` | `1:1` | `512` | <50KB | Avatar, icon, square card |
| `thumb` | `3:4` | `512` | <40KB | Thumbnail, sidebar |
| `og` | `16:9` | `1K` | <150KB | OpenGraph/social share |
| `story` | `9:16` | `512` | <60KB | Mobile full-screen |
| `banner` | `21:9` | `1K` | <150KB | Ultra-wide cinematic |
| `portrait` | `2:3` | `1K` | <120KB | Tall poster |
| `wide` | `3:2` | `1K` | <130KB | Detail page header |

### High-Quality Presets (dùng `--hq` flag)

Thêm `--hq` để tăng resolution lên 2K cho print/marketing:
```powershell
node generate.js hero --hq "prompt" ./output.webp
```

## Step 3: Generate Image

### Cú pháp cơ bản

```powershell
node generate.js <preset> "<prompt>" [output_path]
```

### Các modes

```powershell
# 1. Text-to-Image (mặc định)
node generate.js hero "Cảnh núi tiên hiệp mờ sương, cung điện nổi trên mây" ./hero.webp

# 2. Image Editing — truyền reference image
node generate.js cover --ref ./existing-cover.png "Thay nền thành mây" ./cover-new.webp

# 3. High Quality — resolution 2K
node generate.js hero --hq "Cảnh chiến trường tiên hiệp hoành tráng" ./hero-hq.webp

# 4. Pro Model — dùng Gemini 3 Pro (chất lượng cao nhất, hỗ trợ 4K)
node generate.js hero --pro "Cảnh chiến trường phong cách điện ảnh" ./hero-pro.webp

# 5. Custom ratio + size
node generate.js --custom --ratio 4:5 --size 1K "Portrait character" ./custom.webp

# 6. Chọn format output
node generate.js hero --format png "prompt" ./hero.png   # PNG (lossless)
node generate.js hero --format jpeg "prompt" ./hero.jpg  # JPEG (smaller)

# 7. Vietnamese Text Rendering — render chữ tiếng Việt lên ảnh
node generate.js cover --text "Cover bia truyen voi chu 'PHAM NHAN TU TIEN' phong cach thu phap" ./cover-vn.webp

# 8. Google Search Grounding — tra cứu thông tin truyện chính xác
node generate.js hero --search "Pham Nhan Tu Tien novel cover scene" ./hero-search.webp

# 9. Search + Text combo — vừa tra cứu vừa render text
node generate.js cover --search --text "Cover for Pham Nhan Tu Tien novel with title text" ./cover-full.webp
```

### Lưu ý Vietnamese Text Rendering

- Dùng `--text` flag để model suy nghĩ (TEXT+IMAGE) trước khi render
- Gemini 3 hỗ trợ **enhanced text rendering** cho nhiều ngôn ngữ kể cả tiếng Việt
- Nên dùng prompt gốc tiếng Anh + specify Vietnamese text trong quotes
- Ví dụ: `"Book cover with Vietnamese title 'PHÀM NHÂN TU TIÊN' in golden calligraphy"`

### Lưu ý Google Search Grounding

- Dùng `--search` flag khi cần thông tin chính xác về bộ truyện/nhân vật
- Model sẽ tự tra Google → lấy facts → tạo ảnh dựa trên dữ liệu thực
- Response bao gồm `groundingMetadata` với các nguồn web tham khảo
- **Lưu ý:** Search-based images kết quả dựa trên text search, không phải image search

## Step 4: Viết Prompt Hiệu Quả

> **Nguyên tắc #1 từ Google:** "Mô tả cảnh, đừng liệt kê từ khóa."
> Một đoạn văn tường thuật luôn tốt hơn danh sách keyword rời rạc.

### Prompt Template — Narrative Style

```
[Mô tả bối cảnh + chủ thể + hành động], được chiếu sáng bởi [ánh sáng].
Góc chụp [camera angle], tạo cảm giác [mood/atmosphere].
[Chi tiết bề mặt, texture, phong cách nghệ thuật].
```

### Ví dụ theo preset:

**hero (16:9 cinematic):**
```
"Cảnh rộng đỉnh núi tiên giới lúc hoàng hôn, những ngọn tháp pha lê
nổi giữa biển mây hồng. Ánh sáng vàng chiếu xuyên qua màn sương,
tạo bầu không khí huyền bí. Phía dưới là dòng sông phát sáng.
Góc chụp wide-angle, phong cách fantasy digital art, phần dưới tối
để đặt text overlay."
```

**cover (3:4 portrait):**
```
"Chân dung một kiếm khách trẻ mặc áo dài trắng đứng trước cổng đá cổ,
tay cầm thanh kiếm phát sáng xanh nhạt. Gió thổi tung tóc và vạt áo.
Ánh sáng rim lighting từ phía sau tạo viền sáng quanh nhân vật.
Bối cảnh núi non mờ ảo, phong cách fantasy illustration chi tiết."
```

**thumb (3:4 small — cần đơn giản):**
```
"Biểu tượng ngọn lửa vàng rực trên nền đen, thiết kế icon tối giản,
độ tương phản cao, bố cục centered, tối ưu cho hiển thị nhỏ."
```

### Best Practices (từ Gemini docs):

1. **Càng cụ thể càng tốt** — "giáp tinh xảo khắc hoạ lá bạc" > "giáp fantasy"
2. **Cung cấp bối cảnh & ý định** — "biểu trưng cho thương hiệu chăm sóc da tối giản"
3. **Phủ định ngữ nghĩa** — "con đường yên tĩnh, vắng vẻ" thay vì "không có xe"
4. **Hướng dẫn từng bước** cho cảnh phức tạp — "Trước tiên tạo nền rừng sương...
   Sau đó thêm bàn thờ đá... Cuối cùng đặt thanh kiếm phát sáng lên trên"
5. **Camera language** — wide-angle shot, macro shot, low-angle perspective
6. **Dark area cho text** — hero prompt nên có "phần dưới tối để đặt text overlay"

## Step 5: Batch Generation

```powershell
# Full bộ ảnh cho 1 bộ truyện
$novel = "Phàm Nhân Tu Tiên"
node generate.js hero "Cảnh đỉnh núi tu tiên cho $novel" ./covers/hero-pham-nhan.webp
node generate.js cover "Chân dung nhân vật $novel" ./covers/cover-pham-nhan.webp
node generate.js thumb "Icon cho $novel" ./covers/thumb-pham-nhan.webp
node generate.js og "Banner quảng bá $novel" ./covers/og-pham-nhan.webp
```

## Step 6: Integration

```javascript
// data.js — lightweight image paths
{
  heroBanner: '/covers/hero-pham-nhan.webp',   // 16:9 1K  ~150KB
  cover: '/covers/cover-pham-nhan.webp',        // 3:4  512 ~60KB
  thumbnail: '/covers/thumb-pham-nhan.webp',    // 3:4  512 ~30KB
  ogImage: '/covers/og-pham-nhan.webp',         // 16:9 1K  ~120KB
}
// Total: ~360KB cho 4 ảnh (vs ~1.5MB nếu dùng PNG 2K)
```

# API Reference

## Models

| Model | Best For | Max Res | Ref Images |
|-------|---------|---------|------------|
| `gemini-3.1-flash-image-preview` | Speed + cost balance | 4K | up to 10 |
| `gemini-3-pro-image-preview` | Professional assets | 4K | up to 14 |
| `gemini-2.5-flash-image` | High volume, low latency | 1K | up to 3 |

## Configuration (REST API)

```json
{
  "contents": [{"parts": [{"text": "prompt"}]}],
  "generationConfig": {
    "responseModalities": ["IMAGE"],
    "imageConfig": {
      "aspectRatio": "16:9",
      "imageSize": "1K"
    }
  }
}
```

## Aspect Ratios (Gemini 3.1 Flash)

`1:1` · `1:4` · `1:8` · `2:3` · `3:2` · `3:4` · `4:1` · `4:3` · `4:5` · `5:4` · `8:1` · `9:16` · `16:9` · `21:9`

## Image Sizes

| Value | Approx Pixels | Use Case |
|-------|--------------|----------|
| `512` | ~512px | Thumbnails, cards, icons |
| `1K` | ~1024px | Hero banners, OG images |
| `2K` | ~2048px | Print, marketing (use --hq) |
| `4K` | ~4096px | Ultra-high quality (use --pro) |

> ⚠️ `imageSize` PHẢI uppercase K: `1K` ✅ `1k` ❌. Riêng `512` không có K.

## Languages (Best Performance)

Tiếng Việt ✅ · English ✅ · 日本語 ✅ · 한국어 ✅ · 中文 ✅ + 10 ngôn ngữ khác

# Constraints

- 🚫 KHÔNG hardcode API key (CODE-2)
- 🚫 KHÔNG dùng lowercase 'k' cho imageSize
- 🚫 KHÔNG dùng resolution >1K cho web display (quá nặng, load chậm)
- 🚫 KHÔNG liệt kê keyword — viết prompt narrative style
- ✅ LUÔN đo kích thước vùng web trước khi chọn preset
- ✅ LUÔN dùng WebP cho web (nhẹ hơn PNG 30-50%)
- ✅ LUÔN thêm "phần dưới tối" cho hero prompt (để text đọc được)
- ✅ NÊN dùng `512` cho mọi ảnh hiển thị <600px width
- ✅ NÊN kiểm tra file size sau khi generate — target <200KB

# Examples

## Ví dụ 1: Hero banner nhẹ cho web truyện

**Input:** "Tạo ảnh hero cho trang chủ web truyện tiên hiệp"

**Process:**
1. Đo hero section: 1920×540px → 16:9
2. Chọn preset `hero` (1K, target <200KB)
3. Viết prompt narrative

**Command:**
```powershell
node generate.js hero "Cảnh rộng núi tiên giới lúc bình minh, cung điện
pha lê nổi trên biển mây vàng hồng. Dòng thác nước tinh khí chảy xuống
vực sâu. Ánh sáng golden hour xuyên qua tầng mây tạo god rays huyền bí.
Phong cách fantasy digital art cinematic, phần dưới tối dần cho text" ./covers/hero.webp
```

**Output:** `hero.webp` ~150KB (vs ~500KB nếu PNG 2K)

## Ví dụ 2: Batch cover cho 3 bộ truyện

**Pipeline:**
1. Đo `.novel-card img` → 200×266px → 3:4, cần `512`
2. Generate 3 cover với preset `cover`
3. Output trung bình ~60KB/ảnh → total 180KB cho 3 ảnh

---

<!-- Generated by Skill Creator Ultra v2.0 × Jarvis -->
