> BÍ KÍP CHUYỂN GIAO (Bản V5.0 - Markdown-First Protocol): VIETNAMESE-CONTRACT (BAN PHÁP CHẾ)
> Hướng dẫn cho AI: Mọi yêu cầu liên quan đến soạn thảo hợp đồng, văn bản pháp lý, cam kết tiếng Việt PHẢI tuân thủ thủ tục Tòa Soạn V5 dưới đây. TUYỆT ĐỐI không dùng code native (docx.js).

# Vietnamese Legal Contract Generator (Tòa Soạn V5.0)

> **Author:** Phạm Triết (Tái cấu trúc từ QĐ của Đại Hội Cổ Đông ABM)
> **Quy chuẩn Cốt lõi:** Phương án Xuất file duy nhất là API Skywork (Nano Banana 2). AI đóng vai trò Luật sư (nghĩ nội dung mộc), 100% việc dàn trang giao cho máy in Skywork.

## Mục lục
1. Quy trình tổng quan 4 Bước
2. Bước 1: Xác định loại & Tra cứu pháp lý
3. Bước 2: Soạn nội dung Markdown-First
4. Bước 3: Kiểm duyệt (Spellcheck & Bằng chứng)
5. Bước 4: Tạo DOCX qua Skywork API & Xuất kết quả

---

## 🏛️ Quy trình Tổng quan (Markdown-First & Skywork Render)

```text
Yêu cầu người dùng (Nhờ soạn hợp đồng)
       │
       ▼
┌─────────────────┐
│ 1. Tra pháp lý &│  Tra cứu hiệu lực Luật mới nhất online.
│    Xác định loại│  (Fallback: references/legal-bases.md)
└───────┬─────────┘  (Tùy chọn: Quét CCCD bằng EasyOCR)
        ▼
┌─────────────────┐
│ 2. Soạn Markdown│  AI TẬP TRUNG 100% soạn nội dung, 
│    (.md)        │  in đậm Heading, đúng cấu trúc Hợp đồng,
│                 │  chỗ trống để "......", lưu ra file .md
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 3. Kiểm duyệt   │  Gọi script vn-spellcheck.py (để check lỗi 
│    (Sếp duyệt)  │  chính tả đặc thù). Đợi sếp Gật đầu.
└───────┬─────────┘
        ▼
┌─────────────────┐
│ 4. Skywork API  │  Đẩy Markdown cho Máy in Skywork.
│    (Render DOCX)│  Nhận link tải DOCX và Local Path trong 26s.
└─────────────────┘
```

**QUAN TRỌNG:** Đọc các file reference TRƯỚC khi viết:
- `references/legal-bases.md` — Căn cứ pháp lý từng loại HĐ.
- `references/contract-structures.md` — Cấu trúc điều khoản từng loại.
- (Loại bỏ vĩnh viễn `references/docx-formatting.md` - Skywork nay đã lo việc dàn trang).

---

## Bước 1: Xác định loại & Tra cứu pháp lý

### 1.1 Khai thác thông tin
Nếu người dùng chưa nêu rõ, hãy lịch sự hỏi các trường sau (hoặc điền "......"):
*   **Các bên:** Tên công ty/Cá nhân, CCCD/MST, địa chỉ, người đại diện.
*   **Đối tượng:** Thuê nhà, Mua bán, Thử việc, Góp vốn,...
*   **Giá trị & Thời hạn:** Bao nhiêu tiền (ghi cả bằng chữ), hiệu lực từ ngày nào.
*   **Điều kiện đặc biệt:** Kỳ thanh toán, bảo hành, phạt vi phạm...

### 1.2 Xác minh tính pháp lý (Mạng Sống Của Hợp Đồng)
Không bao giờ tự ý bịa Luật. Đọc file `references/legal-bases.md` để lấy gốc. Sau đó:
**BẮT BUỘC dùng Web Search** để kiểm tra Luật đó còn hiệu lực hay đã bị thay thế trong năm hiện tại, lấy nguồn từ `thuvienphapluat.vn` hoặc `vbpl.vn`. (Ví dụ: Luật Đất đai 2024 thay thế Luật cũ).

### 1.3 Quét CCCD tự động (Trường hợp Sếp quăng ảnh)
Nếu sếp gửi file ảnh CCCD:
1. Chạy OCR nội bộ offline: `python scripts/cccd-ocr.py anh-mat-truoc.jpg --json`
2. AI tự đọc JSON, nắn chỉnh lại bằng tư duy tiếng Việt (VD: "Phạm Mrinh Triet" -> "Phạm Minh Triết"), ráp vào chủ thể Hợp đồng. Bảo mật 100% vì OCR chạy offline, không gửi ảnh qua mạng.

---

