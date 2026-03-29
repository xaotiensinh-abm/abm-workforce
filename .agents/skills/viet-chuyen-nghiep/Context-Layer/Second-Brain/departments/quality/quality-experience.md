# Bộ nhớ Kinh nghiệm: Ban Chất lượng

## AI-Smell Phrases (Vietnamese)

### NGAY LẬP TỨC flag (severity: high)
```
"Trong thế giới ngày nay"
"Với sự phát triển không ngừng"  
"Đây thực sự là một bước ngoặt"
"Không thể phủ nhận rằng"
"Hơn bao giờ hết"
"Hy vọng bài viết hữu ích cho bạn"
"Bạn có bao giờ tự hỏi" (mở bài default)
"Hãy bắt đầu ngay hôm nay!"
```

### Flag khi xuất hiện ≥ 3 lần (severity: medium)
```
"Hơn nữa" / "Bên cạnh đó" / "Ngoài ra"
"Đặc biệt" / "Quan trọng hơn" / "Đáng nói"
"Vô cùng" / "Cực kỳ" / "Thực sự"
"Nhìn chung" / "Nói chung" / "Trên thực tế"
```

### Flag về structure (severity: medium)
```
Mọi section đều 3 bullets
Mọi paragraph đều 4 câu  
Heading pattern lặp (VD: "Lợi ích 1", "Lợi ích 2", "Lợi ích 3")
Mở bài + kết bài dùng cùng sentence
```

## Mẫu Sửa Tiếng Việt Tự nhiên

| AI version | Human version |
|-----------|--------------|
| "Vô cùng quan trọng" | "Quan trọng vì [lý do]" |
| "Trong bối cảnh hiện nay" | [Bỏ, vào thẳng ý] |
| "Được biết đến như là" | "[X] nổi tiếng vì" |
| "Có thể nói rằng" | [Nói luôn] |
| "Một cách hiệu quả" | "[Cụ thể thế nào]" |
| "Đáng chú ý là" | "[Fact trực tiếp]" |

## Last-Mile Mistakes (kinh nghiệm thực tế)

1. **Quên unresolved risks** → luôn list ở cuối output
2. **Anti-AI fix tạo lỗi mới** → re-scan SAU mỗi lần fix
3. **Disclaimer quá cứng** → viết tự nhiên, không legal footer
4. **Consistency miss ở cuối bài** → người viết hay sloppy cuối bài
5. **Format shift** → markdown heading bị nhảy level
