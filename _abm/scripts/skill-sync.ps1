<#
.SYNOPSIS
    ABM Skill Sync — PowerShell version cho Windows
.DESCRIPTION
    Đồng bộ skills từ _abm/bmm/agents/skills/ (Source of Truth)
    sang .agents/skills/ và .gemini/skills/ bằng symlinks/junctions
.PARAMETER DryRun
    Preview changes without executing
.PARAMETER Force
    Overwrite real directories with symlinks
.PARAMETER Verbose
    Show detailed output
.PARAMETER CleanOnly
    Only remove broken symlinks and empty dirs
.EXAMPLE
    .\skill-sync.ps1
    .\skill-sync.ps1 -DryRun
    .\skill-sync.ps1 -Force
#>

param(
    [switch]$DryRun,
    [switch]$Force,
    [switch]$VerboseOutput,
    [switch]$CleanOnly
)

# ─── Configuration ──────────────────────────────────────────
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = (Resolve-Path "$ScriptDir\..\..").Path

$SourceDir = Join-Path $ProjectRoot "_abm\bmm\agents\skills"
$RegistryFile = Join-Path $SourceDir "skill-registry.yaml"

$Targets = @(
    ".agents\skills",
    ".gemini\skills"
)

$Excludes = @("_archive", "skill-registry.yaml")

# ─── Stats ──────────────────────────────────────────────────
$Stats = @{
    Created  = 0
    Skipped  = 0
    Replaced = 0
    Cleaned  = 0
    Errors   = 0
}

# ─── Helpers ────────────────────────────────────────────────
function Write-OK($msg)   { Write-Host "  ✅ $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "  ⚠️  $msg" -ForegroundColor Yellow }
function Write-Err($msg)  { Write-Host "  ❌ $msg" -ForegroundColor Red }
function Write-Skip($msg) { Write-Host "  ⏭️  $msg" -ForegroundColor DarkGray }
function Write-V($msg)    { if ($VerboseOutput) { Write-Host "  📋 $msg" -ForegroundColor DarkCyan } }

function Test-IsExcluded($name) {
    return $Excludes -contains $name
}

# ─── Banner ─────────────────────────────────────────────────
Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║       🔄 ABM Skill Sync — v1.0.0 (Windows)          ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# ─── Validate ───────────────────────────────────────────────
if (-not (Test-Path $SourceDir)) {
    Write-Err "Source directory not found: $SourceDir"
    exit 1
}

# ─── Collect skills ─────────────────────────────────────────
$SkillNames = @()
Get-ChildItem -Path $SourceDir -Directory | ForEach-Object {
    $name = $_.Name
    if (Test-IsExcluded $name) {
        Write-V "Excluded: $name"
        return
    }
    $skillMd = Join-Path $_.FullName "SKILL.md"
    if (-not (Test-Path $skillMd)) {
        Write-V "No SKILL.md: $name (skipped)"
        return
    }
    $SkillNames += $name
}

$SkillCount = $SkillNames.Count
Write-Host "📊 Source: $SourceDir"
Write-Host "📊 Skills found: $SkillCount"
Write-Host "📊 Targets: $($Targets -join ', ')"
if ($DryRun) { Write-Host "📊 Mode: DRY RUN (no changes)" -ForegroundColor Yellow }
if ($Force)  { Write-Host "📊 Mode: FORCE (overwrite real dirs)" -ForegroundColor Yellow }
Write-Host ""

# ─── Phase 1: Clean ────────────────────────────────────────
Write-Host "── Phase 1: Clean up ──────────────────────────────────"

foreach ($target in $Targets) {
    $targetPath = Join-Path $ProjectRoot $target
    if (-not (Test-Path $targetPath)) { continue }

    Write-Host "  Cleaning $target/"

    Get-ChildItem -Path $targetPath -Directory -ErrorAction SilentlyContinue | ForEach-Object {
        $item = $_
        $itemName = $item.Name

        # Check if junction/symlink is broken
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            $linkTarget = (Get-Item $item.FullName -Force).Target
            if (-not (Test-Path $linkTarget -ErrorAction SilentlyContinue)) {
                Write-Warn "Broken symlink: $target\$itemName"
                if (-not $DryRun) {
                    Remove-Item $item.FullName -Force -Recurse
                    $Stats.Cleaned++
                }
            }
            return
        }

        # Empty directories
        $fileCount = (Get-ChildItem -Path $item.FullName -Recurse -File -ErrorAction SilentlyContinue).Count
        if ($fileCount -eq 0) {
            Write-Warn "Empty dir: $target\$itemName"
            if (-not $DryRun) {
                Remove-Item $item.FullName -Force -Recurse
                $Stats.Cleaned++
            }
        }
    }
}

