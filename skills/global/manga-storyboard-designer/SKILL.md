---
name: "Goal"
description: "Chuyển **BẤT KỲ chương truyện** (markdown/text) thành **bộ prompt truyện tranh"
---

﻿---
name: manga-storyboard-designer
description: Convert fiction chapters to manga/manhua storyboard panels with AI-ready prompts.
---
---

# Goal

> **Use this skill when:** converting fiction to manga/manhua storyboard panels

Chuyển **BẤT KỲ chương truyện** (markdown/text) thành **bộ prompt truyện tranh
chuyên nghiệp** — mỗi trang 4-6 khung hình ghép lại, có text tiếng Việt là
điểm nhấn chính, tóm tắt nội dung nổi bật của phân cảnh.

**Output = 2 file:**
1. **`.md`** — Storyboard chi tiết (layout, direction, dialogue, prompt)
2. **`.txt`** — Chỉ prompt, mỗi dòng 1 prompt, đánh số thứ tự, không thêm nội dung

> ⚠️ KHÔNG gọi API tạo ảnh. KHÔNG dùng Nano Banana 2. CHỈ tạo prompt.

---

# Instructions

## Phase 0: Intake — Nhận đầu vào

1. **Đọc chương truyện** user cung cấp (file path hoặc paste text)
2. **Auto-detect** (KHÔNG hỏi nếu tự suy luận được):
   - **Genre**: scan keywords (linh khí/tu luyện → tu tiên, máu/bóng tối → horror...)
   - **Mood**: phân tích tỉ lệ dialogue/action/description → chọn style
   - **Page count**: `word_count / 150 ≈ number of pages` (adjust ±3)
     > Standard: chapter 4000 từ ≈ 24-28 trang. Mỗi beat = 1 trang × 4-6 panel.
3. **Chỉ hỏi user NẾU mơ hồ** (max 2 câu):
   - "Tôi detect style [X], đúng không?"
   - "Chapter này ~[N] trang, OK không?"
4. **Smart defaults** (khi user không trả lời):
   - Format: Manga page 9:16 (dọc) hoặc 16:9 (ngang) — hỏi user nếu chưa rõ
   - Style: Auto-detect từ chapter tone
   - Pages: `word_count / 150` (min 12, max 35)
   - Font: sans-serif đậm không chân nét đều viền trắng trên nền tối, đồng nhất toàn bộ
5. **Edge cases**:
   - Chapter < 1000 từ → 8-12 trang, mỗi trang 4 panels
   - Chapter > 8000 từ → chia thành 2 parts, max 18 trang/part
   - Chapter thuần action → SFX text thay speech bubble, 4-5 panels action-heavy
   - Chapter thuần nội tâm → narration box + biểu cảm, 5-6 panels emotional cascade

## Phase 1: Analysis — Phân tích chương

4. **Đọc toàn bộ chương**, xác định:
   - **Characters**: tên, ngoại hình, trang phục, tính cách
   - **Locations**: địa điểm, không gian, thời gian
   - **Mood arc**: cảm xúc thay đổi qua chương
   - **Key visual moments**: cảnh đỉnh điểm cần panel lớn nhất (nhưng vẫn trong 4-6 panel)

5. **Đánh dấu Beat Points** — mỗi "nhịp kể chuyện":
   - 🔵 **Setup**: thiết lập bối cảnh, giới thiệu
   - 🟡 **Rising**: tension leo thang, di chuyển, đối thoại quan trọng
   - 🔴 **Climax**: đỉnh điểm, reveal, twist
   - ⚫ **Resolution**: hạ nhiệt, suy nghĩ, kết thúc

## Phase 2: Scene Division — Chia cảnh

6. **Group beats thành scenes** theo quy tắc:
   - Location change = new page
   - Significant time skip = new page
   - Major mood shift = new page
   - 1 scene = 1 trang = 4-6 panels

