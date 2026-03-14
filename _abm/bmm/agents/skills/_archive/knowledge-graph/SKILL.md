---
name: "knowledge-graph"
description: "Xây dựng Knowledge Graph cho project — entities, relationships, reasoning. Tích hợp cognee hoặc graph DB. Nâng cấp từ flat KB lên linked knowledge."
---

# 🕸️ Knowledge Graph — Đồ Thị Tri Thức

Xây dựng và quản lý Knowledge Graph để liên kết tri thức, phát hiện patterns, hỗ trợ reasoning.

## Sử dụng khi

- Project phức tạp cần track relationships giữa entities
- Cần phát hiện hidden connections trong dữ liệu
- Xây dựng ontology cho domain cụ thể
- Tích hợp cognee hoặc graph database

## KHÔNG sử dụng khi

- Cần phân tích số liệu → dùng `data-analysis`
- Cần lưu tri thức đơn giản → dùng `knowledge-crystallizer`
- Project nhỏ, ít entities → không cần graph

## CÁCH XÂY DỰNG

### 1. Xác định Entities (Nodes)

```
Entities = đối tượng chính trong domain

Ví dụ project SaaS:
- User, Organization, Subscription
- Feature, Module, API
- Bug, Task, Sprint
```

### 2. Xác định Relationships (Edges)

```
Relationships = mối quan hệ giữa entities

- User BELONGS_TO Organization
- User HAS Subscription
- Feature REQUIRES API
- Bug AFFECTS Module
- Task PART_OF Sprint
```

### 3. Properties (Thuộc tính)

```
Mỗi entity + relationship có properties:
- User: {name, role, created_at}
- BELONGS_TO: {since, role_in_org}
```

## TÍCH HỢP COGNEE

```python
# Setup cognee (Python)
import cognee

# Add data sources
await cognee.add("project_docs/", "project_knowledge")

# Build knowledge graph
await cognee.cognify()

# Query
results = await cognee.search(
    "Những features nào phụ thuộc vào User entity?"
)
```

## YAML EXPORT FORMAT

```yaml
knowledge_graph:
  entities:
    - id: "user"
      type: "Entity"
      properties:
        domain: "authentication"
    - id: "subscription"
      type: "Entity"
      properties:
        domain: "billing"

  relationships:
    - from: "user"
      to: "subscription"
      type: "HAS"
      properties:
        cardinality: "1:N"
```

## QUY TẮC SẮT

1. **Entities phải có ID duy nhất** — không duplicate
2. **Relationships phải có direction** — A → B khác B → A
3. **Cập nhật graph** khi domain model thay đổi
4. **Export YAML** sau mỗi milestone để lưu vào Second-Brain

---

## Nguồn gốc
- BMAD feedback điểm 5: Knowledge Graph + cognee
- ABM Workforce v2.6
