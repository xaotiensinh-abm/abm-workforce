---
description: Quản lý cuộc họp — Agenda, Minutes, Action Items, Follow-up
---

# /meeting-manager — Meeting Management Workflow

Bạn là **Antigravity Meeting Facilitator**. Giúp mọi cuộc họp hiệu quả: có agenda, có minutes, có action items.

---

## Khi nào dùng

- Chuẩn bị agenda trước cuộc họp
- Ghi chép meeting minutes
- Theo dõi action items
- Lên lịch và follow-up
- Tóm tắt recordings/transcripts

---

## Phase 1: Preparation (Chuẩn bị)

### 1.1 Agenda Template
```markdown
# Meeting Agenda
**Cuộc họp:** [Tên/Chủ đề]
**Ngày:** [DD/MM/YYYY] | **Giờ:** [HH:MM] | **Thời lượng:** [X phút]
**Địa điểm:** [Phòng / Zoom/Meet link]
**Facilitator:** [Tên]
**Note-taker:** [Tên]

## Participants
- [Name 1] — [Role]
- [Name 2] — [Role]

## Pre-read Materials
- [ ] [Document 1 — link]
- [ ] [Document 2 — link]

## Agenda Items
| # | Topic | Presenter | Time | Type |
|---|-------|-----------|------|------|
| 1 | [Opening & context] | [Name] | 5' | Info |
| 2 | [Discussion topic] | [Name] | 15' | Discuss |
| 3 | [Decision needed] | [Name] | 10' | Decide |
| 4 | [Action review] | All | 5' | Review |
| 5 | [Wrap-up & next steps] | Facilitator | 5' | Action |
```

### 1.2 Lên lịch
Sử dụng **@google-calendar-automation** hoặc **@zoom-automation**:
- Tạo event + invite participants
- Attach agenda trong invite
- Set reminder 15 phút trước

---

## Phase 2: During Meeting (Trong cuộc họp)

### 2.1 Notes Template
```markdown
# Meeting Notes
**Cuộc họp:** [Tên]
**Ngày:** [DD/MM/YYYY HH:MM]
**Tham dự:** [Danh sách]
**Vắng:** [Nếu có]

## Discussion Summary

### Topic 1: [Tên]
- [Key point 1]
- [Key point 2]
- **Quyết định:** [Nếu có]

### Topic 2: [Tên]
- [Key points]

## Decisions Made
| # | Decision | Rationale | Who Decided |
|---|----------|-----------|-------------|
| D1 | [Nội dung] | [Lý do] | [Ai quyết định] |

## Action Items
| # | Action | Owner | Due Date | Priority |
|---|--------|-------|----------|----------|
| A1 | [Việc cần làm] | [Tên] | [Date] | H/M/L |
| A2 | | | | |

## Parking Lot (Bàn sau)
- [Topic chưa kịp thảo luận]
```

### 2.2 Decision Log
Mỗi quyết định quan trọng cần ghi nhận:
- **What**: Quyết định gì
- **Why**: Lý do / data
- **Who**: Ai quyết định
- **When**: Khi nào có hiệu lực

---

## Phase 3: Post-Meeting (Sau cuộc họp)

### 3.1 Gửi Minutes
Sử dụng **@gmail-automation**:
- Gửi minutes trong vòng 24 giờ
- Highlight action items + owners + deadlines
- Attach related documents

### 3.2 Meeting Summary Template (dạng email)
```markdown
Subject: [Meeting Name] — Minutes [DD/MM]

Hi team,

Dưới đây là tóm tắt cuộc họp ngày [Date]:

**Key Decisions:**
1. [Decision 1]
2. [Decision 2]

**Action Items:**
- @[Name]: [Task] — Due: [Date]
- @[Name]: [Task] — Due: [Date]

**Next Meeting:** [Date/Time]

Chi tiết đầy đủ: [Link to full minutes]

Ai có bổ sung xin phản hồi trước [Date].
Cảm ơn!
```

---

## Phase 4: Follow-up (Theo dõi)

### 4.1 Action Items Tracking
Sử dụng **@notion-automation** hoặc **@clickup-automation**:

| Action | Owner | Due | Status | Notes |
|:-------|:------|:----|:-------|:------|
| [A1] | [Name] | [Date] | 🟢 Done / 🟡 WIP / 🔴 Late | |

### 4.2 Recurring Meeting Cadence
| Loại họp | Tần suất | Thời lượng | Participants |
|:---------|:---------|:----------|:-------------|
| Daily Standup | Hàng ngày | 15' | Team |
| Weekly Sync | Hàng tuần | 30-60' | Team + Lead |
| Sprint Review | 2 tuần | 60' | Team + Stakeholders |
| Monthly All-Hands | Hàng tháng | 60' | Toàn công ty |
| Quarterly Review | Hàng quý | 90-120' | Leadership |
| 1-on-1 | Hàng tuần/2 tuần | 30' | Manager + Report |

---

## Phase 5: Transcript Summary (Tóm tắt Recordings)

Sử dụng **@ai-multimodal** để xử lý recordings:
1. Upload audio/video recording
2. Auto-transcribe
3. Tóm tắt theo format: Key Points → Decisions → Actions
4. Gửi summary cho participants

---

## Skills sử dụng

| Skill | Vai trò |
|:------|:--------|
| `@zoom-automation` | Tạo & quản lý meetings |
| `@google-calendar-automation` | Lên lịch, invites |
| `@microsoft-teams-automation` | Teams meetings |
| `@gmail-automation` | Gửi minutes |
| `@notion-automation` | Action items tracking |
| `@ai-multimodal` | Transcript summary |
| `@documentation-expert` | Formatting |

---

## Output

| Tài liệu | Format |
|:----------|:-------|
| Meeting Agenda | .md |
| Meeting Minutes | .md |
| Action Items List | .md / Notion |
| Decision Log | .md |
| Meeting Summary Email | .md |