7. **Assign page layouts** (TẤT CẢ đều 4-6 panels):

   | Scene type | Layout style | Panel count |
   |---|---|---|
   | Establishing | Wide top + grid dưới | 4-5 |
   | Dialogue | Grid đều hoặc cascade | 4-6 |
   | Action | Dynamic diagonal + impact | 4-5 |
   | Emotional | Close-up cascade | 5-6 |
   | Reveal/Climax | Hero panel lớn + 3-4 panel nhỏ | 4-5 |
   | Transition | Montage/aspect grid | 4-6 |

   > ⛔ KHÔNG BAO GIỜ dùng splash page 1 panel. Tối thiểu 4, tối đa 6.

8. **Verify pacing**:
   - ❌ Không quá 3 trang dialogue liên tiếp
   - ✅ Mỗi 3-4 trang cần 1 visual punch (hero panel lớn chiếm 40-50%)
   - ✅ Chapter climax = trang có hero panel lớn nhất + text dramatic
   - ✅ Trang cuối = cliffhanger hook

## Phase 3: Character DNA — Khóa nhân vật

9. **Viết Character DNA** cho MỌI nhân vật xuất hiện:
   ```
   [Tên] — [Tuổi], [Vóc dáng]. [Chi tiết khuôn mặt — hàm, mắt, da].
   [Tóc — kiểu, màu, độ dài]. [Trang phục — outfit đặc trưng, màu sắc].
   [Đặc điểm nhận dạng — sẹo, nốt ruồi, phụ kiện].
   [NÉT NHẬN DẠNG CHÍNH — 1-2 đặc điểm LUÔN xuất hiện, VD: đeo kính, sẹo, xe cụ thể].
   [Biểu cảm mặc định]. [Năng lượng/vibe].
   ```
   > DNA phải đủ chi tiết để AI tạo CÙNG MỘT nhân vật qua mọi trang.
   > **NÉT NHẬN DẠNG CHÍNH** phải xuất hiện trong MỌI panel có nhân vật đó —
   > biến thể theo ngữ cảnh (VD: kính phản chiếu ánh sáng, kính lấm nước mưa,
   > kính đặt trên bàn khi ngủ, ánh sáng hắt lên gọng kính...).

10. **Viết Style Lock** — aesthetic cố định:
    ```
    [Phong cách vẽ]. [Bảng màu — chính, phụ, nhấn].
    [Phong cách ánh sáng]. [Nét vẽ]. [Mức chi tiết nền].
    Tỉ lệ khung 9:16 hoặc 16:9. [Tham chiếu nghệ sĩ/tác phẩm nếu có].
    ```

## Phase 4: Page Design — Thiết kế từng trang

11. **Chọn Layout Type** cho mỗi trang — KHÔNG dùng grid chữ nhật đều đặn:

    | Layout Type | Mô tả | Khi nào dùng |
    |------------|-------|-------------|
    | **DIAGONAL SLASH** | Đường chéo cắt trang thành vùng tam giác/hình thang | Kịch tính, tension, tốc độ |
    | **SPLASH + INSET** | 1 ảnh lớn full nền + khung nhỏ overlay bên trong | Reveal, establishing shot, moment WOW |
    | **OVERLAPPING CASCADE** | Khung chồng lên nhau, tràn viền, xếp lớp | Chuỗi hành động, montage, hội thoại nhanh |
    | **BROKEN BORDER** | Nhân vật/hiệu ứng phá vỡ viền khung, tràn ra ngoài | Sức mạnh bùng nổ, supernatural |
    | **SHAPED PANEL** | Khung hình dạng đặc biệt: tròn (lens kính), màn hình phone, con mắt | Focus chi tiết, POV đặc biệt |
    | **FILMSTRIP** | Dải khung ngang/dọc hẹp liên tiếp như cuộn phim | Chuỗi monotone, thời gian trôi |
    | **MOSAIC / SHATTERED** | Trang vỡ thành nhiều mảnh không đều, bất đối xứng | Shock, vỡ vụn reality, thế giới thay đổi |
    | **VERTICAL BLEED** | 1 khung dọc xuyên suốt + khung nhỏ bên cạnh | Nhân vật đứng, kiến trúc, mưa rơi |
    | **SPOTLIGHT / VIGNETTE** | Viền mờ dần vào tối, focus trung tâm, không border rõ | Ký ức, flashback, nội tâm, mơ màng |
    | **FREEFORM FLOW** | Không có border, cảnh hòa vào nhau qua gradient/sương/khói/mưa | Chuyển cảnh mượt, siêu thực, bí ẩn |

    > ⚠️ **KHÔNG dùng grid chữ nhật đều đặn** — MỖI trang phải có layout sáng tạo.
    > ❌ KHÔNG 3+ trang liên tiếp cùng layout type.
    > ✅ Xen kẽ layout types để tạo nhịp thị giác phong phú.

