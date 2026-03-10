---
name: "agentic-memory"
description: "Quản lý bộ nhớ dài hạn cho agent — vector DB indexing, semantic search, context retrieval xuyên conversation. Nâng cấp từ flat files."
---

# 🧠 Agentic Memory — Bộ Nhớ Dài Hạn

Nâng cấp Second-Brain từ flat YAML/MD files lên semantic memory có thể search + retrieve.

## Sử dụng khi

- Cần tìm thông tin từ conversations trước
- Project lớn, nhiều context cần persist
- Cần semantic search ("tìm quyết định liên quan API design")
- Knowledge Graph cần enrichment

## KHÔNG sử dụng khi

- Task đơn giản, 1 session → flat files đủ
- Cần lưu trạng thái nhanh → dùng `save`
- Cần tinh chế tri thức → dùng `knowledge-crystallizer`

## ARCHITECTURE

```
                    ┌──────────────┐
                    │   Query      │
                    │  "API design │
                    │   decisions" │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  Embedding   │
                    │   Model      │
                    └──────┬───────┘
                           │
              ┌────────────▼────────────┐
              │     Vector Store        │
              │  (Chroma / Pinecone)    │
              │                         │
              │  ┌─────┐ ┌─────┐       │
              │  │Doc 1│ │Doc 2│ ...   │
              │  └─────┘ └─────┘       │
              └────────────┬────────────┘
                           │
                    ┌──────▼───────┐
                    │  Top-K       │
                    │  Results     │
                    └──────────────┘
```

## IMPLEMENTATION OPTIONS

### Option A: Chroma (Local, Free)

```python
import chromadb

client = chromadb.PersistentClient(path="_abm/Context-Layer/vector-store")
collection = client.get_or_create_collection("abm_memory")

# Index document
collection.add(
    documents=["Sprint 3 quyết định dùng PostgreSQL cho payments"],
    metadatas=[{"type": "decision", "project": "fintech", "date": "2026-03"}],
    ids=["dec-001"]
)

# Search
results = collection.query(query_texts=["database cho payments"], n_results=3)
```

### Option B: Pinecone (Cloud, Scalable)

```python
from pinecone import Pinecone
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index("abm-memory")
```

## DATA PIPELINE

```
1. INGEST — Sau mỗi session/save
   ├── Đọc saves/*.yaml
   ├── Đọc rejected-ideas.yaml
   ├── Đọc council-scoring results
   └── Đọc project-state.yaml

2. CHUNK — Chia nhỏ documents
   └── ~500 tokens/chunk, overlap 50

3. EMBED — Vector hóa
   └── Model: text-embedding-004 / all-MiniLM-L6-v2

4. STORE — Lưu vào vector DB
   └── Metadata: type, project, date, source

5. RETRIEVE — Khi cần
   └── Semantic search → top-K → inject vào context
```

## QUY TẮC

1. **Chỉ index important data**: decisions, patterns, lessons — KHÔNG index raw logs
2. **Metadata đầy đủ**: mọi document phải có type, project, date
3. **Re-index monthly**: cập nhật embeddings khi model thay đổi
4. **Privacy**: KHÔNG index sensitive data (passwords, API keys)

---

## Nguồn gốc
- Wave 2 v3.0: Agentic Memory
