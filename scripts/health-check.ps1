# ABM Workforce Health Check v2.5
# Chay: powershell -ExecutionPolicy Bypass -File scripts/health-check.ps1

param([switch]$Verbose)

$root = Split-Path $PSScriptRoot -Parent
$skillsDir = "$root\_abm\bmm\agents\skills"
$kbDir = "$root\_abm\Context-Layer\Knowledge-Base"
$manifest = "$root\_abm\_config\skill-manifest.csv"
$orchestrator = "$root\_abm\bmm\agents\jarvis-orchestrator.md"
$pass = 0; $fail = 0

function Do-Check($Name, $Result, $Detail) {
    if ($Result) {
        Write-Host "  [PASS] $Name" -ForegroundColor Green
        $script:pass++
    }
    else {
        Write-Host "  [FAIL] $Name - $Detail" -ForegroundColor Red
        $script:fail++
    }
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  ABM Workforce Health Check v2.5" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# 1. SYNC
Write-Host "[1/6] SYNC CHECK" -ForegroundColor Magenta
$sd = (Get-ChildItem $skillsDir -Directory).Count
$kd = (Get-ChildItem $kbDir -Directory).Count
$ml = (Get-Content $manifest | Where-Object { $_ -match '^\s*"' }).Count
Do-Check "Skills=$sd KB=$kd Manifest=$ml" ($sd -eq $kd -and $sd -eq $ml) "Mismatch"

$sn = (Get-ChildItem $skillsDir -Directory).Name | Sort-Object
$kn = (Get-ChildItem $kbDir -Directory).Name | Sort-Object
$diff = Compare-Object $sn $kn
Do-Check "Skills <-> KB names sync" ($diff.Count -eq 0) "$($diff.Count) diffs"

Write-Host ""

# 2. FRONTMATTER
Write-Host "[2/6] FRONTMATTER CHECK" -ForegroundColor Magenta
$noName = 0; $noDesc = 0
foreach ($s in (Get-ChildItem $skillsDir -Directory)) {
    $f = "$($s.FullName)\SKILL.md"
    if (Test-Path $f) {
        $c = Get-Content $f -Raw -Encoding UTF8
        if ($c -notmatch '(?m)^name:') { $noName++ }
        if ($c -notmatch '(?m)^description:') { $noDesc++ }
    }
}
Do-Check "All have name: ($($sd - $noName)/$sd)" ($noName -eq 0) "$noName missing"
Do-Check "All have description: ($($sd - $noDesc)/$sd)" ($noDesc -eq 0) "$noDesc missing"

Write-Host ""

# 3. KHONG SU DUNG
Write-Host "[3/6] KHONG SU DUNG KHI" -ForegroundColor Magenta
$noK = 0
foreach ($s in (Get-ChildItem $skillsDir -Directory)) {
    $f = "$($s.FullName)\SKILL.md"
    if (Test-Path $f) {
        $c = Get-Content $f -Raw -Encoding UTF8
        if ($c -notmatch 'kh.ng s. d.ng') { $noK++ }
    }
}
Do-Check "All have KHONG su dung ($($sd - $noK)/$sd)" ($noK -eq 0) "$noK missing"

Write-Host ""

# 4. ROUTING
Write-Host "[4/6] ROUTING CHECK" -ForegroundColor Magenta
$rc = (Select-String -Path $orchestrator -Pattern 'task_type="' -AllMatches).Matches.Count
Do-Check "Routes ($rc)" ($rc -ge 15) "Only $rc"
$hasGeneral = Select-String -Path $orchestrator -Pattern 'task_type="general"' -Quiet
Do-Check "Has fallback general" ($hasGeneral -eq $true) "No fallback"

Write-Host ""

# 5. COMPONENTS
Write-Host "[5/6] COMPONENTS" -ForegroundColor Magenta
$sa = (Get-ChildItem "$root\_abm\SubAgents" -Directory -ErrorAction SilentlyContinue).Count
$wk = (Get-ChildItem "$root\_abm\Workers" -File -ErrorAction SilentlyContinue).Count
$wf = (Get-ChildItem "$root\.agents\workflows" -File -ErrorAction SilentlyContinue).Count
Do-Check "SubAgents ($sa >= 5)" ($sa -ge 5) "Only $sa"
Do-Check "Workers ($wk >= 10)" ($wk -ge 10) "Only $wk"
Do-Check "Workflows ($wf >= 13)" ($wf -ge 13) "Only $wf"

$mandatory = @("delegation-chain","verification-before-completion","context-engineering")
foreach ($ms in $mandatory) {
    Do-Check "Mandatory: $ms" (Test-Path "$skillsDir\$ms\SKILL.md") "NOT FOUND"
}

Write-Host ""

# 6. INTEGRITY
Write-Host "[6/6] FILE INTEGRITY" -ForegroundColor Magenta
Do-Check "README.md" (Test-Path "$root\README.md") "NOT FOUND"
Do-Check "RULES.md" (Test-Path "$root\.gemini\RULES.md") "NOT FOUND"
Do-Check "config.yaml" (Test-Path "$root\_abm\bmm\config.yaml") "NOT FOUND"

Write-Host ""

# SUMMARY
$total = $pass + $fail
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Skills: $sd | KB: $kd | Manifest: $ml | Routes: $rc" -ForegroundColor White
Write-Host "  SubAgents: $sa | Workers: $wk | Workflows: $wf" -ForegroundColor White
Write-Host ""
if ($fail -eq 0) {
    Write-Host "  PASS: $pass/$total | FAIL: 0 | STATUS: HEALTHY" -ForegroundColor Green
}
else {
    Write-Host "  PASS: $pass/$total | FAIL: $fail | STATUS: NEEDS FIX" -ForegroundColor Red
}
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
