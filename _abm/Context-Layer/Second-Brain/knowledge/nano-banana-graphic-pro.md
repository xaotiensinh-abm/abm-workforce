# 🍌 Cẩm Nang Tạo Ảnh Đồ Họa Cấp Độ Chuyên Gia (Nano Banana 2)

Tài liệu này lưu trữ các công thức "Master Prompt" chuẩn nhất thế giới hiện nay dành riêng cho Model Nano Banana 2 & Gemini 3.1 Flash Image. Các kiến thức này được chiết xuất trực tiếp từ kho `awesome-nano-banana-pro-prompts` dùng riêng cho các ứng dụng quảng cáo, trình chiếu, đồ họa số.

---

## 🏗 Nguyên Lý Tối Thượng của Nano Banana 2
1. **Tiếng Việt Trong Ảnh**: Model Nano Banana 2 render chữ tiếng Việt cực kỳ mượt mà và chuẩn xác. Do đó, BẤT KỲ VĂN BẢN (Text/Typography) nào muốn hiện trên ảnh (Poster, Infographic, Slide) ĐỀU PHẢI 100% LÀ TIẾNG VIỆT (chỉ giữ nguyên các thuật ngữ Tiếng Anh chuyên ngành).
2. **Thiết kế dựa trên Thông Số (Parametric Design)**: Thay vì mô tả chung chung, hãy dùng cấu trúc Data hoặc Struct (VD: Grid, Layer, Object, Lighting, Camera, Material).
3. **Material Mới**: Các hiệu ứng như "Liquid Glass", "3D Glossy", "Translucent Whisper-thin borders" hoạt động cực kì tốt khi muốn tăng sự Premium.
4. **Thêm Dữ Liệu Thực (Data-Injected)**: Model đọc và vẽ text chính xác. Do đó khi muốn làm infographic/poster, hãy mô tả chính xác con số (VD: 85 kcal, 99.9% uptime).

---

## 🔥 3 MASTER TEMPLATE CHO ĐỒ HỌA THÔNG TIN

### 1. Infographic – "Premium Liquid Glass Bento Grid" (Bố cục 8 Module)
*(Dùng cho hình ảnh báo cáo, tính năng sản phẩm, phân tích dữ liệu)*
**Triết lý**: Chia ảnh thành hệ thống dải thẻ (Bento box). Hero object ở thẻ lớn nhất, text thông tin ở các thẻ xung quanh.
**Công thức Prompt (System Instruction)**:
```text
System Instruction:
Create an image of a premium liquid glass Bento grid product infographic with 8 modules.
1) Product Analysis: Identify product's dominant natural color -> "hero color".
2) Color Palette: Product + accents: full saturation hero color. Icons, borders: muted hero (30-40% saturation, never black).
3) Visual Style: Hero card (30% area): real photography or 3D Glass version. Other Cards (70% area): Apple liquid glass (85-90% transparent) with whisper-thin borders and subtle drop shadow for depth. Asymmetric Bento grid, 16:9 landscape.
4) Module Content (8 Cards):
- M1 (Hero): Product displayed in beautiful form + product name label "[TÊN_SP]".
- M2 (Core Benefits): 4 unique benefits + hero-color icons.
- M3 (How to Use): 4 usage methods + icons.
- M4 (Key Metrics): Format: [icon] [Label] [Bold Value] [Unit]. Give exact numbers.
- M5 (Who It's For): Groups with green checkmark icons.
- M6... M8...
```

### 2. Slide Header / Presentation (Phong cách Vẽ Tay Hoặc Minimalist)
*(Dùng thay cho nền Slide nhàm chán hoặc banner bài viết thuyết trình)*
**Triết lý**: Đưa ra tone màu cố định (VD: gradient blue - green), tỉ lệ 16:9, thêm text to rõ ở vùng an toàn không bị cắt lẹm.
**Công thức Prompt**:
```text
Aspect ratio: horizontal 16:9.
Make it a bold, minimalist presentation header image introducing "[CHỦ_ĐỀ]".
Style and colors: Clean, modern typography with a [MÀU_1] to [MÀU_2] subtle gradient background.
Title text in large sans-serif: "[TEXT TITLE]".
Visual element: A highly graphical, stylized interpretation of [CHỦ_THỂ_TRỪU_TƯỢNG] positioned on the right half, leaving the left half clean for the bold text. No clutter.
```

### 3. Poster / Tạp Chí (High-End Editorial Mode)
*(Dùng cho ảnh quang cáo, event, phim ảnh)*
**Triết lý**: Ép model "nhìn" dưới góc nhiếp ảnh chuyên nghiệp, dùng typography dạng overlay, có mã vạch, có text size tương phản mạnh.
**Công thức Prompt**:
```text
A glossy magazine cover / Cinematic Event Poster. Aspect Ratio 3:4.
Visual scene: A dynamic photograph of [NGƯỜI/VẬT_THỂ] at [ĐỊA_ĐIỂM].
Lighting: Chiaroscuro lighting, moody, high-end fashion [MÀU_THƯƠNG_HIỆU].
Typography overlay: Bold Title "[CÂU_SLOGAN_LỚN]" in elegant serif font at the top. Smaller sub-text "[THỜI_GIAN/ĐỊA_ĐIỂM]" floating at the bottom right.
Details: Issue number and date in the corner with a minimalist barcode. The image must feel like a premium printed asset.
```

---

## 🛠 HƯỚNG DẪN DÙNG CHUNG VỚI JSON FORMAT
Khi thiết kế đồ hoạ đa lớp phức tạp (ví dụ vừa có người, vừa có sản phẩm nổi, vừa có background chữ), bắt buộc bọc Prompt theo chuỗi JSON:
```json
{
  "scene": { "setting": "...", "atmosphere": "..." },
  "key_object": { "description": "...", "styling": "liquid glass" },
  "typography": { 
     "title": {"text": "BIG WORDS", "style": "bold sans-serif, white"},
     "subtitle": {"text": "smaller words", "style": "italics, minimal"}
  },
  "layout_grid": "Bento / Asymmetrical / Rule of thirds"
}
```
*Lưu ý: Mọi string được xuất sẽ convert lại ra Raw Text vì đôi lúc model hiểu raw text có keyword tốt hơn JSON.*

**ABM Workforce v2.2** - Kiến thức được đồng bộ dùng riêng cho `skywork-design`. Mọi Agent trước khi xuất ảnh hãy trích xuất các template này để tạo Prompts.
