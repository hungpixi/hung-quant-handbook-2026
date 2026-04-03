param(
    [Parameter(Mandatory = $true)]
    [string]$SetFile
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $SetFile)) {
    throw "Set file not found: $SetFile"
}

$lines = Get-Content -LiteralPath $SetFile
$params = $lines | Where-Object { $_ -match '^[A-Za-z]' }
$headers = $lines | Where-Object { $_ -match '^; ===' }
$trueFlags = $params | Where-Object { $_ -match '=true\|\|false\|\|0\|\|true\|\|N$' }
$falseFlags = $params | Where-Object { $_ -match '=false\|\|false\|\|0\|\|true\|\|N$' }

Write-Host ""
Write-Host "=== Set Analysis ==="
Write-Host "File:        $SetFile"
Write-Host "Param count: $($params.Count)"
Write-Host "Groups:      $($headers.Count)"
Write-Host "Bool true:   $($trueFlags.Count)"
Write-Host "Bool false:  $($falseFlags.Count)"
Write-Host ""
Write-Host "Groups:"
$headers | ForEach-Object { Write-Host "- $_" }

Write-Host ""
Write-Host "Enabled bool flags:"
$trueFlags | ForEach-Object { Write-Host "- $_" }

