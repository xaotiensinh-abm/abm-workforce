---
name: "freepik-spaces"
description: "Hướng dẫn setup Freepik Spaces — tạo luồng tự động chuyên sâu storyboard, batch processing ảnh/video, node-based workflow với Nano Banana Pro + VEO 3.1 + Sora 2 Pro."
---

# Freepik Spaces — Setup Luồng Tự Động Storyboard

Hướng dẫn setup Freepik Spaces từ đầu và xây dựng luồng tự động chuyên sâu cho storyboard — tạo ảnh hàng loạt, biến ảnh thành video, batch processing, và production pipeline.

## Sử dụng skill này khi

- Cần setup Freepik Spaces cho team creative
- Cần tạo storyboard ảnh/video tự động
- Cần batch processing (nhiều biến thể từ 1 concept)
- Cần workflow pipeline: concept → ảnh → video → output
- Cần hướng dẫn node-based workflow cho marketing team

## KHÔNG sử dụng khi

- Chỉ cần 1 ảnh đơn → dùng `imagen`
- Chỉ cần viết prompt video → dùng `veo-video-gen`
- Cần prompt Grok → dùng `grok-imagen`

---

## PHẦN 1: SETUP FREEPIK SPACES TỪ ĐẦU

### Bước 1: Truy cập
```
1. Vào freepik.com → đăng nhập (cần Premium)
2. Menu trái → AI Suite → All Tools → "Spaces"
3. Bấm "New Space" → đặt tên project
```

### Bước 2: Hiểu Canvas & Nodes

Canvas Spaces là một bảng trắng vô hạn, trên đó bạn đặt các **nodes** (khối chức năng) và nối chúng bằng **connectors** (dây kết nối).

#### Danh sách Nodes quan trọng

| Node | Biểu tượng | Chức năng | Khi dùng |
|------|-----------|----------|---------|
| **Upload** | 📤 | Nhập ảnh/video đầu vào | Bắt đầu workflow |
| **Text** | 📝 | Viết prompt, instructions | Mô tả concept |
| **Assistant** | 🤖 | AI xử lý text (tạo list, refine prompt) | Tạo biến thể prompt |
| **Image Generator** | 🖼️ | Tạo ảnh từ prompt | Core node |
| **Video Generator** | 🎬 | Tạo video từ ảnh/prompt | Video production |
| **Upscaler** | 🔍 | Tăng resolution | Quality control |
| **List** | 📋 | Batch input → batch output | **QUAN TRỌNG** cho storyboard |
| **Variations** | 🔄 | Tạo biến thể từ 1 ảnh | Explore directions |

### Bước 3: Chọn AI Models

| Model | Loại | Đặc điểm |
|-------|------|----------|
| **Nano Banana Pro** | Image | Nhanh, visual consistency, text rendering |
| **Flux 2** | Image | Chất lượng cao, chi tiết |
| **Mystic 2.5** | Image | Art/illustration/creative |
| **Kling 3.0** | Video | Realistic motion |
| **Runway** | Video | Creative effects |
| **VEO 3.1** | Video | 4K + audio tích hợp |
| **Sora 2 Pro** | Video | Cinematic quality cao nhất |
| **Magnific** | Edit | Upscale chất lượng cao |

---

## PHẦN 2: LUỒNG STORYBOARD TỰ ĐỘNG

### Workflow 1: Storyboard Ảnh (6-12 frames)

```
┌──────────┐     ┌──────────┐     ┌───────────────┐     ┌──────────┐
│   Text   │────▶│Assistant │────▶│  List Node     │────▶│ Image    │
│(Concept) │     │(Tạo 12   │     │(12 prompts     │     │Generator │
│          │     │ prompts)  │     │ → batch run)   │     │(Nano     │
│          │     │          │     │               │     │Banana)   │
└──────────┘     └──────────┘     └───────────────┘     └────┬─────┘
                                                              │
                                                              ▼
                                                       ┌──────────┐
                                                       │Upscaler  │
                                                       │(Magnific)│
                                                       └──────────┘
```

**Setup từng bước:**

```
Bước 1: Tạo Text node → viết concept tổng:
"Storyboard quảng cáo trà sữa mới: cô gái GenZ khám phá 
thương hiệu, 12 frames, phong cách lifestyle Instagram"

Bước 2: Nối → Assistant node → prompt:
"Dựa trên concept, tạo 12 prompt ảnh cho storyboard.
Mỗi prompt phải có: scene description, camera angle, 
lighting, mood. Nhân vật: cô gái Việt, 22 tuổi, tóc ngắn 
ngang vai, áo crop top trắng. Giữ nhất quán."

Bước 3: Nối → List node → chọn "Split by line"
(Mỗi dòng prompt = 1 input riêng biệt)

Bước 4: Nối → Image Generator → chọn model Nano Banana Pro
Settings: aspect ratio 16:9, quality High

Bước 5: Nối → Upscaler → chọn Magnific 2x

→ BẤM RUN. 12 ảnh storyboard tự động tạo trong 1 lần chạy.
```

### Workflow 2: Ảnh → Video Storyboard

