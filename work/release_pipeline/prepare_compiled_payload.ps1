[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][Alias('GameRoot')][string]$BaselineGameRoot,
    [Parameter(Mandatory=$true)][string]$EngineRoot,
    [Parameter(Mandatory=$true)][string]$EngineManifest,
    [Parameter(Mandatory=$true)][string]$ExpectedBaselineTreeSha256,
    [Parameter(Mandatory=$true)][string]$StageRoot,
    [Parameter(Mandatory=$true)][string]$ReleaseConfig,
    [Parameter(Mandatory=$true)][string]$CleanPayloadRoot,
    [Parameter(Mandatory=$true)][string]$ReportPath
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
$driverBefore = [Environment]::GetEnvironmentVariable('SDL_AUDIODRIVER','Process')
$hashSeedBefore = [Environment]::GetEnvironmentVariable('PYTHONHASHSEED','Process')
try {
    [Environment]::SetEnvironmentVariable('SDL_AUDIODRIVER','dummy','Process')
    [Environment]::SetEnvironmentVariable('PYTHONHASHSEED','0','Process')
    $orchestrator = Join-Path $PSScriptRoot 'compile_isolated_payload.py'
    if (-not (Test-Path -LiteralPath $orchestrator -PathType Leaf)) { throw 'compile_isolated_payload.py is missing.' }
    & python $orchestrator `
        --baseline-game-root $BaselineGameRoot `
        --engine-root $EngineRoot `
        --engine-manifest $EngineManifest `
        --expected-baseline-tree-sha256 $ExpectedBaselineTreeSha256 `
        --stage-root $StageRoot `
        --release-config $ReleaseConfig `
        --clean-payload-root $CleanPayloadRoot `
        --report $ReportPath
    if ($LASTEXITCODE -ne 0) { throw "Isolated compile orchestrator failed with exit code $LASTEXITCODE." }
}
finally {
    [Environment]::SetEnvironmentVariable('SDL_AUDIODRIVER',$driverBefore,'Process')
    [Environment]::SetEnvironmentVariable('PYTHONHASHSEED',$hashSeedBefore,'Process')
}