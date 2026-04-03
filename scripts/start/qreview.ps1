param(
    [Parameter(Mandatory = $true)]
    [ValidateRange(1, 4)]
    [int]$Week,
    [string]$Root = "D:\code\trade"
)

$reportPath = Join-Path $Root ("reports\week-{0:D2}-review.md" -f $Week)
$template = Join-Path $Root "templates\weekly-review-template.md"
$parent = Split-Path -Parent $reportPath

if (-not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Path $parent | Out-Null
}

if (-not (Test-Path -LiteralPath $reportPath)) {
    if (Test-Path -LiteralPath $template) {
        Copy-Item -LiteralPath $template -Destination $reportPath
    } else {
        Set-Content -LiteralPath $reportPath -Value "# Week $Week Review`n" -Encoding UTF8
    }
}

Write-Host ""
Write-Host "=== Weekly Review $Week ==="
Write-Host "Report: $reportPath"
Write-Host ""
Write-Host "Checklist:"
Write-Host "- What did you learn that still holds?"
Write-Host "- What looked good in backtest but weakened under stress?"
Write-Host "- Which one system deserves more time next week?"
Write-Host "- What will you stop doing?"

