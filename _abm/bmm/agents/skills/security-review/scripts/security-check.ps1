# Security Check — ABM System Audit
# Usage: .\security-check.ps1
param([string]$AbmRoot = "G:\AGY\_abm")

Write-Host "=== ABM SECURITY CHECK ==="

# 1. Check for hardcoded secrets
Write-Host "`n[1/5] Scanning for hardcoded secrets..."
$patterns = @("api_key", "secret", "password", "token", "private_key")
$found = 0
Get-ChildItem "$AbmRoot\bmm\agents\skills" -Recurse -File -Filter "*.md" | ForEach-Object {
  $content = Get-Content $_.FullName -Raw
  foreach ($p in $patterns) {
    if ($content -match "$p\s*[:=]\s*[`"']?[A-Za-z0-9]{20}") {
      Write-Host "  [WARN] Possible secret in $($_.FullName): $p"
      $found++
    }
  }
}
if ($found -eq 0) { Write-Host "  [OK] No hardcoded secrets found" }

# 2. Check scope violations in attestations
Write-Host "`n[2/5] Checking scope control..."
$hasContracts = (Get-ChildItem "$AbmRoot\SubAgents" -File -Filter "*.md" -ErrorAction SilentlyContinue).Count
Write-Host "  SubAgents with SOUL.md: $hasContracts"
$hasWorkers = (Get-ChildItem "$AbmRoot\Workers" -Directory -ErrorAction SilentlyContinue).Count
Write-Host "  Workers with scope: $hasWorkers"

# 3. Check prompt-sentinel
Write-Host "`n[3/5] Prompt Security..."
$sentinel = "$AbmRoot\bmm\agents\skills\prompt-sentinel\SKILL.md"
if (Test-Path $sentinel) { Write-Host "  [OK] prompt-sentinel active ($((Get-Content $sentinel).Count) lines)" }
else { Write-Host "  [FAIL] prompt-sentinel NOT FOUND" }

# 4. Check Second-Brain for PII
Write-Host "`n[4/5] Scanning Second-Brain for PII..."
$sbDir = "$AbmRoot\Context-Layer\Second-Brain"
$piiPatterns = @('\d{10,11}', '\w+@\w+\.\w+', '\d{3}-\d{3}-\d{4}')
$piiFound = 0
Get-ChildItem $sbDir -File | ForEach-Object {
  $content = Get-Content $_.FullName -Raw
  foreach ($p in $piiPatterns) {
    if ($content -match $p) { Write-Host "  [WARN] Possible PII in $($_.Name)"; $piiFound++; break }
  }
}
if ($piiFound -eq 0) { Write-Host "  [OK] No PII found in Second-Brain" }

# 5. Check CHANGELOG exists
Write-Host "`n[5/5] Audit Trail..."
if (Test-Path "$AbmRoot\CHANGELOG.md") { Write-Host "  [OK] CHANGELOG.md exists" } else { Write-Host "  [WARN] No CHANGELOG.md" }
if (Test-Path "$AbmRoot\_config\manifest-sync.ps1") { Write-Host "  [OK] manifest-sync.ps1 exists" } else { Write-Host "  [WARN] No manifest-sync" }

Write-Host "`n=== SECURITY CHECK COMPLETE ==="
