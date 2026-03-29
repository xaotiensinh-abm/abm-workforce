---
name: "imagen"
description: "Skill chuyên gia tạo prompt ảnh cho Nano Banana 2 / Gemini 3.1 Flash Image — Master Formula 6 yếu tố, Consistency Mode, JSON structured prompts, 10+ use cases chuyên biệt. Giao tiếp tiếng Việt, output prompt song ngữ."
---

# 🍌 Imagen — Kỹ Thuật Viết Prompt Nano Banana 2

Skill cao cấp nhất để viết prompt tạo ảnh chuyên sâu cho **Nano Banana 2** / **Google Gemini 3.1 Flash Image Preview**. Giao tiếp tiếng Việt 🇻🇳, output prompt song ngữ (EN + VN).

## Sử dụng skill này khi

- Cần viết prompt tạo ảnh chất lượng cao (sản phẩm, marketing, social)
- Cần tạo series ảnh đồng nhất (character consistency, brand)
- Cần ảnh có text/chữ chính xác trong ảnh
- Cần storyboard ảnh, lookbook, infographic
- Cần chỉnh sửa ảnh (thay nền, đổi phong cách, chỉnh sửa vùng)

## KHÔNG sử dụng khi

- Cần tạo video → dùng `veo-video-gen`
- Cần storyboard workflow tự động → dùng `freepik-spaces`
- Cần ảnh từ Grok/xAI → dùng `grok-imagen`

---

## PHẦN 1: MASTER FORMULA — CÔNG THỨC 6 YẾU TỐ

Nano Banana 2 là model "Thinking" — hiểu ngữ cảnh và ý định, không chỉ match keywords. Mọi prompt phải tuân theo:

```
[SUBJECT + CHI TIẾT] + [HÀNH ĐỘNG] + [BỐI CẢNH/ĐỊA ĐIỂM]
+ [CAMERA/GÓC MÁY] + [ÁNH SÁNG] + [PHONG CÁCH]
```

| Yếu tố | Ý nghĩa | Ví dụ |
|--------|---------|-------|
| **Subject** | Ai/cái gì | "A 25-year-old Vietnamese woman with long wavy hair" |
| **Action** | Đang làm gì | "smiling softly while holding a coffee cup" |
| **Location** | Bối cảnh | "in a cozy Hanoi cafe with vintage decor" |
| **Camera** | Lens, góc | "85mm f/1.8, medium shot, eye level" |
| **Lighting** | Ánh sáng | "golden hour light streaming through window" |
| **Style** | Phong cách | "Kodak Portra 400 film aesthetic, cinematic" |

### ✅ NÊN làm
- Dùng **ngôn ngữ tự nhiên** mô tả chi tiết
- Chỉ định **camera settings cụ thể**: "85mm f/1.8"
- Mô tả **lighting direction và mood**: "golden hour from left"
- Đặt **text trong ngoặc kép** + chỉ rõ font/màu
- **Edit thay vì re-roll** nếu ảnh đạt 80%

### ❌ KHÔNG cần
- "4k, masterpiece, trending on artstation" (tag spam kiểu cũ)
- Lặp lại keywords vô nghĩa
- Prompt quá ngắn thiếu context

---

## PHẦN 2: CONSISTENCY MODE — GIỮ ĐỒNG NHẤT

### Khi nào kích hoạt?
User nói: "giữ nguyên mặt", "giữ nguyên sản phẩm", "giống hệt", "bóc tách"

### 3 chế độ chính

**1. Giữ Nhân Vật / Khuôn Mặt:**
```
Keep the person exactly as shown in the reference image with 
100% identical facial features and bone structure. 
Same skin tone, hair color, and body type.
[RỒI MÔ TẢ CẢNH MỚI]
```

**2. Giữ Sản Phẩm / Object:**
```
Keep the product exactly as shown in the reference image with 
100% identical design, logo, colors, and details. 
Do not alter the shape or key features.
[RỒI MÔ TẢ BỐI CẢNH MỚI]
```

**3. Bóc Tách Trang Phục (Product Extraction):**
```
Keep the outfit exactly as shown, preserving 100% of the 
original form, silhouette, fabric texture, seams, buttons, 
and print patterns. Do not change colors or design details. 
Isolate the garment on a white background.
```

