---
name: "grok-imagen"
description: "Kỹ thuật viết prompt tạo ảnh và video trên Grok (xAI Aurora) — prompt ảnh photorealistic, prompt video, extend video, workflow chuyên sâu."
---

# Grok Imagen — Viết Prompt Ảnh & Video Trên Grok

Skill hướng dẫn viết prompt chuyên sâu cho **xAI Aurora** (Grok Imagine). Bao gồm: tạo ảnh photorealistic, tạo video ngắn, extend video, và workflow kết hợp.

## Sử dụng skill này khi

- Cần viết prompt tạo ảnh trên Grok/X
- Cần viết prompt tạo video trên Grok Imagine
- Cần extend video (kéo dài video) trên Grok
- Cần workflow: ý tưởng → ảnh → video trên hệ sinh thái xAI

## KHÔNG sử dụng khi

- Cần ảnh Nano Banana 2 / Gemini → dùng `imagen`
- Cần video 4K / VEO → dùng `veo-video-gen`
- Cần storyboard workflow → dùng `freepik-spaces`

---

## PHẦN 1: CẤU TRÚC PROMPT ẢNH AURORA

### Công thức 5 thành phần

```
[CHỦ THỂ] + [STYLE/MEDIUM] + [COMPOSITION/SETTING] + [LIGHTING/MOOD] + [KỸ THUẬT]
```

### Bảng từ vựng chuyên biệt Aurora

**Aurora đặc biệt mạnh về:**

| Điểm mạnh | Mô tả | Ví dụ prompt |
|-----------|-------|-------------|
| Photorealistic faces | Khuôn mặt siêu thực | "ultra-realistic portrait, skin pores visible, subtle asymmetry" |
| Text adherence | Theo sát text prompt | Mô tả chi tiết = kết quả chính xác |
| Multimodal edit | Chỉnh sửa từ ảnh input | Upload ảnh + "change background to..." |

### Ví dụ prompt theo level

**Level 1 — Cơ bản:**
```
"Chân dung doanh nhân Việt Nam, vest xanh navy, 
nền studio trắng, ánh sáng studio chuyên nghiệp"
```

**Level 2 — Nâng cao:**
```
"Chân dung doanh nhân Việt Nam 35 tuổi, vest xanh navy slim-fit,
cà vạt xám bạc, mắt nhìn thẳng camera với ánh mắt tự tin.
Nền studio gradient xám nhạt → trắng.
Three-point lighting: key light 45° bên trái, fill light mềm bên phải,
rim light tạo viền sáng trên vai. 
Phong cách corporate headshot, lens 85mm, sharp focus,
shallow depth of field."
```

**Level 3 — Chuyên gia:**
```
"Ultra-realistic corporate portrait — Vietnamese CEO, male, 35-40,
sharp jawline, subtle confident smile, wearing navy Armani suit
with silver-grey silk tie, french cuff with minimalist cufflinks.
Studio setting: seamless grey-to-white gradient backdrop.
Rembrandt lighting pattern — key light 45° camera-left creating
signature triangle on shadow-side cheek, soft fill at 2:1 ratio,
hair light from behind-right separating from background.
Skin detail: visible pores, natural slight skin texture,
no airbrushing, subtle under-eye shadow for authenticity.
Shot on Phase One IQ4 150MP, Schneider Kreuznach 80mm f/2.8,
1/200 at f/8, ISO 100. Color: calibrated neutral with slight warm shift."
```

---

## PHẦN 2: PROMPT TẠO VIDEO GROK IMAGINE

### Thông số Grok Imagine Video

| Thông số | Giá trị |
|---------|---------|
| Resolution | 720p (hiện tại) |
| Duration | 6-10 giây / clip |
| Audio | ✅ Tự động — nhạc, SFX, dialogue |
| Pricing | $0.05/giây |

### Template prompt video

```
"[LOẠI SHOT] — [CHỦ THỂ] [HÀNH ĐỘNG cụ thể]
trong [BỐI CẢNH chi tiết], [THỜI GIAN].
Camera: [MOVEMENT — dolly/pan/track/static].
Ánh sáng: [KIỂU — tự nhiên / studio / dramatic].
Âm thanh: [NHẠC NỀN] + [SFX cụ thể] + [DIALOGUE nếu có].
Phong cách: [CINEMATIC / COMMERCIAL / DOCUMENTARY].
Mood: [CẢM XÚC — energetic / calm / mysterious]."
```

### Ví dụ prompt video

