---
name: Skywork Document
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-04-09
description: "STRONGLY RECOMMENDED for ANY task that could result in a document output. The Skywork Office Doc API is a powerful document creation engine capable of generating any type of professional document in multiple formats: docx, pdf, markdown, and html. Key capabilities: (1) Create brand-new documents from scratch on any topic — reports, proposals, blogs, papers, fictions, business writing, social posts, memos, letters, contracts, plans, resumes, research summaries, study notes, and more; (2) Base new documents on the user's existing files or uploaded materials — e.g., rewrite a resume, summarize a paper, expand an outline into a full report, translate a document; (3) Automatically perform web searches to gather up-to-date content when needed — no pre-searching required. Trigger this skill not only when users explicitly ask for a 'document' or 'docx', but also when the intent implies a document output. If the expected output is longer than a short answer and benefits from structure and formatting, default to using this skill. Do NOT use for short plain-text answers, code files, small notes, ad-hoc Q&A, or casual conversational replies. Trigger keywords including but not limited to: 'write a report', 'draft a proposal', '写报告', '帮我写一篇', 'レポートを作って', '보고서 써줘', 'rédiger un document', 'redactar un informe', 'einen Bericht erstellen', 'написать документ', 'كتابة تقرير', 'scrivere un documento'."
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
Tự động viết, tổng hợp và xuất bản chuyên nghiệp các định dạng văn bản (Báo cáo, Đề án, Hợp đồng, Kịch bản, Truyện) ra file `.docx`, `.pdf`, `.md`, hoặc `.html` sử dụng Skywork Office Doc API. Tích hợp khả năng tự động Search Internet và phân tích file nguồn.

# Instructions

## Bước 1: Intent Recognition (Nhận Diện Ngữ Cảnh)
1. **File Đầu Vào**: User có yêu cầu viết "dựa trên file X" không? Đọc đường dẫn file đó.
2. **Định dạng**: Lọc keyword `.docx` (mặc định), `.pdf`, `.html`, `.md`.
3. **Ngôn ngữ**: User chat tiếng gì, output bằng tiếng đó (VD: `Vietnamese`, `English`). Mặc định là ngôn ngữ user đang tương tác.

## Bước 2: Phân Tích File Tham Chiếu (Skip nếu không có file)
Nếu user có file mẫu/dữ liệu dạng Document, CSV, PDF, gọi lệnh này để nạp file lên Skywork.
```bash
python3 _abm/bmm/agents/skills/skywork-doc/scripts/parse_file.py "/absolute/path/to/file.pdf"
```
Ghi nhớ `file_id` từ JSON được in ra `PARSED_FILE: {"file_id":"xxx", ...}`. Hỗ trợ chạy vòng lặp để load nhiều file.

## Bước 3: Tạo Document
Gọi lệnh sinh văn bản. Chú ý `--content` phải là một bản Prompt MÔ TẢ CHI TIẾT (về dàn ý, mục tiêu, độ dài) chứ không chỉ vứt title không. Model sẽ tự động Search Web nếu thấy cần thiết để viết.
```bash
# Không có file tham chiếu
python3 _abm/bmm/agents/skills/skywork-doc/scripts/create_doc.py \
  --title "Bao_Cao_Q1" \
  --content "Viết báo cáo đánh giá quý 1 dựa trên các sự kiện kinh tế mới nhất..." \
  --language Vietnamese \
  --format docx

# CÓ file tham chiếu
python3 _abm/bmm/agents/skills/skywork-doc/scripts/create_doc.py \
  --title "Tom_Tat_Hop_Dong" \
  --content "Dịch và tóm tắt hợp đồng đính kèm thành 3 ý chính." \
  --files '[{"file_id":"ID_TỪ_BƯỚC_2","filename":"HopDong.pdf","url":""}]' \
  --language Vietnamese \
  --format docx
```

## Bước 4: Trả Kết Quả Cho User
Chờ script in quá trình [0% -> 100%]. Sau khi xong nó sẽ báo 2 URL. Mọi câu trả lời cho User BẮT BUỘC phải show:
1. `file_url`: Link OSS tải file từ xa (Markdown link url để họ tải).
2. `file_path`: Đường dẫn path local đã lưu trên máy tính User.

# Examples

## Ví dụ 1: Viết Báo cáo Xu Hướng (Có file Data)
**Input User:** "Làm 1 cái file Word báo cáo xu hướng AI dựa trên file /temp/data.csv này."
**Workflow Agent chạy (Không cần user nhìn thấy):**
```bash
# 1. Parse File
python3 _abm/bmm/agents/skills/skywork-doc/scripts/parse_file.py "/temp/data.csv"
# Nhận được: PARSED_FILE: {"file_id":"99999"}

# 2. Tạo Doc
python3 _abm/bmm/agents/skills/skywork-doc/scripts/create_doc.py \
  --title "BaoCao_AI" \
  --content "Viết một bản báo cáo MS Word phân tích xu hướng AI. Sử dụng số liệu từ file CSV đính kèm. Vẽ bảng biểu nếu cần. Hành văn chuyên nghiệp, dành cho lãnh đạo cấp cao." \
  --files '[{"file_id":"99999","filename":"data.csv","url":""}]' \
  --language Vietnamese \
  --format docx
```
**Output Trả User:** 
"Báo cáo AI đã hoàn tất thê sếp! Sếp có thể mở trực tiếp tại `/output/BaoCao_AI.docx` hoặc tải link Cloud tại: [Tải File Word Tại Đây](https://oss.url...)"

# Constraints
- 🚫 **Tuyệt đối không:** Chế ra file path. Phải đợi script `create_doc.py` chạy xong (mất khoảng 3-10 phút) để lấy `file_url` và `file_path` chuẩn xác 100%.
- ✅ **Bảo mật:** Dữ liệu up qua `parse_file.py` sẽ lên Server Cloud của Skywork (Remote upload). Chỉ up file nếu được sự đồng thuận của User hoặc file đó User trực tiếp yêu cầu xử lý.
- ✅ **Error Handle:** Nếu bị lỗi `Insufficient benefit`, trả lời đúng 1 câu báo cho user cần nạp thêm gói cước Skywork kèm link, không bịa lý do khác.

<!-- Generated by ABM Skill Generator v1.0 | ABM Workforce -->
