param(
    [Parameter(Mandatory = $true)]
    [string]$CsvFile,
    [int]$Digits = 2,
    [int]$AtrWindow = 14
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $CsvFile)) {
    throw "CSV not found: $CsvFile"
}

$scriptPath = Join-Path $PSScriptRoot "..\analysis\price_spectrum_analyzer.py"
$resolved = (Resolve-Path $scriptPath).Path

python $resolved --csv $CsvFile --digits $Digits --atr-window $AtrWindow

