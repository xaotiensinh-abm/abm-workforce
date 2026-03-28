# Output Contract: Code Domain

> Áp dụng cho tất cả skill thuộc category `development` (W1:CodeAgent)
> Version: 1.0 | Last Updated: 2026-03-28

---

## Required Sections

Mọi code output PHẢI có:

- [ ] **Working code** — chạy được, không stub hay placeholder
- [ ] **Error handling** — try-catch cho mọi async operation
- [ ] **Input validation** — validate parameters trước khi xử lý
- [ ] **Type safety** — TypeScript strict mode preferred, tránh `any`
- [ ] **Logging** — structured logging thay vì `console.log`
- [ ] **Comments** — giải thích complex logic, WHY chứ không phải WHAT

## Format Standards

| Tiêu chí | Yêu cầu |
|----------|---------|
| Language | TypeScript preferred, JS/Python/Go acceptable |
| Function length | ≤50 lines per function |
| File length | ≤300 lines per file (tách nếu vượt) |
| Naming | camelCase (vars/funcs), PascalCase (types/classes) |
| Constants | UPPER_SNAKE_CASE, no magic numbers |
| Imports | Organized, no unused imports |
| Comments | English cho code comments, Vietnamese acceptable cho user-facing |

## Security Checklist (Hard Constraints)

- [ ] ❌ KHÔNG hard-code API keys, passwords, tokens, secrets
- [ ] ✅ Dùng environment variables cho sensitive data
- [ ] ✅ Sanitize user input trước khi lưu DB
- [ ] ✅ Validate authentication/authorization tại mọi endpoint
- [ ] ❌ KHÔNG dùng `eval()` hoặc dynamic code execution từ user input

## Self-Check Rubric (0-10)

| Dimension | Weight | Mô tả |
|-----------|:------:|-------|
| **Correctness** | 30% | Code chạy đúng theo spec, output khớp expected |
| **Robustness** | 20% | Handle edge cases, error recovery, graceful degradation |
| **Security** | 20% | Không lỗ hổng OWASP Top 10, secrets protected |
| **Readability** | 15% | Code dễ hiểu, maintain, naming rõ ràng |
| **Performance** | 15% | Không O(n²) khi O(n) đủ, không memory leak |

### Grading Scale

| Score | Grade | Action |
|:-----:|:-----:|--------|
| 9-10 | S | Ship it |
| 7-8 | A | Minor polish → ship |
| 5-6 | B | Needs improvement → iterate |
| 3-4 | C | Significant issues → refactor |
| 0-2 | F | Rewrite from scratch |

**Minimum threshold**: Grade B (5/10) hoặc không được ship.

## Testing Requirements

| Complexity | Unit Tests | Integration | E2E |
|:----------:|:----------:|:-----------:|:---:|
| Simple (1-5) | ≥1 test | Optional | No |
| Medium (6-12) | ≥3 tests | ≥1 test | Optional |
| Complex (13-20) | ≥5 tests | ≥2 tests | ≥1 test |
| Enterprise (21+) | Coverage ≥80% | ≥3 tests | ≥2 tests |

## Anti-Patterns (Cái gì KHÔNG chấp nhận)

```
❌ "should work" / "probably fixed" / "seems correct"
   → PHẢI chạy test và show evidence

❌ Code chỉ handle happy path
   → PHẢI có error handling cho edge cases

❌ Copy-paste code (>10 lines duplicate)
   → PHẢI extract shared logic

❌ Hardcoded values giữa code
   → PHẢI extract thành named constants

❌ console.log trong production code
   → PHẢI dùng structured logger
```
