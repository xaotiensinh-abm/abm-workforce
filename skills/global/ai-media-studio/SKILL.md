---
name: "Goal"
description: "Orchestrate sản xuất media AI end-to-end — user chỉ cần mô tả ý tưởng → system tự chọn engine (VEO3, Seedance, NanoBanana, Gemini) + preset (Fashion, Wildlife, TVC, Pet Edu) → deliver production-ready"
---

﻿---
name: ai-media-studio
description: Unified AI media production orchestrator â€” routes between Video, Image, Audio workflows.
---
---

# Goal

> **Use this skill when:** AI video, image, or audio production tasks

Orchestrate sản xuất media AI end-to-end — user chỉ cần mô tả ý tưởng → system tự chọn engine (VEO3, Seedance, NanoBanana, Gemini) + preset (Fashion, Wildlife, TVC, Pet Edu) → deliver production-ready package (storyboard + image prompts + video prompts + voice over).

# Instructions

## Step 1: Media Type Router

Phân tích yêu cầu user → xác định loại media cần tạo:

| Tín hiệu | Media Type | Primary Engine |
|-----------|-----------|---------------|
| "video", "clip", "TVC", "quảng cáo video" | 🎥 VIDEO | VEO3 Storyboard Director |
| "ảnh", "hình", "thumbnail", "poster" | 🖼️ IMAGE | NanoBanana Pro Master |
| "transcribe", "phân tích audio/video" | 🎵 ANALYSIS | ai-multimodal |
| "video + ảnh", "storyboard full" | 📦 PACKAGE | VEO3 + NanoBanana combo |

## Step 2: Genre/Preset Router (chỉ cho VIDEO)

| Tín hiệu | Preset | Workflow Source |
|-----------|--------|---------------|
| "thời trang", "fashion", "áo dài", "model" | 👗 Fashion | veo-fashion-director.md |
| "động vật", "wildlife", "thú cưng" | 🦁 Wildlife | wildlife-director.md |
| "quảng cáo", "TVC", "sản phẩm", "thương hiệu" | 📺 TVC Vietnam | sora2-tvc-vietnam.md |
| "thú cưng", "chó mèo", "giáo dục", "edu shorts" | 🐾 Pet Edu | thu-cung-edu-shorts.md |
| "faceless", "AI character", "content machine" | 🤖 Faceless | faceless-content-machine.md |
| Không match preset | 🎬 Generic | VEO3 base workflow |

## Step 3: Execute Pipeline

### 🎥 VIDEO Pipeline:
1. **Director Phase**: Load VEO3 Storyboard Director skill
   - Xác định mode: SEAMLESS (narrative) vs CINEMATIC (TVC)
   - Scene count = Total Duration ÷ 8s
   - Tạo identity locks + scene breakdown
2. **Image Phase**: Load NanoBanana Pro Master skill
   - Sinh Start Frame + End Frame prompts (Master Formula 6 yếu tố)
   - Apply Consistency Lock nếu Seamless mode
3. **Video Phase**: Sinh VEO3 motion prompts (JSON + Natural Language)
   - Nếu user prefer Seedance → switch sang Seedance 2.0 skill
4. **Voice Over Phase** (optional): Script sync 8s timing
5. **Preset Overlay**: Apply genre-specific rules từ matched preset workflow

### 🖼️ IMAGE Pipeline:
1. Load NanoBanana Pro Master skill
2. Phân tích input: text vs image → chọn generation vs editing
3. Apply Master Formula: Subject + Action + Location + Camera + Lighting + Style
4. Generate with `generate_image` tool
5. Đề xuất 3 variations

### 🎵 ANALYSIS Pipeline:
1. Load ai-multimodal skill
2. Route theo format: audio → transcribe, video → analyze, image → understand
3. Batch process nếu multiple files

## Step 4: Quality Check & Delivery

1. Cross-check consistency giữa image prompts và video prompts
2. Verify identity locks maintained across scenes
3. Package all outputs: storyboard + prompts + voice over + reference images
4. Present final package với tree structure

# Examples

## Ví dụ 1: Video thời trang 32 giây

**Input:** "Tạo video thời trang cho bộ sưu tập áo dài mới, 32 giây, style cinematic"
**Router:** Video → Fashion Preset → CINEMATIC mode
**Pipeline:**
- Director: 4 scenes × 8s, product lock (áo dài design)
- NanoBanana: 8 frame prompts (4 start + 4 end), fashion photography style
- VEO3: 4 motion prompts, dynamic lighting per scene
- Voice Over: 4 × 2-second segments, elegant tone
**Output:** `storyboard_aodai/` — 4 files (scene_breakdown + image_prompts + veo3_prompts + voice_over)

## Ví dụ 2: Ảnh sản phẩm cao cấp

**Input:** "Tạo ảnh quảng cáo cho chai nước hoa, style luxury"
**Router:** Image → NanoBanana Pro
**Pipeline:** Master Formula → 90mm macro, golden hour, commercial style → 3 variations
**Output:** EN prompt + VN giải thích + 3 đề xuất nâng cao

## Ví dụ 3: Full package TVC 16 giây

**Input:** "TVC 16 giây cho thương hiệu Vinamilk, target thị trường Việt Nam"
**Router:** Video → TVC Vietnam Preset → CINEMATIC mode
**Pipeline:**
- TVC preset: hỏi khách hàng mục tiêu (IMG-5 rule)
- Director: 2 scenes × 8s + product/brand lock
- NanoBanana: 4 frame prompts
- VEO3: 2 motion prompts, jump cuts ok
**Output:** Complete TVC package sẵn sàng sản xuất

# Constraints

- 🚫 KHÔNG ĐƯỢC tạo video clip >8 giây (VEO3 optimal = 8s)
- 🚫 KHÔNG ĐƯỢC bỏ Consistency Lock cho SEAMLESS mode video
- 🚫 KHÔNG ĐƯỢC xoay người mẫu khi ảnh input chỉ có mặt trước (IMG-3)
- 🚫 KHÔNG ĐƯỢC tạo TVC mà chưa hỏi khách hàng mục tiêu (IMG-5)
- 🚫 KHÔNG ĐƯỢC dùng prompt Seedance >2000 ký tự
- ✅ LUÔN LUÔN hỏi user chọn engine (VEO3 vs Seedance) nếu cả 2 phù hợp
- ✅ LUÔN LUÔN output song ngữ EN+VN cho image prompts (IMG-4)
- ✅ LUÔN LUÔN apply Master Formula 6 yếu tố cho image prompts
- ✅ LUÔN LUÔN chạy seedance-copyright module trước khi dùng Seedance

---

📦 Generated by Skill Generator v4.0