**Quảng cáo F&B:**
```
"Medium shot — bartender Việt Nam thành thạo pha cocktail, 
shaker lắc nhịp nhàng, rót ra ly highball với ice sphere.  
Quầy bar gỗ tối, đèn pendant ấm áp phía trên.
Camera: slow tracking left-to-right, shallow DOF.
Ánh sáng: warm key light từ pendant, LED strip dưới quầy.
Âm thanh: tiếng đá va ly, tiếng rót nước, jazz nhẹ.
Phong cách: luxury commercial. Mood: sophisticated.
10 giây."
```

---

## PHẦN 3: EXTEND VIDEO — KỸ THUẬT CHUYÊN SÂU

### Cơ chế "Extend from Frame"

```
Video gốc (6-10s) → Lấy khung hình cuối → Dùng làm "first frame" 
cho segment tiếp → Chain nhiều segments → Video dài 30-50+ giây
```

### Quy tắc vàng khi extend

1. **MÔ TẢ CHÍNH XÁC khung hình cuối** — AI cần biết nó đang continue từ đâu
2. **GIỮ NHẤT QUÁN**: ánh sáng, trang phục, màu sắc, bối cảnh
3. **CHUYỂN TIẾP MỘT**: hành động tiếp nối logic, không nhảy đột ngột
4. **CAMERA FLOW**: camera movement nên tiếp tục hoặc chuyển mượt
5. **TRÁNH**: thay đổi thời gian ngày đêm đột ngột, thay đổi trang phục

### Template extend

```
"EXTEND — Tiếp từ frame cuối:
[MÔ TẢ CHÍNH XÁC frame cuối: nhân vật đang làm gì, ở đâu, pose nào].
Tiếp theo: [HÀNH ĐỘNG MỚI — tự nhiên, logic].
Camera: [TIẾP TỤC movement hoặc CẮT sang shot mới].
Giữ: ánh sáng [CÙNG KIỂU], trang phục [CÙNG], nền [CÙNG].
Âm thanh: [TIẾP TỤC nhạc/SFX hoặc transition].
6-10 giây."
```

### Ví dụ chuỗi 4 segments (≈32s)

```
Seg 1 (8s): "Wide shot — cô gái bước vào showroom xe hơi,
nhìn quanh, mắt sáng ngạc nhiên. Camera tracking follow.
Ánh sáng showroom trắng sáng + spotlights trên xe."

Seg 2 (8s): "EXTEND — Cô ấy đã dừng trước chiếc sedan đen bóng.
Tiếp: tay trượt nhẹ trên thân xe, camera orbit chậm quanh xe,
thấy phản chiếu cô ấy trên surface xe. Ánh sáng spotlight."

Seg 3 (8s): "EXTEND — Cô ấy đang đứng cạnh cửa xe.
Tiếp: mở cửa xe, ngồi vào ghế lái, tay chạm vô-lăng.
Camera: từ exterior dolly in qua cửa xe đang mở.
SFX: tiếng cửa xe đóng nhẹ, tiếng da ghế."

Seg 4 (8s): "EXTEND — Cô ấy ngồi trong xe, tay trên vô-lăng.
Tiếp: bấm nút start, dashboard sáng lên, mỉm cười tự tin.
Camera: close-up khuôn mặt qua gương chiếu hậu. 
SFX: engine start mượt, nhạc trong xe fade in."
```

### ⚠️ Cảnh báo khi extend

| Vấn đề | Giải pháp |
|--------|----------|
| Khuôn mặt biến đổi | Mô tả lại đặc điểm khuôn mặt ở mỗi segment |
| Ánh sáng nhảy | Ghi rõ "ánh sáng NHẤT QUÁN với segment trước" |
| Chất lượng giảm | Không extend quá 5-6 segments liên tiếp |
| Hành động đứt | Mô tả hành động chuyển tiếp rất cụ thể |

---

## PHẦN 4: WORKFLOW PROMPT NÂNG CAO

### Workflow: X Trend → Ảnh → Video

```
Bước 1: Ask Grok "Xu hướng visual content trên X tuần này?"
Bước 2: Chọn trend phù hợp brand
Bước 3: Viết prompt ảnh Aurora theo trend
Bước 4: Dùng ảnh đẹp nhất → prompt video Grok Imagine
Bước 5: Extend video nếu cần dài hơn
Bước 6: Đăng trên X kèm hashtag trending
```

## Nguồn gốc
- Deep research: xAI Aurora + Grok Imagine API (01-03/2026)
- Cập nhật: ABM Workforce v2.2 — Jarvis Orchestrator
