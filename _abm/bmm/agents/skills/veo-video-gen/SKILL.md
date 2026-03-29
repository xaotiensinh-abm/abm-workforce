---
name: "veo-video-gen"
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-28
description: "Kỹ thuật viết prompt đỉnh cao cho Google VEO 3.1 — text-to-video, image-to-video, extend video, thêm/xóa thành phần, camera language, audio sync."
---

# VEO Video Gen — Viết Prompt Đỉnh Cao Cho VEO 3.1

Skill chuyên sâu về kỹ thuật viết prompt cho **Google VEO 3.1**. Tập trung vào ngôn ngữ đạo diễn, camera, ánh sáng, audio, cho mọi ứng dụng: text-to-video, image-to-video, extend, và chỉnh sửa thành phần.

## Sử dụng skill này khi

- Cần viết prompt tạo video (quảng cáo, social, demo sản phẩm)
- Cần viết prompt extend video (kéo dài cảnh)
- Cần viết prompt image-to-video (biến ảnh thành video)
- Cần viết prompt thêm/xóa thành phần trong video
- Cần hướng dẫn prompt engineering cho video AI

## KHÔNG sử dụng khi

- Chỉ cần tạo ảnh → dùng `imagen`
- Cần storyboard workflow tự động → dùng `freepik-spaces`

---

## PHẦN 1: CÔNG THỨC PROMPT VIDEO — 7 LỚP

### Sơ đồ cấu trúc

```
[CHỦ THỂ + HÀNH ĐỘNG]
  + [MÔI TRƯỜNG + THỜI GIAN]
    + [CAMERA MOVEMENT + COMPOSITION]
      + [ÁNH SÁNG + MÀU SẮC]
        + [ÂM THANH + ĐỐI THOẠI]
          + [PHONG CÁCH ĐIỆN ẢNH]
            + [KỸ THUẬT (resolution, aspect ratio, duration)]
```

### Ví dụ phân tích đầy đủ

```
❌ Prompt yếu: "Video quán café"

✅ Prompt đỉnh cao:
"Slow dolly-in vào quán café Việt Nam giữa phố cổ Hà Nội. 
Camera bắt đầu ở wide shot phía ngoài cửa kính, 
di chuyển chậm qua cánh cửa gỗ mở nửa.
Bên trong, cô gái trẻ ngồi cạnh cửa sổ đang nhấp cà phê sữa đá,
nhìn ra phố. Ánh sáng golden hour chiếu xéo qua cửa sổ, 
tạo bóng dài trên bàn gỗ. Hạt bụi lấp lánh trong tia nắng.
Âm thanh: tiếng xe máy xa xa, tiếng cốc chạm đĩa nhẹ, 
nhạc acoustic guitar nhẹ từ loa quán.
Phong cách: cinematic, film grain nhẹ, color grading warm tones.
Aspect ratio 16:9, 8 giây."
```

---

## PHẦN 2: TỪ VỰNG CAMERA — NGÔN NGỮ ĐẠO DIỄN

### Camera Movements

| Từ khóa | Mô tả | Khi dùng |
|---------|-------|---------|
| `slow dolly in` | Camera tiến lại gần, chậm | Tạo kịch tính, gần gũi |
| `dolly out / pull back` | Camera lùi xa | Reveal cảnh rộng |
| `tracking shot` | Camera đi theo chủ thể | Hành động, di chuyển |
| `pan left / pan right` | Quay ngang trái/phải | Quét cảnh rộng |
| `tilt up / tilt down` | Ngẩng lên / cúi xuống | Reveal tòa nhà, nhân vật |
| `crane shot` | Camera nâng cao dần | Cinematic reveal |
| `handheld` | Rung tay nhẹ | Tự nhiên, documentary |
| `steadicam following` | Theo sát, mượt | Walk-and-talk |
| `orbit / 360° rotation` | Xoay quanh chủ thể | Product showcase |
| `zoom in / zoom out` | Phóng to / thu nhỏ | Nhấn mạnh, reveal |

### Shot Types

| Từ khóa | Mô tả |
|---------|-------|
| `extreme wide shot (EWS)` | Cảnh toàn, thiên nhiên, thành phố |
| `wide shot (WS)` | Thấy toàn thân + bối cảnh |
| `medium shot (MS)` | Từ thắt lưng trở lên |
| `close-up (CU)` | Khuôn mặt, chi tiết |
| `extreme close-up (ECU)` | Mắt, tay, chi tiết nhỏ |
| `over-the-shoulder (OTS)` | Qua vai nhân vật |
| `bird's eye view` | Nhìn thẳng từ trên xuống |
| `worm's eye view` | Nhìn thẳng từ dưới lên |

---

## PHẦN 3: PROMPT CHO TỪNG ỨNG DỤNG

### 3.1 Text-to-Video

**Template:**
```
"[CAMERA MOVEMENT] [SHOT TYPE] — [CHỦ THỂ] [HÀNH ĐỘNG] 
trong [MÔI TRƯỜNG], [THỜI GIAN TRONG NGÀY].
Ánh sáng: [KIỂU ÁNH SÁNG].
Âm thanh: [DIALOGUE nếu có], [SFX], [NHẠC NỀN].
Phong cách: [CINEMATIC STYLE], [COLOR GRADING].
[DURATION] giây, [ASPECT RATIO]."
```

**Ví dụ Quảng cáo sản phẩm:**
```
"Slow orbit shot — chai nước hoa sang trọng xoay chậm trên bệ đá cẩm thạch,
camera quay 180°. Ánh sáng studio ba điểm, tia sáng prismatic 
tạo cầu vồng nhỏ trên thân chai. Giọt nước ngưng tụ chảy chậm 
trên bề mặt kính. Âm thanh: tiếng kính chạm đá nhẹ, nhạc ambient 
elegant. Phong cách luxury commercial, color grading tông lạnh bạc.
8 giây, 9:16."
```

