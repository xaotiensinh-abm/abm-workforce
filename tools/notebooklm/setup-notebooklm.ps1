#Requires -Version 5.1
<#
.SYNOPSIS
    ABM - DũngTQ | Cài đặt NotebookLM-py tự động
.DESCRIPTION
    Script tự động cài đặt thư viện notebooklm-py (Unofficial Python API cho Google NotebookLM).
    Bao gồm: kiểm tra Python, cài pip package, Playwright Chromium, agent skill, và đăng nhập.
.NOTES
    Author : ABM - DũngTQ
    Version: 1.0.0
    Repo   : https://github.com/teng-lin/notebooklm-py
#>

param(
    [switch]$SkipLogin,
    [switch]$DevInstall,
    [switch]$Help
)

# ============================================================
# CONFIG
# ============================================================
$BRAND = "ABM - DungTQ"
$MIN_PYTHON_VERSION = [version]"3.9"
$PACKAGE_NAME = "notebooklm-py[browser]"
$DEV_PACKAGE_URL = "git+https://github.com/teng-lin/notebooklm-py@main"

# ============================================================
# HELPERS
# ============================================================
function Write-Brand {
    Write-Host ""
    Write-Host "  ╔══════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "  ║                                                  ║" -ForegroundColor Cyan
    Write-Host "  ║     🤖  $BRAND  —  NotebookLM Setup           ║" -ForegroundColor Cyan
    Write-Host "  ║                                                  ║" -ForegroundColor Cyan
    Write-Host "  ╚══════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Step {
    param([int]$Number, [string]$Message)
    Write-Host "  [$Number/5] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message -ForegroundColor White
}

function Write-OK {
    param([string]$Message)
    Write-Host "   ✅ " -ForegroundColor Green -NoNewline
    Write-Host $Message -ForegroundColor Gray
}

function Write-Err {
    param([string]$Message)
    Write-Host "   ❌ " -ForegroundColor Red -NoNewline
    Write-Host $Message -ForegroundColor Gray
}

function Write-Warn {
    param([string]$Message)
    Write-Host "   ⚠️  " -ForegroundColor Yellow -NoNewline
    Write-Host $Message -ForegroundColor Gray
}

function Write-Info {
    param([string]$Message)
    Write-Host "   ℹ️  " -ForegroundColor Blue -NoNewline
    Write-Host $Message -ForegroundColor Gray
}

function Show-Help {
    Write-Brand
    Write-Host "  CÁCH DÙNG:" -ForegroundColor Yellow
    Write-Host "    .\setup-notebooklm.ps1              Cài đặt đầy đủ + đăng nhập"
    Write-Host "    .\setup-notebooklm.ps1 -SkipLogin   Cài đặt mà không đăng nhập"
    Write-Host "    .\setup-notebooklm.ps1 -DevInstall  Cài bản dev từ GitHub main"
    Write-Host "    .\setup-notebooklm.ps1 -Help        Hiện trợ giúp"
    Write-Host ""
    Write-Host "  YÊU CẦU:" -ForegroundColor Yellow
    Write-Host "    - Python >= 3.9"
    Write-Host "    - pip (đi kèm Python)"
    Write-Host "    - Kết nối internet"
    Write-Host ""
    exit 0
}

# ============================================================
# MAIN
# ============================================================
if ($Help) { Show-Help }

Write-Brand
Write-Host "  Bắt đầu cài đặt NotebookLM-py..." -ForegroundColor Gray
Write-Host ""

# --- STEP 1: Kiểm tra Python ---
Write-Step 1 "Kiểm tra Python..."

$pythonCmd = $null
foreach ($cmd in @("python", "python3", "py")) {
    try {
        $ver = & $cmd --version 2>&1
        if ($ver -match "Python (\d+\.\d+\.\d+)") {
            $currentVersion = [version]$Matches[1]
            if ($currentVersion -ge $MIN_PYTHON_VERSION) {
                $pythonCmd = $cmd
                Write-OK "Tìm thấy $ver (yêu cầu >= $MIN_PYTHON_VERSION)"
                break
            } else {
                Write-Warn "$ver quá cũ (yêu cầu >= $MIN_PYTHON_VERSION)"
            }
        }
    } catch {
        continue
    }
}

