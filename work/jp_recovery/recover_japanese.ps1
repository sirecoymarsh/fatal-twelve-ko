[CmdletBinding()]
param(
    [string]$GameDir = 'F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve\game',
    [string]$ProjectDir,
    [int]$Processes = 4
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ([string]::IsNullOrWhiteSpace($ProjectDir)) {
    $ProjectDir = $PSScriptRoot
}

$expected = @{
    'scenario.rpa' = 'EA39387AE13432A79FFE4601AF7B50478D063432CE3B7BC4013C92E09F036D22'
    'system.rpa'   = 'A298B88F12C98435B015A647B51F5A35987EA4D714B5BF92E90972F3FCF6B648'
}

$project = [IO.Path]::GetFullPath($ProjectDir)
$raw = Join-Path $project 'raw'
$unicode = Join-Path $project 'unicode'
$unrpyc = Join-Path $project 'tools\unrpyc\unrpyc.py'
$extractor = Join-Path $project 'extract_rpa_readonly.py'
$collector = Join-Path $project 'collect_japanese_strings.py'
$inspector = Join-Path $project 'inspect_rpyc_unicode.py'

foreach ($required in @($unrpyc, $extractor, $collector, $inspector)) {
    if (-not (Test-Path -LiteralPath $required -PathType Leaf)) {
        throw "Required tool is missing: $required"
    }
}

$archives = @()
foreach ($name in @('scenario.rpa', 'system.rpa')) {
    $path = Join-Path $GameDir $name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Source archive is missing: $path"
    }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
    if ($actual -ne $expected[$name]) {
        throw "Trusted hash mismatch for $name. Expected $($expected[$name]), got $actual"
    }
    $archives += $path
}

New-Item -ItemType Directory -Force -Path $raw, $unicode | Out-Null

# The extractor opens source archives only as rb and verifies their hashes again
# after extraction.  No command below writes under $GameDir.
& python $extractor $raw @archives --suffix '.rpyc' --manifest (Join-Path $project 'extraction_manifest.json')
if ($LASTEXITCODE -ne 0) { throw "RPA extraction failed with exit code $LASTEXITCODE" }

& python $unrpyc -c -p $Processes $raw
if ($LASTEXITCODE -ne 0) { throw "unrpyc failed with exit code $LASTEXITCODE" }

& python $collector $raw $unicode --sample-count 30
if ($LASTEXITCODE -ne 0) { throw "Japanese string collection failed with exit code $LASTEXITCODE" }

& python $inspector $raw (Join-Path $unicode 'rpyc_unicode_evidence.json')
if ($LASTEXITCODE -ne 0) { throw "RPYC Unicode inspection failed with exit code $LASTEXITCODE" }

$rpycCount = @(Get-ChildItem -LiteralPath $raw -Recurse -File | Where-Object Extension -eq '.rpyc').Count
$rpyCount = @(Get-ChildItem -LiteralPath $raw -Recurse -File | Where-Object Extension -eq '.rpy').Count
if ($rpycCount -ne 38 -or $rpyCount -ne 38) {
    throw "Unexpected script count: rpyc=$rpycCount, rpy=$rpyCount (expected 38 each)"
}

Write-Host "Recovery complete: $project"
Write-Host "RPYC/RPY files: $rpycCount / $rpyCount"
