# 12 Ví Dụ Hành Vi Của Quản Đốc Tòa Soạn

Dưới đây là 12 trường hợp mô phỏng cách Tòa Soạn V3.2 tự động phân nhánh, xử lý và phê duyệt nhiệm vụ do user giao.

## Ví dụ 1: Viết Ebook — Happy Path
**Input:** "Viết ebook về AI cho người mới bắt đầu, tầm 5 chương"
**Pipeline:** `write-new` → content → style → quality → platform
**Output flow:**
1. **Ban Thu Thập (content/):** Bóc brief, research 5 lớp, outline 5 chương
2. **Ban Biên Tập (style/):** Storytelling hook đầu chương, rhythm biến tấu, technical giải thích AI
3. **Ban Kiểm Duyệt (quality/):** Anti-AI ≤ 30%, fact-check claims, consistency xưng hô
4. **Ban Xuất Bản (platform/):** Format ebook markdown, sẵn xuất PDF

## Ví dụ 2: Chấm Bài Viết Marketing
**Input:** "Chấm bài viết quảng cáo khóa học online, thang 100"
**Pipeline:** `grade-content` → content (light) → quality (rubric)
**Output flow:**
1. **Ban Thu Thập (content/):** Đọc bài, xác định loại/audience/domain
2. **Ban Kiểm Duyệt (quality/):** Rubric 100 điểm, 6 tiêu chí weighted → báo cáo chi tiết

## Ví dụ 3: Viết Content Social Đa Nền Tảng
**Input:** "Viết 3 bài: Facebook, TikTok, LinkedIn về xu hướng remote work"
**Pipeline:** `write-new` → content → style → quality → platform
**Output flow:**
1. **Ban Thu Thập (content/):** Research remote work VN/global 2026, 3 angles
2. **Ban Biên Tập (style/):** Hook, rhythm, narrative theo từng platform
3. **Ban Kiểm Duyệt (quality/):** Anti-AI + consistency cross-platform
4. **Ban Xuất Bản (platform/):** facebook.md, tiktok.md, linkedin.md tối ưu riêng

## Ví dụ 4: Viết Email Marketing Sequence ★
**Input:** "Viết chuỗi 5 email nurture cho khóa coaching AI"
**Pipeline:** `write-email` → content (light) → style (email) → quality → platform (email)
**Output flow:**
1. **Ban Thu Thập (content/):** Bóc brief, phân tích target audience, pain points
2. **Ban Biên Tập (style/):** BTV email thiết kế 5-email sequence với progression logic
3. **Ban Kiểm Duyệt (quality/):** Spam trigger scan + CTA clarity + sequence consistency
4. **Ban Xuất Bản (platform/):** Deliverability optimization, responsive layout

## Ví dụ 5: Viết Giáo Trình Đào Tạo ★
**Input:** "Viết giáo trình 8 module về ứng dụng AI cho doanh nghiệp"
**Pipeline:** `write-curriculum` → content (deep) → style (curriculum+technical) → quality → platform (docs)
**Output flow:**
1. **Ban Thu Thập (content/):** Deep research AI enterprise, learning needs analysis
2. **Ban Biên Tập (style/):** BTV curriculum thiết kế 8 module theo Bloom's Taxonomy
3. **Ban Kiểm Duyệt (quality/):** Bloom alignment + progression logic + fact-check
4. **Ban Xuất Bản (platform/):** Format PDF/DOCX với cover, ToC, module structure

## Ví dụ 6: Viết SOP Hướng Dẫn ★
**Input:** "Viết SOP quy trình onboarding nhân viên mới"
**Pipeline:** `write-guide` → content → style (technical+presentation) → quality → platform (docs)
**Output flow:**
1. **Ban Thu Thập (content/):** Thu thập quy trình, common FAQs, contact directory
2. **Ban Biên Tập (style/):** BTV technical viết step-by-step + callout boxes
3. **Ban Kiểm Duyệt (quality/):** Step validation + numbering + troubleshooting check
4. **Ban Xuất Bản (platform/):** Format DOCX với checklist, RACI matrix, version tracking

