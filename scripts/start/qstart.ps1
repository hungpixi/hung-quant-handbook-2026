param(
    [string]$Root = "D:\code\trade"
)

$today = Get-Date -Format "yyyy-MM-dd"

Write-Host ""
Write-Host "=== Quant Lab Daily Start ==="
Write-Host "Date: $today"
Write-Host "Root: $Root"
Write-Host ""
Write-Host "90-minute rhythm:"
Write-Host "1. 15m review market and current regime"
Write-Host "2. 25m study one concept only"
Write-Host "3. 25m test or annotate one hypothesis"
Write-Host "4. 25m write note and next action"
Write-Host ""
Write-Host "Suggested files:"
Write-Host "- Main report: $Root\SIEU_BAO_CAO_CHIEN_LUOC_2026_V3_FINAL.md"
Write-Host "- Concepts:    $Root\memory\concepts"
Write-Host "- Research:    $Root\research"
Write-Host "- Reports:     $Root\reports"
Write-Host ""
Write-Host "Next command:"
Write-Host ".\scripts\start\qday.ps1 -Day 1"

