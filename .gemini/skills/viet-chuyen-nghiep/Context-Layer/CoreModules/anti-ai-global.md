# Anti-AI Global — Phát hiện & xử lý văn phong AI

## Mục đích

Skill phải tạo output **nghe như người viết**, không nghe như máy.
File này liệt kê patterns "mùi AI" phổ biến trong tiếng Việt và cách sửa.

## Red flags — Patterns cần phát hiện và sửa

### 1. Mở bài sáo rỗng
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| "Trong thế giới ngày nay..." | Bỏ, vào thẳng ý chính |
| "Với sự phát triển không ngừng của..." | Bắt đầu bằng fact cụ thể hoặc câu hỏi |
| "Bạn có bao giờ tự hỏi..." | Chỉ dùng khi thật sự relevant, tránh dùng mặc định |
| "[Chủ đề] đang trở thành xu hướng..." | Nêu data cụ thể hoặc anecdote |

### 2. Từ nối lặp
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| "Hơn nữa" + "Bên cạnh đó" + "Ngoài ra" liên tục | Đa dạng: "Điểm đáng chú ý khác...", bỏ từ nối |
| "Đặc biệt" + "Quan trọng hơn" + "Đáng nói" | Dùng tối đa 1 lần mỗi loại |
| "Thứ nhất... Thứ hai... Thứ ba..." | Dùng bullets hoặc heading |

### 3. Kết bài khuôn mẫu
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| "Tóm lại, [lặp lại mở bài]" | Viết kết mới: gợi mở, call to action, hoặc quote |
| "Hy vọng bài viết hữu ích cho bạn" | Bỏ hoặc thay bằng CTA cụ thể |
| "Hãy bắt đầu ngay hôm nay!" | Chỉ dùng khi thật sự muốn CTA |

### 4. Từ hoa mỹ quá mức
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| "Vô cùng quan trọng" | "Quan trọng vì [lý do cụ thể]" |
| "Thực sự ấn tượng" | "[Cụ thể gì] ấn tượng" |
| "Cực kỳ hiệu quả" | "Hiệu quả: [số liệu hoặc ví dụ]" |
| "Đáng kinh ngạc" | Mô tả cụ thể thay vì cảm thán |

### 5. Cấu trúc đều tăm tắp
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| Mọi section đều 3 bullets | Đa dạng: 2, 4, 5 bullets tùy nội dung |
| Mọi paragraph đều 4 câu | Xen kẽ paragraph ngắn/dài |
| Mọi heading đều cùng pattern | Đa dạng dạng heading |

### 6. Passive voice tiếng Việt
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| "Được biết đến như là..." | "[Chủ thể] nổi tiếng vì..." |
| "Đã được chứng minh rằng..." | "Nghiên cứu [X] cho thấy..." |
| "Được coi là..." | "[Ai] coi [cái gì] là..." |

### 7. Filler phrases
| ❌ Pattern | ✅ Cách sửa |
|-----------|-----------|
| "Nhìn chung", "Nói chung" | Bỏ, vào thẳng ý |
| "Có thể nói rằng" | Nói luôn |
| "Trên thực tế" | Bỏ hoặc thay bằng evidence |
| "Không thể phủ nhận rằng" | Nêu fact trực tiếp |

## Chấm điểm

Anti-AI score:
- **0-20:** Rất tự nhiên — gần như người viết 100%
- **21-40:** Tự nhiên — chấp nhận được
- **41-60:** Có dấu hiệu AI — cần sửa
- **61-80:** Rõ AI — phải rewrite
- **81-100:** Hoàn toàn AI — không chấp nhận

Target: output phải ≤ 40.

## Quy trình sửa

1. **Scan** — đọc toàn bài, đánh dấu patterns
2. **Score** — ước lượng AI score
3. **Rewrite** — sửa từng pattern, ưu tiên mở bài + kết bài
4. **Rescan** — verify score giảm
5. **Repeat** — cho đến khi ≤ 40