## Bước 2: Soạn nội dung Markdown-First

**→ Tham khảo `references/contract-structures.md`** để biết lõi cấu trúc từng loại hợp đồng.

### Nguyên tắc 5 Điểm Chết của Văn bản Pháp quy
1. **Quốc hiệu phải đầy đủ:** Lên đầu cùng, căn giữa (Markdown ngầm hiểu).
2. **Cấu trúc Điều khoản:** Phân cấp rõ nét: `ĐIỀU 1` -> `1.1` -> `a, b, c`.
3. **Double Highlight:** Giá tiền phải có chữ số và chữ viết (VD: 5.000.000 VNĐ - Bằng chữ: Năm triệu đồng chẵn).
4. **Không viết Code JS/CSS:** Đây là Markdown thuần túy. Tuyệt đối KHÔNG gõ mã định dạng màu mè. Dùng Heading `#`, và in đậm `**` là đủ. Skywork Engine sẽ tự gán các style đó thành cỡ chữ 13pt/14pt Times New Roman, đôn dòng, canh đều (Justified text) cực đẹp.
5. **Chữ ký cuối:** Luôn ghi BÊN A và BÊN B trên cùng 1 đoạn, Skywork sẽ tự phân rã bảng cột cho 2 vị trí chữ ký.

**Ví dụ Markdown chuẩn:**
```markdown
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập - Tự do - Hạnh phúc

HỢP ĐỒNG DỊCH VỤ
Số: ..../2026/HĐDV

Hôm nay,...

**BÊN A: CÔNG TY TNHH ABM**
Đại diện: ...

**ĐIỀU 1: NỘI DUNG DỊCH VỤ**
1.1. Phạm vi công việc: ...

**BÊN A**                    **BÊN B**
```

---

## Bước 3: Kiểm duyệt (Evidence-based Verification)
Khâu Kiểm tra chất lượng (Quality Gate) tại Tòa Soạn V5:
1. Viết bản nháp Markdown và lưu tạm vào `/tmp/hopdong_nhap.md`.
2. Gõ lệnh gọi `python scripts/vn-spellcheck.py /tmp/hopdong_nhap.md` để check nhanh 50+ lỗi chính tả phổ biến trong hợp đồng.
3. Dùng con mắt Biên tập viên: Đọc lại 1 lượt xem các biến "......" đã điền logic chưa. 
4. **Xin phép Sếp:** Hiện Preview Markdown cho Sếp xem qua (hoặc tóm tắt các core-terms). 
5. Chỉ khi Sếp duyệt "ok" mới nhảy sang Bước 4. **KHÔNG BAO GIỜ GỌI SKYWORK KHI SẾP CHƯA DUYỆT BẢN THÔ.**

---

## Bước 4: Tạo DOCX qua Skywork API & Xuất kết quả

Sau khi Sếp duyệt nội dung Markdown, gọi sức mạnh của Lò Bát Quái.
Kích hoạt **Skywork Document Skill** (Engine: Nano Banana 2) thông qua Script CLI có sẵn:

```bash
# Nhớ check xem biến môi trường SKYWORK_API_KEY đã có chưa
python3 _abm/bmm/agents/skills/skywork-doc/scripts/create_doc.py \
  --title "Ten_Hop_Dong_Khong_Dau" \
  --content "$(cat /tmp/hopdong_nhap.md)" \
  --language Vietnamese \
  --format docx
```

### Xử lý Kết quả (Đóng Gói Chuyên Nghiệp)
Quá trình Skywork render mất khoảng 20 - 30 giây. Script sẽ in ra % loading rồi trả về JSON kết quả chứa thông số:
- `file_path`: Đường dẫn file Word tại máy (Local).
- `file_url`: Link Tải file nhanh trên Cloud OSS.

**Hành động của AI (Sứ mệnh Giao thư):**
Thông báo rực rỡ cho Sếp biết Hợp đồng đã hoàn thiện. Bắt buộc cung cấp cả 2 link:
> "Thưa Sếp, Bản Hợp đồng lộng lẫy đã ra lò theo chuẩn Tòa Soạn V5."
> 🖥️ Mở file Local: `[Tên File](file:///path/to/local/file)`
> ☁️ Link tải siêu tốc (Share đi xa): `[Tải File DOCX Trực Tuyến](url_skywork)`

**Cảnh báo Khắc cốt ghi tâm (IRON LAW):** 
🚫 Tuyệt đối không bao giờ được bịa đặt (hallucinate) đường dẫn PATH hoặc URL của tệp. Phải đọc Output của Script `create_doc.py` rồi copy y xì đúc thông số nó nhả ra!

<!-- Generated by ABM Skill Generator v1.0 | ABM Workforce | Updated: Tòa Soạn V5.0 -->