12. **Cho MỖI trang**, viết chi tiết:

    ```markdown
    ## TRANG [N]: "[Tên cảnh]"

    **Beat**: [🔵/🟡/🔴/⚫]
    **Địa điểm**: [Location]
    **Thời gian**: [Time]
    **Cảm xúc**: [Mood chủ đạo]
    **Nội dung nổi bật**: [1-2 câu tóm tắt điểm nhấn chính của phân cảnh]

    ### Layout: [LAYOUT TYPE] — [N] panels

    **Bố cục sáng tạo:**
    - [Mô tả cách chia khung — đường chéo, hình dạng đặc biệt, chồng lớp, tràn viền...]
    - [Panel nào là HERO/focus, panel nào là inset/phụ]
    - [Cách các panel kết nối — gradient, sương, speed lines, năng lượng...]

    | Panel | Hình dạng & Vị trí | Cỡ cảnh + Góc | Nội dung |
    |-------|-------------------|---------------|---------|
    | P1 | [hình dạng sáng tạo, vị trí] | [shot + angle] | [mô tả chi tiết] |
    | P2 | ... | ... | ... |
    | P3 | ... | ... | ... |
    | P4 | ... | ... | ... |
    | (P5) | ... | ... | ... |
    | (P6) | ... | ... | ... |

    ### Text tiếng Việt (điểm nhấn chính)
    - NARRATION: "[text tiếng Việt — LÀ ĐIỂM NHẤN CHÍNH]"
    - [NHÂN VẬT]: "[thoại tiếng Việt]"
    - SFX: "[hiệu ứng âm thanh tiếng Việt]"

    ### Chuyển tiếp → Trang [N+1]
    [Loại transition]: [giải thích]
    ```

    > ⚠️ **Text tiếng Việt là điểm nhấn CHÍNH** — mỗi trang PHẢI có text
    > nổi bật (narration box hoặc dialogue) tóm tắt nội dung cảnh đó.

13. **Camera/Shot**, chọn từ:
    - Toàn cảnh xa → Toàn cảnh → Trung cảnh rộng → Trung cảnh → Cận trung → Cận cảnh → Đặc tả
    - Góc: Ngang tầm mắt, Góc thấp, Góc cao, Nhìn từ trên, Nhìn từ dưới, Nghiêng, POV

14. **Ánh sáng**, chọn từ:
    - Viền sáng, Đèn vùng, Neon, Sáng từ dưới, Bóng đen
    - Tia sáng, Chiaroscuro, Tối xung quanh, Spotlight trực tiếp

## Phase 5: Prompt Generation — Sinh prompt

