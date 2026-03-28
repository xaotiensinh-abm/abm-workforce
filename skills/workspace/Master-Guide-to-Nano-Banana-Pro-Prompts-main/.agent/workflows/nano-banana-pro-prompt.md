---
description: Workflow viết prompt cho Gemini 3 Pro Image (Nano Banana Pro) - Tạo ảnh chuyên nghiệp với chất lượng cao
---

# 🍌 Nano Banana Pro Prompt Workflow

Workflow chuẩn để viết prompt tạo ảnh cho **Google Gemini 3 Pro Image**. Giao tiếp bằng **Tiếng Việt**, output song ngữ.

---

## Bước 1: Phân tích Yêu cầu

1. **Xác định loại input**:
   - TEXT: Mô tả ý tưởng của người dùng
   - IMAGE: Ảnh mẫu cần tham khảo/chỉnh sửa

2. **Kiểm tra Consistency Mode** - Có yêu cầu nào sau KHÔNG?
   - "Giữ nguyên mặt / khuôn mặt" → Kích hoạt **Face Consistency**
   - "Giữ nguyên sản phẩm / trang phục" → Kích hoạt **Product Consistency**
   - "Bóc tách" → Kích hoạt **Product Extraction Mode**

3. **Xác định category**:
   - Chân dung/Portrait
   - Sản phẩm thương mại
   - Infographic/Slide
   - Anime/Illustration
   - Photo Editing
   - Text/Typography
   - Khác (specialized)

---

## Bước 2: Tra cứu Thư viện Mẫu

// turbo
Đọc file tham khảo phù hợp từ thư mục `D:\Antigravity\Skill\Master-Guide-to-Nano-Banana-Pro-Prompts-main`:

| Category | File tham khảo |
|----------|----------------|
| Chân dung, selfie | `portrait_part1.md`, `portrait_part2.md`, `portrait_part3.md` |
| Sản phẩm thương mại | `product_part1.md`, `product_part2.md` |
| Infographic, Slide | `infographic_slide.md` |
| Anime, Illustration | `anime_illustration.md` |
| Logo, Thương hiệu | `brand_design.md` |
| Chỉnh sửa ảnh | `photo_editing.md` |
| Chữ trong ảnh | `text_rendering.md` |
| Kỹ thuật nâng cao | `advanced_prompts.md` |
| Use-case đặc biệt | `specialized_usecases.md` |
| Style keywords | `style_references.md` |

**Cách tìm nhanh**: `grep_search` trong thư mục trên với keyword phù hợp.

---

## Bước 3: Xây dựng Prompt theo Master Formula (6 Yếu tố)

```
[SUBJECT + CHI TIẾT] + [HÀNH ĐỘNG] + [BỐI CẢNH/ĐỊA ĐIỂM]
+ [CAMERA/GÓC MÁY] + [ÁNH SÁNG] + [PHONG CÁCH]
```

### Chi tiết từng yếu tố:

| Yếu tố | Mô tả | Ví dụ |
|--------|-------|-------|
| **Subject** | Ai/cái gì (chi tiết, tuổi, đặc điểm) | "A 25-year-old Vietnamese woman with long wavy hair" |
| **Action** | Đang làm gì | "smiling softly while holding a coffee cup" |
| **Location** | Bối cảnh, địa điểm | "in a cozy Hanoi cafe with vintage decor" |
| **Camera** | Lens, góc máy, framing | "85mm f/1.8, medium shot, eye level" |
| **Lighting** | Ánh sáng, hướng, mood | "golden hour light streaming through window" |
| **Style** | Phong cách, film stock | "Kodak Portra 400 film aesthetic, cinematic" |

---

## Bước 4: Áp dụng Consistency Prompt (nếu cần)

### Giữ Nhân Vật / Khuôn Mặt:
```
Keep the person exactly as shown in the reference image with 100% identical facial features and bone structure. Same skin tone, hair color, and body type.
```

### Giữ Sản Phẩm / Trang Phục:
```
Keep the product exactly as shown in the reference image with 100% identical design, logo, colors, and details. Do not alter the shape or key features.
```

### Bóc Tách Trang Phục (Product Extraction):
```
Keep the outfit exactly as shown, preserving 100% of the original form, silhouette, fabric texture, seams, buttons, and print patterns. Do not change colors or design details. Isolate the garment on a white background.
```

**Quan trọng**: Đặt câu lệnh Consistency **VÀO ĐẦU** prompt!

---

## Bước 5: Format Output Chuẩn

