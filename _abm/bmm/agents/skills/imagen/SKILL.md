---
name: "imagen"
description: "Tạo ảnh bằng Google Gemini API — UI assets, documentation illustrations, concept art. Cross-platform Python script."
---

# Imagen — Tạo Ảnh Google Gemini

Tạo ảnh bằng Google Gemini (`gemini-3-pro-image-preview`). Phù hợp cho UI assets, minh họa tài liệu, concept art. Cross-platform (Windows/macOS/Linux).

## Sử dụng skill này khi

- Cần tạo ảnh nhanh cho frontend (placeholder, hero image)
- Cần minh họa cho tài liệu, diagram
- Cần icons, logos, UI assets
- Cần ảnh concept cho ý tưởng

## KHÔNG sử dụng khi

- Cần routing thông minh giữa nhiều models → dùng `image-studio`
- Cần ảnh người thực chi tiết → dùng `image-studio` (Gemini mode)
- Cần tạo video → dùng `veo-video-gen`

## Cách Sử Dụng

### Yêu cầu
- Python 3.6+ (chỉ dùng standard library)
- Biến môi trường: `GEMINI_API_KEY`

### Tạo ảnh cơ bản
```bash
python scripts/generate_image.py "Skyline thành phố tương lai lúc hoàng hôn"
```

### Tùy chỉnh output
```bash
# Chỉ định đường dẫn output
python scripts/generate_image.py "Icon app music player" "./assets/icons/music.png"

# Độ phân giải cao
python scripts/generate_image.py --size 2K "Landscape" "./wallpaper.png"
```

## Ví Dụ

| Use Case | Prompt | Output |
|----------|--------|--------|
| Frontend | "Hero image landing page, abstract tech" | PNG cho HTML/CSS |
| Documentation | "Diagram kiến trúc microservices" | Ảnh cho README |
| UI Assets | "Avatar placeholder cho user profile" | Icon phù hợp component |

## Output
- Format: PNG
- Trả về: file path nếu thành công, error message nếu thất bại

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) — `imagen` (community)
- Adapter: ABM Workforce v2.1 — Jarvis Orchestrator
