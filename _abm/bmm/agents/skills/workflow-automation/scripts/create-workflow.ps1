# Create Workflow Template
# Usage: .\create-workflow.ps1 -Name "new-workflow" -Desc "Description"
param([string]$Name, [string]$Desc = "New workflow")

$wfDir = "G:\AGY\.agents\workflows"
$file = "$wfDir\$Name.md"
if (Test-Path $file) { Write-Host "[EXISTS] $file"; return }

$template = @"
---
description: $Desc
---

# $($Name.Replace('-',' ').ToUpper())

## Buoc 1: [Action]
[Instructions]

## Buoc 2: [Action]
[Instructions]

## Buoc 3: Report
Trinh ket qua cho CEO
"@
Set-Content $file $template -Encoding utf8
Write-Host "[CREATED] $file"
