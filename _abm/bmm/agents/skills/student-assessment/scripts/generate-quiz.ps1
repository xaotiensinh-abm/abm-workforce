# Quiz Generator Template
# Usage: .\generate-quiz.ps1 -Module "Master AI" -Questions 10
param([string]$Module = "General", [int]$Questions = 5)

Write-Host "=== QUIZ: $Module ($Questions questions) ==="
Write-Host ""
Write-Host "# Quiz: $Module"
Write-Host "## Date: $(Get-Date -Format 'yyyy-MM-dd')"
Write-Host ""
for ($i=1; $i -le $Questions; $i++) {
  Write-Host "### Q$i. [Question about $Module]"
  Write-Host "A) [Option]"
  Write-Host "B) [Option]"
  Write-Host "C) [Option]"
  Write-Host "D) [Option]"
  Write-Host "**Answer**: [ ]"
  Write-Host ""
}
Write-Host "---"
Write-Host "Pass Score: $([math]::Ceiling($Questions * 0.7))/$Questions (70%)"