15. **Sinh prompt cho mỗi trang** — 1 prompt = 1 trang = 4-6 panels:

    **Cấu trúc prompt (1 dòng liền mạch):**
    ```
    Trang truyện tranh manga [PHONG CÁCH], [TÔNG MÀU], tương phản cao. Bố cục [LAYOUT TYPE] trên trang [dọc 9:16 / ngang 16:9] với [SỐ] khung hình sáng tạo: [MÔ TẢ CÁCH CHIA KHUNG — đường chéo/hình dạng đặc biệt/chồng lớp/tràn viền/không viền...]. Panel 1 ([HÌNH DẠNG + VỊ TRÍ SÁNG TẠO]): [MÔ TẢ CẢNH CHI TIẾT]. Panel 2 ([HÌNH DẠNG]): [MÔ TẢ]. Panel 3: [MÔ TẢ]. Panel 4: [MÔ TẢ]. (Panel 5-6 nếu có). Ô chữ narration nổi bật: "[TEXT TIẾNG VIỆT LÀ ĐIỂM NHẤN CHÍNH]". Bong bóng thoại: "[THOẠI TIẾNG VIỆT]". Nhân vật [TÊN]: [DNA MÔ TẢ NGOẠI HÌNH]. Phong cách: [STYLE LOCK]. Tất cả chữ trong ảnh phải là tiếng Việt, font sans-serif đậm không chân nét đều viền trắng trên nền tối, chữ to rõ ràng dễ đọc, đồng nhất font toàn bộ các trang. [QUY TẮC THAM CHIẾU]
    ```

16. **Quy tắc prompt:**
    - ✅ Viết prompt LIỀN MẠCH trên 1 dòng duy nhất
    - ✅ Mô tả ĐỦ 4-6 panel trong prompt
    - ✅ Text tiếng Việt là ĐIỂM NHẤN — phải có narration/dialogue nổi bật
    - ✅ Character DNA đầy đủ + NÉT NHẬN DẠNG CHÍNH lặp lại mọi panel
    - ✅ Style Lock nhất quán
    - ✅ Tỉ lệ 9:16 hoặc 16:9 explicit
    - ✅ Font đồng nhất toàn bộ các trang
    - ❌ KHÔNG viết prompt tiếng Anh
    - ❌ KHÔNG tạo ảnh, KHÔNG gọi API

17. **Quy tắc tham chiếu ảnh (REFERENCE RULE):**
    - Mỗi prompt PHẢI kết thúc bằng `[QUY TẮC THAM CHIẾU]`
    - **Prompt 1** (trang đầu): `Upload kèm ảnh nhân vật chính [TÊN] làm reference để giữ đồng nhất khuôn mặt và phong cách nhân vật xuyên suốt.`
    - **Prompt 2+** (trang tiếp): `Upload kèm ảnh trang [N-1] đã tạo trước đó + ảnh nhân vật chính [TÊN] làm reference để giữ đồng nhất phong cách vẽ, khuôn mặt và bố cục xuyên suốt.`
    > Quy tắc này đảm bảo khi user feed prompt vào AI image generator,
    > họ biết cần upload kèm ảnh nào để giữ visual consistency.

18. **Confidence scoring** cho mỗi trang:
    - 🟢 **CAO** (8-10): Scene rõ ràng, 1-2 nhân vật, 4 panels đơn giản
    - 🟡 **TRUNG BÌNH** (5-7): Nhiều nhân vật, 5-6 panels, dynamic action
    - 🔴 **THẤP** (1-4): Crowd scenes, abstract, complex 6-panel layout

## Phase 6: Assembly — Xuất file

19. **File .md** — Storyboard chi tiết:
    ```
    # Storyboard [Tên Chapter]
    
    ## Thông tin chung
    - Chương: [tên]
    - Số trang: [N]
    - Phong cách: [style]
    - Bảng màu: [palette]
    
    ## Character DNA Registry
    [Tất cả nhân vật]
    
    ## Style Lock
    [Aesthetic cố định]
    
    ## Các trang
    [TRANG 1 ... TRANG N — chi tiết layout + prompt]
    
    ## Pacing Diagram
    [Biểu đồ nhịp]
    ```

