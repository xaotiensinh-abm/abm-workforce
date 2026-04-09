# Code Review Checklist Generator
# Usage: .\review-checklist.ps1 -File "path/to/file.js"
param([string]$File)

if (-not (Test-Path $File)) { Write-Host "[ERROR] File not found: $File"; return }

$ext = [System.IO.Path]::GetExtension($File)
$lines = (Get-Content $File).Count

Write-Host "=== CODE REVIEW: $File ==="
Write-Host "  Extension: $ext | Lines: $lines"
Write-Host ""
Write-Host "## Checklist"
Write-Host "[ ] Code readability — clear naming, comments"
Write-Host "[ ] Error handling — try/catch, edge cases"
Write-Host "[ ] Security — no hardcoded secrets, input validation"
Write-Host "[ ] Performance — no N+1, efficient loops"
Write-Host "[ ] Accessibility — ARIA labels (if HTML)"
Write-Host "[ ] Responsive — mobile-first (if CSS)"
Write-Host "[ ] SEO — meta tags, semantic HTML (if HTML)"
Write-Host "[ ] Tests — unit tests exist"
