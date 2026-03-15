# ============================================
# ABM Dashboard Sync Script v4.0
# Pipeline: task-history.json → task-data.js
# Quét workspace → cập nhật dashboard
# Chạy: powershell dashboard/sync.ps1
# ============================================

param(
    [string]$WorkspaceRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$Verbose
)

$dashboardDir = Join-Path $WorkspaceRoot "dashboard"
$taskDataFile = Join-Path $dashboardDir "task-data.js"
$taskHistoryFile = Join-Path $dashboardDir "task-history.json"
$skillsDir = Join-Path $WorkspaceRoot "_abm\bmm\agents\skills"
$manifestFile = Join-Path $WorkspaceRoot "_abm\_config\skill-manifest.csv"
$workflowsDir = Join-Path $WorkspaceRoot ".agents\workflows"
$subagentsDir = Join-Path $WorkspaceRoot "_abm\SubAgents"
$workersDir = Join-Path $WorkspaceRoot "_abm\Workers"

Write-Host "`n🔄 ABM Dashboard Sync v4.0" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

# === 1. Đếm Skills ===
$skillCount = 0
if (Test-Path $skillsDir) {
    $skillCount = (Get-ChildItem -Path $skillsDir -Directory).Count
}
Write-Host "📦 Skills: $skillCount" -ForegroundColor Green

# === 2. Đếm Routes (từ manifest) ===
$routeCount = 0
if (Test-Path $manifestFile) {
    $lines = Get-Content $manifestFile | Where-Object { $_ -match "^[^#]" -and $_ -match "," }
    $routeCount = $lines.Count
}
Write-Host "🔀 Routes: $routeCount" -ForegroundColor Blue

# === 3. Đếm Workflows ===
$workflowCount = 0
if (Test-Path $workflowsDir) {
    $workflowCount = (Get-ChildItem -Path $workflowsDir -Filter "*.md").Count
}
Write-Host "⚡ Workflows: $workflowCount" -ForegroundColor Yellow

# === 4. Đếm SubAgents ===
$subagentCount = 0
if (Test-Path $subagentsDir) {
    $subagentCount = (Get-ChildItem -Path $subagentsDir -Filter "*.md").Count
}
Write-Host "🤖 SubAgents: $subagentCount" -ForegroundColor Magenta

# === 5. Đếm Workers ===
$workerCount = 0
if (Test-Path $workersDir) {
    $workerCount = (Get-ChildItem -Path $workersDir -Filter "*.md").Count
} else {
    $workerCount = 5  # Default
}
Write-Host "👷 Workers: $workerCount" -ForegroundColor White

# === 6. Đọc task-history.json ===
$tasks = @()
if (Test-Path $taskHistoryFile) {
    $tasks = Get-Content $taskHistoryFile -Raw -Encoding UTF8 | ConvertFrom-Json
}
$taskCount = $tasks.Count
Write-Host "📋 Tasks: $taskCount" -ForegroundColor Cyan

# === 7. Đếm phòng ban ===
$departments = @()
if ($tasks.Count -gt 0) {
    $departments = $tasks | ForEach-Object { $_.department } | Sort-Object -Unique
}
$deptCount = $departments.Count
Write-Host "🏢 Phòng Ban: $deptCount" -ForegroundColor White

# === 8. Tạo task-data.js v4.0 (với detail fields) ===
Write-Host "`n📝 Generating task-data.js v4.0..." -ForegroundColor Cyan

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

$jsHeader = @"
// === ABM DASHBOARD v4.0 — AUTO-GENERATED DATA ===
// Generated: $timestamp
// Script: dashboard/sync.ps1 v4.0
// KHÔNG SỬA TAY — chạy: powershell dashboard/sync.ps1

"@

# Convert tasks to JS (với detail fields)
$taskLines = @()
foreach ($t in $tasks) {
    $skillsStr = ($t.skills | ForEach-Object { "`"$_`"" }) -join ","
    $title = ($t.title -replace '"', '\"') -replace "'", "\'"
    $result = ($t.result -replace '"', '\"') -replace "'", "\'"
    $dept = ($t.department -replace '"', '\"')
    $desc = if ($t.description) { ($t.description -replace '"', '\"') -replace "`n", " " } else { "" }
    $evidence = if ($t.evidence) { ($t.evidence -replace '"', '\"') -replace "`n", " " } else { "" }
    $sessionId = if ($t.session_id) { $t.session_id } else { "" }
    $duration = if ($t.duration_minutes) { $t.duration_minutes } else { 0 }

    # files_changed array
    $filesStr = ""
    if ($t.files_changed) {
        $filesStr = ($t.files_changed | ForEach-Object { "`"$($_ -replace '"', '\"')`"" }) -join ","
    }

    # decisions array
    $decisionsStr = ""
    if ($t.decisions) {
        $decisionsStr = ($t.decisions | ForEach-Object { "`"$($_ -replace '"', '\"')`"" }) -join ","
    }

    $taskLines += "    {id:`"$($t.id)`",date:`"$($t.date)`",title:`"$title`",department:`"$dept`",agent:`"$($t.agent)`",worker:`"$($t.worker)`",skills:[$skillsStr],status:`"$($t.status)`",completion:$($t.completion),result:`"$result`",description:`"$desc`",files_changed:[$filesStr],decisions:[$decisionsStr],evidence:`"$evidence`",session_id:`"$sessionId`",duration:$duration}"
}
$taskJs = $taskLines -join ",`n"

$jsContent = @"
$jsHeader
const TASK_DATA = [
$taskJs
];

// Workspace stats — v4.0 auto-scanned
const WORKSPACE_STATS = {
    skills: $skillCount,
    routes: $routeCount,
    workflows: $workflowCount,
    subagents: $subagentCount,
    workers: $workerCount,
    departments: $deptCount,
    version: "v4.0",
    lastSync: "$timestamp"
};
"@

# Write with UTF8 BOM-free
[System.IO.File]::WriteAllText($taskDataFile, $jsContent, [System.Text.UTF8Encoding]::new($false))

Write-Host "`n✅ Sync v4.0 hoàn tất!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "📦 Skills:      $skillCount"
Write-Host "🔀 Routes:      $routeCount"
Write-Host "⚡ Workflows:   $workflowCount"
Write-Host "🤖 SubAgents:   $subagentCount"
Write-Host "👷 Workers:     $workerCount"
Write-Host "📋 Tasks:       $taskCount (with detail)"
Write-Host "🏢 Phòng Ban:   $deptCount"
Write-Host "📂 Output:      $taskDataFile"
Write-Host "🔄 Refresh dashboard (F5) để thấy thay đổi" -ForegroundColor Yellow
