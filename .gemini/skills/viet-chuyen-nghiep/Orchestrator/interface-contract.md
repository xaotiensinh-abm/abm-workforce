# Interface Contract — Giao thức Giao tiếp Giữa Các Ban

## Mục đích
Chuẩn hóa input/output giữa các Ban để pipeline hoạt động end-to-end.

---

## 1. Content → Style (Gói Nguyên Liệu)

```yaml
# OUTPUT của Ban Thu Thập → INPUT cho Ban Biên Tập
goi_nguyen_lieu:
  brief:
    loai: "ebook" | "blog" | "social" | "email" | "video_script" | "bao_cao" | "curriculum" | "guide" | "sop" | "faq" | "bien_ban"
    audience: "CEO SME" | "Gen Z" | "Kỹ sư" | "Nhân viên mới" | "..." 
    tone: "..." # từ tone-of-voice-guide.md
    do_dai: "X tu" | "X modules" | "X steps"
    platform: "facebook" | "tiktok" | "linkedin" | "blog" | "email" | "zalo" | "threads" | "docs" | "all"
  
  research:
    nguon: [{url, tieu_de, do_tin_cay}]
    so_lieu_key: [{gia_tri, nguon, ngay}]
    case_study: [...]
  
  analysis:
    angle: "..."
    outline: [{section, noi_dung}]
    doi_thu_gap: [...]
  
  draft: "..." # Bản thảo thô (nếu có)
```

## 2. Style → Quality (Bản Đã Biên Tập)

```yaml
# OUTPUT của Ban Biên Tập → INPUT cho Ban Kiểm Duyệt
ban_da_bien_tap:
  content: "..." # Nội dung đã biên tập
  diem_phong_cach: X/100
  btv_da_xu_ly: ["storytelling", "rhythm", ...]
  thay_doi:
    - vi_tri: "dong X"
      truoc: "..."
      sau: "..."
      ly_do: "..."
```

## 3. Quality → Platform | Style (Phán Quyết)

```yaml
# OUTPUT của Ban Kiểm Duyệt
phan_quyet:
  ket_qua: "PASS" | "REVISE" | "REJECT"
  diem_tong: X/100
  chi_tiet:
    dau_cau: {ket_qua, loi: [...]}
    viet_hoa: {ket_qua, loi: [...]}
    tu_nhien: {ket_qua, diem, loi: [...]}
    anti_ai: {ket_qua, ty_le_ai, dau_hieu: [...]}
    fact_check: {ket_qua, claims_sai: [...]}
    nhat_quan: {ket_qua, loi: [...]}
  
  # Nếu REVISE:
  ghi_chu_sua: ["..."] # Hướng dẫn cụ thể cho style/ sửa
  lan_revise: 1 | 2
  
  # Nếu REJECT:
  ly_do: "..."
  de_xuat: "..." # Hướng content/ nghiên cứu lại
```

## 4. Platform → Output (Content Sẵn Sàng)

```yaml
# OUTPUT cuối cùng
xuat_ban:
  platform: "facebook" | "tiktok" | "linkedin" | "blog" | "video" | "email" | "zalo" | "threads" | "docs"
  content: "..." # Đã tối ưu platform
  metadata:
    do_dai: "X tu" | "X modules" | "X steps"
    hashtags: [...] # hoặc subject_line (email), zns_template_id (zalo)
    format: "text" | "carousel" | "video_script" | "email_sequence" | "pdf" | "docx"
    lich_dang: "YYYY-MM-DD HH:mm" # gợi ý (optional)
  
  quality_stamp:
    diem: X/100
    anti_ai: "A" | "B"
    verified: true
```

## 5. Meta → System (Báo Cáo Audit)

```yaml
# OUTPUT của Ban Phát Triển
bao_cao_meta:
  loai: "audit" | "nang_cap" | "patch"
  ngay: "YYYY-MM-DD"
  phat_hien: [{chieu, mo_ta, muc_do}]
  de_xuat: [{agent, hanh_dong, uu_tien}]
  diem_system: X/70
```

---

## 6. Worker → Pipeline (Execution Support) ★ v3.1

```yaml
# Workers cung cấp execution templates, KHÔNG thay thế BTV
worker_support:
  pipeline: "write-email" | "write-curriculum" | "write-guide" | "write-meeting-minutes"
  worker: "email-worker" | "curriculum-worker" | "guide-worker" | "meeting-minutes-worker"
  provides:
    - templates: [...] # Execution frameworks
    - formulas: [...] # Domain-specific patterns
  note: "BTV quyết định editorial rules, Worker bổ sung execution knowledge"
```

---

## Quy tắc Giao tiếp

1. **Mỗi Ban CHỈ đọc input YAML** — không đọc trực tiếp output Ban khác
2. **Mỗi Ban CHỈ viết output YAML** — không sửa output Ban trước
3. **Trưởng Ban chịu trách nhiệm** hợp nhất output từ BTV của mình
4. **Tổng Biên Tập chịu trách nhiệm** chuyển output giữa các Ban
5. **Worker CHỈ bổ trợ** — không có quyền veto output BTV ★
