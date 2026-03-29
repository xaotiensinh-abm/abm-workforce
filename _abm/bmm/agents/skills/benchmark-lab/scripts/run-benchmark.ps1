# Benchmark Lab — Performance Testing
# Usage: .\run-benchmark.ps1 -Url "https://abmedu.vn"
param([string]$Url = "https://example.com", [int]$Iterations = 5)

Write-Host "=== BENCHMARK: $Url ($Iterations iterations) ==="
$times = @()
for ($i=1; $i -le $Iterations; $i++) {
  $sw = [System.Diagnostics.Stopwatch]::StartNew()
  try { Invoke-WebRequest $Url -TimeoutSec 30 | Out-Null }
  catch { Write-Host "  [FAIL] Request $i failed" }
  $sw.Stop()
  $times += $sw.ElapsedMilliseconds
  Write-Host "  Run $i/$Iterations : $($sw.ElapsedMilliseconds)ms"
}
$avg = [math]::Round(($times | Measure-Object -Average).Average)
$min = ($times | Measure-Object -Minimum).Minimum
$max = ($times | Measure-Object -Maximum).Maximum
Write-Host "`n--- Results ---"
Write-Host "  Avg: ${avg}ms | Min: ${min}ms | Max: ${max}ms"
Write-Host "  $(if($avg -lt 2000){'[PASS]'}elseif($avg -lt 4000){'[WARN]'}else{'[FAIL]'}) Target: <2000ms"
