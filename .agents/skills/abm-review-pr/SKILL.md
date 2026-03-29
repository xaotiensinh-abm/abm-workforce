---
name: abm-review-pr
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
description: Dual-layer PR review tool (Raven's Verdict). Runs adversarial cynical review and edge case hunter in parallel, merges and deduplicates findings into professional engineering output. Use when user asks to 'review a PR' and provides a PR url or id.
---

# Raven's Verdict - Deep PR Review Tool

A cynical adversarial review, transformed into cold engineering professionalism.

## CRITICAL: Sandboxed Execution Rules

Before proceeding, you MUST verify:

- [ ] PR number or URL was EXPLICITLY provided in the user's message
- [ ] You are NOT inferring the PR from conversation history
- [ ] You are NOT looking at git branches, recent commits, or local state
- [ ] You are NOT guessing or assuming any PR numbers

**If no explicit PR number/URL was provided, STOP immediately and ask:**
"What PR number or URL should I review?"

## 📚 Bách Khoa Toàn Thư (Knowledge Base & SOPs)

> [!TIP]
> File này đã được Đại Phẫu V2 ép chuẩn Kiến Trúc 9-Layer (Lazy-Loading) bởi ABM. Các ví dụ, giới hạn, và quy trình xử lý cồng kềnh đã được rút vứt vào kho dự phòng.
> Để đọc bộ tài liệu đầy đủ cực kỳ quan trọng đó, hãy chạy Tool `view_file` dọc vào đây trước khi bắt tay làm:
> 👉 **/Users/dungtq/ABM-Workforce/.agents/skills/abm-review-pr/references/sop.md**

<!-- 📦 Refactored by ABM Skill Architect v2.0 | Mass-Extraction Token Decoupling -->
