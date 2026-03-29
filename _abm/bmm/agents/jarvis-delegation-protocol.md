# 📋 Jarvis Delegation Protocol — Lazy Load Module

> **File này CHỈ load khi Jarvis cần ủy quyền task cho worker.**
> Load bằng: `{project-root}/_abm/bmm/agents/jarvis-delegation-protocol.md`

---

## Menu Handlers

```xml
<menu-handlers>
  <handlers>
    <handler type="exec">
      Khi menu item có: exec="path/to/file.md":
      1. Đọc toàn bộ và thực thi file tại đường dẫn đó
      2. Xử lý file hoàn chỉnh và tuân thủ mọi hướng dẫn trong đó
      3. Nếu có data="some/path/data-foo.md" cùng item, truyền đường dẫn data làm context
    </handler>
    <handler type="data">
      Khi menu item có: data="path/to/file.json|yaml|yml|csv|xml"
      Load file trước, parse theo phần mở rộng
      Đặt sẵn như biến {data} cho các handler tiếp theo
    </handler>
    <handler type="workflow">
      Khi menu item có: workflow="path/to/workflow.yaml":
      1. QUAN TRỌNG: LUÔN LOAD {project-root}/_abm/core/tasks/workflow.xml
      2. Đọc toàn bộ file — đây là HỆ ĐIỀU HÀNH LÕI để xử lý ABM workflows
      3. Truyền đường dẫn yaml làm tham số 'workflow-config'
      4. Tuân thủ CHÍNH XÁC mọi bước trong workflow.xml
      5. Lưu output sau TỪNG bước (không gộp nhiều bước)
      6. Nếu workflow.yaml là "todo", thông báo user workflow chưa triển khai
    </handler>
    <handler type="action">
      Khi menu item có: action="#id" → Tìm prompt với id="id" trong XML, thực thi nội dung
      Khi menu item có: action="text" → Thực thi text trực tiếp như hướng dẫn inline
    </handler>
  </handlers>
</menu-handlers>
```

## Delegation Chain Protocol

```xml
<delegation-chain-protocol>
  <forward-delegation>
    <rule>Jarvis (Người giao A/Orchestrator) tạo hợp_đồng_1 với phạm vi, tiêu chí, ngân sách</rule>
    <rule>Worker (Người nhận B) nhận hợp_đồng_1, có thể tạo hợp_đồng_2 cho SubAgent (Người phụ C)</rule>
    <rule>Mỗi cấp ủy quyền có cặp hợp đồng + chứng nhận riêng</rule>
  </forward-delegation>
  <liability-return>
    <rule>Người phụ C trả chứng_nhận_2 cho Worker B</rule>
    <rule>Worker B xác minh, rồi trả chứng_nhận_1 cho Jarvis</rule>
    <rule>Jarvis xác minh tất cả chứng nhận, tổng hợp output cuối cho CEO</rule>
    <rule>Trách nhiệm LUÔN đi lên: C → B → Jarvis → CEO</rule>
  </liability-return>
</delegation-chain-protocol>
```

## Task Logging Format

```xml
<task-logging>
  <rule>Sau MỖI hợp đồng hoàn tất, ghi thêm mục vào {output_folder}/task-log.yaml</rule>
  <entry-format>
    - task_id: "{task_id}"
      timestamp: "{date}"
      type: "{task_type}"
      worker: "{executor_agent}"
      status: "{attestation_status}"
      confidence: {confidence}
      files_changed: {count}
      retries: {retries_used}
      human_gate: {required}
      risk_level: "{risk_level}"
  </entry-format>
</task-logging>
```

## Delegation Dashboard Prompt

```xml
<prompt id="delegation-dashboard">
  ## 🧠 Bảng Điều Phối Jarvis

  ### Hợp Đồng Đang Chạy
  | Mã Task | Worker | Trạng thái | Độ tin cậy |
  |---------|--------|------------|------------|
  | (chưa có hợp đồng) | — | — | — |

  ### Chứng Nhận Đang Chờ
  | Mã Task | Worker | Dự kiến | Quá hạn |
  |---------|--------|---------|--------|
  | (chưa có) | — | — | — |

  ### Hàng Đợi Xác Minh
  | Mã Task | Loại | Bằng chứng | Quyết định |
  |---------|------|-----------|------------|
  | (trống) | — | — | — |
</prompt>
```
