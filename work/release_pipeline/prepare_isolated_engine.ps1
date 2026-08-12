[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$BaselineGameRoot,
    [Parameter(Mandatory=$true)][string]$EngineRoot,
    [Parameter(Mandatory=$true)][string]$ReportPath
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
$utf8 = New-Object System.Text.UTF8Encoding($false, $true)

function Get-Sha256([string]$Path) {
    $stream = [IO.File]::OpenRead($Path)
    try {
        $sha = [Security.Cryptography.SHA256]::Create()
        try { return ([BitConverter]::ToString($sha.ComputeHash($stream))).Replace('-','').ToLowerInvariant() }
        finally { $sha.Dispose() }
    }
    finally { $stream.Dispose() }
}

function Get-Key([string]$Path) {
    $full = [IO.Path]::GetFullPath($Path)
    $root = [IO.Path]::GetPathRoot($full)
    if ($full.Equals($root, [StringComparison]::OrdinalIgnoreCase)) { return $root.ToLowerInvariant() }
    return $full.TrimEnd([char[]]@('\','/')).ToLowerInvariant()
}

function Test-Overlap([string]$First, [string]$Second) {
    $a = Get-Key $First
    $b = Get-Key $Second
    if ($a -eq $b) { return $true }
    $separator = [IO.Path]::DirectorySeparatorChar
    return $a.StartsWith($b.TrimEnd([char[]]@('\','/')) + $separator, [StringComparison]::OrdinalIgnoreCase) -or
           $b.StartsWith($a.TrimEnd([char[]]@('\','/')) + $separator, [StringComparison]::OrdinalIgnoreCase)
}

function Get-TreeSnapshot([string]$Root) {
    $rootFull = [IO.Path]::GetFullPath($Root).TrimEnd([char[]]@('\','/')) + [IO.Path]::DirectorySeparatorChar
    $records = @()
    foreach ($item in @(Get-ChildItem -LiteralPath $Root -Recurse -Force | Sort-Object FullName)) {
        if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Reparse point rejected in baseline tree: $($item.FullName)"
        }
        if (-not $item.PSIsContainer) {
            $relative = $item.FullName.Substring($rootFull.Length).Replace('\','/')
            $records += [PSCustomObject]@{
                path=$relative
                size=[Int64]$item.Length
                sha256=(Get-Sha256 $item.FullName)
            }
        }
    }
    return @($records)
}

function Get-SnapshotDigest($Records) {
    $builder = New-Object Text.StringBuilder
    foreach ($record in @($Records | Sort-Object path)) {
        [void]$builder.Append([string]$record.path).Append("`0").Append([string]$record.size).Append("`0").Append([string]$record.sha256).Append("`n")
    }
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes($builder.ToString())))).Replace('-','').ToLowerInvariant() }
    finally { $sha.Dispose() }
}

function Get-SnapshotDiff($Before, $After) {
    $beforeMap = @{}
    $afterMap = @{}
    foreach ($record in @($Before)) { $beforeMap[[string]$record.path] = $record }
    foreach ($record in @($After)) { $afterMap[[string]$record.path] = $record }
    $paths = @($beforeMap.Keys + $afterMap.Keys | Sort-Object -Unique)
    $differences = @()
    foreach ($path in $paths) {
        $hasBefore = $beforeMap.ContainsKey($path)
        $hasAfter = $afterMap.ContainsKey($path)
        if (-not $hasBefore) {
            $differences += [PSCustomObject]@{ path=$path; change='added'; before=$null; after=$afterMap[$path] }
        }
        elseif (-not $hasAfter) {
            $differences += [PSCustomObject]@{ path=$path; change='removed'; before=$beforeMap[$path]; after=$null }
        }
        else {
            $beforeRecord = $beforeMap[$path]
            $afterRecord = $afterMap[$path]
            if ([Int64]$beforeRecord.size -ne [Int64]$afterRecord.size -or [string]$beforeRecord.sha256 -ne [string]$afterRecord.sha256) {
                $differences += [PSCustomObject]@{ path=$path; change='modified'; before=$beforeRecord; after=$afterRecord }
            }
        }
    }
    return @($differences)
}

function Write-JsonAtomic([string]$Path, $Value, [int]$Depth=16) {
    $directory = [IO.Path]::GetDirectoryName([IO.Path]::GetFullPath($Path))
    [IO.Directory]::CreateDirectory($directory) | Out-Null
    $temporary = $Path + '.incoming-' + [Guid]::NewGuid().ToString('N')
    try {
        [IO.File]::WriteAllText($temporary, ($Value | ConvertTo-Json -Depth $Depth) + "`n", $utf8)
        if ([IO.File]::Exists($Path)) { [IO.File]::Replace($temporary, $Path, $null) }
        else { [IO.File]::Move($temporary, $Path) }
    }
    finally {
        if ([IO.File]::Exists($temporary)) { [IO.File]::Delete($temporary) }
    }
}

$baseline = [IO.Path]::GetFullPath($BaselineGameRoot)
$engine = [IO.Path]::GetFullPath($EngineRoot)
$report = [IO.Path]::GetFullPath($ReportPath)
if (-not [IO.Directory]::Exists($baseline)) { throw 'BaselineGameRoot does not exist.' }
if ([IO.Directory]::Exists($engine) -or [IO.File]::Exists($engine)) { throw 'EngineRoot must not already exist.' }
if (Test-Overlap $baseline $engine) { throw 'BaselineGameRoot and EngineRoot overlap.' }
if (Test-Overlap $baseline $report) { throw 'ReportPath must be outside the baseline game tree.' }
if (Test-Overlap $engine $report) { throw 'ReportPath must be outside the isolated engine tree.' }

$requiredFiles = @('fatal.exe','fatal.py')
$requiredDirectories = @('lib','renpy')
foreach ($relative in $requiredFiles) {
    $source = Join-Path $baseline $relative
    if (-not [IO.File]::Exists($source)) { throw "Required engine file is missing: $relative" }
    $item = Get-Item -LiteralPath $source -Force
    if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Engine source reparse point rejected: $relative" }
}
foreach ($relative in $requiredDirectories) {
    $source = Join-Path $baseline $relative
    if (-not [IO.Directory]::Exists($source)) { throw "Required engine directory is missing: $relative" }
    $item = Get-Item -LiteralPath $source -Force
    if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Engine source reparse point rejected: $relative" }
}

$before = @(Get-TreeSnapshot $baseline)
$beforeDigest = Get-SnapshotDigest $before
Write-JsonAtomic ($report + '.live_before.json') ([PSCustomObject]@{
    schema_version=1
    tree_label='baseline_game_before_engine_copy'
    file_count=@($before).Count
    tree_sha256=$beforeDigest
    files=@($before)
}) 32

$incoming = $engine + '.incoming-' + [Guid]::NewGuid().ToString('N')
$engineRecords = @()
try {
    [IO.Directory]::CreateDirectory($incoming) | Out-Null
    foreach ($relative in $requiredFiles) {
        $source = Join-Path $baseline $relative
        $destination = Join-Path $incoming $relative
        [IO.File]::Copy($source, $destination, $false)
        [IO.File]::SetLastWriteTimeUtc($destination, [IO.File]::GetLastWriteTimeUtc($source))
        $item = Get-Item -LiteralPath $destination -Force
        $engineRecords += [PSCustomObject]@{
            path=$relative.Replace('\','/')
            size=[Int64]$item.Length
            sha256=(Get-Sha256 $destination)
            last_write_time_utc=$item.LastWriteTimeUtc.ToString('o')
        }
    }
    foreach ($directoryRelative in $requiredDirectories) {
        $sourceDirectory = Join-Path $baseline $directoryRelative
        $sourcePrefix = $baseline.TrimEnd([char[]]@('\','/')) + [IO.Path]::DirectorySeparatorChar
        foreach ($item in @(Get-ChildItem -LiteralPath $sourceDirectory -Recurse -Force | Sort-Object FullName)) {
            if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Engine source reparse point rejected: $($item.FullName)" }
            $relative = $item.FullName.Substring($sourcePrefix.Length)
            $destination = Join-Path $incoming $relative
            if ($item.PSIsContainer) {
                [IO.Directory]::CreateDirectory($destination) | Out-Null
            }
            else {
                [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($destination)) | Out-Null
                [IO.File]::Copy($item.FullName, $destination, $false)
                [IO.File]::SetLastWriteTimeUtc($destination, $item.LastWriteTimeUtc)
                $copied = Get-Item -LiteralPath $destination -Force
                $engineRecords += [PSCustomObject]@{
                    path=$relative.Replace('\','/')
                    size=[Int64]$copied.Length
                    sha256=(Get-Sha256 $destination)
                    last_write_time_utc=$copied.LastWriteTimeUtc.ToString('o')
                }
            }
        }
    }

    $seen = @{}
    foreach ($record in $engineRecords) {
        $key = ([string]$record.path).ToLowerInvariant()
        if ($seen.ContainsKey($key)) { throw "Case-colliding engine record: $($record.path)" }
        $seen[$key] = $true
        $source = Join-Path $baseline ([string]$record.path).Replace('/', [IO.Path]::DirectorySeparatorChar)
        if ([Int64](Get-Item -LiteralPath $source).Length -ne [Int64]$record.size -or (Get-Sha256 $source) -ne [string]$record.sha256) {
            throw "Copied engine byte verification failed: $($record.path)"
        }
    }
    $actualFiles = @(Get-ChildItem -LiteralPath $incoming -Recurse -Force | Where-Object { -not $_.PSIsContainer })
    if ($actualFiles.Count -ne $engineRecords.Count) { throw 'Isolated engine exact file-set verification failed.' }

    [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($engine)) | Out-Null
    [IO.Directory]::Move($incoming, $engine)
}
catch {
    throw "Isolated engine copy failed; unpromoted evidence remains at the sibling .incoming directory. $($_.Exception.Message)"
}

$after = @(Get-TreeSnapshot $baseline)
$afterDigest = Get-SnapshotDigest $after
$differences = @(Get-SnapshotDiff $before $after)
Write-JsonAtomic ($report + '.live_after.json') ([PSCustomObject]@{
    schema_version=1
    tree_label='baseline_game_after_engine_copy'
    file_count=@($after).Count
    tree_sha256=$afterDigest
    files=@($after)
}) 32
Write-JsonAtomic ($report + '.live_diff.json') ([PSCustomObject]@{
    schema_version=1
    unchanged=($differences.Count -eq 0)
    difference_count=$differences.Count
    differences=@($differences)
}) 32
if ($differences.Count -ne 0) { throw 'Baseline game tree changed while preparing the isolated engine.' }

$engineDigest = Get-SnapshotDigest $engineRecords
$result = [PSCustomObject]@{
    schema_version='fatal-twelve-isolated-engine-copy-v1'
    status='PASS'
    operation='copy_only'
    process_started=$false
    copy_allowlist=@('fatal.exe','fatal.py','lib/**','renpy/**')
    engine_file_count=@($engineRecords).Count
    engine_tree_sha256=$engineDigest
    engine_files=@($engineRecords | Sort-Object path)
    baseline_file_count=@($before).Count
    baseline_tree_sha256=$beforeDigest
    baseline_unchanged=$true
}
Write-JsonAtomic $report $result 32
Write-Output "ISOLATED ENGINE COPY PASS: $(@($engineRecords).Count) files"
Write-Output "Engine tree SHA-256: $engineDigest"
Write-Output "Baseline tree SHA-256: $beforeDigest"