Write-Host "  Cleaned: $($Stats.Cleaned) items"
Write-Host ""

if ($CleanOnly) {
    Write-Host "── Done (clean-only mode) ─────────────────────────────"
    exit 0
}

# ─── Phase 2: Create Symlinks ──────────────────────────────
Write-Host "── Phase 2: Create symlinks ───────────────────────────"

# Check admin privileges for symlinks
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Warn "Not running as admin — using directory junctions (mklink /J) instead of symlinks"
}

foreach ($target in $Targets) {
    $targetPath = Join-Path $ProjectRoot $target

    if (-not (Test-Path $targetPath)) {
        Write-Host "  Creating $target/"
        if (-not $DryRun) {
            New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
        }
    }

    Write-Host ""
    Write-Host "  → $target/"

    foreach ($skillName in $SkillNames) {
        $skillSource = Join-Path $SourceDir $skillName
        $skillTarget = Join-Path $targetPath $skillName

        # Case 1: Already a junction/symlink
        if ((Test-Path $skillTarget) -and ((Get-Item $skillTarget -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            Write-V "OK: $skillName (already linked)"
            $Stats.Skipped++
            continue
        }

        # Case 2: Real directory exists
        if (Test-Path $skillTarget) {
            if ($Force) {
                Write-Warn "Replace real dir: $skillName"
                if (-not $DryRun) {
                    Remove-Item $skillTarget -Force -Recurse
                    # Use junction (no admin needed) or symlink (admin needed)
                    if ($isAdmin) {
                        New-Item -ItemType SymbolicLink -Path $skillTarget -Target $skillSource | Out-Null
                    } else {
                        cmd /c mklink /J "$skillTarget" "$skillSource" | Out-Null
                    }
                    $Stats.Replaced++
                }
            } else {
                Write-Skip "$skillName (real dir exists, use -Force to replace)"
                $Stats.Skipped++
            }
            continue
        }

        # Case 3: Create new
        Write-OK "$skillName"
        if (-not $DryRun) {
            if ($isAdmin) {
                New-Item -ItemType SymbolicLink -Path $skillTarget -Target $skillSource | Out-Null
            } else {
                cmd /c mklink /J "$skillTarget" "$skillSource" | Out-Null
            }
            $Stats.Created++
        } else {
            $Stats.Created++
        }
    }
}

Write-Host ""

# ─── Phase 3: Update Registry ──────────────────────────────
if ((Test-Path $RegistryFile) -and (-not $DryRun)) {
    $timestamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $content = Get-Content $RegistryFile -Raw
    $content = $content -replace 'last_sync:.*', "last_sync: `"$timestamp`""
    $content = $content -replace 'total_skills:.*', "total_skills: $SkillCount"
    Set-Content $RegistryFile -Value $content
}

# ─── Summary ───────────────────────────────────────────────
Write-Host "══════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  📊 Sync Summary"
Write-Host "──────────────────────────────────────────────────────"
Write-Host "  Skills in source:  $SkillCount"
Write-Host "  Symlinks created:  $($Stats.Created)"
Write-Host "  Symlinks replaced: $($Stats.Replaced)"
Write-Host "  Skipped:           $($Stats.Skipped)"
Write-Host "  Cleaned:           $($Stats.Cleaned)"
Write-Host "  Errors:            $($Stats.Errors)"
Write-Host "══════════════════════════════════════════════════════" -ForegroundColor Cyan
if ($DryRun) { Write-Host "  ⚠️  DRY RUN — no changes were made" -ForegroundColor Yellow }
Write-Host ""