```
┌──────────┐     ┌──────────┐     ┌───────────┐     ┌──────────┐
│ Upload   │────▶│Variations│────▶│ List Node │────▶│  Video   │
│(Ảnh key  │     │(Storyboard│    │(Auto feed │     │Generator │
│ frames)  │     │ mode)     │    │ each var) │     │(Kling/   │
│          │     │           │    │           │     │ VEO)     │
└──────────┘     └──────────┘     └───────────┘     └──────────┘
```

**Setup:**
```
Bước 1: Upload node → đưa vào 3-4 ảnh key frames
Bước 2: Right-click ảnh → Variations → chọn mode "Storyboard"
Bước 3: Nối variations → List node
Bước 4: Nối → Video Generator → chọn model (Kling cho realistic)
Bước 5: Assistant node nối vào Video Generator:
"Với mỗi ảnh: tạo camera movement phù hợp nội dung.
Indoor → slow dolly/pan. Outdoor → tracking. Product → orbit."

→ BẤM RUN. Mỗi ảnh → 1 video clip 4-6 giây.
```

### Workflow 3: Batch Quảng Cáo Đa Ngôn Ngữ

```
┌──────────┐     ┌──────────┐     ┌───────────┐     ┌──────────┐
│   Text   │────▶│Assistant │────▶│ List Node │────▶│ Image    │
│(Ad copy  │     │(Translate │    │(5 languages│    │Generator │
│ tiếng    │     │ → VN, EN, │    │ × 3 styles │    │(Flux 2)  │
│ Việt)    │     │ JP, KR,   │    │ = 15 runs) │    │          │
│          │     │ TH)       │    │            │    │          │
└──────────┘     └──────────┘     └───────────┘     └──────────┘
```

---

## PHẦN 3: TEMPLATE STORYBOARD

### Template A: Video Quảng Cáo Sản Phẩm (30s)

```
Frame 1: Wide shot — bối cảnh lifestyle, chưa thấy sản phẩm
Frame 2: Medium shot — nhân vật trong hoạt động hàng ngày
Frame 3: Close-up — vấn đề/nhu cầu hiện lên trên khuôn mặt
Frame 4: Medium — nhân vật phát hiện sản phẩm
Frame 5: Close-up — cầm sản phẩm, chi tiết packaging
Frame 6: Medium — sử dụng sản phẩm, biểu cảm hài lòng
Frame 7: Wide — kết quả, cuộc sống tốt hơn
Frame 8: Product hero shot — sản phẩm + tagline + CTA
```

### Template B: Story Instagram (9:16, 5 slides)

```
Slide 1: HOOK — hình ảnh gây tò mò, text lớn "Bạn có biết...?"
Slide 2: PROBLEM — minh họa vấn đề, biểu cảm lo lắng
Slide 3: SOLUTION — sản phẩm xuất hiện, ánh sáng highlight
Slide 4: PROOF — before/after hoặc testimonial visual
Slide 5: CTA — "Swipe up" / "Link in bio" + sản phẩm hero shot
```

### Template C: Brand Story (12 frames cinematic)

```
Act 1 — Giới thiệu (Frame 1-3):
F1: Establishing shot — bối cảnh thương hiệu
F2: Nhân vật chính xuất hiện — lifestyle
F3: Chi tiết nội tâm — close-up biểu cảm

Act 2 — Hành trình (Frame 4-8):
F4: Thách thức — dramatic lighting
F5: Hành động — dynamic movement
F6: Sản phẩm/dịch vụ — hero moment
F7: Chuyển biến — before/after
F8: Thành quả — bright, hopeful

Act 3 — Kết thúc (Frame 9-12):
F9: Mở rộng — wider context, impact
F10: Cộng đồng — group shot, connection
F11: Tương lai — forward-looking
F12: Brand lock-up — logo + tagline
```

---

## PHẦN 4: TIPS CHUYÊN SÂU

### Giữ Visual Consistency trong batch

```
✅ Dùng 1 model nhất quán (chọn Nano Banana Pro cho cả batch)
✅ Thêm "style anchor" vào mọi prompt: "phong cách editorial, 
   warm tones, golden hour nhất quán"
✅ Upload reference image + nối vào mọi Image Generator nodes
✅ Dùng Custom Style Training nếu có subscription cao
```

### Tối ưu credits

```
✅ Prototype bằng Nano Banana Pro (nhanh, rẻ) → confirm direction
✅ Final render bằng Flux 2 (chất lượng cao)
✅ Video dùng Kling 3.0 cho realistic, VEO 3.1 cho cinematic
✅ Batch processing qua List node tiết kiệm hơn chạy từng cái
```

### Collaboration workflow

```
1. Creative Director → tạo Space + concept
2. Mời team → Share link, permission: Can Edit
3. Designer → build node workflow
4. Copywriter → viết prompts trong Text nodes
5. Reviewer → comment trên từng output
6. Manager → approve → export final assets
```

## Nguồn gốc
- Deep research: Freepik Spaces Platform (11/2025 - 03/2026)
- Cập nhật: ABM Workforce v2.2 — Jarvis Orchestrator
