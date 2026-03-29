---
name: "form-cro"
description: "Tối ưu lead capture forms — field optimization, multi-step, conditional logic."
---

# 📋 Form CRO — Tối Ưu Biểu Mẫu

## Sử dụng khi

- Lead capture form conversion thấp
- Form quá dài → user bỏ ngang
- Cần thiết kế multi-step form
- Optimize existing forms

## KHÔNG sử dụng khi

- Signup flow toàn bộ → dùng `signup-flow-cro`
- Landing page → dùng `page-cro`
- Popup → dùng `popup-cro`

## NGUYÊN TẮC

```
Ít fields hơn = nhiều conversions hơn

3 fields: ~25% conversion
5 fields: ~20% conversion  
7 fields: ~15% conversion
10+ fields: ~10% conversion
```

## CHECKLIST

### Field Optimization
- [ ] Chỉ fields BẮT BUỘC cho bước tiếp theo
- [ ] Email + 1 field max cho giai đoạn đầu
- [ ] Progressive profiling (hỏi thêm sau)
- [ ] Dropdown thay vì text input khi có thể
- [ ] Auto-detect (country từ IP, phone format)

### Multi-Step Form
```
Step 1: Câu hỏi dễ (chọn mục đích) — commitment thấp
Step 2: Thông tin cơ bản — đã invest effort
Step 3: Contact info — sunk cost effect
```

### UX Best Practices
- [ ] Labels trên field (không inside placeholder)
- [ ] Error messages cụ thể (không "Invalid input")
- [ ] Tab order đúng
- [ ] Submit button CTA rõ ("Nhận báo giá" > "Submit")
- [ ] Thank you page có next step

## QUY TẮC

1. Test 3 vs 5 fields trước
2. Multi-step > single long form
3. Mobile: 1 cột, input type đúng

---

## Nguồn gốc
- Repo: coreyhaines31/marketingskills
