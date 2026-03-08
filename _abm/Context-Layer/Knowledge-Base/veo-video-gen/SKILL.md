---
name: "veo-video-gen"
description: "Tạo video AI bằng Google VEO 3.1 — video 4K lên đến 148 giây, text-to-video, image-to-video, audio tích hợp, qua Gemini API hoặc Vertex AI."
---

# VEO Video Gen — Tạo Video AI Google VEO 3.1

Tạo video chất lượng cao bằng Google VEO 3.1 — model video generation hàng đầu của Google DeepMind. Hỗ trợ 4K, audio tích hợp, text-to-video và image-to-video.

## Sử dụng skill này khi

- Cần tạo video từ mô tả text (text-to-video)
- Cần biến ảnh tĩnh thành video (image-to-video)
- Cần video quảng cáo, clip social media, demo sản phẩm
- Cần video có âm thanh tự động (dialogue, sound effects)
- Cần video chất lượng chuyên nghiệp (4K, cinematic)

## KHÔNG sử dụng khi

- Chỉ cần tạo ảnh → dùng `image-studio` hoặc `imagen`
- Cần animation đơn giản → dùng CSS/JS
- Budget hạn chế → VEO 3.1 là paid preview

## Thông Số Kỹ Thuật

| Tính năng | Giá trị |
|-----------|---------|
| **Độ phân giải** | 720p, 1080p, **4K** |
| **Tỷ lệ khung hình** | 16:9 (landscape), 9:16 (portrait) |
| **Thời lượng** | 4-8 giây (1 clip), tối đa **148 giây** (chain 7s segments) |
| **Audio** | ✅ Tự động — dialogue, sound effects, ambient |
| **Input** | Text prompt, image (tối đa 3 reference images) |
| **Models** | `veo-3.1-generate-preview`, `veo-3.1-generate-001`, `veo-3.1-fast-generate-001` |

## Cách Sử Dụng

### Yêu cầu
- Google Cloud project với billing enabled
- Gemini API key hoặc Vertex AI API enabled

### Text-to-Video (Python SDK)
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Tạo video 8 giây
operation = genai.generate_video(
    model="veo-3.1-generate-001",
    prompt="Một quán café Sài Gòn buổi sáng, ánh nắng chiếu qua cửa kính, khách hàng đang uống cà phê, camera pan chậm từ trái sang phải",
    config={
        "aspect_ratio": "16:9",
        "duration": 8,
        "resolution": "1080p"
    }
)

# Chờ video hoàn thành (async)
result = operation.result()
print(f"Video URL: {result.video_url}")
```

### Image-to-Video
```python
operation = genai.generate_video(
    model="veo-3.1-generate-001",
    prompt="Camera zoom chậm vào sản phẩm, ánh sáng studio",
    reference_images=["product_photo.jpg"],
    config={"aspect_ratio": "9:16", "duration": 6}
)
```

### Video Extension (kéo dài video)
```python
operation = genai.extend_video(
    model="veo-3.1-generate-001",
    video="clip_ban_dau.mp4",
    prompt="Tiếp tục cảnh với camera di chuyển ra xa"
)
```

## Kỹ Thuật Prompt

### Cấu trúc prompt tốt
```
[Chủ thể] + [Hành động] + [Môi trường] + [Ánh sáng] + [Phong cách] + [Camera]
```

**Ví dụ:**
- "Cô gái Việt Nam đi bộ trên phố cổ Hà Nội, ánh đèn lồng đỏ, phong cách cinematic, camera tracking shot"
- "Sản phẩm skincare xoay trên bàn, nền gradient pastel, ánh sáng studio, slow motion 4K"

### Negative Prompt
```python
config={"negative_prompt": "mờ, biến dạng, chất lượng thấp, text"}
```

## Các Use Case Kinh Doanh

| Use Case | Aspect Ratio | Duration | Prompt gợi ý |
|----------|-------------|----------|---------------|
| Quảng cáo Facebook | 16:9 | 6-8s | Sản phẩm + lifestyle + CTA |
| Story Instagram | 9:16 | 4-6s | Quick demo + visual impact |
| Demo sản phẩm | 16:9 | 8s ×5 | Mỗi tính năng 1 clip, chain lại |
| Thumbnail YouTube | 16:9 | 4s | Dynamic opener |

## Lưu Ý

- Video generation là async — cần poll status cho đến khi hoàn thành
- VEO 3.1 đang ở "paid preview" — cần Google Cloud billing
- Audio được tạo tự động — bao gồm dialogue nếu có trong prompt
- Tối đa 3 reference images cho consistency

## Nguồn gốc
- Deep research: Google VEO 3.1 API Documentation (2025-2026)
- Xây dựng bởi: ABM Workforce v2.1 — Jarvis Orchestrator
