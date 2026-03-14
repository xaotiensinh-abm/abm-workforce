# ============================================
# ABM Dashboard Sync Script
# Quét workspace → cập nhật dashboard/task-data.js
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

Write-Host "🔄 ABM Dashboard Sync" -ForegroundColor Cyan
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
    $subagentCount = (Get-ChildItem -Path $subagentsDir -Directory).Count
}
Write-Host "🤖 SubAgents: $subagentCount" -ForegroundColor Magenta

# === 5. Đọc task-history.json ===
$tasks = @()
if (Test-Path $taskHistoryFile) {
    $tasks = Get-Content $taskHistoryFile -Raw | ConvertFrom-Json
}
$taskCount = $tasks.Count
Write-Host "📋 Tasks: $taskCount" -ForegroundColor Cyan

# === 6. Đếm phòng ban (unique departments) ===
$departments = @()
if ($tasks.Count -gt 0) {
    $departments = $tasks | ForEach-Object { $_.department } | Sort-Object -Unique
}
$deptCount = $departments.Count
Write-Host "🏢 Phòng Ban: $deptCount" -ForegroundColor White

# === 7. Tạo task-data.js ===
Write-Host "`n📝 Generating task-data.js..." -ForegroundColor Cyan

$jsHeader = @"
// === ABM DASHBOARD — AUTO-GENERATED DATA ===
// Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
// Script: dashboard/sync.ps1
// KHÔNG SỬA TAY — chạy: powershell dashboard/sync.ps1

"@

# Convert tasks to JS
$taskLines = @()
foreach ($t in $tasks) {
    $skillsStr = ($t.skills | ForEach-Object { "`"$_`"" }) -join ","
    $title = $t.title -replace '"', '\"'
    $result = $t.result -replace '"', '\"'
    $dept = $t.department -replace '"', '\"'
    $taskLines += "    {id:`"$($t.id)`",date:`"$($t.date)`",title:`"$title`",department:`"$dept`",agent:`"$($t.agent)`",worker:`"$($t.worker)`",skills:[$skillsStr],status:`"$($t.status)`",completion:$($t.completion),result:`"$result`"}"
}
$taskJs = $taskLines -join ",`n"

$jsContent = @"
$jsHeader
const TASK_DATA = [
$taskJs
];

// Workspace stats — auto-scanned
const WORKSPACE_STATS = {
    skills: $skillCount,
    routes: $routeCount,
    workflows: $workflowCount,
    subagents: $subagentCount,
    departments: $deptCount,
    version: "v3.0",
    lastSync: "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
};
"@

$jsContent | Out-File -FilePath $taskDataFile -Encoding UTF8 -Force

Write-Host "`n✅ Sync hoàn tất!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "📦 Skills:      $skillCount"
Write-Host "🔀 Routes:      $routeCount"
Write-Host "⚡ Workflows:   $workflowCount"
Write-Host "🤖 SubAgents:   $subagentCount"
Write-Host "📋 Tasks:       $taskCount"
Write-Host "🏢 Phòng Ban:   $deptCount"
Write-Host "📂 Output:      $taskDataFile"
Write-Host "🔄 Refresh dashboard (F5) để thấy thay đổi" -ForegroundColor Yellow