20. **File .txt** — Prompt only:
    ```
    1. [Prompt trang 1 — 1 dòng liền mạch, không xuống hàng]
    2. [Prompt trang 2 — 1 dòng liền mạch, không xuống hàng]
    3. [Prompt trang 3 — 1 dòng liền mạch, không xuống hàng]
    ...
    N. [Prompt trang N — 1 dòng liền mạch, không xuống hàng]
    ```

    > ⛔ File .txt TUYỆT ĐỐI:
    > - Mỗi prompt 1 dòng liền mạch
    > - Đánh số thứ tự: `1.`, `2.`, `3.`, ...
    > - KHÔNG thêm header, footer, comment, separator
    > - KHÔNG xuống hàng giữa prompt
    > - KHÔNG thêm bất kỳ nội dung nào ngoài prompt

20. **Pacing diagram** ở cuối .md:
    ```
    Trang:  1   2   3   ...
    Beat:   🔵  🟡  🔴  ...
    Panels: 4   5   4   ...
    Type:   GRD CAS DYN ...
    Conf:   🟢  🟢  🟡  ...
    ```

---

# Examples

## Ví dụ 1: Tu Tiên Đô Thị — Trang 1

**Beat**: 🔵 Setup | **Location**: Hồ Tây | **Mood**: noir, cô đơn
**Nội dung nổi bật**: Hà Nội lúc 1:14 sáng, Dũng Cận trên xe Wave, pin 10%

### Layout: Establishing — 5 panels

| Panel | Vị trí | Cỡ cảnh | Nội dung |
|-------|--------|---------|---------|
| P1 | Trên cùng, 35% | Toàn cảnh xa, góc cao | Đường Thanh Niên vắng, Hồ Tây đêm, mưa phùn |
| P2 | Giữa trái, 15% | Cận cảnh | Tay nắm ghi-đông, xương ngón nổi |
| P3 | Giữa phải, 15% | Đặc tả | Màn hình điện thoại: 1:14, pin 10% |
| P4 | Dưới trái, 15% | Trung cảnh | Dũng trên Wave cũ, áo Grab bạc màu |
| P5 | Dưới phải, 20% | Cận cảnh | Mắt Dũng — mệt mỏi nhưng sắc lẻm |

**Text tiếng Việt (điểm nhấn):**
- NARRATION: **"HÀ NỘI. 1 GIỜ 14 PHÚT SÁNG."**
- NARRATION: "Pin 10%. Đêm nay chắc nghỉ sớm."

### Prompt (1 dòng liền mạch):
```
Trang truyện tranh manga phong cách noir Việt Nam, tông tối xanh xám, tương phản cao, nét vẽ ink wash. 5 khung hình (panel) ghép trên một trang dọc 9:16: Panel 1 (trên cùng, chiếm 35%): Toàn cảnh xa góc cao đường Thanh Niên Hà Nội lúc đêm khuya vắng tanh, Hồ Tây mặt nước đen phản chiếu ánh đèn đường vàng ấm, mưa phùn tạo gợn sóng nhẹ, hàng cây trụi lá. Panel 2 (giữa trái, 15%): Cận cảnh tay nắm ghi-đông xe máy cũ, xương ngón tay nổi vì gầy, găng tay rách. Panel 3 (giữa phải, 15%): Đặc tả màn hình điện thoại nứt vỡ hiển thị 1:14 sáng và biểu tượng pin đỏ 10 phần trăm, giọt mưa trên kính. Panel 4 (dưới trái, 15%): Trung cảnh nhân vật nam Dũng Cận ngồi trên xe Honda Wave cũ bên đường, mặc áo khoác Grab xanh bạc màu ngoài hoodie đen. Panel 5 (dưới phải, 20%): Cận cảnh mắt Dũng Cận với quầng thâm dưới mắt, ánh mắt mệt mỏi nhưng vẫn sắc lẻm. Ô chữ narration box lớn nổi bật ở góc trên: HÀ NỘI. 1 GIỜ 14 PHÚT SÁNG. Ô chữ narration nhỏ hơn ở panel cuối: Pin 10 phần trăm. Đêm nay chắc nghỉ sớm. Nhân vật Dũng Cận: nam Việt Nam 24 tuổi, gầy, mặt góc cạnh, tóc đen ngắn bù xù, quầng thâm mắt, mặc áo khoác Grab xanh bạc ngoài hoodie đen. Phong cách manga noir tối, ink wash, tông xanh xám lạnh với điểm nhấn amber đèn đường. Tất cả chữ trong ảnh phải là tiếng Việt, chữ to rõ ràng dễ đọc.
```

