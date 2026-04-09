# SEO Audit Script — ABM Workforce
# Usage: .\run-seo-audit.ps1 -Url "https://abmedu.vn"
param([string]$Url = "https://example.com")

Write-Host "=== SEO AUDIT: $Url ==="
Write-Host ""

# 1. Technical SEO
Write-Host "[1/5] Technical SEO..."
Write-Host "  Checking robots.txt..."
try { $robots = Invoke-WebRequest "$Url/robots.txt" -TimeoutSec 10; Write-Host "  [OK] robots.txt found ($($robots.Content.Length) bytes)" } catch { Write-Host "  [WARN] robots.txt NOT found" }
try { $sitemap = Invoke-WebRequest "$Url/sitemap.xml" -TimeoutSec 10; Write-Host "  [OK] sitemap.xml found" } catch { Write-Host "  [WARN] sitemap.xml NOT found" }

# 2. HTTPS
Write-Host "`n[2/5] HTTPS..."
if ($Url -match "^https") { Write-Host "  [OK] HTTPS enabled" } else { Write-Host "  [FAIL] HTTP only — need HTTPS" }

# 3. Response time
Write-Host "`n[3/5] Performance..."
$sw = [System.Diagnostics.Stopwatch]::StartNew()
try { Invoke-WebRequest $Url -TimeoutSec 30 | Out-Null; $sw.Stop(); $ms = $sw.ElapsedMilliseconds
  if ($ms -lt 2000) { Write-Host "  [OK] Response: ${ms}ms (< 2s)" }
  elseif ($ms -lt 4000) { Write-Host "  [WARN] Response: ${ms}ms (2-4s)" }
  else { Write-Host "  [FAIL] Response: ${ms}ms (> 4s)" }
} catch { Write-Host "  [FAIL] Could not connect" }

# 4. Meta tags
Write-Host "`n[4/5] On-Page SEO..."
try {
  $html = (Invoke-WebRequest $Url -TimeoutSec 30).Content
  if ($html -match '<title>([^<]+)</title>') { $title = $matches[1]; Write-Host "  Title: $title ($($title.Length) chars)" }
  if ($html -match 'meta.*description.*content="([^"]+)"') { $desc = $matches[1]; Write-Host "  Description: $($desc.Substring(0,[Math]::Min(80,$desc.Length)))... ($($desc.Length) chars)" }
  $h1Count = ([regex]::Matches($html, '<h1')).Count
  Write-Host "  H1 tags: $h1Count $(if($h1Count -eq 1){'[OK]'}else{'[WARN] should be 1'})"
} catch { Write-Host "  [FAIL] Could not fetch page" }

# 5. Summary
Write-Host "`n[5/5] Summary"
Write-Host "  URL: $Url"
Write-Host "  Date: $(Get-Date -Format 'yyyy-MM-dd')"
Write-Host "  Output: _abm-output/seo/"
Write-Host "`n=== AUDIT COMPLETE ==="
