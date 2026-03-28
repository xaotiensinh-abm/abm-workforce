---
description: Tạo video giáo dục thú cưng 2D (40s = 5 cảnh × 8s) cho TikTok/YouTube Shorts
---

Workflow tạo video edutainment với **nhân vật động vật 2D hoạt hình** cho trẻ em (40 giây = 5 cảnh × 8 giây).

---

## Giai đoạn 1: Thu thập Thông tin

| Thông tin | Giá trị mặc định |
|-----------|------------------|
| **Độ tuổi** | 6-8 tuổi |
| **Chủ đề bài học** | Bắt buộc nhập |
| **Giọng điệu** | Vui nhộn |
| **Thời lượng** | 40s = 5×8s |
| **Ngôn ngữ** | Tiếng Việt |
| **Nền tảng** | TikTok |

Nếu thiếu thông tin, hỏi người dùng:
```
📋 Để tạo video hoàn chỉnh, vui lòng cung cấp:
- Độ tuổi mục tiêu của khán giả?
- Chủ đề/bài học muốn truyền tải?
- Bạn có ý tưởng về 2 nhân vật thú cưng chính không?
- Bối cảnh series (rừng xanh, thành phố, trang trại...)?
```

---

## Giai đoạn 2: Series Bible Mini

### 2.1 Hai Nhân Vật Chính
- **Tên**: Tên thân thiện, dễ nhớ (VD: Mèo Miu, Cún Bông)
- **Tính cách**: 2-3 đặc điểm chính
- **Đặc điểm ngoại hình**: Màu sắc, phụ kiện đặc trưng
- **Câu nói đặc trưng**: Catchphrase

### 2.2 Thông Điệp Bài Học
- Câu tóm tắt bài học 1 dòng
- Cách truyền tải phù hợp độ tuổi

---

## Giai đoạn 3: Episode Beat Map

| Cảnh | Thời lượng | Mục đích | Nội dung |
|------|------------|----------|----------|
| **Scene 1: HOOK** | 0-8s | Thu hút ngay | Câu hỏi/Tình huống bất ngờ |
| **Scene 2: PROBLEM** | 8-16s | Giới thiệu vấn đề | Nhân vật gặp khó khăn |
| **Scene 3: TRY & FAIL** | 16-24s | Thử và thất bại | Nỗ lực chưa thành công |
| **Scene 4: SOLUTION** | 24-32s | Tìm ra giải pháp | Áp dụng kiến thức/bài học |
| **Scene 5: MORAL** | 32-40s | Kết luận bài học | Tóm tắt + Catchphrase |

---

## Giai đoạn 4: Viết Kịch bản

Format:
```
SCENE 1: HOOK (0-8s)
[Mô tả hình ảnh]
NHÂN VẬT: "Lời thoại"
[Hành động]

SCENE 2: PROBLEM (8-16s)
...
```

---

## Giai đoạn 5: VEO 3.1 Storyboard

```
┌────────────────────────────────────────┐
│ SCENE 1: HOOK                          │
│ Timecode: 0:00 - 0:08                  │
├────────────────────────────────────────┤
│ VISUAL: [Mô tả hình ảnh chi tiết]     │
│ ACTION: [Hành động nhân vật]          │
│ CAMERA: [Góc quay, chuyển động]       │
│ VO: [Lời thoại/thuyết minh]           │
│ SFX: [Hiệu ứng âm thanh]              │
└────────────────────────────────────────┘
```

---

## Giai đoạn 6: Character Spec Sheet

```
╔═══════════════════════════════════════════╗
║        CHARACTER SPEC SHEET               ║
║        [TÊN NHÂN VẬT]                     ║
╠═══════════════════════════════════════════╣
║ 🎨 LOOK & COLORS                          ║
║ - Màu chính / Màu phụ / Màu mắt          ║
║ - Phong cách: 2D cartoon/chibi/cute       ║
╠═══════════════════════════════════════════╣
║ 😊 EXPRESSIONS (6 cơ bản)                 ║
║ Vui vẻ, Buồn, Tức giận, Ngạc nhiên,      ║
║ Sợ hãi, Tò mò                             ║
╠═══════════════════════════════════════════╣
║ ✅ DO / ❌ DON'T                          ║
╚═══════════════════════════════════════════╝
```

---

## Giai đoạn 7: Image Prompts

### Turnaround Sheet
```
2D cartoon [animal type] character, [name], [color description], 
[accessories], character turnaround sheet showing front view, 
3/4 view, side view, white background, children's animation style
```

### Expression Sheet
```
2D cartoon [animal type] character [name], expression sheet 
showing 6 emotions: happy, sad, angry, surprised, scared, curious,
white background, children's book illustration style
```

---

## Giai đoạn 8: VEO 3.1 Video Prompts

```
╔═══════════════════════════════════════════╗
║ VEO 3.1 VIDEO PROMPT - SCENE [N]          ║
║ Duration: 8 seconds                       ║
╠═══════════════════════════════════════════╣
║ MOTION: [Chuyển động nhân vật]           ║
║ CAMERA: [Static/Pan/Zoom/Track]          ║
║ ACTING BEATS:                             ║
║ - Beat 1 (0-2s): [action]                ║
║ - Beat 2 (2-5s): [action]                ║
║ - Beat 3 (5-8s): [action]                ║
║ SAFETY LOCKS:                             ║
║ - Maintain character identity             ║
║ - Keep 2D animation style                 ║
╚═══════════════════════════════════════════╝
```

---

## Delivery Package

```
📦 DELIVERY PACKAGE
├── 1. script.md           # Kịch bản đầy đủ
├── 2. storyboard.md       # Storyboard 5 cảnh × 8s
├── 3. character_specs/    # Character Spec Sheets
├── 4. image_prompts/      # Prompts tạo hình ảnh
├── 5. frame_prompts/      # Start/End frame prompts
├── 6. video_prompts/      # VEO 3.1 I2V prompts
└── 7. qa_checklist.md     # QA checklist
```

---

## Nguyên tắc

- **Giao tiếp**: 100% Tiếng Việt
- **Prompts**: Tiếng Anh (để AI tools hiểu tốt nhất)
- **Thời lượng chuẩn**: 5 cảnh × 8 giây = 40 giây
- **Consistency**: Ưu tiên tính nhất quán của nhân vật
