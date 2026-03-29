<#
.SYNOPSIS
ABM Workforce
Kịch bản đồng bộ não bộ Antigravity IDE (Trí Nhớ) lên Cloud Drive cho thiết bị mạng WINDOWS
#>

Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "🧠 THIẾT LẬP ĐỒNG BỘ NGUYÊN KHỐI ANTIGRAVITY IDE (WINDOWS)" -ForegroundColor Cyan
Write-Host "================================================="
Write-Host ""

# Đòi hỏi quyền qủan trị Administrator để tạo Symlink ở Windows
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warning "❌ Thất bại: Sếp cần chạy script này bằng quyền Administrator (Chạy PowerShell as Administrator) để có quyền tạo màng Symlink ảo!"
    Exit
}

# Đường dẫn mặc định của Antigravity App Data ở Windows
$AntigravityDir = Join-Path $env:USERPROFILE ".gemini\antigravity"

# Nếu chạy ở máy 1 (Chưa Sync) -> Chuyển data lên Cloud
# Nếu chạy ở máy 2 (Đã Sync) -> Chỉ cắm Symlink về Cloud

Write-Host "Nhập đường dẫn thư mục Cloud Drive dùng để đồng bộ gốc của sếp:"
Write-Host "(Ví dụ: G:\My Drive\ABM-Cloud hoặc C:\Users\Username\OneDrive\ABM-Cloud)"
$CloudDir = Read-Host "Đường dẫn Cloud "

if ([string]::IsNullOrWhiteSpace($CloudDir)) {
    Write-Warning "❌ Hủy. Vui lòng cung cấp đường dẫn Cloud Drive hợp lệ."
    Exit
}

# Đảm bảo Cloud Directory tồn tại
if (-not (Test-Path $CloudDir)) {
    New-Item -ItemType Directory -Force -Path $CloudDir | Out-Null
}

$DestDir = Join-Path $CloudDir "antigravity-brain"

Write-Host "Đang xử lý thiết lập..." -ForegroundColor Yellow

# Kiểm tra xem đây có phải là Symlink hay không
function Test-Symlink {
    param([string]$Path)
    if (Test-Path $Path) {
        $Item = Get-Item $Path -Force
        if ($Item.Attributes -match "ReparsePoint") { return $true }
    }
    return $false
}

# Case 1: Thư mục gốc Antigravity tồn tại tĩnh (chưa Symlink)
if ((Test-Path $AntigravityDir) -and (-not (Test-Symlink $AntigravityDir))) {
    Write-Host "🔍 Phát hiện thư mục gốc Antigravity IDE chưa được đồng bộ."
    
    # Nếu Cloud đã có data, backup máy hiện tại
    if (Test-Path $DestDir) {
        Write-Warning "⚠️ TRÊN MÂY ĐÃ TỒN TẠI BỘ NÃO ANTIGRAVITY KHÁC"
        Write-Host "Script sẽ đổi tên bộ não trên máy thành .gemini\antigravity.bak"
        Start-Sleep -Seconds 3
        Rename-Item -Path $AntigravityDir -NewName "antigravity.bak" -Force
        Write-Host "Đã backup não bộ cũ trên máy thành antigravity.bak" -ForegroundColor Green
    } else {
        Write-Host "🚀 Đang bê toàn bộ Trí nhớ đưa lên Cloud Mây ($DestDir)..."
        Move-Item -Path $AntigravityDir -Destination $DestDir -Force
    }
    
    Write-Host "🔗 Đang tạo luồng (Symlink) từ mây về lại ổ C laptop: $AntigravityDir ..."
    New-Item -ItemType Junction -Path $AntigravityDir -Target $DestDir | Out-Null
    Write-Host "✅ XONG MÁY WINDOWS 1! Lịch sử chat và trí khôn đã bắt đầu được Cloud Drive Upload lên mạng." -ForegroundColor Green

# Case 2: Nếu chưa có thư mục Antigravity trên máy (Laptop Windows thứ 2)
} elseif (-not (Test-Path $AntigravityDir)) {
    Write-Host "🔍 Phát hiện máy thứ 2 (hoặc chưa khởi tạo Antigravity)."
    
    if (-not (Test-Path $DestDir)) {
        Write-Warning "❌ LỖI: Trên $DestDir chưa có dữ liệu não bộ. Hãy chạy kịch bản này ở máy chủ (Máy Số 1) trước, chờ Google Drive/OneDrive Upload xong rồi mới nhảy sang máy này nhé sếp!"
        Exit
    }
    
    # Ensure parent dir .gemini exists
    $GeminiParent = Join-Path $env:USERPROFILE ".gemini"
    if (-not (Test-Path $GeminiParent)) {
        New-Item -ItemType Directory -Force -Path $GeminiParent | Out-Null
    }

    Write-Host "🔗 Khởi tạo luồng thần kinh (Symlink) nối vào não máy Win này..."
    New-Item -ItemType Junction -Path $AntigravityDir -Target $DestDir | Out-Null
    Write-Host "✅ XONG MÁY WINDOWS 2! Sếp có thể mở IDE, dữ liệu phiên trước của Macbook đã được khôi phục thành công 100%!" -ForegroundColor Green

# Case 3: Trạng thái đã là Symlink rồi
} elseif (Test-Symlink $AntigravityDir) {
    Write-Host "✅ Máy Windows này đã được setup đồng bộ mây thành công rồi sếp ơi!" -ForegroundColor Green
}

Write-Host ""
Write-Host "================================================="
Write-Host "🎉 Tất cả hoàn thành. Hạ tầng Đa Nền Tảng Ký Kết Thành Công!" -ForegroundColor Cyan
