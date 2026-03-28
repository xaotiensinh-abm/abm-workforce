---
description: Hướng dẫn xây dựng MCP Server để LLM tương tác với external services
---

Workflow tạo MCP (Model Context Protocol) Server chất lượng cao cho Python hoặc Node/TypeScript.

---

## Tổng quan

MCP Server cung cấp tools cho LLMs truy cập external services và APIs. Chất lượng được đo bằng khả năng LLM hoàn thành real-world tasks.

---

## Phase 1: Research & Planning

### 1.1 Agent-Centric Design Principles

- **Build for Workflows**: Không chỉ wrap API endpoints - tạo workflow tools
- **Optimize for Limited Context**: Return high-signal info, không data dumps
- **Actionable Error Messages**: Hướng dẫn agent sửa lỗi
- **Natural Task Subdivisions**: Tool names reflect human thinking

### 1.2 Study Documentation

// turbo
Fetch MCP Protocol documentation:
```
WebFetch: https://modelcontextprotocol.io/llms-full.txt
```

Load reference files từ `D:\Antigravity\Skill\claude-skills\mcp-builder\reference\`:
- `mcp_best_practices.md`
- `python_mcp_server.md` (Python)
- `node_mcp_server.md` (TypeScript)

### 1.3 API Documentation

Đọc **TẤT CẢ** API documentation:
- Official API reference
- Authentication requirements
- Rate limiting, pagination
- Error responses, data models

---

## Phase 2: Implementation

### 2.1 Project Structure

**Python:**
- Single `.py` file hoặc modules nếu complex
- MCP Python SDK, Pydantic models

**TypeScript:**
- `package.json`, `tsconfig.json`
- MCP TypeScript SDK, Zod schemas

### 2.2 Core Infrastructure First

Tạo shared utilities trước tools:
- API request helpers
- Error handling utilities
- Response formatting (JSON/Markdown)
- Pagination helpers
- Authentication management

### 2.3 Implement Tools

**Input Schema:**
```python
# Python - Pydantic
class SearchInput(BaseModel):
    query: str = Field(..., min_length=1, max_length=100, description="Search query")
```

```typescript
// TypeScript - Zod
const SearchInput = z.object({
    query: z.string().min(1).max(100).describe("Search query")
}).strict();
```

**Tool Annotations:**
- `readOnlyHint`: true (read-only ops)
- `destructiveHint`: false (non-destructive)
- `idempotentHint`: true (repeated calls = same effect)

---

## Phase 3: Review & Refine

### Quality Checklist

- [ ] **DRY**: No duplicated code
- [ ] **Composability**: Shared logic extracted
- [ ] **Consistency**: Similar ops return similar formats
- [ ] **Error Handling**: All external calls handled
- [ ] **Type Safety**: Full type coverage
- [ ] **Documentation**: Comprehensive docstrings

### Testing

**Important**: MCP servers là long-running processes. KHÔNG chạy trực tiếp.

Safe testing:
- Sử dụng evaluation harness
- Run server trong tmux
- Dùng timeout: `timeout 5s python server.py`

---

## Phase 4: Create Evaluations

Tạo 10 evaluation questions:

```xml
<evaluation>
  <qa_pair>
    <question>Complex, realistic question requiring multiple tool calls</question>
    <answer>Single, verifiable answer</answer>
  </qa_pair>
</evaluation>
```

Requirements:
- Independent, Read-only, Complex, Realistic
- Verifiable by string comparison
- Stable (answer won't change over time)
