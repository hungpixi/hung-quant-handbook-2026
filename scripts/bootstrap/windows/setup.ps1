param(
    [string]$Root = "D:\code\trade"
)

$ErrorActionPreference = "Stop"

function Test-Tool {
    param([string]$Name)

    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($cmd) {
        Write-Host "[OK] $Name -> $($cmd.Source)"
        return $true
    }

    Write-Warning "[Missing] $Name"
    return $false
}

function Ensure-Directory {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "[Create] $Path"
    } else {
        Write-Host "[Keep]   $Path"
    }
}

function Ensure-File {
    param(
        [string]$Path,
        [string]$Content
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        $parent = Split-Path -Parent $Path
        if ($parent) {
            Ensure-Directory -Path $parent
        }
        Set-Content -LiteralPath $Path -Value $Content -Encoding UTF8
        Write-Host "[Create] $Path"
    } else {
        Write-Host "[Keep]   $Path"
    }
}

Write-Host ""
Write-Host "=== Quant Lab Bootstrap ==="
Write-Host "Root: $Root"
Write-Host ""

$tools = @("git", "python", "uv", "node", "codex", "antigravity")
$missing = @()
foreach ($tool in $tools) {
    if (-not (Test-Tool -Name $tool)) {
        $missing += $tool
    }
}

Write-Host ""
Write-Host "=== Scaffold ==="

$dirs = @(
    (Join-Path $Root "docs"),
    (Join-Path $Root "docs\playbooks"),
    (Join-Path $Root "memory"),
    (Join-Path $Root "memory\bots"),
    (Join-Path $Root "memory\brokers"),
    (Join-Path $Root "memory\concepts"),
    (Join-Path $Root "research"),
    (Join-Path $Root "reports"),
    (Join-Path $Root "journals"),
    (Join-Path $Root "templates"),
    (Join-Path $Root "scripts"),
    (Join-Path $Root "scripts\start")
)

foreach ($dir in $dirs) {
    Ensure-Directory -Path $dir
}

$noteTemplate = @"
# Tieu de

## Gia thuyet

## Ly do tin

## Cach kiem chung

## Ket qua hien tai

## Quyet dinh

## Lenh goi lai
"@

$weeklyTemplate = @"
# Weekly Review

## Viec da hoc

## Gia thuyet moi

## Thu giu lai

## Thu loai bo

## Lenh cho tuan toi
"@

Ensure-File -Path (Join-Path $Root "templates\note-template.md") -Content $noteTemplate
Ensure-File -Path (Join-Path $Root "templates\weekly-review-template.md") -Content $weeklyTemplate

Write-Host ""
Write-Host "=== Suggested Aliases ==="
Write-Host "Set-Alias qstart `"$Root\scripts\start\qstart.ps1`""
Write-Host "Set-Alias qday `"$Root\scripts\start\qday.ps1`""
Write-Host "Set-Alias qreview `"$Root\scripts\start\qreview.ps1`""

Write-Host ""
Write-Host "=== Next Steps ==="
Write-Host "1. Run: $Root\scripts\start\qstart.ps1"
Write-Host "2. Run: $Root\scripts\start\qday.ps1 -Day 1"
Write-Host "3. Put bot .set files into $Root for further analysis."

if ($missing.Count -gt 0) {
    Write-Host ""
    Write-Warning "Missing tools: $($missing -join ', ')"
    Write-Host "Install them, then rerun setup.ps1."
}

