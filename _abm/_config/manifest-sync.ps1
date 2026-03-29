# ABM Manifest Sync Script
# Run after ANY skill/agent/worker change
$base = 'G:\AGY\_abm\bmm\agents\skills'
$config = 'G:\AGY\_abm\_config'

# Rebuild skill-manifest.csv
$csv = 'name,tags,tier,lines,has_checklist'
Get-ChildItem $base -Directory | Where-Object { $_.Name -ne '_archive' } | Sort-Object Name | ForEach-Object {
  $f = Join-Path $_.FullName 'SKILL.md'
  $ck = Join-Path $_.FullName 'CHECKLIST.md'
  if (Test-Path $f) {
    $lines = (Get-Content $f).Count
    $tier = if ($lines -ge 250) { 3 } elseif ($lines -ge 120) { 2 } else { 1 }
    $hasCk = if (Test-Path $ck) { 'yes' } else { 'no' }
    $content = Get-Content $f -Raw
    $tags = ''
    if ($content -match 'tags:\s*\[([^\]]+)\]') { $tags = $matches[1].Trim() }
    $csv += [char]10 + "$($_.Name),$tags,$tier,$lines,$hasCk"
  }
}
Set-Content "$config\skill-manifest.csv" $csv -Encoding utf8

# Rebuild agent-manifest.csv
$agentCsv = 'name,type,path,status'
Get-ChildItem "$base\.." -File -Filter '*.md' | ForEach-Object { $agentCsv += [char]10 + "$($_.BaseName),agent,_abm/bmm/agents/$($_.Name),active" }
Get-ChildItem 'G:\AGY\_abm\SubAgents\*.md' | ForEach-Object { $agentCsv += [char]10 + "$($_.BaseName),subagent,_abm/SubAgents/$($_.Name),active" }
Get-ChildItem 'G:\AGY\_abm\Workers' -Directory | ForEach-Object { $agentCsv += [char]10 + "$($_.Name),worker,_abm/Workers/$($_.Name)/WORKER.md,active" }
Set-Content "$config\agent-manifest.csv" $agentCsv -Encoding utf8

$count = (Get-ChildItem $base -Directory | Where-Object { $_.Name -ne '_archive' }).Count
Write-Host "[SYNCED] $count skills | $((Get-ChildItem 'G:\AGY\_abm\SubAgents' -File).Count) SubAgents | $((Get-ChildItem 'G:\AGY\_abm\Workers' -Directory).Count) Workers"