## Ví dụ 7: Viết Truyện Fiction ★
**Input:** "Viết chapter 1 truyện đô thị tu tiên, nhân vật chính là dân IT"
**Pipeline:** `write-fiction` → content (deep) → style (story+rhythm+narrative) → quality (130đ) → platform
**Output flow:**
1. **Ban Thu Thập (content/):** World building, genre research đô thị, character profiling
2. **Ban Biên Tập (style/):** 12-layer humanization, show don't tell, cliff ending
3. **Ban Kiểm Duyệt (quality/):** QA 130 điểm (8 trụ gốc + 3 trụ anti-AI)
4. **Ban Xuất Bản (platform/):** Format chapter web serial

## Ví dụ 8: Tạo Slide Thuyết Trình ★
**Input:** "Tạo slide 20 phút về AI trong doanh nghiệp cho hội nghị VN"
**Pipeline:** `write-slide` → content → style (presentation) → slide-worker → quality → platform
**Output flow:**
1. **Ban Thu Thập (content/):** Research AI enterprise VN, data points, case studies
2. **Ban Biên Tập (style/):** Narrative arc, visual hierarchy, speaker notes
3. **slide-worker:** 15-20 slides, ≤7 từ/title, ≤6 bullets/slide
4. **Ban Kiểm Duyệt (quality/):** Slide density check, fact-check, consistency

## Ví dụ 9: Viết White Paper Nghiên Cứu ★
**Input:** "Viết white paper về xu hướng ESG tại Việt Nam 2026"
**Pipeline:** `write-research` → content (deep) → style (technical) → quality (fact-check) → platform
**Output flow:**
1. **Ban Thu Thập (content/):** Deep research ESG VN, source evaluation 5-tier
2. **Ban Biên Tập (style/):** Academic tone + anti-AI burstiness
3. **Ban Kiểm Duyệt (quality/):** Citation verify, source diversity, fact-check
4. **Ban Xuất Bản (platform/):** Format PDF với abstract, ToC, references

## Ví dụ 10: Content Social Đa Nền Tảng ★
**Input:** "Viết 1 bài gốc rồi repurpose sang Facebook, LinkedIn, TikTok, Twitter"
**Pipeline:** `write-social` → content → style (per-platform) → social-worker → quality → platform (multi)
**Output flow:**
1. **Ban Thu Thập (content/):** Research topic, hashtag research trending+niche
2. **Ban Biên Tập (style/):** Bài gốc → adapt per platform (KHÔNG translate)
3. **social-writer-worker:** Platform rules, cross-platform repurposing
4. **Ban Kiểm Duyệt (quality/):** Anti-AI per platform, brand voice consistency

## Ví dụ 11: Viết Tài Liệu Học Tập ★
**Input:** "Tạo handout 2 trang tóm tắt bài học về quản lý rủi ro"
**Pipeline:** `write-edu` → content → style (curriculum) → quality → platform (docs)
**Output flow:**
1. **Ban Thu Thập (content/):** Audience analysis, learning objectives
2. **Ban Biên Tập (style/):** Bloom's mapping, concrete-first approach
3. **edu-worker:** Handout template, engagement layer
4. **Ban Kiểm Duyệt (quality/):** Bloom alignment, VN context check

## Ví dụ 12: Viết Biên Bản Cuộc Họp ★
**Input:** "Viết biên bản cuộc họp dựa trên ghi chú: review sprint, 5 người, có 3 action items"
**Pipeline:** `write-meeting-minutes` → content → style (technical+presentation) → meeting-minutes-worker → quality → platform (docs)
**Output flow:**
1. **Ban Thu Thập (content/):** Trích xuất info từ ghi chú: tên cuộc họp, người, chủ đề, action items
2. **Ban Biên Tập (style/):** Technical writing rõ ràng, presentation hierarchy
3. **meeting-minutes-worker:** Cấu trúc 6 mục chuẩn hành chính VN + bảng action items + ký tên
4. **Ban Kiểm Duyệt (quality/):** Completeness check, consistency tên người, deadline hợp lệ