if (-not $pythonCmd) {
    Write-Err "Không tìm thấy Python >= $MIN_PYTHON_VERSION"
    Write-Host ""
    Write-Host "  Tải Python tại: https://www.python.org/downloads/" -ForegroundColor Cyan
    Write-Host "  Lưu ý: Tick 'Add Python to PATH' khi cài đặt." -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

# --- STEP 2: Cài notebooklm-py ---
Write-Step 2 "Cài đặt notebooklm-py..."

try {
    if ($DevInstall) {
        Write-Info "Cài bản dev từ GitHub main branch..."
        & $pythonCmd -m pip install $DEV_PACKAGE_URL 2>&1 | Out-Null
    } else {
        & $pythonCmd -m pip install $PACKAGE_NAME 2>&1 | Out-Null
    }

    # Xác minh cài đặt
    $version = & notebooklm --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-OK "Đã cài notebooklm-py ($version)"
    } else {
        throw "Cài đặt không thành công"
    }
} catch {
    Write-Err "Lỗi cài đặt: $_"
    Write-Host "  Thử chạy thủ công: pip install `"notebooklm-py[browser]`"" -ForegroundColor Yellow
    exit 1
}

# --- STEP 3: Cài Playwright Chromium ---
Write-Step 3 "Cài Playwright Chromium browser..."

try {
    & playwright install chromium 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-OK "Playwright Chromium đã sẵn sàng"
    } else {
        throw "Lỗi cài Playwright"
    }
} catch {
    Write-Warn "Không cài được Playwright tự động. Thử chạy: playwright install chromium"
}

# --- STEP 4: Cài Agent Skill ---
Write-Step 4 "Cài đặt Agent Skill..."

try {
    & notebooklm skill install 2>&1 | Out-Null
    Write-OK "Agent skill đã cài vào ~/.claude/skills/notebooklm"
} catch {
    Write-Warn "Không cài được skill tự động. Thử: notebooklm skill install"
}

# --- STEP 5: Đăng nhập ---
if ($SkipLogin) {
    Write-Step 5 "Bỏ qua đăng nhập (dùng -SkipLogin)"
    Write-Info "Chạy sau: notebooklm login  HOẶC  python login-notebooklm.py"
} else {
    Write-Step 5 "Đăng nhập Google NotebookLM..."
    Write-Host ""
    Write-Info "Mở trình duyệt Chromium để đăng nhập Google..."
    Write-Info "Nếu bị timeout, dùng script: python login-notebooklm.py"
    Write-Host ""

    $loginScript = Join-Path $PSScriptRoot "login-notebooklm.py"
    if (Test-Path $loginScript) {
        & $pythonCmd $loginScript
    } else {
        try {
            & notebooklm login
        } catch {
            Write-Warn "Login CLI bị lỗi. Thử: python login-notebooklm.py"
        }
    }

    # Kiểm tra kết quả
    try {
        $authResult = & notebooklm auth check 2>&1
        if ($authResult -match "valid") {
            Write-OK "Đăng nhập thành công!"
        } else {
            Write-Warn "Chưa xác minh được. Chạy: notebooklm auth check --test"
        }
    } catch {
        Write-Warn "Chưa xác minh được đăng nhập."
    }
}

# --- KẾT QUẢ ---
Write-Host ""
Write-Host "  ╔══════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ║     ✅  CÀI ĐẶT HOÀN TẤT  —  $BRAND        ║" -ForegroundColor Green
Write-Host "  ║                                                  ║" -ForegroundColor Green
Write-Host "  ╚══════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "  Lệnh hữu ích:" -ForegroundColor Yellow
Write-Host "    notebooklm create `"Tên notebook`"         Tạo notebook mới"
Write-Host "    notebooklm source add `"url/file`"          Thêm nguồn"
Write-Host "    notebooklm ask `"câu hỏi`"                  Hỏi đáp với nguồn"
Write-Host "    notebooklm generate audio `"chủ đề`"        Tạo podcast"
Write-Host "    notebooklm generate video --wait            Tạo video"
Write-Host "    notebooklm generate quiz                    Tạo bài kiểm tra"
Write-Host ""
Write-Host "  Tài liệu: https://github.com/teng-lin/notebooklm-py" -ForegroundColor Cyan
Write-Host ""
