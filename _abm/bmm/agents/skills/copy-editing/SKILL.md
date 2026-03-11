---
name: "copy-editing"
description: "Edit + polish bài viết có sẵn — cải thiện clarity, flow, tone, grammar. Complement cho copywriting (viết mới)."
---

# ✏️ Copy Editing — Biên Tập & Hoàn Thiện

## Sử dụng khi

- Có bài viết draft cần polish
- Cải thiện clarity, readability
- Thống nhất tone of voice
- Review trước khi publish

## KHÔNG sử dụng khi

- Viết từ đầu → dùng `copywriting`
- Content strategy → dùng `content-strategy`
- Review code → dùng `code-review`

## CHECKLIST BIÊN TẬP

### 1. Clarity (Rõ ràng)
- [ ] Mỗi câu chỉ 1 ý
- [ ] Không jargon không cần thiết
- [ ] Active voice > passive voice
- [ ] Cắt bỏ từ thừa (rất, thực sự, cơ bản là)

### 2. Flow (Mạch truyện)
- [ ] Mở bài hook trong 2 câu đầu
- [ ] Transitions tự nhiên giữa paragraphs
- [ ] Kết bài có CTA rõ ràng
- [ ] Đoạn không quá 3-4 câu

### 3. Tone (Giọng văn)
- [ ] Nhất quán từ đầu đến cuối
- [ ] Phù hợp audience
- [ ] Không quá formal hoặc quá casual

### 4. Grammar & Format
- [ ] Không lỗi chính tả
- [ ] Heading hierarchy đúng (H1 → H2 → H3)
- [ ] Lists cho > 3 items
- [ ] Bold cho keywords quan trọng

## OUTPUT FORMAT

```yaml
copy_edit:
  original_word_count: 0
  edited_word_count: 0
  changes_made: 0
  readability_before: "" # grade level
  readability_after: ""
  major_changes:
    - type: "clarity/flow/tone/grammar"
      description: ""
```

## QUY TẮC

1. **Giữ voice tác giả** — edit, không rewrite
2. Track changes cho mọi sửa đổi
3. Readability: Flesch score > 60

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
