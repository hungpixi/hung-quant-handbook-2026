param(
    [Parameter(Mandatory = $true)]
    [ValidateRange(1, 30)]
    [int]$Day,
    [string]$Root = "D:\code\trade"
)

$dayMap = @{
    1  = "memory\concepts\edge-definition.md"
    2  = "memory\concepts\auction-logic-xauusd.md"
    3  = "memory\concepts\why-trend-still-works.md"
    4  = "memory\bots\bot-298-architecture.md"
    5  = "memory\bots\bot-298-antithesis.md"
    6  = "research\signal-scorecard.md"
    7  = "reports\week-01-review.md"
    8  = "research\xauusd-ichimoku-hypothesis.md"
    9  = "docs\playbooks\xauusd-trend-engine.md"
    10 = "memory\concepts\regime-map.md"
    11 = "docs\playbooks\risk-engine.md"
    12 = "docs\playbooks\dca-safety-framework.md"
    13 = "memory\concepts\execution-guard.md"
    14 = "reports\week-02-review.md"
    15 = "research\backtest-protocol.md"
    16 = "research\signal-alone-test.md"
    17 = "research\filter-ablation.md"
    18 = "research\sizing-comparison.md"
    19 = "research\stress-test.md"
    20 = "research\parameter-stability.md"
    21 = "reports\week-03-review.md"
    22 = "docs\playbooks\live-ops-sop.md"
    23 = "docs\playbooks\research-loop.md"
    24 = "docs\playbooks\product-engine.md"
    25 = "docs\playbooks\affiliate-engine.md"
    26 = "docs\playbooks\teaching-outline.md"
    27 = "docs\playbooks\knowledge-base-map.md"
    28 = "reports\bootstrap-test.md"
    29 = "docs\playbooks\daily-rhythm.md"
    30 = "reports\month-02-order.md"
}

$targetRelative = $dayMap[$Day]
$target = Join-Path $Root $targetRelative
$template = Join-Path $Root "templates\note-template.md"

$parent = Split-Path -Parent $target
if (-not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Path $parent | Out-Null
}

if (-not (Test-Path -LiteralPath $target)) {
    if (Test-Path -LiteralPath $template) {
        Copy-Item -LiteralPath $template -Destination $target
    } else {
        Set-Content -LiteralPath $target -Value "# Day $Day`n" -Encoding UTF8
    }
}

Write-Host ""
Write-Host "=== Day $Day ==="
Write-Host "Target note: $target"
Write-Host "Read first:  $Root\SIEU_BAO_CAO_CHIEN_LUOC_2026_V3_FINAL.md"
Write-Host ""
Write-Host "Action:"
Write-Host "- Open the target note."
Write-Host "- Study the matching section in the main report."
Write-Host "- Write your own hypothesis, not copied slogans."
Write-Host "- Finish with one concrete decision."

