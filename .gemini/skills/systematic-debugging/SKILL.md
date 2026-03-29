---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
version: 1.0.0
author: ABM Skill Architect
last_updated_date: 2026-03-29
---

# Systematic Debugging

## Overview

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Manager wants it fixed NOW (systematic is faster than thrashing)

## Bách Khoa Toàn Thư (Knowledge Base & SOPs)

> [!TIP]
> File này đã được áp dụng phương án Kiến Trúc 9-Layer (Lazy-Loading) của ABM để tối ưu Token.
> Để đọc bộ tài liệu đầy đủ bao gồm 4 Giai đoạn Debug khoa học (The Four Phases), Bảng đối soát rủi ro (Red Flags), và các biện luận thông thường (Common Rationalizations), hãy kích hoạt Tool `view_file` dọc vào đây trước khi bắt tay làm:
> 👉 **/Users/dungtq/ABM-Workforce/.agents/skills/systematic-debugging/references/sop.md**


<!-- 📦 Refactored by ABM Skill Architect v1.0 | ABM Workforce | 9-Layer Token Optimized -->