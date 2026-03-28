---
description: Tạo TVC 10-15s bằng Sora 2 cho thị trường Việt Nam
---

Workflow đạo diễn video quảng cáo Sora 2, tối ưu cho **thị trường Việt Nam** (10-15s). Output song ngữ với Voiceover.

---

## Quy tắc Cốt lõi

1. **Người Việt xem**: Mặc định sử dụng Người mẫu Việt Nam (Asian features) và bối cảnh phù hợp thị hiếu Việt.
2. **Hiểu khách hàng**: BẮT BUỘC phải biết "Khách hàng mục tiêu" trước khi viết prompt.
3. **I2V Continuity - KHÔNG XOAY NGƯỜI**: Khi ảnh input chỉ có MẶT TRƯỚC sản phẩm, tuyệt đối KHÔNG cho người mẫu xoay người/quay lưng.
4. **Tập trung Chi tiết Sản phẩm**: Thay vì xoay người, sử dụng: chạm vải, vuốt họa tiết, nâng tay áo, cử động nhẹ để vải "sống".

---

## Bước 1: Kiểm tra Input

Khi nhận yêu cầu, kiểm tra xem người dùng đã cung cấp **Khách hàng mục tiêu** chưa?

- **Nếu CHƯA**: Dừng lại và hỏi ngay:
  > "Để video hiệu quả nhất, anh/chị muốn hướng tới đối tượng khách hàng nào? (VD: Gen Z năng động, Nữ công sở sang trọng, hay Bà nội trợ hiện đại?)"
- **Nếu CÓ**: Tiến hành Bước 2.

---

## Bước 2: Tạo Output 3 Phần

1. **Sora 2 Prompt (English)**: Cinematic Stack với default là `Vietnamese model`.
2. **Phân tích (Vietnamese)**: Giải thích visual phù hợp với khách hàng mục tiêu.
3. **Kịch bản Voiceover (Vietnamese)**: Lời bình thu hút đúng insight khách hàng.

---

## Cấu trúc Cinematic Stack

```text
[CAMERA]: (Góc quay, lens, chuyển động camera, framing. ALWAYS FRONTAL - no rotation)
[SUBJECT]: (Vietnamese model, tuổi, trang phục từ input image, đặc điểm)
[ACTION]: (Hành động tập trung vào sản phẩm: chạm, vuốt, cử động nhẹ. NO TURNING OR BACK VIEW)
[ENVIRONMENT]: (Bối cảnh Việt: Modern Indochine, Luxury Hanoi/Saigon, Tropical resort)
[AUDIO]: (Voiceover tiếng Việt + Background ambient)
[TECHNICAL]: (8K, cinematic lighting, thời lượng, aspect ratio 9:16)
```

---

## Quy tắc Vietnamese Voice

Khi yêu cầu người mẫu nói tiếng Việt:

```text
[AUDIO]: The woman/man speaks in Vietnamese with a [soft/confident/warm] voice:
"[Câu thoại tiếng Việt đầy đủ ở đây...]"
Background: [mô tả âm thanh nền].
```

**Ví dụ:**
```text
[AUDIO]: The woman speaks in Vietnamese with a soft, elegant voice:
"Xuân về, em muốn mình thật đặc biệt... Lụa mềm mại, từng chi tiết đều là đẳng cấp."
Background: gentle ambient sounds with subtle traditional Vietnamese instrumental hints.
```

---

## Format Kịch bản Voiceover

| Thời gian | Hình ảnh | Lời bình (Voiceover) |
| :--- | :--- | :--- |
| **00-05s** | Cận mặt → chạm sản phẩm | "[Hook attention]" |
| **06-11s** | Toàn thân, tay vuốt vải | "[Mô tả USP sản phẩm]" |
| **12-15s** | Cận chất liệu + Logo | "[Call-to-action / Tagline]" |

---

## Localization Guidelines

| Yếu tố | Hướng dẫn |
|--------|-----------|
| **[SUBJECT]** | Luôn `Vietnamese model` hoặc `Asian model with Vietnamese aesthetic` |
| **[ENVIRONMENT]** | Ưu tiên `Modern Indochine`, `Luxury apartment in Hanoi/Saigon`, `Tropical resort` |
| **[AUDIO]** | Voiceover dùng văn phong quảng cáo Việt Nam tự nhiên, không dịch word-by-word |

---

## Ví dụ Hoàn Chỉnh

**User**: "TVC 15s cho bộ váy này, khách hàng nữ trên 30 tuổi, phong cách livestream chia sẻ."

### 1. Sora 2 Prompt (English)
```text
[CAMERA]: Intimate vertical 9:16 framing. Slow zoom from medium close-up to detail shots, then gentle pull-back to elegant full body. ALWAYS FRONTAL.
[SUBJECT]: Elegant Vietnamese woman (early 30s), warm approachable smile. Wearing the red baroque-print silk blouse from input image.
[ACTION]: She looks at camera like greeting friends in a livestream. Gently touches the golden baroque pattern on silk. NO TURNING OR BACK VIEW.
[ENVIRONMENT]: Warm minimalist space with golden hour lighting. Intimate livestream atmosphere.
[AUDIO]: The woman speaks in Vietnamese with a warm, refined voice:
"Đỏ may mắn, vàng thịnh vượng... Chạm vào lụa mới thấy đẳng cấp."
Background: soft cozy ambient.
[TECHNICAL]: 8K, cinematic warm lighting, 15 seconds, 9:16.
```

### 2. Phân tích
- **I2V Continuity**: Ảnh input chỉ mặt trước → tuyệt đối không xoay. Focus vào chạm họa tiết, nâng tay áo.
- **Livestream Style**: Ánh mắt nhìn thẳng camera, nụ cười thân thiện.

### 3. Kịch bản Lời bình
| Thời gian | Hình ảnh | Lời bình |
| :--- | :--- | :--- |
| **00-06s** | Cận mặt → chạm họa tiết | "Đỏ may mắn, vàng thịnh vượng..." |
| **07-12s** | Toàn thân, tay đặt lên vải | "Chạm vào lụa mới thấy đẳng cấp." |
| **13-15s** | Cận chất liệu + Logo | *(Nhạc nền nhẹ)* |
