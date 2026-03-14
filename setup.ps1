<#
.SYNOPSIS
    ABM Workforce Auto Setup Script (Windows PowerShell)
.DESCRIPTION
    Auto install ABM Workforce: skills, workflows, rules become global
    User only needs: git clone -> .\setup.ps1 -> Done!
.NOTES
    Requirements: Windows 10+, PowerShell 5.1+, Run as Administrator recommended
#>

param(
    [switch]$Force,
    [switch]$Uninstall,
    [switch]$Verify
)

$ErrorActionPreference = "Stop"
$ABM_ROOT = $PSScriptRoot
if (-not $ABM_ROOT) { $ABM_ROOT = (Get-Location).Path }

$SKILLS_SRC    = Join-Path $ABM_ROOT "_abm\bmm\agents\skills"
$WORKFLOWS_SRC = Join-Path $ABM_ROOT ".agents\workflows"
$GLOBAL_DIR    = Join-Path $env:USERPROFILE ".agents"
$GLOBAL_SKILLS = Join-Path $GLOBAL_DIR "skills"
$GLOBAL_WF     = Join-Path $GLOBAL_DIR "workflows"

function Show-Banner {
    Write-Host ""
    Write-Host "  =======================================" -ForegroundColor Cyan
    Write-Host "    ABM Workforce - Auto Setup v9.0" -ForegroundColor Cyan
    Write-Host "    AI Business Master" -ForegroundColor Cyan
    Write-Host "  =======================================" -ForegroundColor Cyan
    Write-Host ""
}

function Test-Prerequisites {
    Write-Host "[CHECK] Checking prerequisites..." -ForegroundColor Yellow
    if (-not (Test-Path $SKILLS_SRC)) {
        Write-Host "  [FAIL] _abm/bmm/agents/skills/ not found" -ForegroundColor Red
        Write-Host "  Run this script from ABM Workforce root." -ForegroundColor Red
        exit 1
    }
    Write-Host "  [OK] ABM source: $ABM_ROOT" -ForegroundColor Green
    Write-Host "  [OK] PowerShell $($PSVersionTable.PSVersion)" -ForegroundColor Green
    $isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    if ($isAdmin) { Write-Host "  [OK] Administrator" -ForegroundColor Green }
    else { Write-Host "  [WARN] Not admin - junctions may fail. Try Run as Administrator" -ForegroundColor Yellow }
}

