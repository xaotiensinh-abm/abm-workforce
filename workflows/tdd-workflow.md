---
description: Test-Driven Development - viết test trước, code sau
---

Workflow TDD: Write test → Watch fail → Write minimal code → Pass → Refactor.

---

## The Iron Law

```
KHÔNG VIẾT CODE TRƯỚC KHI CÓ FAILING TEST
```

Viết code trước test? **Delete nó. Bắt đầu lại.**

---

## Red-Green-Refactor Cycle

### 1. RED - Write Failing Test

```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };

  const result = await retryOperation(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```

**Requirements:**
- One behavior
- Clear name
- Real code (no mocks unless unavoidable)

### 2. Verify RED - Watch It Fail

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test **fails** (not errors)
- Failure message là expected
- Fails vì feature missing (không phải typos)

### 3. GREEN - Minimal Code

```typescript
async function retryOperation<T>(fn: () => Promise<T>): Promise<T> {
  for (let i = 0; i < 3; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === 2) throw e;
    }
  }
  throw new Error('unreachable');
}
```

**Chỉ viết đủ code để pass.** Không thêm features.

### 4. Verify GREEN

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test passes
- Other tests still pass

### 5. REFACTOR

Sau green:
- Remove duplication
- Improve names
- Extract helpers

**Keep tests green. Don't add behavior.**

---

## Khi nào dùng TDD

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (hỏi human partner):**
- Throwaway prototypes
- Generated code
- Config files

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30s. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "TDD slows me down" | TDD faster than debugging. |

---

## Red Flags - STOP & Start Over

- Code before test
- Test passes immediately
- Can't explain why test failed
- "I already manually tested it"
- "Just this once"

---

## Bug Fix Example

**Bug:** Empty email accepted

**RED:**
```typescript
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});
```

**Verify RED:** `FAIL: expected 'Email required', got undefined`

**GREEN:**
```typescript
function submitForm(data: FormData) {
  if (!data.email?.trim()) {
    return { error: 'Email required' };
  }
  // ...
}
```

**Verify GREEN:** `PASS`

---

## Verification Checklist

- [ ] Every new function has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason
- [ ] Wrote minimal code to pass
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
