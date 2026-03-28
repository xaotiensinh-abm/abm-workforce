---
description: Multi-Agent Content Pipeline với Human-in-the-Loop - Research → Outline → Script → Optimize
---

# Content Pipeline Orchestrator

Workflow tự động tạo content với 4 phases và 3 điểm chạm cho phép user can thiệp.

// turbo-all

---

## Khởi động

Khi user gọi `/content-pipeline`, hỏi:
- **Topic**: Chủ đề content
- **Channel**: Facebook | TikTok | YouTube | Blog | Newsletter
- **Tone**: Casual | Professional | Entertaining

---

## Phase 1: Research (DataCollector Agent)

1. Search web để thu thập data về topic
2. Tổng hợp: statistics, trends, expert quotes
3. Tạo artifact `data_collection.md` trong brain folder

```
Đã thu thập dữ liệu và lưu vào `data_collection.md`.
📍 **ĐIỂM CHẠM 1**: Bạn có thể mở file, thêm tài liệu nội bộ hoặc xóa tin rác.
→ Chat **"Tiếp tục"** khi sẵn sàng.
```

**DỪNG** - Chờ user approve hoặc edit

---

## Phase 2: Structure (OutlineWriter Agent)

1. Đọc `data_collection.md` (bao gồm cả phần user edit nếu có)
2. Xây dựng outline logic: Hook → Main → CTA
3. Tạo artifact `outline.md`

```
Đã tạo dàn ý tại `outline.md`.
📍 **ĐIỂM CHẠM 2**: Kiểm tra logic, thêm/bớt ý nếu cần.
→ Chat **"Tiếp tục"** khi sẵn sàng.
```

**DỪNG** - Chờ user approve hoặc edit

---

## Phase 3: Content Creation (ScriptGenerator Agent)

1. Đọc `outline.md` (đã được user approve/edit)
2. Viết full script theo channel format
3. Tạo artifact `content_{CHANNEL}.md`

```
Đã viết script tại `content_{CHANNEL}.md`.
📍 **ĐIỂM CHẠM 3**: Review văn phong, sửa từ ngữ, thêm drama nếu cần.
→ Chat **"Tiếp tục"** khi sẵn sàng.
```

**DỪNG** - Chờ user approve hoặc edit

---

## Phase 4: Optimization & Finalize (Parallel Agents)

Chạy 3 agents song song:

### 4.1 KeywordExtractor
- Trích xuất primary/secondary keywords
- Đề xuất hashtags tối ưu
- Append vào section `## 🔑 KEYWORDS` trong content file

### 4.2 HookImagePrompter  
- Phân tích content để tạo thumbnail prompts
- Tạo 2-3 options cho visual hook
- Append vào section `## 🖼️ HOOK IMAGE PROMPTS`

### 4.3 QualityChecker
- Verify checklist: hook, flow, CTA, length, tone
- Sign-off section với timestamp
- Append vào section `## ✅ QUALITY CHECK`

---

## Final Approval

```
🎉 **CONTENT HOÀN TẤT!**

📄 File: `content_{CHANNEL}.md`
✅ Keywords: Đã optimize
✅ Thumbnails: Đã có prompts
✅ Quality: Đã QC pass

→ Approve để hoàn tất hoặc yêu cầu chỉnh sửa.
```

---

## Artifacts Location

Tất cả artifacts được lưu tại:
```
{brain_folder}/
├── data_collection.md
├── outline.md
└── content_{CHANNEL}.md
```

---

## User Commands

| Command | Action |
|:---|:---|
| **"Tiếp tục"** | Proceed to next phase |
| **"OK", "Approve"** | Approve và continue |
| **"Làm lại phase X"** | Redo specific phase |
| **"Dừng lại"** | Pause workflow |

---

## Channel-Specific Formats

### Facebook
- Hook: Bold statement + số liệu
- Length: 60-90s video / 150-300 words post
- CTA: Comment + Share driven

### TikTok
- Hook: Pattern interrupt trong 2s đầu
- Length: 15-60s
- CTA: Follow + Stitch/Duet invitation

### YouTube
- Hook: Promise + Curiosity gap
- Length: 8-15 min optimal
- CTA: Subscribe + Like + Comment question

### Blog
- Hook: SEO-optimized H1
- Length: 1500-2500 words
- CTA: Newsletter signup + Related content

---

## Full Skill Reference

Xem chi tiết agents, templates, và architecture tại:
- [SKILL.md](file:///d:/Antigravity/Skill/content-pipeline-orchestrator/SKILL.md)
