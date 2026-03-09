---
name: "agent-email-cli"
description: "Gửi email tự động qua CLI — thông báo nội bộ, follow-up khách hàng, email sequence. SMTP/API integration. Giao tiếp tiếng Việt."
---

# 📧 Agent Email CLI — Gửi Email Tự Động

Skill gửi email tự động qua command line — SMTP hoặc API (SendGrid, Resend).

## Sử dụng khi

- Gửi thông báo nội bộ tự động
- Follow-up khách hàng sau cuộc họp
- Gửi email sequence (welcome, nurture)
- Gửi báo cáo định kỳ qua email

## KHÔNG sử dụng khi

- Cần viết copy email → dùng `copywriting` hoặc `email-marketing`
- Cần chiến lược email → dùng `email-marketing`
- Cần cold outreach sequence → dùng `cold-email`

## VÍ DỤ NHANH

```
Input:  "Gửi thông báo họp team 2pm thứ 2"
Output: Email sent to team@company.com
  → Subject: [Thông báo] Họp team — Thứ 2, 14:00
  → Body: Nội dung cuộc họp + link Meet
  → CC: manager@company.com
```

---

## CÁCH TRIỂN KHAI

### Option 1: SMTP (Gmail / Outlook)

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, subject, body, cc=None):
    msg = MIMEMultipart()
    msg['From'] = 'sender@company.com'
    msg['To'] = to
    msg['Subject'] = subject
    if cc:
        msg['Cc'] = cc
    
    msg.attach(MIMEText(body, 'html'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('sender@company.com', 'app_password')
        server.send_message(msg)
    
    return f"✅ Email sent to {to}"
```

### Option 2: Resend API

```python
import resend

resend.api_key = "re_xxxxx"

params = {
    "from": "noreply@company.com",
    "to": ["recipient@example.com"],
    "subject": "Thông báo",
    "html": "<h1>Nội dung</h1>"
}

email = resend.Emails.send(params)
```

### Email Template HTML

```html
<div style="font-family: Arial; max-width: 600px; margin: 0 auto;">
  <div style="background: #0F172A; padding: 20px; text-align: center;">
    <h1 style="color: white;">Công Ty ABC</h1>
  </div>
  <div style="padding: 20px;">
    <p>Xin chào {{name}},</p>
    <p>{{content}}</p>
    <a href="{{cta_link}}" style="background: #3B82F6; color: white; 
       padding: 12px 24px; text-decoration: none; border-radius: 6px;">
      {{cta_text}}
    </a>
  </div>
  <div style="background: #F1F5F9; padding: 15px; text-align: center; font-size: 12px;">
    <p>© 2026 Công Ty ABC</p>
  </div>
</div>
```

---

## QUY TẮC AN TOÀN

1. ⚠️ **KHÔNG gửi email mà chưa được CEO duyệt nội dung**
2. **Confirm trước khi gửi**: Hiển thị preview → chờ "ok" → mới gửi
3. **Rate limit**: Tối đa 50 emails/giờ
4. **BCC bản thân**: Luôn BCC sender để theo dõi
5. **Unsubscribe link**: Bắt buộc cho email marketing
6. **Environment variables**: API keys trong `.env`, KHÔNG hardcode

---

## Nguồn gốc
- Gốc: community skills (agent-email-cli) — adapt cho ABM
- ABM Workforce v2.4 — Jarvis Orchestrator