function Install-Skills {
    Write-Host ""
    Write-Host "[SKILLS] Installing skills..." -ForegroundColor Yellow
    if (-not (Test-Path $GLOBAL_SKILLS)) { New-Item -ItemType Directory -Path $GLOBAL_SKILLS -Force | Out-Null }
    $installed = 0; $skipped = 0; $failed = 0
    Get-ChildItem $SKILLS_SRC -Directory | Where-Object { $_.Name -ne '_archive' } | ForEach-Object {
        $name = $_.Name; $src = $_.FullName; $tgt = Join-Path $GLOBAL_SKILLS $name
        if (Test-Path $tgt) {
            if ($Force) {
                if ((Get-Item $tgt).Attributes -band [IO.FileAttributes]::ReparsePoint) { cmd /c "rmdir `"$tgt`"" 2>$null }
                else { Remove-Item $tgt -Recurse -Force }
            } else { $skipped++; return }
        }
        try { cmd /c "mklink /J `"$tgt`" `"$src`"" 2>$null | Out-Null; $installed++ }
        catch { $failed++; Write-Host "  [FAIL] $name" -ForegroundColor Red }
    }
    $color = if ($failed -gt 0) { 'Red' } else { 'Green' }
    Write-Host "  [DONE] Installed: $installed | Skipped: $skipped | Failed: $failed" -ForegroundColor $color
}

function Install-Workflows {
    Write-Host ""
    Write-Host "[WORKFLOWS] Installing workflows..." -ForegroundColor Yellow
    if (-not (Test-Path $WORKFLOWS_SRC)) { Write-Host "  [SKIP] .agents/workflows/ not found" -ForegroundColor Yellow; return }
    if (-not (Test-Path $GLOBAL_WF)) { New-Item -ItemType Directory -Path $GLOBAL_WF -Force | Out-Null }
    $installed = 0
    Get-ChildItem $WORKFLOWS_SRC -File -Filter "*.md" | ForEach-Object {
        $tgt = Join-Path $GLOBAL_WF $_.Name
        if (-not (Test-Path $tgt) -or $Force) { Copy-Item $_.FullName $tgt -Force; $installed++ }
    }
    Write-Host "  [DONE] $installed workflows installed" -ForegroundColor Green
}

function Install-Rules {
    Write-Host ""
    Write-Host "[RULES] Installing global rules..." -ForegroundColor Yellow
    $globalGemini = Join-Path $env:USERPROFILE ".gemini"
    if (-not (Test-Path $globalGemini)) { New-Item -ItemType Directory -Path $globalGemini -Force | Out-Null }
    $rulesFile = Join-Path $ABM_ROOT "_abm\RULES_GLOBAL.md"
    if (Test-Path $rulesFile) {
        $globalRules = Join-Path $globalGemini "RULES.md"
        Copy-Item $rulesFile $globalRules -Force
        Write-Host "  [DONE] Global rules -> $globalRules" -ForegroundColor Green
    } else { Write-Host "  [SKIP] RULES_GLOBAL.md not found" -ForegroundColor Yellow }
}

function Test-Installation {
    Write-Host ""
    Write-Host "[VERIFY] Checking installation..." -ForegroundColor Yellow
    $issues = 0
    if (Test-Path $GLOBAL_SKILLS) {
        $c = (Get-ChildItem $GLOBAL_SKILLS -Directory).Count
        Write-Host "  [OK] Global skills: $c" -ForegroundColor Green
    } else { Write-Host "  [FAIL] Global skills missing" -ForegroundColor Red; $issues++ }
    if (Test-Path $GLOBAL_WF) {
        $c = (Get-ChildItem $GLOBAL_WF -File -Filter "*.md").Count
        Write-Host "  [OK] Global workflows: $c" -ForegroundColor Green
    } else { Write-Host "  [FAIL] Global workflows missing" -ForegroundColor Red; $issues++ }
    $sample = Join-Path $GLOBAL_SKILLS "high-ticket-sales\SKILL.md"
    if (Test-Path $sample) { Write-Host "  [OK] Sample skill link valid" -ForegroundColor Green }
    else { Write-Host "  [WARN] Sample skill link broken" -ForegroundColor Yellow; $issues++ }
    Write-Host ""
    if ($issues -eq 0) {
        Write-Host "  ABM Workforce installed successfully!" -ForegroundColor Green
        Write-Host "  Type /jarvis in Antigravity IDE to start." -ForegroundColor Cyan
    } else { Write-Host "  $issues issues found. Run with -Force to fix." -ForegroundColor Yellow }
}

function Uninstall-ABM {
    Write-Host ""
    Write-Host "[UNINSTALL] Removing ABM Workforce..." -ForegroundColor Yellow
    if (Test-Path $GLOBAL_SKILLS) {
        Get-ChildItem $GLOBAL_SKILLS -Directory | ForEach-Object {
            if ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) { cmd /c "rmdir `"$($_.FullName)`"" 2>$null }
        }
        Write-Host "  [DONE] Skill junctions removed" -ForegroundColor Green
    }
    if (Test-Path $GLOBAL_WF) {
        Remove-Item "$GLOBAL_WF\*.md" -Force -ErrorAction SilentlyContinue
        Write-Host "  [DONE] Workflows removed" -ForegroundColor Green
    }
    Write-Host "  ABM Workforce uninstalled." -ForegroundColor Green
}

Show-Banner
if ($Verify) { Test-Installation; exit 0 }
if ($Uninstall) { Uninstall-ABM; exit 0 }
Test-Prerequisites
Install-Skills
Install-Workflows
Install-Rules
Test-Installation
Write-Host ""
Write-Host "  Setup complete! Type /jarvis to start." -ForegroundColor Green
Write-Host ""
