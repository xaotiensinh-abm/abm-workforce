# Output Format Specification

## 1. File .md — Storyboard chi tiết

### Cấu trúc

```markdown
# Storyboard: [Tên Chapter]

## Thông tin chung
- **Chương**: [tên chapter]
- **Nguồn**: [file path]
- **Số trang**: [N]
- **Phong cách**: [style lock tóm tắt]
- **Bảng màu**: [palette name]
- **Thể loại**: [genre auto-detected]

---

## Character DNA Registry

### [Tên nhân vật 1]
[DNA đầy đủ]

### [Tên nhân vật 2]
[DNA đầy đủ]

---

## Style Lock
[Style lock đầy đủ]

---

## Các Trang

### TRANG 1: "[Tên cảnh]"
**Beat**: [emoji] | **Địa điểm**: [...] | **Thời gian**: [...]
**Cảm xúc**: [...] | **Confidence**: [emoji]
**Nội dung nổi bật**: [1-2 câu tóm tắt]

#### Layout: [Type] — [N] panels
| Panel | Vị trí & KT | Cỡ cảnh + Góc | Nội dung |
|-------|------------|---------------|---------|
| P1 | ... | ... | ... |
| P2 | ... | ... | ... |
| P3 | ... | ... | ... |
| P4 | ... | ... | ... |

#### Text tiếng Việt
- NARRATION: "..."
- [NV]: "..."
- SFX: "..."

#### Prompt
```
[Prompt 1 dòng liền mạch]
```

#### Chuyển tiếp → Trang 2
[Loại]: [giải thích]

---

[Lặp lại cho mỗi trang]

---

## Pacing Diagram
```
Trang:  1   2   3   ...
Beat:   🔵  🟡  🔴  ...
Panels: 5   4   5   ...
Type:   EST DLG ACT ...
Conf:   🟢  🟢  🟡  ...
```
```

### Quy tắc .md
- Markdown chuẩn, dễ đọc
- Mỗi trang = 1 section (## TRANG N)
- Bảng panel phải đủ 4-6 hàng
- Prompt nằm trong code block
- Text tiếng Việt nổi bật (bold hoặc CAPS)

---

## 2. File .txt — Prompt only

### Cấu trúc

```
1. [Prompt trang 1 — một dòng liền mạch không xuống hàng]
2. [Prompt trang 2 — một dòng liền mạch không xuống hàng]
3. [Prompt trang 3 — một dòng liền mạch không xuống hàng]
...
N. [Prompt trang N — một dòng liền mạch không xuống hàng]
```

### Quy tắc .txt — LUẬT SẮT

| Quy tắc | Mô tả |
|---------|-------|
| **1 dòng = 1 prompt** | Mỗi prompt nằm trọn trên 1 dòng, KHÔNG xuống hàng |
| **Đánh số** | Bắt đầu bằng `1.`, `2.`, `3.` ... kèm dấu chấm + khoảng trắng |
| **Không thêm nội dung** | KHÔNG header, footer, comment, separator, dòng trống |
| **Liền mạch** | Prompt viết liền, không ngắt đoạn, không bullet points |
| **Encoding** | UTF-8, hỗ trợ tiếng Việt |

### Ví dụ .txt hoàn chỉnh (3 trang)

```
1. Trang truyện tranh manga phong cách noir Việt Nam, tông tối xanh xám, tương phản cao. 5 khung hình ghép trên trang dọc 9:16: Panel 1 (trên, 35%): Toàn cảnh đường Thanh Niên đêm vắng. Panel 2 (giữa trái, 15%): Cận cảnh tay trên ghi-đông. Panel 3 (giữa phải, 15%): Đặc tả màn hình 1:14 pin 10%. Panel 4 (dưới trái, 20%): Trung cảnh Dũng trên xe Wave. Panel 5 (dưới phải, 15%): Cận cảnh mắt mệt mỏi. Narration lớn: HÀ NỘI. 1 GIỜ 14 PHÚT SÁNG. Nhân vật Dũng Cận: nam VN 24 tuổi gầy tóc đen bù mặc áo Grab xanh bạc. Manga noir ink wash tông xanh xám amber.
2. Trang truyện tranh manga phong cách noir Việt Nam, tông tối. 4 khung hình grid trên trang dọc 9:16: Panel 1 (trên, 30%): Góc thấp xe Wave rung nhẹ trên đường loang nước đèn đường nhòe. Panel 2 (giữa trái, 20%): Cận cảnh tay trái giữ ga tay phải xoa cổ gáy. Panel 3 (giữa phải, 20%): Toàn cảnh đường vắng cửa hàng tắt đèn. Panel 4 (dưới, 30%): Trung cảnh Dũng cúi đầu trên xe dưới mưa. Narration: Mùi xăng pha mưa đêm không ai thích nhưng quen rồi thì không cần thích nữa. Nhân vật Dũng Cận: nam VN 24 tuổi gầy tóc đen bù mặc áo Grab xanh bạc. Manga noir ink wash.
3. Trang truyện tranh manga phong cách noir Việt Nam, tông tối. 5 khung hình trên trang dọc 9:16: Panel 1 (trên, 30%): Toàn cảnh rộng đường Thanh Niên hàng sấu trụi lá hồ đen. Panel 2 (giữa trên trái, 15%): Ông bảo vệ ngáp dài trong chốt. Panel 3 (giữa trên phải, 15%): Chó hoang ven đê Hồ Tây. Panel 4 (giữa dưới, 20%): Trung cảnh silhouette Grab rider cô đơn trên đường. Panel 5 (dưới, 20%): Cận cảnh mắt Dũng quét nhìn bốn phía. Narration lớn: Hà Nội lúc này thuộc về mấy thằng chạy Grab đêm. Nhân vật Dũng Cận: nam VN 24 tuổi. Manga noir ink wash tông xanh xám.
```

### ❌ Ví dụ SAI

```
# Prompts cho Chapter 1          ← SAI: có header
                                  ← SAI: có dòng trống
1. Panel 1: ...                   ← SAI: xuống hàng giữa prompt
   Panel 2: ...
   Panel 3: ...

---                               ← SAI: có separator
2. ...
```