### .txt output (dòng tương ứng):
```
1. Trang truyện tranh manga phong cách noir Việt Nam, tông tối xanh xám, tương phản cao, nét vẽ ink wash. 5 khung hình (panel) ghép trên một trang dọc 9:16: Panel 1 (trên cùng, chiếm 35%): Toàn cảnh xa góc cao đường Thanh Niên Hà Nội lúc đêm khuya vắng tanh, Hồ Tây mặt nước đen phản chiếu ánh đèn đường vàng ấm, mưa phùn tạo gợn sóng nhẹ, hàng cây trụi lá. Panel 2 (giữa trái, 15%): Cận cảnh tay nắm ghi-đông xe máy cũ, xương ngón tay nổi vì gầy, găng tay rách. Panel 3 (giữa phải, 15%): Đặc tả màn hình điện thoại nứt vỡ hiển thị 1:14 sáng và biểu tượng pin đỏ 10 phần trăm, giọt mưa trên kính. Panel 4 (dưới trái, 15%): Trung cảnh nhân vật nam Dũng Cận ngồi trên xe Honda Wave cũ bên đường, mặc áo khoác Grab xanh bạc màu ngoài hoodie đen. Panel 5 (dưới phải, 20%): Cận cảnh mắt Dũng Cận với quầng thâm dưới mắt, ánh mắt mệt mỏi nhưng vẫn sắc lẻm. Ô chữ narration box lớn nổi bật ở góc trên: HÀ NỘI. 1 GIỜ 14 PHÚT SÁNG. Ô chữ narration nhỏ hơn ở panel cuối: Pin 10 phần trăm. Đêm nay chắc nghỉ sớm. Nhân vật Dũng Cận: nam Việt Nam 24 tuổi, gầy, mặt góc cạnh, tóc đen ngắn bù xù, quầng thâm mắt, mặc áo khoác Grab xanh bạc ngoài hoodie đen. Phong cách manga noir tối, ink wash, tông xanh xám lạnh với điểm nhấn amber đèn đường. Tất cả chữ trong ảnh phải là tiếng Việt, chữ to rõ ràng dễ đọc.
```

## Ví dụ 2: Romance — Trang cảm xúc

**Beat**: 🟡 Rising | **Layout**: Cascade — 6 panels

| Panel | Vị trí | Cỡ cảnh | Nội dung |
|-------|--------|---------|---------|
| P1 | Trên, 20% | Trung cảnh | Hai người ngồi quán cà phê, im lặng |
| P2 | Giữa trái, 15% | Cận cảnh | Tay cô gái quấn quanh ly trà |
| P3 | Giữa phải, 15% | Cận cảnh | Mắt chàng trai nhìn sang |
| P4 | Giữa, 20% | Trung cận | Hai bàn tay gần chạm trên bàn |
| P5 | Dưới trái, 15% | Đặc tả | Giọt nước rơi trên cửa kính |
| P6 | Dưới phải, 15% | Cận cảnh | Nụ cười nhẹ của cô gái |

**Text**: NARRATION: **"Có những khoảng lặng nói nhiều hơn lời."**

---

# Constraints