### Multi-Pose Consistency (giữ nhân vật qua nhiều ảnh)
```
Create [N] images of the same character:
- Pose 1: [description]
- Pose 2: [description]
- Pose 3: [description]

Maintain absolute consistency in:
- Facial features and identity
- Clothing and accessories
- Art style and color palette
- Lighting direction
```

---

## PHẦN 3: TEMPLATES THEO USE CASE

### 🖼️ Portrait / Chân dung

```
Create a photorealistic image of [mô tả người].
[Tư thế và biểu cảm]. [Địa điểm/bối cảnh].
[Lighting: golden hour/studio/natural].
Shot on [lens: 85mm/35mm], [aperture: f/1.8].
[Mood/atmosphere].
```

**Professional Headshot (Silicon Valley Style):**
```
Keep the facial features exactly consistent. 
Dress in a professional navy blue business suit with white shirt.
Background: clean, solid dark gray studio backdrop with subtle 
gradient vignette. Shot on Sony A7III, 85mm f/1.4 lens.
Classic three-point lighting. Natural skin texture with visible 
pores — not airbrushed. Natural catchlights in eyes.
Ultra-realistic, 8K professional headshot.
```

**Emotional Film Photography:**
```
Style: cinematic portrait shot on Kodak Portra 400 film.
Setting: urban street coffee shop window at Golden Hour.
Warm, nostalgic lighting hitting the side of the face.
Film grain and soft focus for dreamy, storytelling vibe.
Action: looking slightly away, holding coffee, relaxed candid expression.
Depth of field, bokeh background of city lights.
```

### 📦 Product Photography

```
Product: [name] - [shape], [material], [color]
Scene: [setting with props]
Lighting: [studio setup / natural]
Camera: [angle], [lens], shallow depth of field
Style: High-end commercial, [mood]
```

**Amazon-Style Product Shot:**
```
Product: [your product]
Background: Pure white (#FFFFFF), no shadows
Lighting: Even diffused lighting from all sides
Camera: Straight-on product shot, fills 85% of frame
Requirements: Clean cutout ready, RGB white background
Style: Amazon/Shopify product listing compliant
```

**Luxury Floating Product:**
```
Product: [BRAND] [PRODUCT NAME] - [bottle shape], [label], [color]
Scene: Luxury product shot floating on dark water with 
[flower type] in [colors] arranged around it.
[Lighting style] creates reflections and ripples.
Mood: [ethereal and luxurious], high-end commercial photography,
[camera angle], shallow depth of field with soft bokeh.
```

### 📊 Infographic / Slide

```
Create a [style: McKinsey/flat/hand-drawn] [type: infographic/slide].
Topic: [subject]
Include: [data points/sections]
Style: [color palette], professional typography
Layout: [structure description]
```

### 🎨 Anime / Illustration

```
[Anime style: Ghibli/Shinkai/Shonen/Chibi]
[Character description with details]
[Pose and action]
[Scene/background]
[Color palette]
[Effects: sparkles/speed lines/glow]
```

### 📱 Social Media Templates

**Instagram Story (9:16):**
```
Create an Instagram Story (9:16 aspect ratio) for [topic].
Style: [minimal/bold/playful/elegant]
Include: [main visual element]
Text: "[headline text]" in [font style]
Color palette: [brand colors]
Interactive element: [poll/question/slider placeholder]
```

**YouTube Thumbnail:**
```
Create an attention-grabbing YouTube thumbnail for [topic].
Include: [person's face with exaggerated expression] 
+ [relevant imagery] + bold text: "[KEY PHRASE]".
High contrast, saturated colors.
Clear focal point, readable at small sizes. 16:9.
```

---

## PHẦN 4: JSON STRUCTURED PROMPTS — PROMPT CẤU TRÚC

### Khi nào dùng JSON?
- Prompt phức tạp nhiều yếu tố
- Cần control chính xác từng thành phần
- Tạo template có thể tái sử dụng

