---
name: "image-studio"
description: "Studio tạo ảnh thông minh — routing tự động giữa Gemini (ảnh người thực) và Stability AI (art/illustration/editing). Một lệnh, model tối ưu, kết quả tốt nhất."
---

# Image Studio — Studio Tạo Ảnh Thông Minh

Hệ thống routing thông minh tự chọn model AI phù hợp: Gemini 2.0 Flash cho ảnh người thực (miễn phí), Stability AI SD3.5 cho art/illustration/editing.

## Sử dụng skill này khi

- Cần tạo ảnh bất kỳ loại nào (người thực, art, illustration)
- Cần chỉnh sửa ảnh (style transfer, inpaint, remove background)
- Cần upscale ảnh lên độ phân giải cao
- Tạo ảnh cho social media, thumbnail, profile

## KHÔNG sử dụng khi

- Cần tạo video → dùng `veo-video-gen`
- Cần PPT với styled images → dùng workflow khác
- Cần thiết kế node-based phức tạp → dùng `freepik-spaces`

## Ma Trận Quyết Định

```
YÊU CẦU CỦA USER
      ↓
Là ẢNH THỰC của người/influencer?
  ↓ CÓ → Gemini 2.0 Flash (ai-studio-image)
  ↓ KHÔNG → Là ILLUSTRATION, ART hoặc THIẾT KẾ?
               ↓ CÓ → Stability AI (generate/ultra/core)
               ↓ KHÔNG → Là CHỈNH SỬA ảnh có sẵn?
                          ↓ CÓ → Stability AI (img2img/inpaint/search-replace)
                          ↓ KHÔNG → Là UPSCALE hoặc XÓA BACKGROUND?
                                    ↓ CÓ → Stability AI (upscale/remove-bg)
                                    ↓ KHÔNG → Hỏi thêm chi tiết
```

## 2 Engine

### Gemini 2.0 Flash — Ảnh Người Thực (Miễn phí)

| Loại | Ví dụ |
|------|-------|
| Ảnh influencer | "ảnh style Instagram cô gái trong quán café" |
| Ảnh profile | "headshot chuyên nghiệp, áo vest, phông nền trung tính" |
| Ảnh lifestyle | "người trên bãi biển với điện thoại, ánh sáng vàng" |
| Ảnh giáo dục | "giáo viên đang giảng bài trước bảng" |

**Ưu điểm:** Miễn phí (50 ảnh/ngày), 5 lớp humanization, 20 templates sẵn
**Hạn chế:** 1 ảnh/lần (~9s), ~1K resolution

### Stability AI SD3.5 — Art & Editing

| Loại | Mode | Ví dụ |
|------|------|-------|
| Art/illustration | `generate` | "rồng bay trên núi, phong cách fantasy" |
| Chất lượng cao | `ultra` | "chân dung studio, ánh sáng chuyên nghiệp" |
| Nhanh/lặp | `core` | "mèo anime kawaii" |
| Chuyển đổi ảnh | `img2img` | "chuyển ảnh thành tranh sơn dầu" |
| Upscale | `upscale` | "tăng độ phân giải lên 4K" |
| Xóa nền | `remove-bg` | "tạo nền trong suốt (PNG)" |
| Chỉnh sửa vùng | `inpaint` | "thay đổi quần áo thành vest" |
| Thay đổi object | `search-replace` | "đổi xe đỏ thành xe xanh" |
| Xóa object | `erase` | "xóa người ở phía sau" |

**15 Styles:** photorealistic, anime, digital-art, oil-painting, watercolor, pixel-art, 3d-render, concept-art, comic, minimalist, fantasy, sci-fi, sketch, pop-art, noir

## Output

Trả về ảnh + metadata:
- File path ảnh đã tạo
- Model đã sử dụng (Gemini/Stability)
- Prompt đã optimize
- Gợi ý variations hoặc chỉnh sửa thêm

## Nguồn gốc
- Nguồn: [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) — `image-studio` (community)
- Adapter: ABM Workforce v2.1 — Jarvis Orchestrator
