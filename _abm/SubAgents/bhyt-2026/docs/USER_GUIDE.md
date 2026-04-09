# 📖 HƯỚNG DẪN SỬ DỤNG: PHÒNG BAN AI "GIẢI PHÁP KD BH Y TẾ 2026"

> **Phiên bản:** 1.0 | **Ngày:** 05/04/2026
> **Đối tượng:** CEO, Ban TGĐ, Lãnh đạo cấp cao sử dụng hệ thống AI
> **Yêu cầu:** Truy cập vào Antigravity IDE hoặc bất kỳ IDE tích hợp Jarvis Orchestrator

---

## MỤC LỤC

1. [Giới thiệu tổng quan](#1-giới-thiệu-tổng-quan)
2. [Kiến trúc hệ thống — Ai làm gì?](#2-kiến-trúc-hệ-thống--ai-làm-gì)
3. [Bắt đầu nhanh trong 2 phút](#3-bắt-đầu-nhanh-trong-2-phút)
4. [Cách giao việc — 4 phương thức](#4-cách-giao-việc--4-phương-thức)
5. [Thư viện câu lệnh mẫu — 30+ kịch bản thực chiến](#5-thư-viện-câu-lệnh-mẫu--30-kịch-bản-thực-chiến)
6. [Cách đọc kết quả AI trả về](#6-cách-đọc-kết-quả-ai-trả-về)
7. [Nạp dữ liệu — Khi nào cần, khi nào không](#7-nạp-dữ-liệu--khi-nào-cần-khi-nào-không)
8. [Cơ chế phản biện chéo — Vũ khí bí mật](#8-cơ-chế-phản-biện-chéo--vũ-khí-bí-mật)
9. [Xử lý tình huống thường gặp (FAQ)](#9-xử-lý-tình-huống-thường-gặp-faq)
10. [Quy ước an toàn & giới hạn](#10-quy-ước-an-toàn--giới-hạn)

---

## 1. GIỚI THIỆU TỔNG QUAN

### Phòng ban BHYT 2026 là gì?

Đây là một **phòng ban ảo hoàn toàn tự trị**, vận hành bởi 7 Chuyên gia AI chuyên biệt và 1 Trưởng phòng AI. Thay vì thuê thêm hàng chục chuyên viên actuarial, phân tích tài chính, marketing — CEO chỉ cần **gõ lệnh bằng tiếng Việt** và nhận về bản phân tích/tư vấn cấp C-level trong vài phút.

### Phòng ban này giải quyết những bài toán nào?

| Bài toán kinh doanh | Ví dụ câu hỏi CEO có thể đặt ra |
|:---|:---|
| Tăng trưởng doanh thu | *"Làm sao tăng DT BHYT 15% mà không phá giá?"* |
| Kiểm soát bồi thường | *"Tại sao Loss Ratio An Gia quý 1 lên 85%?"* |
| Ra mắt sản phẩm mới | *"Thiết kế gói BH cho Freelancer dưới 35 tuổi"* |
| Tối ưu kênh bán hàng | *"So sánh hiệu quả Bancassurance vs Đại lý truyền thống"* |
| Hỗ trợ công ty thành viên | *"CTTV nào đang lỗ nặng nhất? Turnaround Plan?"* |
| Cắt giảm chi phí | *"Chi phí TPA đang chiếm bao nhiêu % expense ratio?"* |
| Trải nghiệm khách hàng | *"NPS đang bao nhiêu? Khách hàng phàn nàn gì nhiều nhất?"* |

### Nguyên tắc vàng khi sử dụng

> **Hãy ra lệnh như bạn đang nói chuyện với Trưởng phòng giỏi nhất công ty.**
> Càng cụ thể yêu cầu → Càng sắc bén kết quả.

---

## 2. KIẾN TRÚC HỆ THỐNG — AI LÀM GÌ?

Hệ thống gồm **1 Trưởng phòng + 7 Chuyên gia**, tổ chức như một phòng ban thực tế:

```
                    ┌───────────────────┐
                    │    CEO / BAN TGĐ  │
                    └────────┬──────────┘
                             │ Giao việc
                    ┌────────▼──────────┐
                    │  JARVIS           │
                    │  (Tổng điều phối) │
                    └────────┬──────────┘
                             │
                    ┌────────▼──────────┐
                    │  📋 TRƯỞNG PHÒNG  │
                    │  Điều phối 7 Agent│
                    │  Tổng hợp báo cáo │
                    └────────┬──────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
    ┌─────▼─────┐     ┌─────▼─────┐     ┌─────▼─────┐
    │ KHỐI TĂNG │     │ KHỐI PHÒNG│     │ KHỐI KIẾN │
    │ TRƯỞNG    │     │ THỦ       │     │ TẠO       │
    ├───────────┤     ├───────────┤     ├───────────┤
    │🚀 Agent 1 │     │💰 Agent 2 │     │🧪 Agent 3 │
    │Doanh thu  │     │Loss Ratio │     │Sản phẩm   │
    │           │     │           │     │           │
    │🌐 Agent 4 │     │📊 Agent 6 │     │🎯 Agent 7 │
    │Kênh PP    │     │Expense R. │     │Trải nghiệm│
    │           │     │           │     │           │
    │🏗️ Agent 5 │     │           │     │           │
    │CTTV       │     │           │     │           │
    └───────────┘     └───────────┘     └───────────┘
```

### Chi tiết từng Agent

#### 🚀 Agent 1: Revenue Growth Strategist (Chiến lược gia Doanh thu)
- **Nhiệm vụ:** Tìm cách tăng doanh thu BHYT ≥ 10%/năm
- **Chuyên môn:** Phân tích thị trường, chiến lược giá, cross-sell, upsell, giảm churn
- **Khi nào gọi:** Khi cần tăng doanh thu, phân tích cạnh tranh, tìm thị trường mới
- **Framework:** GAPC (Growth – Acquisition – Portfolio – Competition)

#### 💰 Agent 2: Combined Ratio Optimizer (Tối ưu Bồi thường)
- **Nhiệm vụ:** Kiểm soát Loss Ratio (Tỷ lệ bồi thường) ≤ 65%
- **Chuyên môn:** Underwriting, phát hiện gian lận, quản lý claims, tái bảo hiểm, IBNR
- **Khi nào gọi:** Khi bồi thường tăng vọt, cần siết chính sách bồi thường, đàm phán tái BH
- **Framework:** CRACK (Claims – Risk – Actuarial – Control – Knowledge)
- **⚠️ Lưu ý:** Agent này CHỈ phụ trách Loss Ratio. Expense Ratio thuộc Agent 6.

#### 🧪 Agent 3: Product Innovation Architect (Kiến trúc sư Sản phẩm)
- **Nhiệm vụ:** Thiết kế sản phẩm BHYT mới, cải tiến sản phẩm hiện hữu
- **Chuyên môn:** Product design, pricing, rider, wording, market-fit analysis
- **Khi nào gọi:** Khi cần ra sản phẩm mới, cải tiến An Gia/Intercare, thiết kế gói SME/Micro
- **Framework:** BRIDGE (Benchmark – Research – Innovate – Design – Go-to-market – Evaluate)

#### 🌐 Agent 4: Distribution Channel Developer (Phát triển Kênh Phân Phối)
- **Nhiệm vụ:** Mở rộng và tối ưu 6 kênh phân phối
- **Chuyên môn:** Bancassurance, broker, agency, pool, digital, cross-sell
- **Khi nào gọi:** Khi cần mở kênh mới, đánh giá hiệu suất kênh, thiết kế chính sách hoa hồng
- **Framework:** REACH (Revenue-per-channel – Efficiency – Acquisition – Channel-mix – Harmonize)

#### 🏗️ Agent 5: Subsidiary Growth Advisor (Cố vấn Công ty Thành viên)
- **Nhiệm vụ:** Hỗ trợ ~80 CTTV phát triển mảng BHYT
- **Chuyên môn:** Phân tích P&L theo CTTV, Turnaround Plan, đào tạo, KPI theo vùng
- **Khi nào gọi:** Khi cần xếp hạng CTTV, lập kế hoạch cứu CTTV đang lỗ, phân bổ target
- **Framework:** TIER (Territory – Investigate – Elevate – Review)

#### 📊 Agent 6: Cost Impact Analyst (Phân tích Chi phí)
- **Nhiệm vụ:** Kiểm soát Expense Ratio (Tỷ lệ chi phí) ≤ 35%
- **Chuyên môn:** Hoa hồng, TPA fee, chi phí marketing, admin, IT & vận hành
- **Khi nào gọi:** Khi cần rà soát cấu trúc chi phí, so sánh chi phí giữa các kênh, cắt giảm
- **Framework:** COST (Categorize – Optimize – Standardize – Track)
- **⚠️ Lưu ý:** Agent này CHỈ phụ trách Expense Ratio. Loss Ratio thuộc Agent 2.

#### 🎯 Agent 7: Customer Experience Guardian (Bảo vệ Trải nghiệm KH)
- **Nhiệm vụ:** Bảo vệ tiếng nói khách hàng, đảm bảo NPS ≥ 45
- **Chuyên môn:** NPS, CSAT, thời gian xử lý bồi thường (TAT), khiếu nại, retention
- **Khi nào gọi:** Khi cần đánh giá tác động CX của quyết định kinh doanh, phân tích khiếu nại
- **Framework:** CARE (Capture – Analyze – Respond – Elevate)
- **⚡ Đặc quyền:** Agent 7 có **quyền phủ quyết CX** — nếu bất kỳ giải pháp nào của 6 Agent kia gây hại nghiêm trọng cho khách hàng, Agent 7 sẽ cảnh báo đỏ.

---

## 3. BẮT ĐẦU NHANH TRONG 2 PHÚT

### Bước 1: Mở Antigravity IDE (hoặc terminal có kết nối Jarvis)

### Bước 2: Gõ lệnh đầu tiên

Cách đơn giản nhất — chỉ cần gõ câu hỏi tiếng Việt có chứa từ khóa liên quan BHYT:

```
Phân tích hiệu quả nghiệp vụ bảo hiểm y tế năm 2025, 
đánh giá Combined Ratio và đề xuất giải pháp cải thiện cho 2026.
```

Hệ thống sẽ **tự động nhận diện** đây là bài toán của phòng BHYT 2026 và kích hoạt các Agent phù hợp.

### Bước 3: Đọc kết quả

AI sẽ trả về một bản báo cáo chuẩn C-level gồm:
- Tóm tắt điều hành (≤ 200 từ)
- Phân tích số liệu
- Đề xuất giải pháp có KPI + Timeline
- Cảnh báo rủi ro (nếu có)

### Bước 4: Ra lệnh tiếp (nếu cần đào sâu)

```
Đào sâu vào Loss Ratio — tỉnh nào đang bồi thường cao nhất?
```

Hệ thống sẽ tự động gọi Agent 2 để phân tích chi tiết.

---

## 4. CÁCH GIAO VIỆC — 4 PHƯƠNG THỨC

### Phương thức 1: Giao qua Jarvis (Khuyến nghị — Toàn diện nhất)

```
/jarvis Giao việc cho phòng BHYT 2026: [Mô tả yêu cầu chi tiết]
```

**Ưu điểm:** Jarvis sẽ phân tích yêu cầu, giao cho đúng Agent, thu thập kết quả và tổng hợp. Phù hợp cho các bài toán phức tạp cần phối hợp nhiều Agent.

**Ví dụ:**
```
/jarvis Giao việc cho phòng BHYT 2026: Phân tích nguyên nhân Combined Ratio 
tăng từ 95% lên 105% trong quý 1/2026. Tách riêng Loss Ratio và Expense Ratio.
Đề xuất 3 kịch bản cắt giảm: thận trọng, trung bình, mạnh tay. 
Mỗi kịch bản phải đánh giá tác động lên khách hàng.
```

### Phương thức 2: Gõ trực tiếp bằng từ khóa (Nhanh — Tự động nhận diện)

Chỉ cần gõ câu hỏi có chứa **từ khóa kích hoạt**, hệ thống tự nhận diện:

**Danh sách từ khóa kích hoạt:**
- `BHYT`, `bảo hiểm y tế`, `bảo hiểm sức khỏe`
- `An Gia`, `Intercare`, `Tâm Bình`
- `combined ratio`, `loss ratio`, `expense ratio`
- `doanh thu BHYT`, `kênh phân phối BH`
- `công ty thành viên`, `chi phí nghiệp vụ`
- `NPS bảo hiểm`, `bồi thường sức khỏe`

**Ví dụ:** (chỉ cần gõ)
```
So sánh Loss Ratio của An Gia với Intercare năm 2025
```

### Phương thức 3: Gọi đích danh Agent (Khi biết rõ cần ai)

```
Agent Revenue Growth: Phân tích 5 tệp khách hàng tiềm năng chưa được khai thác
Agent Cost Analyst: Rà soát toàn bộ chi phí TPA quý 1/2026
Agent CX Guardian: Đánh giá tác động NPS nếu tăng mức khấu trừ An Gia lên 500K
```

### Phương thức 4: Nạp file dữ liệu + câu lệnh (Khi có data thực tế)

```
@[đường_dẫn_file.xlsx] Phân tích file HQNV này, chỉ ra CTTV nào đang lỗ 
và đề xuất Turnaround Plan 90 ngày.
```

**Định dạng file hỗ trợ:** `.xlsx`, `.csv`, `.pdf`, `.md`

---

## 5. THƯ VIỆN CÂU LỆNH MẪU — 30+ KỊCH BẢN THỰC CHIẾN

### 📈 Nhóm Tăng Trưởng Doanh Thu (Agent 1)

```
1. "Phân tích thị trường BHYT Việt Nam 2026, xác định 3 phân khúc tăng trưởng 
    nhanh nhất mà Bảo Việt chưa thâm nhập đủ sâu."

2. "Xây dựng chiến lược cross-sell BHYT cho tệp khách hàng hiện hữu 
    của BV Nhân thọ và BaoViet Bank."

3. "Tỷ lệ tái tục hợp đồng BHYT cá nhân đang là 78%. 
    Đề xuất 5 giải pháp nâng lên 85%."

4. "Phân tích chiến lược pricing của PVI, Bảo Minh, PTI cho sản phẩm 
    BHYT doanh nghiệp. So sánh với Bảo Việt."

5. "Thiết kế chương trình khuyến mãi Q3/2026 cho sản phẩm An Gia, 
    mục tiêu tăng 20% hợp đồng mới."
```

### 💰 Nhóm Kiểm Soát Rủi Ro — Loss Ratio (Agent 2)

```
6. "Loss Ratio quý 1 tăng từ 62% lên 72%. Phân tích nguyên nhân gốc rễ: 
    do frequency tăng hay severity tăng? Tỉnh/sản phẩm nào đóng góp nhiều nhất?"

7. "Lập danh sách 10 bệnh viện/phòng khám có chi phí bồi thường trung bình 
    cao nhất hệ thống. Đề xuất hành động cụ thể cho từng cơ sở."

8. "Đánh giá hiệu quả chương trình chống trục lợi bảo hiểm năm 2025. 
    Bao nhiêu vụ phát hiện? Tiết kiệm bao nhiêu?"

9. "Phân tích IBNR (phát sinh chưa báo cáo) mảng BHYT. 
    Dự phòng bồi thường hiện tại đã đủ chưa?"

10. "Đàm phán lại Hiệp ước tái bảo hiểm: Bảo Việt nên nâng mức giữ lại 
     (Net Retention) lên bao nhiêu? Phân tích chi phí vs lợi ích."
```

### 🧪 Nhóm Sản Phẩm (Agent 3)

```
11. "Thiết kế gói BHYT cho đối tượng Freelancer/Gig Worker (25-35 tuổi). 
     Yêu cầu: phí thấp, linh hoạt, thanh toán tháng, bán online."

12. "Phân tích hiệu quả kinh doanh từng gói An Gia (Đồng/Bạc/Vàng/BK/KC). 
     Gói nào đang 'hút máu' bồi thường? Đề xuất điều chỉnh."

13. "Thiết kế sản phẩm BHYT bổ sung cho du học sinh — 
     phạm vi toàn cầu, tuân thủ yêu cầu visa, giá cạnh tranh."

14. "Đánh giá có nên ngừng bán gói An Gia Đồng (phí thấp, LR cao) hay 
     redesign quyền lợi. Phân tích 3 kịch bản."

15. "Thiết kế gói Micro-Insurance BHYT: phí 500K/năm, quyền lợi cơ bản, 
     target thu nhập thấp, bán qua Momo/ZaloPay."
```

### 🌐 Nhóm Kênh Phân Phối (Agent 4)

```
16. "So sánh ROI (doanh thu/chi phí) giữa 6 kênh phân phối BHYT. 
     Kênh nào hiệu quả nhất? Kênh nào đang đốt tiền?"

17. "Xây dựng kế hoạch đẩy mạnh Bancassurance BHYT qua BaoViet Bank. 
     Script bán hàng, KPI nhân viên ngân hàng, incentive."

18. "Đánh giá cơ hội phân phối BHYT qua ví điện tử (Momo, ZaloPay, VNPay). 
     Mô hình hợp tác và chia sẻ doanh thu."

19. "Thiết kế chính sách hoa hồng mới cho kênh Broker 2026. 
     Benchmark với PVI và Bảo Minh."

20. "Phân tích hiệu quả kênh Pool/Captive (Allianz, Asahi). 
     Nên mở rộng hay thu hẹp?"
```

### 🏗️ Nhóm Công Ty Thành Viên (Agent 5)

```
21. "Xếp hạng 80 CTTV theo hiệu quả nghiệp vụ BHYT (DT, LR, CR). 
     Tách 3 nhóm: Xanh-Vàng-Đỏ."

22. "CTTV Đà Nẵng có Loss Ratio 120% (lỗ nặng). 
     Phân tích nguyên nhân và lập Turnaround Plan 90 ngày."

23. "So sánh CTTV Hà Nội vs HCM vs Đà Nẵng: doanh thu, chi phí, 
     cơ cấu sản phẩm, kênh phân phối."

24. "Thiết kế KPI BHYT 2026 cho từng nhóm CTTV 
     (Tier 1: TP lớn, Tier 2: Tỉnh trung, Tier 3: Tỉnh nhỏ)."

25. "Đào tạo CTTV triển khai sản phẩm Tâm Bình và An Gia: 
     nội dung training, timeline, đo lường hiệu quả."
```

### 📊 Nhóm Chi Phí (Agent 6)

```
26. "Phân rã cấu trúc Expense Ratio theo từng hạng mục: 
     hoa hồng, lương, TPA, marketing, IT. Hạng mục nào đang bất thường?"

27. "So sánh chi phí TPA (quản lý bồi thường bên thứ 3) giữa các đối tác. 
     Nên tái đàm phán với đối tác nào?"

28. "Tác động tài chính nếu tăng phí hoa hồng Bancassurance thêm 3%. 
     Expense Ratio thay đổi bao nhiêu? Break-even ở mức DT nào?"

29. "Rà soát các khoản chi phí chung đang phân bổ cho mảng Y Tế. 
     Tỷ lệ 7% có hợp lý không?"
```

### 🎯 Nhóm Trải Nghiệm Khách Hàng (Agent 7)

```
30. "Phân tích top 5 loại khiếu nại BHYT phổ biến nhất năm 2025. 
     Đề xuất cải tiến quy trình cho từng loại."

31. "Đánh giá tác động NPS nếu siết tiêu chuẩn bồi thường ngoại trú 
     xuống mức tối đa 2 lần/tháng?"

32. "Thiết kế chương trình Loyalty cho KH tái tục năm thứ 3+. 
     Budget ≤ 2% lợi nhuận gộp."

33. "Thời gian giải quyết bồi thường (TAT) trung bình đang là bao lâu? 
     Benchmark với đối thủ? Lộ trình rút ngắn xuống 48h?"
```

### 📋 Nhóm Tổng Hợp — Trưởng Phòng

```
34. "Lập báo cáo tổng hợp tình hình BHYT quý 1/2026 trình Ban TGĐ."

35. "Agent 1 muốn tăng hoa hồng để đẩy doanh thu. Agent 6 nói chi phí đã cao. 
     Agent 7 nói KH đang hài lòng. Giải quyết xung đột này."

36. "Xây dựng Roadmap BHYT 2026 theo quý, phân bổ nguồn lực 
     và xác định mốc milestone quan trọng."
```

---

## 6. CÁCH ĐỌC KẾT QUẢ AI TRẢ VỀ

Mỗi lần AI phản hồi, kết quả sẽ được cấu trúc theo format chuẩn:

### 6.1 Cấu trúc báo cáo chuẩn

```
┌─────────────────────────────────────────────┐
│  📋 TÓM TẮT ĐIỀU HÀNH (≤ 200 từ)           │  ← CEO đọc đây TRƯỚC
│  • Tình hình tổng quan                      │
│  • Phát hiện quan trọng nhất                │
│  • Khuyến nghị cốt lõi                      │
├─────────────────────────────────────────────┤
│  📊 DASHBOARD KPI                            │  ← Nhìn nhanh: Xanh/Vàng/Đỏ
│  Bảng số liệu: Hiện tại vs Mục tiêu        │
├─────────────────────────────────────────────┤
│  🔍 PHÂN TÍCH CHI TIẾT                      │  ← Đào sâu khi cần
│  Root cause, data, benchmark                │
├─────────────────────────────────────────────┤
│  💡 ĐỀ XUẤT GIẢI PHÁP                       │  ← Hành động cụ thể
│  Kịch bản A / B / C + KPI + Timeline        │
├─────────────────────────────────────────────┤
│  ⚠️ CẢNH BÁO RỦI RO                         │  ← Đọc trước khi quyết
│  Rủi ro + Xác suất + Biện pháp              │
├─────────────────────────────────────────────┤
│  📎 NGUỒN DỮ LIỆU                           │  ← Kiểm chứng
│  Ghi rõ: dữ liệu thực / benchmark / assume │
└─────────────────────────────────────────────┘
```

### 6.2 Các ký hiệu cần chú ý

| Ký hiệu | Ý nghĩa |
|:---:|:---|
| 🟢 | Chỉ số trong vùng an toàn (đạt/vượt target) |
| 🟡 | Chỉ số cần theo dõi (gần ngưỡng cảnh báo) |
| 🔴 | Chỉ số nguy hiểm (vượt ngưỡng cho phép) |
| ↑ ↓ → | Xu hướng tăng / giảm / đi ngang |
| `[Benchmark]` | Số liệu từ thị trường, không phải nội bộ |
| `[Assumption]` | Giả định hợp lý — cần xác minh với data thực |
| `[Cross-check: Agent X]` | Đã được Agent khác phản biện |

### 6.3 Cách phản hồi với AI sau khi nhận kết quả

| CEO muốn | Gõ lệnh |
|:---|:---|
| Đồng ý, triển khai | `"ok"` hoặc `"duyệt"` |
| Đào sâu một phần | `"Đào sâu vào [phần cụ thể]"` |
| Yêu cầu sửa | `"Sửa lại phần [X], theo hướng [Y]"` |
| Yêu cầu phản biện | `"Cho Agent 7 phản biện giải pháp này"` |
| Xuất file | `"Xuất báo cáo này ra PDF"` hoặc `"Xuất ra Excel"` |
| Lưu lại | `"/save"` |

---

## 7. NẠP DỮ LIỆU — KHI NÀO CẦN, KHI NÀO KHÔNG

### 7.1 KHÔNG CẦN nạp gì vẫn chạy được (AI tự có)

AI đã được trang bị sẵn những kiến thức sau — CEO **không cần cung cấp**:

- ✅ Kiến thức ngành bảo hiểm (luật, thông tư, quy định BTC, chuẩn actuarial)
- ✅ Thông tin công khai về Bảo Việt (sản phẩm, website, cấu trúc tập đoàn)
- ✅ Dữ liệu thị trường BHPNT Việt Nam (doanh thu ngành, loss ratio trung bình, đối thủ)
- ✅ Kiến thức y khoa, lạm phát y tế, xu hướng HealthTech
- ✅ Best practices quốc tế (AXA, Allianz, Prudential, AIA)
- ✅ Mô hình tài chính, công thức actuarial, framework quản trị rủi ro

**Khi không có data nội bộ, AI sẽ tự động:** Sử dụng benchmark ngành + giả định hợp lý + ghi rõ nguồn. Kết quả vẫn có giá trị định hướng chiến lược.

### 7.2 CẦN NẠP để có kết quả chính xác tuyệt đối

Sau đây là 4 nhóm tài liệu nội bộ **chỉ CEO mới có** mà AI không thể tự tìm:

| # | Dữ liệu | Mô tả | Agent sử dụng | Mức độ |
|:---:|:---|:---|:---|:---:|
| 1 | **Báo cáo HQNV** | P&L nghiệp vụ: DT, bồi thường, chi phí theo sản phẩm/kênh/vùng | Agent 2, 6 | 🔴 Quan trọng |
| 2 | **Cấu trúc chi phí** | Bảng phân bổ: hoa hồng, TPA, lương, marketing, IT theo kênh | Agent 6 | 🔴 Quan trọng |
| 3 | **Rulebook sản phẩm** | Wording, quyền lợi BH, bảng phí nội bộ | Agent 3 | 🟡 Rất cần |
| 4 | **Dữ liệu KH & CTTV** | NPS survey, log khiếu nại, P&L theo CTTV | Agent 5, 7 | 🟡 Rất cần |

### 7.3 Cách nạp dữ liệu

**Cách 1:** Kéo-thả file vào cửa sổ chat hoặc dùng ký hiệu `@`:
```
@[đường_dẫn/file_HQNV.xlsx] Phân tích file này cho mảng BHYT
```

**Cách 2:** Copy-paste bảng số liệu trực tiếp vào chat:
```
Đây là số liệu HQNV quý 1:
- Phí gốc: 3.050 tỷ
- Loss Ratio: 65%
- Expense Ratio: 35%
Phân tích và đề xuất giải pháp.
```

**Cách 3:** Lưu file vào thư mục data chuyên dụng:
```
/Users/dungtq/ABM-Workforce/_abm/SubAgents/bhyt-2026/docs/
```
AI sẽ tự động truy cập khi cần tham chiếu.

---

## 8. CƠ CHẾ PHẢN BIỆN CHÉO — VŨ KHÍ BÍ MẬT

Đây là điểm khác biệt lớn nhất so với mọi công cụ AI thông thường. Các Agent trong phòng ban BHYT 2026 **không "gật đầu đồng ý" với nhau** — chúng BẮT BUỘC phải phản biện chéo.

### Quy tắc phản biện bắt buộc (Không tắt được)

```
┌─ Agent 1 (Doanh thu) đề xuất tăng trưởng
│    ↓ BẮT BUỘC kiểm tra
│    └─→ Agent 2 (Rủi ro): "Tăng DT này có làm Loss Ratio vượt 65% không?"
│    └─→ Agent 6 (Chi phí): "Chi phí khai thác thêm bao nhiêu?"
│
├─ Agent 2 (Rủi ro) đề xuất siết bồi thường
│    ↓ BẮT BUỘC kiểm tra
│    └─→ Agent 7 (CX): "Siết vậy KH có rời bỏ hàng loạt không? NPS tụt bao nhiêu?"
│
├─ Agent 3 (Sản phẩm) thiết kế SP mới
│    ↓ BẮT BUỘC kiểm tra
│    └─→ Agent 4 (Kênh): "Bán qua kênh nào? Đại lý có đủ năng lực bán SP này?"
│    └─→ Agent 2 (Rủi ro): "Rủi ro bồi thường SP mới ước tính bao nhiêu?"
│
├─ Agent 6 (Chi phí) đề xuất cắt giảm
│    ↓ BẮT BUỘC kiểm tra
│    └─→ Agent 7 (CX): "Cắt chi phí này có ảnh hưởng chất lượng dịch vụ?"
│    └─→ Agent 5 (CTTV): "CTTV có khả năng vận hành với budget thấp hơn?"
│
└─ BẤT KỲ thay đổi nào tác động KH
     ↓ BẮT BUỘC kiểm tra
     └─→ Agent 7 (CX): Quyền phủ quyết CX
```

### Ví dụ thực tế — Phản biện cứu CEO khỏi quyết định sai

**Tình huống:** CEO hỏi *"Ngừng bán An Gia Đồng vì Loss Ratio 90%"*

| Bước | Agent | Phản hồi |
|:---:|:---:|:---|
| 1 | Agent 2 | "Đúng, An Gia Đồng LR 90% — ngừng bán sẽ hạ LR chung xuống 58%." ✅ |
| 2 | Agent 7 | "⚠️ **CẢNH BÁO ĐỎ:** An Gia Đồng có 45.000 KH. Ngừng bán → mất 45K KH + 15% KH gia đình sẽ hủy theo. NPS tụt 23 điểm. Khủng hoảng truyền thông." 🔴 |
| 3 | Agent 3 | "Phương án thay thế: Không ngừng bán. Thêm mức khấu trừ 300K/lần ngoại trú + tăng phí 12%. Hoặc upgrade lên gói 'An Gia Senior' cho nhóm ≥60 tuổi." 💡 |
| 4 | Agent 1 | "Nếu upgrade 30% KH lên gói Senior, DT tăng ~45 tỷ/năm." 📈 |
| **KQ** | **Trưởng phòng** | **LR giảm từ 90% → 68%, giữ nguyên 90% tệp KH, DT tăng thêm 45 tỷ, NPS ổn định.** |

→ Không có cơ chế phản biện này, CEO có thể đã "giết" 45.000 khách hàng chỉ để tiết kiệm vài chục tỷ bồi thường.

---

## 9. XỬ LÝ TÌNH HUỐNG THƯỜNG GẶP (FAQ)

### Q1: "AI trả lời quá chung chung, không cụ thể"

**Nguyên nhân:** Câu lệnh chưa đủ chi tiết.

**Cách sửa:** Thêm ngữ cảnh cụ thể:
```
❌ "Làm sao tăng doanh thu?"
✅ "Phân tích 3 chiến lược tăng doanh thu BHYT cá nhân (An Gia) tại kênh 
    Bancassurance cho BaoViet Bank, target tăng 20% trong 6 tháng."
```

### Q2: "AI dùng số liệu cũ hoặc không chính xác"

**Nguyên nhân:** AI đang dùng benchmark (do chưa có data nội bộ).

**Cách sửa:** Nạp file data thực tế:
```
@[file_HQNV.xlsx] Dùng data thực tế này thay vì benchmark.
```

### Q3: "Muốn AI tập trung vào một Agent cụ thể, không cần tổng hợp"

**Cách làm:**
```
Agent 2 ONLY: Phân tích Loss Ratio BHYT quý 1 theo từng tỉnh. 
Không cần các Agent khác tham gia.
```

### Q4: "Muốn so sánh 2 kịch bản quyết định"

**Cách làm:**
```
Kịch bản A: Tăng phí An Gia 15%, giữ nguyên quyền lợi.
Kịch bản B: Giữ phí, giảm quyền lợi ngoại trú 20%.
Phân tích tác động: DT, LR, NPS, tỷ lệ tái tục. 
Bảng so sánh chi tiết. Khuyến nghị chọn A hay B.
```

### Q5: "Muốn AI xuất ra file để trình BĐH"

**Cách làm:**
```
Xuất báo cáo này ra file PDF, format chuẩn trình Hội đồng Quản trị.
```
hoặc
```
Tạo slide PowerPoint từ phân tích này, tối đa 10 slides.
```

### Q6: "Muốn lưu lại phiên làm việc để hôm sau tiếp"

```
/save
```
Hệ thống sẽ lưu toàn bộ ngữ cảnh. Hôm sau gõ `/recap` để khôi phục.

### Q7: "Muốn AI đánh giá phản biện quyết định của tôi"

```
Tôi dự định [quyết định cụ thể]. 
Hệ thống BHYT 2026 hãy phản biện đa chiều: tài chính, rủi ro, khách hàng, 
kênh phân phối, CTTV. Chỉ ra mọi rủi ro ẩn.
```

---

## 10. QUY ƯỚC AN TOÀN & GIỚI HẠN

### 10.1 Những gì AI TUYỆT ĐỐI KHÔNG LÀM

| # | Giới hạn | Lý do |
|:---:|:---|:---|
| 1 | ❌ Không bịa số liệu không ghi chú | Luôn ghi rõ: nội bộ / benchmark / assumption |
| 2 | ❌ Không khuyến nghị vi phạm pháp luật | Tuân thủ Bộ Tài chính, Cục QLGS Bảo hiểm |
| 3 | ❌ Không đề xuất phá giá thị trường | Bảo vệ uy tín thương hiệu số 1 Bảo Việt |
| 4 | ❌ Không đề xuất cắt bồi thường hợp lệ | Bảo vệ quyền lợi chính đáng của KH |
| 5 | ❌ Không tự ý quyết thay CEO | Luôn trình phương án → CEO phê duyệt |

### 10.2 Data Availability Protocol — Cách AI xử lý khi thiếu dữ liệu

| Cấp độ | AI sẽ làm gì | Ví dụ |
|:---:|:---|:---|
| **Level 1** | Hỏi CEO cung cấp | *"Để tính chính xác Loss Ratio An Gia, CEO có thể cung cấp data bồi thường theo sản phẩm?"* |
| **Level 2** | Dùng benchmark ngành | *"Chưa có data nội bộ, sử dụng LR trung bình ngành BHPNT 2025: 30,9% (nguồn: IAV)"* |
| **Level 3** | Giả định hợp lý | *"Giả định LR An Gia ≈ 75% dựa trên cấu trúc quyền lợi. Nếu sai ±10%, tác động..."* |

### 10.3 Đặc thù Bảo Việt cần nhớ

- **Doanh nghiệp Nhà nước** (BTC sở hữu 65%) → quy trình phê duyệt chặt chẽ
- **Hệ thống CTTV đa dạng** → giải pháp phải linh hoạt theo vùng miền
- **Thương hiệu #1 thị trường** → mọi giải pháp xứng tầm leader, không theo đuôi

---

## PHỤ LỤC: BẢNG TRA NHANH — GẶP VẤN ĐỀ NÀY THÌ GỌI AGENT NÀO?

| Vấn đề gặp phải | Agent chính | Agent phối hợp |
|:---|:---:|:---:|
| Doanh thu giảm / tăng chậm | Agent 1 | 4, 5 |
| Loss Ratio tăng vọt | Agent 2 | 5, 7 |
| Cần sản phẩm mới | Agent 3 | 2, 4 |
| Kênh bán không hiệu quả | Agent 4 | 1, 6 |
| CTTV đang lỗ | Agent 5 | 2, 6 |
| Chi phí quá cao | Agent 6 | 2, 5 |
| Khách hàng phàn nàn | Agent 7 | 1, 2 |
| Báo cáo tổng hợp cho BĐH | Trưởng phòng | Tất cả |
| Phản biện quyết định | Trưởng phòng | 2, 7 |
| Xung đột giữa các đề xuất | Trưởng phòng | Liên quan |

---

> **Lưu ý cuối:** Hệ thống này được thiết kế để **phục vụ CEO ra quyết định tốt hơn**, không phải để thay thế CEO ra quyết định. Mọi khuyến nghị đều cần sự phê duyệt của Ban lãnh đạo trước khi triển khai.
>
> *— Jarvis Orchestrator, ABM-Workforce System*