## Panel count — LUẬT SẮT
- **Tối thiểu 4 panels, tối đa 6 panels** cho MỌI trang
- ❌ TUYỆT ĐỐI KHÔNG splash page 1 panel
- ❌ TUYỆT ĐỐI KHÔNG dưới 4 panels
- ✅ Cảnh climax/reveal: dùng hero panel chiếm 40-50% + 3-4 panel nhỏ = tổng 4-5

## Text tiếng Việt — LUẬT SẮT
- **100% text trong prompt và trong ảnh phải là tiếng Việt**
- Mỗi trang PHẢI có text tiếng Việt là **ĐIỂM NHẤN CHÍNH**
- Text phải tóm tắt nội dung nổi bật của phân cảnh đó
- Narration box hoặc dialogue bubble phải rõ ràng, chữ to dễ đọc

## Font — LUẬT SẮT
- **Đồng nhất 1 loại font toàn bộ các trang**: sans-serif đậm không chân nét đều viền trắng trên nền tối
- Chữ to rõ ràng dễ đọc
- Mỗi prompt PHẢI ghi rõ font specification

## Tham chiếu ảnh — LUẬT SẮT
- Mỗi prompt PHẢI kết thúc bằng `[QUY TẮC THAM CHIẾU]`
- **Trang 1**: chỉ tham chiếu ảnh nhân vật chính
- **Trang 2+**: tham chiếu ảnh trang trước đó + ảnh nhân vật chính
- Mục đích: giữ đồng nhất phong cách vẽ, khuôn mặt, bố cục xuyên suốt

## Nét nhận dạng chính — LUẬT SẮT
- Mỗi nhân vật PHẢI có 1-2 **nét nhận dạng chính** (VD: đeo kính, sẹo, xe cụ thể)
- Nét này PHẢI xuất hiện trong **MỌI panel** có nhân vật đó
- Biến thể theo context (kính phản chiếu, kính lấm nước, kính đặt trên bàn...)

## Output — LUẬT SẮT
- Xuất 2 file: `.md` (chi tiết) + `.txt` (prompt only)
- File .txt: mỗi prompt 1 dòng liền mạch, đánh số, KHÔNG thêm bất kỳ nội dung nào
- ❌ KHÔNG gọi API tạo ảnh
- ❌ KHÔNG dùng Nano Banana 2 script
- Chỉ TẠO PROMPT

## Character DNA
- LUÔN giữ Character DNA NGUYÊN VẸN qua mọi prompt
- Style Lock NGUYÊN VẸN qua mọi prompt
- NÉT NHẬN DẠNG CHÍNH phải nhất quán 100%

## Storytelling
- Show, don't tell — chuyển nội tâm thành visual
- Pacing variety — không 3+ trang cùng loại layout liên tiếp
- Layout variety — xen kẽ layout types sáng tạo, tránh lặp monotone
- Trang cuối = cliffhanger hook

## Layout — LUẬT SẮT
- ❌ **KHÔNG dùng grid chữ nhật đều đặn** cho mọi trang
- ❌ **KHÔNG 3+ trang liên tiếp** cùng layout type
- ✅ Chọn từ **10 Layout Types sáng tạo**: DIAGONAL SLASH, SPLASH+INSET, OVERLAPPING CASCADE, BROKEN BORDER, SHAPED PANEL, FILMSTRIP, MOSAIC/SHATTERED, VERTICAL BLEED, SPOTLIGHT/VIGNETTE, FREEFORM FLOW
- ✅ Mô tả cách chia khung bằng **hình dạng sáng tạo** (đường chéo, hình tròn, lens, tràn viền, chồng lớp...)
- ✅ Hỗ trợ 2 format: **9:16** (dọc) và **16:9** (ngang)
- ✅ Xen kẽ layout types tạo nhịp thị giác phong phú

## An toàn
- 🚫 KHÔNG nội dung bạo lực máu me quá mức
- ✅ Action: dùng energy effects, motion lines, impact frames

<!-- Generated by Skill Creator Ultra v2.0 — Redesigned v2.0 -->