### Portrait JSON Template
```json
{
  "subject": {
    "face": {"preserve_original": true},
    "description": "[detailed character description]",
    "pose": "[pose description]",
    "expression": "[emotion]",
    "clothing": {"outfit": "[mô tả]", "style": "[style]"}
  },
  "environment": {
    "setting": "[location]",
    "elements": ["[prop1]", "[prop2]"],
    "atmosphere": "[mood]"
  },
  "photography": {
    "camera": "[camera model]",
    "lens": "[focal length]mm f/[aperture]",
    "lighting": "[lighting setup]",
    "style": "[photography style]"
  },
  "post_processing": {
    "color_grading": "[color style]",
    "texture": "[grain/smooth]",
    "effects": ["[effect1]", "[effect2]"]
  }
}
```

### Product JSON Template
```json
{
  "product": {
    "name": "[product name]",
    "type": "[category]",
    "material": "[material]",
    "color": "[color palette]"
  },
  "scene": {
    "background": "[background type]",
    "surface": "[surface material]",
    "props": ["[prop1]", "[prop2]"]
  },
  "lighting": {
    "main": "[key light]",
    "fill": "[fill light]",
    "accent": "[rim/accent]",
    "mood": "[lighting mood]"
  },
  "camera": {
    "angle": "[camera angle]",
    "distance": "[shot type]",
    "depth_of_field": "[shallow/deep]"
  },
  "style": "[commercial/editorial/lifestyle]"
}
```

---

## PHẦN 5: PHOTO EDITING — CHỈNH SỬA ẢNH

### Conversational Editing (sau khi generate)
Nano Banana 2 hỗ trợ chỉnh sửa bằng ngôn ngữ tự nhiên:
```
"Change the background to sunset beach"
"Make her dress red instead of blue"
"Add more dramatic shadows"
"Remove the person in background"
"Change from day to night"
```
→ Model tự điều chỉnh lighting và reflections.

### Templates chỉnh sửa
**Thay nền:**
```
Keep the subject exactly as shown.
Replace the background with [new background].
Adjust lighting on subject to match new environment.
Add appropriate shadows and reflections.
Natural edge blending, no halo effect.
```

**Ngày → Đêm:**
```
Convert this daytime scene to nighttime.
Add appropriate artificial lighting sources.
Adjust all colors to cool night tones.
Add stars or moon if sky is visible.
Maintain all subject details while changing atmosphere.
```

**Age Progression:**
```
Show the same person at different ages: 
childhood (5), teenager (15), young adult (25), 
middle age (45), elderly (70).
Maintain consistent facial features across all ages.
```

---

## PHẦN 6: KEYWORD REFERENCE — TRA CỨU NHANH

### Camera & Lens
| Mục đích | Keyword |
|----------|---------|
| Chân dung đẹp | `85mm f/1.4`, `shallow depth of field` |
| Cận cảnh chi tiết | `105mm macro` |
| Street/Documentary | `35mm lens`, `candid` |
| Rộng bối cảnh | `24mm wide angle` |
| Nén hình đẹp | `135mm telephoto compression` |
| Fisheye effect | `fisheye lens, barrel distortion` |

### Lighting
| Mục đích | Keyword |
|----------|---------|
| Ấm áp, magical | `golden hour`, `warm rim light` |
| Moody, dramatic | `blue hour`, `low key`, `chiaroscuro` |
| Studio chuyên nghiệp | `softbox`, `three-point lighting` |
| Đều, flattering | `ring light`, `even illumination` |
| Neon/retro | `pink neon from left`, `blue gel from right` |
| Rembrandt | `Rembrandt lighting pattern, triangle on cheek` |

### Photography Styles
| Style | Keywords |
|-------|----------|
| Editorial | `editorial photography, fashion magazine, high-end` |
| Commercial | `commercial photography, advertising, clean` |
| Lifestyle | `lifestyle photography, candid, natural` |
| Documentary | `documentary style, authentic, raw` |

### Art Styles
| Style | Keywords |
|-------|----------|
| Oil Painting | `oil painting, thick brushstrokes, impasto` |
| Watercolor | `watercolor, soft washes, flowing, delicate` |
| Anime Ghibli | `Studio Ghibli style, Miyazaki aesthetic` |
| Pixel Art | `pixel art, 8-bit, retro gaming` |

