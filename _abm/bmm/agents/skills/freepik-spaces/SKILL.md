---
name: "freepik-spaces"
description: "Nền tảng thiết kế AI đa model — node-based workflows kết hợp Flux 2, Nano Banana Pro, Kling 3.0, Runway, VEO 3.1, Sora 2 Pro. Batch processing, real-time collaboration, API integration."
---

# Freepik Spaces — Nền Tảng Thiết Kế AI Đa Model

Hệ thống node-based workflows kết hợp nhiều model AI hàng đầu (Flux 2, Nano Banana Pro, Kling 3.0, Runway, VEO 3.1, Sora 2 Pro) trên một canvas duy nhất. Hỗ trợ batch processing, collaboration, và API integration.

## Sử dụng skill này khi

- Cần tạo ảnh/video hàng loạt (batch processing)
- Cần workflow phức tạp kết hợp nhiều công cụ AI
- Cần collaboration real-time trong team creative
- Cần chuyển đổi content đa ngôn ngữ/đa format
- Cần xây dựng pipeline sản xuất content tự động
- Cần template-based production đảm bảo brand consistency

## KHÔNG sử dụng khi

- Chỉ cần 1 ảnh đơn giản → dùng `imagen` hoặc `image-studio`
- Chỉ cần 1 video → dùng `veo-video-gen`
- Cần code/script → dùng tools trực tiếp

## Tổng Quan Nền Tảng

Freepik Spaces (ra mắt 11/2025) là phần của Freepik AI Creative Suite — nền tảng thiết kế node-based cho phép:

```
                    FREEPIK SPACES
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   IMAGE GEN        VIDEO GEN         EDITING
   ├─ Flux 2        ├─ Kling 3.0      ├─ Magnific (upscale)
   ├─ Mystic 2.5    ├─ Runway         ├─ Remove BG
   └─ Nano Banana   ├─ VEO 3.1       ├─ Relight
      Pro           └─ Sora 2 Pro    └─ Style Transfer
                         │
                    ┌────┼────┐
                    ↓         ↓
               AUDIO      AUTOMATION
               ├─ Voice    ├─ List Node (batch)
               ├─ Music    ├─ Templates
               └─ SFX      └─ API Triggers
```

## Node-Based Workflow

### Cấu trúc cơ bản
Mỗi task là một "node" có thể kết nối với nhau:

```
[Text Prompt] → [Image Gen: Flux 2] → [Upscale: Magnific] → [Remove BG] → [Export]
      ↓
[Translate: EN→VN] → [Image Gen: Nano Banana] → [Video Gen: Kling 3.0] → [Add Audio]
```

### Batch Processing (List Node)
Tạo nhiều variations từ 1 workflow:

```
Input List:
├─ Product A + "Phong cách minimalist"
├─ Product B + "Phong cách luxury"
└─ Product C + "Phong cách tech"

→ Kết quả: 3 ảnh sản phẩm × 3 styles = 9 outputs tự động
```

## Các Model Tích Hợp

### Image Generation
| Model | Đặc điểm | Khi dùng |
|-------|----------|---------|
| **Flux 2** | Chất lượng cao, chi tiết | Ảnh marketing chuyên nghiệp |
| **Mystic 2.5** | Art/illustration | Thiết kế sáng tạo |
| **Nano Banana Pro** | Nhanh, rẻ | Batch/iteration nhanh |

### Video Generation
| Model | Đặc điểm | Khi dùng |
|-------|----------|---------|
| **Kling 3.0** | Realistic motion | Video sản phẩm |
| **Runway** | Creative effects | Video quảng cáo nghệ thuật |
| **VEO 3.1** | 4K + audio tích hợp | Video chuyên nghiệp |
| **Sora 2 Pro** | Cinematic quality | Video thương hiệu/film |

### AI Editing
| Công cụ | Chức năng |
|---------|----------|
| **Magnific** | Upscale ảnh chất lượng cao |
| **Remove BG** | Xóa nền tự động |
| **Relight** | Thay đổi ánh sáng |
| **Style Transfer** | Chuyển đổi phong cách ảnh |

## API Integration

### Freepik API
```python
import requests

headers = {"x-freepik-api-key": "YOUR_FREEPIK_API_KEY"}

# Tạo ảnh
response = requests.post("https://api.freepik.com/v1/ai/text-to-image", 
    headers=headers,
    json={
        "prompt": "Sản phẩm trà Việt Nam, phong cách premium",
        "num_images": 4,
        "image_size": "landscape_16_9"
    }
)

# Tạo video từ ảnh
response = requests.post("https://api.freepik.com/v1/ai/image-to-video",
    headers=headers,
    json={
        "image_url": "https://...",
        "motion_type": "zoom_in",
        "duration": 4
    }
)
```

### Workflow Automation qua API
```python
# Trigger workflow từ bên ngoài
response = requests.post("https://api.freepik.com/v1/spaces/workflows/run",
    headers=headers,
    json={
        "workflow_id": "wf_product_shots",
        "inputs": [
            {"product_image": "product_a.jpg", "style": "minimalist"},
            {"product_image": "product_b.jpg", "style": "luxury"}
        ]
    }
)
```

## Use Cases Kinh Doanh

| Use Case | Workflow | Output |
|----------|---------|--------|
| **Content Marketing** | Prompt → Image Gen → Video Gen → Audio | 30 posts/tháng tự động |
| **Product Catalog** | Product Photos → Remove BG → Relight → Batch Export | Catalog hoàn chỉnh |
| **Ad Localization** | English Ad → Translate → Regenerate → Export | Ads cho 5+ thị trường |
| **Brand Kit** | Style Guide → Custom Training → Templates | Consistent branding |
| **Social Media** | Content Calendar → Batch Generate → Schedule | Cross-platform posts |

## Tính Năng Enterprise

- **Permission Management**: Phân quyền user trong team
- **Credit-based Usage**: Kiểm soát chi phí theo credits
- **Custom Style Training**: Train model trên style riêng
- **Legal Indemnification**: Bảo vệ pháp lý cho content AI
- **Real-time Collaboration**: Nhiều người cùng làm trên 1 canvas

## Lưu Ý

- Freepik Spaces chủ yếu chạy trên desktop (mobile đang phát triển)
- Models khác nhau tiêu thụ credits khác nhau — VEO 3.1 và Sora 2 Pro tốn nhiều nhất
- Dùng List Node cho batch processing hiệu quả hơn chạy từng cái
- Kết nối API cần Freepik Premium/Business subscription

## Nguồn gốc
- Deep research: Freepik Spaces Platform Documentation (2025-2026)
- Xây dựng bởi: ABM Workforce v2.1 — Jarvis Orchestrator
