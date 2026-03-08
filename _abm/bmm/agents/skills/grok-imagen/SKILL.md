---
name: "grok-imagen"
description: "Tạo ảnh photorealistic bằng xAI Aurora + Grok Imagine API — text-to-image, image editing, text-to-video. Tích hợp với hệ sinh thái X/Twitter."
---

# Grok Imagen — Tạo Ảnh & Video xAI Aurora

Tạo ảnh photorealistic bằng Aurora (xAI) và Grok Imagine API. Hỗ trợ text-to-image, image editing, text-to-video. Tích hợp hệ sinh thái X/Twitter.

## Sử dụng skill này khi

- Cần tạo ảnh photorealistic chất lượng cao
- Cần tạo ảnh cho content X/Twitter
- Cần chỉnh sửa ảnh AI (multimodal input)
- Cần tạo video ngắn (text-to-video qua Grok Imagine)
- User yêu cầu "dùng Grok tạo ảnh", "Aurora image"

## KHÔNG sử dụng khi

- Cần routing thông minh giữa nhiều models → dùng `image-studio`
- Cần video dài, 4K → dùng `veo-video-gen`
- Cần workflow thiết kế → dùng `freepik-spaces`
- Cần real-time X data (không phải ảnh) → dùng `blockrun` + search=True

## Về Aurora — xAI Image Model

Aurora là autoregressive mixture-of-experts network do xAI phát triển riêng (không còn dùng Flux/Black Forest Labs). Đặc điểm:

| Tính năng | Mô tả |
|-----------|-------|
| **Kiểu model** | Autoregressive MoE (Mixture of Experts) |
| **Chuyên biệt** | Ảnh photorealistic, tuân thủ text prompt chính xác |
| **Input** | Text prompt + ảnh tham khảo (multimodal) |
| **Output** | Ảnh photorealistic chất lượng cao |
| **Platform** | X/Twitter (qua Grok), API (Grok Imagine) |

## Grok Imagine API (Ra mắt 01/2026)

### Capabilities
- **Text-to-Image**: Tạo ảnh từ mô tả text
- **Image-to-Image**: Chỉnh sửa ảnh bằng prompt
- **Text-to-Video**: Tạo video ngắn + audio
- **Video Editing**: Chỉnh sửa video có sẵn

### Sử dụng qua BlockRun
```python
from blockrun_llm import ImageClient

# Tạo ảnh qua Aurora
client = ImageClient()
result = client.generate("Logo công ty công nghệ Việt Nam, phong cách hiện đại")
print(result.data[0].url)
```

### Sử dụng Grok API trực tiếp
```python
import requests

headers = {"Authorization": "Bearer YOUR_XAI_API_KEY"}
payload = {
    "model": "grok-imagine",
    "prompt": "Cô gái Việt Nam trong áo dài trắng, phong cách studio portrait",
    "n": 1,
    "size": "1024x1024"
}
response = requests.post("https://api.x.ai/v1/images/generations", 
                        headers=headers, json=payload)
```

### Kết hợp Grok Chat + Image
```python
from blockrun_llm import setup_agent_wallet
client = setup_agent_wallet()

# Phân tích xu hướng → Tạo ảnh phù hợp
trends = client.chat("xai/grok-3", "Top 5 xu hướng thiết kế 2026?", search=True)
# Sau đó tạo ảnh dựa trên trends...
```

## So Sánh Với Các Model Khác

| Model | Ưu điểm | Nhược điểm | Giá |
|-------|---------|-----------|-----|
| **Aurora (Grok)** | Photorealistic, prompt adherence cao | Mới — ecosystem đang phát triển | API pricing TBD |
| DALL-E 3 | Mature, đa dạng style | Đắt hơn | $0.04/ảnh |
| Nano Banana | Rẻ nhất, nhanh | Artistic, không photorealistic | $0.01/ảnh |
| Gemini Imagen | Free tier, tích hợp Google | Cần API key riêng | Free/Paid |

## Lưu Ý

- Grok Imagine API ra mắt 01/2026 — kiểm tra docs mới nhất
- Aurora tối ưu cho photorealistic — dùng Stability AI cho art/illustration
- Kết hợp với BlockRun để dùng qua micropayment (không cần xAI API key riêng)
- API endpoints có thể thay đổi — check api.x.ai cho version mới nhất

## Nguồn gốc
- Deep research: xAI Aurora + Grok Imagine API Documentation (2025-2026)
- Xây dựng bởi: ABM Workforce v2.1 — Jarvis Orchestrator
