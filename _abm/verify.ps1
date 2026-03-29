# ABM Workforce Structure Validator
# Kiểm tra cấu trúc ABM Workforce có đầy đủ không

$root = "G:\AGY\_abm"
$errors = @()
$checks = 0
$passed = 0

function Check-Path {
    param($path, $description)
    $script:checks++
    if (Test-Path $path) {
        $script:passed++
        Write-Host "[OK] $description" -ForegroundColor Green
    } else {
        $script:errors += $description
        Write-Host "[FAIL] $description" -ForegroundColor Red
    }
}

Write-Host "=== ABM Workforce Structure Validation ===" -ForegroundColor Cyan
Write-Host ""

# Core directories
Check-Path "$root\SubAgents" "SubAgents/ directory"
Check-Path "$root\Workers" "Workers/ directory"
Check-Path "$root\Autonomous-Core" "Autonomous-Core/ directory"
Check-Path "$root\Team-Orchestration" "Team-Orchestration/ directory"
Check-Path "$root\_design-specs" "_design-specs/ directory"
Check-Path "$root\Context-Layer" "Context-Layer/ directory"
Check-Path "$root\Context-Layer\CoreModules" "Context-Layer/CoreModules/"
Check-Path "$root\Context-Layer\Knowledge-Base" "Context-Layer/Knowledge-Base/"
Check-Path "$root\Context-Layer\Second-Brain" "Context-Layer/Second-Brain/"
Check-Path "$root\Outputs" "Outputs/ directory"

# Root files
Check-Path "$root\workforce-config.json" "workforce-config.json"
Check-Path "$root\README.md" "README.md"
Check-Path "$root\HUONG-DAN-SU-DUNG.md" "HUONG-DAN-SU-DUNG.md"

# Key files
Check-Path "$root\Autonomous-Core\jarvis-orchestrator.md" "Jarvis orchestrator"
Check-Path "$root\Autonomous-Core\consciousness\SOUL.md" "Jarvis SOUL.md"
Check-Path "$root\Autonomous-Core\consciousness\HEARTBEAT.md" "HEARTBEAT.md"
Check-Path "$root\Outputs\task-log.yaml" "Task log"

# SubAgents
$subagents = @("marketing-specialist", "hr-specialist", "office-manager", "automation-engineer", "business-analyst")
foreach ($sa in $subagents) {
    Check-Path "$root\SubAgents\$sa\SOUL.md" "SubAgent: $sa"
}

# Counts
Write-Host ""
Write-Host "=== File Counts ===" -ForegroundColor Cyan
$components = @(
    @{Name="SubAgents"; Path="$root\SubAgents"},
    @{Name="Workers"; Path="$root\Workers"},
    @{Name="Autonomous-Core"; Path="$root\Autonomous-Core"},
    @{Name="Team-Orchestration"; Path="$root\Team-Orchestration"},
    @{Name="_design-specs"; Path="$root\_design-specs"},
    @{Name="Context-Layer"; Path="$root\Context-Layer"},
    @{Name="Outputs"; Path="$root\Outputs"}
)

$total = 0
foreach ($c in $components) {
    if (Test-Path $c.Path) {
        $count = (Get-ChildItem -Path $c.Path -Recurse -File).Count
        $total += $count
        Write-Host "$($c.Name): $count files"
    }
}
Write-Host "TOTAL: $total files" -ForegroundColor Yellow

# Summary
Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
Write-Host "Checks: $checks | Passed: $passed | Failed: $($errors.Count)" -ForegroundColor $(if ($errors.Count -eq 0) { "Green" } else { "Red" })
if ($errors.Count -gt 0) {
    Write-Host "Failures:" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
}
