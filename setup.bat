@echo off
REM ============================================================
REM ABM Workforce — Quick Setup (Windows CMD)
REM Double-click this file to install ABM Workforce!
REM ============================================================

echo.
echo   ========================================
echo     ABM Workforce - Auto Setup
echo     AI Business Master v9.0
echo   ========================================
echo.

REM Check if PowerShell is available
where powershell >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] PowerShell khong duoc tim thay!
    echo Hay cai dat PowerShell truoc.
    pause
    exit /b 1
)

REM Run the PowerShell setup script
echo Dang chay setup script...
echo.
powershell -ExecutionPolicy Bypass -File "%~dp0setup.ps1"

echo.
echo Setup hoan tat! Nhan phim bat ky de dong...
pause >nul
