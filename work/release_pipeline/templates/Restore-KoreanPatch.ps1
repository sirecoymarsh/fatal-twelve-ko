[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$GameRoot,
    [string]$BackupRoot = '',
    [string]$StateRoot = '',
    [string]$RecoveryRoot = '',
    [int]$TestFailAfterReplacement = 0
)

$ErrorActionPreference = 'Stop'
try {
    $base = Join-Path ([Environment]::GetFolderPath('LocalApplicationData')) 'FatalTwelveKoreanPatch'
    if ([string]::IsNullOrWhiteSpace($BackupRoot)) { $BackupRoot = Join-Path $base 'backups' }
    if ([string]::IsNullOrWhiteSpace($StateRoot)) { $StateRoot = Join-Path $base 'state' }
    if ([string]::IsNullOrWhiteSpace($RecoveryRoot)) { $RecoveryRoot = Join-Path $base 'recovery' }

    $manifestPath = Join-Path $PSScriptRoot 'install_manifest.json'
    $sidecarPath = Join-Path $PSScriptRoot 'install_manifest.sha256'
    $utf8 = New-Object System.Text.UTF8Encoding($false, $true)
    $sidecar = [System.IO.File]::ReadAllText($sidecarPath, [System.Text.Encoding]::ASCII)
    $match = [regex]::Match($sidecar, '^([0-9a-f]{64}) \*install_manifest\.json\r?\n?$')
    if (-not $match.Success) { throw 'install_manifest.sha256 형식이 잘못되었습니다.' }
    $manifestHash = (Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($manifestHash -ne $match.Groups[1].Value) { throw 'install_manifest.json 해시가 일치하지 않습니다.' }
    $manifest = ([System.IO.File]::ReadAllText($manifestPath, $utf8) | ConvertFrom-Json)
    $moduleRecord = @($manifest.package_files | Where-Object { [string]$_.path -eq 'PatchCore.psm1' })
    if ($moduleRecord.Count -ne 1) { throw 'PatchCore.psm1 해시 레코드가 없습니다.' }
    $modulePath = Join-Path $PSScriptRoot 'PatchCore.psm1'
    $moduleItem = Get-Item -LiteralPath $modulePath -Force
    $moduleHash = (Get-FileHash -LiteralPath $modulePath -Algorithm SHA256).Hash.ToLowerInvariant()
    if ([Int64]$moduleItem.Length -ne [Int64]$moduleRecord[0].size -or $moduleHash -ne [string]$moduleRecord[0].sha256) {
        throw 'PatchCore.psm1 무결성 검증에 실패했습니다.'
    }
    Import-Module -Name $modulePath -Force
    Invoke-KoreanPatchRestore -GameRoot $GameRoot -PackageRoot $PSScriptRoot -BackupRoot $BackupRoot `
        -StateRoot $StateRoot -RecoveryRoot $RecoveryRoot -TestFailAfterReplacement $TestFailAfterReplacement
    exit 0
}
catch {
    [Console]::Error.WriteLine('RESTORE REJECTED: ' + $_.Exception.Message)
    exit 1
}

