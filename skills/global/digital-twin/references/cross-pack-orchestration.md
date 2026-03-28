# Cross-pack orchestration

Dùng file này khi một case không thể được mô hình hóa tốt chỉ bằng một industry pack hoặc một sub-pack.

## Khi nào cần orchestration
- flow vận hành đi qua nhiều đội hoặc nhiều motion rõ ràng
- một pack mô tả phần đầu funnel nhưng thiếu handoff ở phần sau
- một doanh nghiệp SMEs vừa cần layer ngành, vừa cần layer governance, reporting và decision cadence
- tài liệu nguồn thể hiện nhiều scope có quan hệ chặt nhưng không nên nhét hết vào một pack đơn lẻ

## Cách làm
1. chọn **primary pack** gần business model nhất
2. chọn 1–2 **adjacent packs** bổ sung các phần còn thiếu
3. viết `orchestration-brief.md` để khóa composition goal
4. tạo `orchestration-map.md` mô tả các integration points
5. chỉ lấy cấu trúc, role logic và cadence phù hợp; không copy facts cụ thể từ sample pack
6. nêu rõ `boundary_notes` trong `twin.yaml` nếu pack ghép có phần chồng lấp

## Quy tắc ưu tiên
- primary pack quyết định ngôn ngữ mô hình hóa chính
- adjacent pack chỉ được bổ sung phần thiếu như legal handoff, implant treatment cadence, founder governance, debt-control loop
- nếu có xung đột giữa packs, ưu tiên scope thực từ nguồn người dùng hơn sample pack

## Output nên có khi orchestrate
- `orchestration-brief.md`
- `orchestration-map.md`
- `integration-risks.md`
- `twin.yaml` có `orchestration_system`