### 3.2 Image-to-Video

**Template:**
```
"Ảnh tham khảo: [MÔ TẢ ẢNH INPUT].
Animation: [PHẦN NÀO DI CHUYỂN — tóc, mắt, nền, toàn cảnh].
Camera: [MOVEMENT từ ảnh gốc].
Thêm: [ÂM THANH, HIỆU ỨNG bổ sung].
Giữ nguyên: [CÁC YẾU TỐ KHÔNG ĐỔI].
[DURATION], [ASPECT RATIO]."
```

**Ví dụ:**
```
"Ảnh tham khảo: portrait cô gái nhìn thẳng camera, nền studio.
Animation: tóc bay nhẹ sang trái, mắt chớp tự nhiên 1 lần,
môi hơi mỉm cười dần. Camera dolly in rất chậm.
Thêm: ánh sáng lung linh nhẹ trên background.
Giữ nguyên: trang phục, trang điểm, pose cơ thể.
6 giây, 9:16."
```

### 3.3 Extend Video (Kéo dài video)

**Template cho segment tiếp theo:**
```
"Tiếp tục cảnh trước:
[MÔ TẢ CHÍNH XÁC khung hình cuối của video gốc].
Chuyển tiếp: [HÀNH ĐỘNG mới — mượt, logic].
Camera: [MOVEMENT tiếp tục hoặc chuyển mới].
Giữ nhất quán: ánh sáng [CÙNG KIỂU], color grading [CÙNG TÔNG],
trang phục [CÙNG], bối cảnh [CÙNG hoặc pan sang mới].
Âm thanh: [TIẾP TỤC hoặc transition].
7 giây."
```

**Ví dụ chuỗi extend (8s + 7s + 7s = 22s):**
```
Segment 1 (8s): "Wide shot cô gái bước vào căn hộ hiện đại,
đặt túi xuống sofa, nhìn ra cửa kính. Golden hour."

Segment 2 (7s): "Tiếp tục — medium shot cô ấy bước ra ban công,
tay vịn lan can, gió thổi nhẹ tóc. Camera dolly in chậm.
Ánh sáng golden hour nhất quán. Tiếng gió + thành phố xa xa."

Segment 3 (7s): "Tiếp tục — close-up khuôn mặt nhìn hoàng hôn,
mỉm cười nhẹ. Camera tilt up chậm thấy skyline thành phố.
Ánh sáng ấm nhất quán. Nhạc piano nhẹ fade in."
```

### 3.4 Thêm/Xóa Thành Phần

**Thêm thành phần:**
```
"Video gốc: [MÔ TẢ CẢNH GỐC].
THÊM vào cảnh: [THÀNH PHẦN MỚI] ở vị trí [VỊ TRÍ],
di chuyển [CÁCH DI CHUYỂN].
Giữ nguyên toàn bộ: nhân vật, camera movement, ánh sáng, âm thanh.
Thành phần mới phải match: ánh sáng [CÙNG HƯỚNG], shadow [ĐÚNG GÓC]."
```

**Xóa thành phần:**
```
"Video gốc: [MÔ TẢ CẢNH GỐC].
XÓA khỏi cảnh: [THÀNH PHẦN CẦN XÓA].
Thay thế bằng: [NỀN/BỐI CẢNH phù hợp — hòa trộn tự nhiên].
Giữ nguyên: tất cả thành phần khác, camera, timing, âm thanh."
```

---

## PHẦN 4: ÂM THANH TRONG PROMPT

VEO 3.1 tạo audio TỰ ĐỘNG — bạn điều khiển bằng prompt:

### Dialogue (đối thoại)
```
Nhân vật nói: "Xin chào, rất vui được gặp bạn" 
giọng nữ trẻ, ấm áp, tốc độ vừa phải.
```

### Sound Effects
```
Âm thanh: tiếng cốc café đặt xuống bàn gỗ (0:02),
tiếng mưa nhẹ ngoài cửa sổ (liên tục), 
tiếng bước chân trên sàn gỗ (0:05-0:07).
```

### Ambient + Music
```
Nhạc nền: acoustic guitar fingerstyle nhẹ nhàng.
Ambient: quán café đông vừa, tiếng nói chuyện xa xa.
```

---

## PHẦN 5: NEGATIVE PROMPTS CHO VIDEO

```
Negative: "jittery motion, morphing faces, extra limbs,
inconsistent lighting between frames, text overlays,
watermark, logo, unrealistic physics, floating objects,
sudden color shifts, audio glitches, robotic voice"
```

---

## PHẦN 6: THÔNG SỐ KỸ THUẬT

| Thông số | Giá trị | Ghi chú |
|---------|---------|---------|
| Models | `veo-3.1-generate-001`, `veo-3.1-fast-generate-001` | Fast = nhanh hơn, chất lượng hơi thấp |
| Duration | 4, 6, 8 giây / segment | Chain nhiều segment cho video dài |
| Max duration | **148 giây** (chain 7s segments) | Cần prompt nhất quán |
| Resolution | 720p, 1080p, **4K** | 4K cho production |
| Aspect ratio | 16:9 (landscape), 9:16 (portrait) | — |
| Reference images | Tối đa **3 ảnh** | Cho character/style consistency |
| Audio | Tự động tích hợp | Dialogue + SFX + ambient |

## Nguồn gốc
- Deep research: Google VEO 3.1 Prompt Engineering (2025-2026)
- Cập nhật: ABM Workforce v2.2 — Jarvis Orchestrator