```markdown
## 🎨 Kết quả Prompt

### 📝 Prompt Tiếng Anh (English)
> [Prompt hoàn chỉnh bằng tiếng Anh - ĐÂY LÀ PROMPT CHÍNH]

### 📝 Prompt Tiếng Việt (Vietnamese)
> [Bản dịch/diễn giải để người dùng hiểu]

### 💡 Giải thích Chi tiết
- **Subject**: [Lý do chọn cách mô tả]
- **Lighting**: [Tại sao chọn ánh sáng này]
- **Camera**: [Lens/góc máy phù hợp thế nào]
- **Style**: [Phong cách này đạt mục tiêu gì]

### 🚀 Đề xuất Nâng cao
1. **[Variation 1]**: [Mô tả] → `[keyword thay đổi]`
2. **[Variation 2]**: [Mô tả] → `[keyword thay đổi]`
3. **[Variation 3]**: [Mô tả] → `[keyword thay đổi]`
```

---

## Bước 6: Tạo Ảnh (nếu yêu cầu)

Khi người dùng yêu cầu tạo ảnh ("Tạo ảnh đi", "Generate", "Vẽ cho tôi"):

// turbo
Sử dụng tool `generate_image` với **Prompt Tiếng Anh** đã viết ở Bước 5.

---

## Quick Reference: Keywords Quan trọng

### 📷 Camera & Lens
| Mục đích | Keyword |
|----------|---------|
| Chân dung bokeh | `85mm f/1.8`, `shallow depth of field` |
| Cận cảnh chi tiết | `105mm macro` |
| Street/Documentary | `35mm lens`, `candid` |
| Wide shot | `24mm wide angle` |
| Góc anh hùng | `low angle` |
| Góc yếu đuối | `high angle` |

### 💡 Lighting
| Mood | Keyword |
|------|---------|
| Ấm áp, magical | `golden hour`, `warm rim light` |
| Moody, dramatic | `blue hour`, `low key`, `chiaroscuro` |
| Studio chuyên nghiệp | `softbox`, `three-point lighting` |
| Ngoài trời mềm | `overcast`, `diffused natural light` |

### 🎨 Style
| Mục đích | Keyword |
|----------|---------|
| Ảnh thật như chụp | `photorealistic`, `shot on Sony A7R IV` |
| Film cổ điển | `Kodak Portra 400`, `film grain` |
| Anime Ghibli | `Studio Ghibli style`, `Miyazaki aesthetic` |
| Anime Shinkai | `Makoto Shinkai style`, `Your Name aesthetic` |
| Thương mại cao cấp | `luxury commercial photography`, `high-end` |

### ⚙️ Aspect Ratio
- Portrait: `Aspect Ratio 9:16`
- Landscape: `Aspect Ratio 16:9`
- Square: `Aspect Ratio 1:1`

---

## ⚠️ Lưu ý Quan trọng

### ✅ NÊN làm:
- Dùng **ngôn ngữ tự nhiên** mô tả chi tiết (Nano = "Thinking" model)
- Chỉ định **camera settings cụ thể**: "85mm f/1.8"
- Mô tả **lighting direction và mood**: "golden hour from left"
- Đặt **text trong ngoặc kép** + font/màu nếu cần chữ
- **Edit thay vì re-roll** nếu ảnh đạt 80%

### ❌ KHÔNG nên:
- "4k, masterpiece, trending on artstation" (tag spam kiểu cũ)
- Lặp lại keywords vô nghĩa
- Prompt quá ngắn thiếu context

---

## Ví dụ Prompt Hoàn Chỉnh

**User yêu cầu**: "Tạo ảnh chụp sản phẩm nước hoa cao cấp"

**Output**:

### 📝 Prompt Tiếng Anh
> A luxurious product shot of an elegant perfume bottle with a gold cap, floating gracefully on dark water. White orchid petals and soft pink rose petals are scattered around it. Golden hour sunlight creates warm reflections and gentle ripples across the water surface. Shot with a 90mm macro lens at f/2.8, shallow depth of field with creamy bokeh. High-end commercial photography style, ethereal and sophisticated mood.

### 📝 Prompt Tiếng Việt
> Ảnh sản phẩm cao cấp của một chai nước hoa thanh lịch với nắp vàng, lơ lửng trên mặt nước tối. Cánh hoa lan trắng và cánh hồng nhạt rải rác xung quanh. Ánh nắng hoàng hôn tạo phản chiếu ấm áp và gợn sóng nhẹ nhàng. Chụp với ống kính macro 90mm ở f/2.8, bokeh mịn màng. Phong cách thương mại cao cấp, tâm trạng mơ màng và tinh tế.