### Film/Era Styles
| Style | Keywords |
|-------|----------|
| Kodak Portra | `Kodak Portra 400, warm skin tones, soft grain` |
| Film Noir | `film noir, high contrast, 1940s` |
| 70s Vintage | `70s aesthetic, warm tones, film grain, faded` |
| Y2K | `Y2K aesthetic, glossy, chrome, early 2000s` |

### Color Palettes
| Bảng màu | Mô tả |
|----------|-------|
| Pastel | soft pink, mint, lavender |
| Earth tones | brown, tan, olive |
| Neon | hot pink, electric blue, lime |
| Muted | desaturated, low saturation |
| Monochrome | black, white, gray |

### Aspect Ratios
| Tỷ lệ | Dùng cho |
|--------|---------|
| **1:1** | Instagram post |
| **4:5** | Instagram portrait |
| **9:16** | Stories/Reels/TikTok |
| **16:9** | YouTube/Cinema |
| **3:2** | Standard photo |
| **21:9** | Ultrawide cinema |

---

## PHẦN 7: USE CASES CHUYÊN BIỆT

### E-commerce Virtual Try-On
```
Place [product from image 1] on [model from image 2].
Adjust lighting and shadows to match.
Maintain realistic fabric drape and fit.
Keep model's pose and expression unchanged.
Professional e-commerce photography quality.
```

### 360° Product View
```
Create a 360-degree product turnaround of [product].
Show 8 angles: front, front-left, left, back-left, 
back, back-right, right, front-right.
Consistent lighting across all views. White background.
```

### Food Photography
```
Create a hero shot for [dish name].
Styling: Food styled at peak freshness
Plating: [specific plating description]
Surface: [table/cutting board/marble]
Props: [ingredients, utensils]
Lighting: [natural window/studio overhead]
Steam/freshness: [show warmth if applicable]
```

### Interior Design
```
Redesign this room in [style: Scandinavian/Industrial/Bohemian].
Keep the room layout and architecture.
Replace furniture and decor to match the new style.
Adjust color palette. Maintain realistic lighting.
```

### Magazine Cover
```
A glossy magazine cover with bold words "[TITLE]" in serif font.
Dynamic portrait in high-end fashion [brand colors].
Issue number and date in the corner with barcode.
The magazine is on a white shelf against a wall.
```

---

## PHẦN 8: QUY TRÌNH OUTPUT

### Format output bắt buộc

```markdown
## 🎨 Kết quả Prompt

### 📝 Prompt Tiếng Anh (English)
> [Prompt hoàn chỉnh — ĐÂY LÀ PROMPT CHÍNH cho model]

### 📝 Prompt Tiếng Việt (Vietnamese)
> [Bản dịch/diễn giải để người dùng hiểu]

### 💡 Giải thích Chi tiết
- **Subject**: [Tại sao chọn cách mô tả này]
- **Lighting**: [Tại sao chọn loại ánh sáng này]
- **Camera**: [Tại sao chọn lens/góc máy này]
- **Style**: [Phong cách phù hợp như thế nào]

### 🚀 Đề xuất Nâng cao
1. **[Variation 1]**: [Mô tả] → `[keyword thay đổi]`
2. **[Variation 2]**: [Mô tả] → `[keyword thay đổi]`
3. **[Variation 3]**: [Mô tả] → `[keyword thay đổi]`
```

### Khi tạo ảnh trực tiếp
- Tool: `generate_image` 
- Model: `models/gemini-3-pro-image-preview`
- Dùng **Prompt Tiếng Anh** từ output

---

## Negative Prompts (copy-paste nhanh)
```
Avoid: blurry, low quality, distorted face, extra limbs, 
watermark, text overlay, cropped, out of frame, 
oversaturated, extra fingers, deformed.
```

## Nguồn gốc
- Tài liệu chính thức: `docs/Nano Banana 2 Document/` (SKILL.md + 20 files chuyên biệt)
- Deep research: Google Nano Banana 2 + Gemini 3.1 Flash Image (02/2026)
- Cập nhật: ABM Workforce v2.2 — Jarvis Orchestrator
