---
name: Skywork Design
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: Generate or edit images via backend Skywork Image API. Use for any image creation, poster design, logo design, visual asset generation, or image modification request. Supports text-to-image and image-to-image editing with aspect ratio and resolution control.
metadata:
  openclaw:
    requires:
      bins:
        - python3
      env:
        - SKYWORK_API_KEY
    primaryEnv: SKYWORK_API_KEY
---

# Goal
Tạo hoặc chỉnh sửa hình ảnh (Poster, Graphic Design, Infographic, Logo) chất lượng cao thông qua Skywork Image API, ứng dụng chuẩn viết Prompt đặc biệt của model Nano Banana 2.

# Instructions

## Bước 1: Thu thập Yêu cầu & Xác định Thông số
Hỏi người dùng để chốt các thông số thiết kế (nếu họ chưa nói rõ):
1. **Chế độ**: Tạo mới (Generate) hay Chỉnh sửa ảnh có sẵn (Edit)?
2. **Kích thước (Aspect Ratio)**:
   - `1:1` (Avatar, Social)
   - `3:4` / `4:3` (Poster nhỏ, Slide)
   - `9:16` / `16:9` (Story, Hình nền Desktop, Video Cover)
   - `21:9` (Banner rộng)
3. **Độ phân giải (Resolution)**: Default là `2K`. Dùng `1K` cho nháp, `4K` cho in ấn/chất lượng cao.
4. **Nội dung Văn Bản**: **TUYỆT ĐỐI 100% TIẾNG VIỆT** đối với dòng chữ muốn hiển thị trên ảnh. Model render Tiếng Việt cực kỳ xuất sắc.

## Bước 2: Thiết kế Prompt theo chuẩn Nano Banana
Nano Banana 2 cực mạnh ở khả năng hiểu cấu trúc (Parametric Design) thay vì miêu tả mơ hồ. Không cần viết mây gió, hãy chia prompt thành các cấu trúc rõ ràng:
- **Style/Material**: Dùng "Liquid Glass", "3D Glossy", "Apple liquid glass" giúp ảnh cực kì Premium.
- **Data-Injected**: Nếu làm Infographic, ép thông số có thật (VD: 85 độ C, 99 kcal) vào để tăng độ chân thực.
- **Text Injection**: Ghi rõ text nào hiển thị ở đâu (VD: Tiêu đề lớn: "GIẢM GIÁ 50%", Tiêu đề phụ: "Chỉ hôm nay").

## Bước 3: Chạy Lệnh Thực Thi (Command)
Sử dụng python script được lưu ở `_abm/bmm/agents/skills/skywork-design/scripts/generate_image.py`.
*Lưu ý: Luôn chạy ở thư mục hiện tại của workspace.*

**Tạo Ảnh (Generate):**
```bash
python3 _abm/bmm/agents/skills/skywork-design/scripts/generate_image.py --prompt "<NỘI_DUNG_PROMPT>" --filename "<TÊN_FILE.png>" --aspect-ratio 16:9 --resolution 2K
```

**Sửa Ảnh (Edit):**
```bash
python3 _abm/bmm/agents/skills/skywork-design/scripts/generate_image.py --prompt "<NỘI_DUNG_CẦN_SỬA>" --filename "<TÊN_FILE_MỚI.png>" --input-image "<FILE_GỐC.png>"
```

# Examples

## Ví dụ 1: Tạo Infographic Dạng Bento Grid (Xịn nhất hiện nay)
**Input User:** "Làm cho tôi 1 ảnh infographic giới thiệu Trà Sen Tây Hồ."
**Prompt Agent dùng chạy lệnh (Nên giữ System Prompt là tiếng Anh, nhưng text truyền vào bắt buộc Tiếng Việt):**
```text
System Instruction:
Create an image of premium liquid glass Bento grid product infographic with 8 modules (card 2 to 8 show text titles only).
1) Product Analysis: dominant natural color -> delicate lotus pink and fresh green.
2) Color Palette: full saturation lotus pink and green. Icons, borders: muted.
3) Visual Style: Hero product: real photography of porcelain tea cup filled with golden tea and fresh lotus flowers on a wooden table. Cards: Apple liquid glass (90% transparent) with whisper-thin borders and subtle drop shadow. Asymmetric Bento grid layout.
4) Module Content (Text must be exactly rendered in Vietnamese):
M1 - Hero Box: "Trà Sen Tây Hồ" label.
M2 - Core Benefits: 4 unique benefits ("An Thần", "Thải Độc", "Chống Lão Hóa", "Ngủ Ngon") + icons.
M3 - How to Brew: 4 steps to brew ("Đun Sôi", "Tráng Trà", "Hãm 3 Phút", "Thưởng Thức") + icons.
M4 - Key Metrics: "Xuất Xứ: Hồ Tây", "Nhiệt Độ: 85°C", "Nhịp Độ: 3-5 Phút", "Mùa Vụ: Mùa Hè".
M5 - Who It's For: 4 recommended groups ("Dân Văn Phòng", "Người Mất Ngủ", "Đam Mê Trà Đạo").
M6 - Important Notes: 4 precautions ("Bảo quản kín", "Tránh ánh nắng", "Không dùng ruột rỗng", "Không để qua đêm").
M7 - Quick Reference: Taste profile ("Hương Hoa Sen", "Vị Ngọt Hậu").
M8 - Artisan Process: "Nghệ Thuật Ướp Trà Truyền Thống".

Make ALL text clearly visible natively inside the generated image IN VIETNAMESE completely. Do not use random placeholder characters.
```

## Ví dụ 2: Tạo Poster Cinematic / Tạp Chí
**Input User:** "Làm 1 cái poster ra mắt phim ngắn về Sài Gòn Mưa"
**Prompt Agent dùng chạy lệnh:**
```text
A glossy magazine cover / Cinematic Event Poster. Aspect Ratio 3:4.
Visual scene: A dynamic photograph of a raining scene in Saigon at night, neon lights reflecting on wet asphalt.
Lighting: Chiaroscuro lighting, moody.
Typography overlay: Bold Title "SÀI GÒN MƯA RƠI" in elegant serif font at the top. Smaller sub-text "Ngày 15 Tháng 8" floating at the bottom right.
Details: Issue number and date in the corner with a minimalist barcode. The image must feel like a premium printed asset. All texts are exclusively in Vietnamese.
```

# Constraints
- 🚫 **Bảo Mật Keys:** Tuyệt đối không thay đổi `SKYWORK_API_KEY`.
- 🚫 **Tuân thủ Ngôn Ngữ:** Nội dung văn bản xuất hiện in lên ảnh BẮT BUỘC 100% TIẾNG VIỆT, vì model render Tiếng Việt rất tốt.
- ✅ **Chờ Đợi & Cập Nhật:** Lệnh tạo ảnh chạy 30s-120s. Trong quá trình đó script sẽ in phần trăm [0%] -> [100%]. Hãy dùng tool status để canh và báo người dùng không cần sốt ruột.
- ✅ **Lỗi Benefit:** Nếu API in ra `Insufficient benefit`, báo user "Gói cước Skywork hết hạn hoặc không đủ quyền, yêu cầu nâng cấp" cùng với link nâng cấp có trong log. Không tự bịa ra lý do khác.

<!-- Generated by ABM Skill Generator v1.0 | ABM Workforce -->
