Set-StrictMode -Version 2.0

$script:Utf8NoBomStrict = New-Object System.Text.UTF8Encoding($false, $true)
$script:ShaPattern = '^[0-9a-f]{64}$'
$script:PatchIdPattern = '^[a-z0-9][a-z0-9._-]{0,63}$'

function Get-FileSha256 {
    param([Parameter(Mandatory=$true)][string]$Path)
    $stream = [System.IO.File]::OpenRead($Path)
    try {
        $sha = [System.Security.Cryptography.SHA256]::Create()
        try {
            $bytes = $sha.ComputeHash($stream)
            return ([System.BitConverter]::ToString($bytes)).Replace('-', '').ToLowerInvariant()
        }
        finally { $sha.Dispose() }
    }
    finally { $stream.Dispose() }
}

function Read-JsonUtf8 {
    param([Parameter(Mandatory=$true)][string]$Path)
    $text = [System.IO.File]::ReadAllText($Path, $script:Utf8NoBomStrict)
    if ($text.Length -gt 0 -and [int]$text[0] -eq 0xFEFF) { throw "UTF-8 BOM is not accepted: $Path" }
    try { return ($text | ConvertFrom-Json) }
    catch { throw "Invalid JSON: $Path : $($_.Exception.Message)" }
}

function Write-JsonAtomic {
    param([Parameter(Mandatory=$true)]$Value, [Parameter(Mandatory=$true)][string]$Path)
    $parent = [System.IO.Path]::GetDirectoryName($Path)
    if (-not [System.IO.Directory]::Exists($parent)) { [System.IO.Directory]::CreateDirectory($parent) | Out-Null }
    $temp = $Path + '.tmp-' + [Guid]::NewGuid().ToString('N')
    $json = ($Value | ConvertTo-Json -Depth 32)
    [System.IO.File]::WriteAllText($temp, $json + "`n", $script:Utf8NoBomStrict)
    try {
        if ([System.IO.File]::Exists($Path)) {
            $old = $Path + '.old-' + [Guid]::NewGuid().ToString('N')
            [System.IO.File]::Replace($temp, $Path, $old, $true)
            if ([System.IO.File]::Exists($old)) { [System.IO.File]::Delete($old) }
        }
        else { [System.IO.File]::Move($temp, $Path) }
    }
    finally { if ([System.IO.File]::Exists($temp)) { [System.IO.File]::Delete($temp) } }
}

function Get-CanonicalFullPath {
    param([Parameter(Mandatory=$true)][string]$Path)
    if ([string]::IsNullOrWhiteSpace($Path)) { throw 'Empty path is not accepted.' }
    return [System.IO.Path]::GetFullPath($Path)
}

function Get-PathKey {
    param([Parameter(Mandatory=$true)][string]$Path)
    $full = Get-CanonicalFullPath $Path
    $root = [System.IO.Path]::GetPathRoot($full)
    if ($full.Equals($root, [StringComparison]::OrdinalIgnoreCase)) { return $root.ToLowerInvariant() }
    return $full.TrimEnd([char[]]@('\','/')).ToLowerInvariant()
}

function Test-PathOverlap {
    param([Parameter(Mandatory=$true)][string]$First, [Parameter(Mandatory=$true)][string]$Second)
    $a = Get-PathKey $First
    $b = Get-PathKey $Second
    if ($a -eq $b) { return $true }
    $sep = [System.IO.Path]::DirectorySeparatorChar
    return $a.StartsWith($b.TrimEnd([char[]]@('\','/')) + $sep, [StringComparison]::OrdinalIgnoreCase) -or
           $b.StartsWith($a.TrimEnd([char[]]@('\','/')) + $sep, [StringComparison]::OrdinalIgnoreCase)
}

function Test-PathWithinOrSame {
    param([Parameter(Mandatory=$true)][string]$Child, [Parameter(Mandatory=$true)][string]$Parent)
    $childKey = Get-PathKey $Child
    $parentKey = Get-PathKey $Parent
    if ($childKey -eq $parentKey) { return $true }
    $prefix = $parentKey.TrimEnd([char[]]@('\','/')) + [System.IO.Path]::DirectorySeparatorChar
    return $childKey.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)
}

function Assert-NoReparseAncestry {
    param([Parameter(Mandatory=$true)][string]$Path, [Parameter(Mandatory=$true)][string]$Label)
    $current = Get-CanonicalFullPath $Path
    while (-not ([System.IO.Directory]::Exists($current) -or [System.IO.File]::Exists($current))) {
        $parent = [System.IO.Path]::GetDirectoryName($current)
        if ([string]::IsNullOrEmpty($parent) -or $parent -eq $current) { break }
        $current = $parent
    }
    while (-not [string]::IsNullOrEmpty($current)) {
        if ([System.IO.Directory]::Exists($current) -or [System.IO.File]::Exists($current)) {
            $item = Get-Item -LiteralPath $current -Force
            if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw "$Label has a reparse-point ancestor: $current"
            }
        }
        $root = [System.IO.Path]::GetPathRoot($current)
        if ($current.Equals($root, [StringComparison]::OrdinalIgnoreCase)) { break }
        $current = [System.IO.Path]::GetDirectoryName($current)
    }
}

function Assert-ExternalRoots {
    param(
        [Parameter(Mandatory=$true)][string]$GameRoot,
        [Parameter(Mandatory=$true)][string]$PackageRoot,
        [Parameter(Mandatory=$true)][string]$BackupRoot,
        [Parameter(Mandatory=$true)][string]$StateRoot,
        [Parameter(Mandatory=$true)][string]$RecoveryRoot
    )
    $externals = @(
        [PSCustomObject]@{ Name='BackupRoot'; Path=(Get-CanonicalFullPath $BackupRoot) },
        [PSCustomObject]@{ Name='StateRoot'; Path=(Get-CanonicalFullPath $StateRoot) },
        [PSCustomObject]@{ Name='RecoveryRoot'; Path=(Get-CanonicalFullPath $RecoveryRoot) }
    )
    if (Test-PathOverlap $GameRoot $PackageRoot) { throw 'GameRoot and PackageRoot must not overlap.' }
    foreach ($entry in $externals) {
        Assert-NoReparseAncestry -Path $entry.Path -Label $entry.Name
        if (Test-PathOverlap $entry.Path $GameRoot) { throw "$($entry.Name) overlaps GameRoot." }
        if (Test-PathOverlap $entry.Path $PackageRoot) { throw "$($entry.Name) overlaps PackageRoot." }
    }
    for ($i = 0; $i -lt $externals.Count; $i++) {
        for ($j = $i + 1; $j -lt $externals.Count; $j++) {
            if (Test-PathOverlap $externals[$i].Path $externals[$j].Path) {
                throw "$($externals[$i].Name) and $($externals[$j].Name) overlap. Use sibling directories."
            }
        }
    }
    return $externals
}

function Assert-RelativePath {
    param([Parameter(Mandatory=$true)][string]$Path, [Parameter(Mandatory=$true)][string]$Label)
    if ([string]::IsNullOrWhiteSpace($Path) -or $Path.Contains('\') -or $Path.StartsWith('/') -or
        [System.IO.Path]::IsPathRooted($Path) -or $Path.Contains(':')) { throw "$Label is not a canonical '/' relative path: $Path" }
    $parts = @($Path.Split('/'))
    if ($parts.Count -eq 0) { throw "$Label is empty." }
    foreach ($part in $parts) { if ([string]::IsNullOrEmpty($part) -or $part -eq '.' -or $part -eq '..') { throw "$Label escapes its root: $Path" } }
    return $Path
}

function Join-SafeRelativePath {
    param([Parameter(Mandatory=$true)][string]$Root, [Parameter(Mandatory=$true)][string]$Relative, [Parameter(Mandatory=$true)][string]$Label)
    Assert-RelativePath $Relative $Label | Out-Null
    $candidate = Get-CanonicalFullPath (Join-Path $Root ($Relative.Replace('/', [System.IO.Path]::DirectorySeparatorChar)))
    $rootKey = Get-PathKey $Root
    $candidateKey = Get-PathKey $candidate
    $prefix = $rootKey.TrimEnd([char[]]@('\','/')) + [System.IO.Path]::DirectorySeparatorChar
    if (-not $candidateKey.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) { throw "$Label escapes root: $Relative" }
    return $candidate
}

function Get-RelativeForwardPath {
    param([Parameter(Mandatory=$true)][string]$Root, [Parameter(Mandatory=$true)][string]$Path)
    $rootFull = (Get-CanonicalFullPath $Root).TrimEnd([char[]]@('\','/')) + [System.IO.Path]::DirectorySeparatorChar
    $pathFull = Get-CanonicalFullPath $Path
    if (-not $pathFull.StartsWith($rootFull, [StringComparison]::OrdinalIgnoreCase)) { throw "Path is outside root: $Path" }
    return $pathFull.Substring($rootFull.Length).Replace('\','/')
}

function Assert-HashRecord {
    param($Record, [Parameter(Mandatory=$true)][string]$Label)
    if ($null -eq $Record) { throw "$Label is missing." }
    $size = [Int64]$Record.size
    if ($size -lt 0) { throw "$Label size is invalid." }
    $digest = [string]$Record.sha256
    if (-not [regex]::IsMatch($digest, $script:ShaPattern)) { throw "$Label SHA-256 is invalid." }
}

function Assert-FileHash {
    param([Parameter(Mandatory=$true)][string]$Path, [Parameter(Mandatory=$true)][Int64]$Size,
          [Parameter(Mandatory=$true)][string]$Sha256, [Parameter(Mandatory=$true)][string]$Label)
    if (-not [System.IO.File]::Exists($Path)) { throw "$Label is missing: $Path" }
    $item = Get-Item -LiteralPath $Path -Force
    if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) { throw "$Label is a reparse point: $Path" }
    if ([Int64]$item.Length -ne $Size) { throw "$Label size mismatch: $Path" }
    $actual = Get-FileSha256 $Path
    if (-not $actual.Equals($Sha256, [StringComparison]::Ordinal)) { throw "$Label hash mismatch: $Path" }
}

function Get-PackageContext {
    param([Parameter(Mandatory=$true)][string]$PackageRoot)
    $package = Get-CanonicalFullPath $PackageRoot
    $manifestPath = Join-Path $package 'install_manifest.json'
    $sidecarPath = Join-Path $package 'install_manifest.sha256'
    if (-not [System.IO.File]::Exists($manifestPath) -or -not [System.IO.File]::Exists($sidecarPath)) { throw 'Package manifest or its hash sidecar is missing.' }
    $sidecar = [System.IO.File]::ReadAllText($sidecarPath, [System.Text.Encoding]::ASCII)
    $match = [regex]::Match($sidecar, '^([0-9a-f]{64}) \*install_manifest\.json\r?\n?$')
    if (-not $match.Success) { throw 'install_manifest.sha256 has an invalid format.' }
    $manifestSha = $match.Groups[1].Value
    if (-not (Get-FileSha256 $manifestPath).Equals($manifestSha, [StringComparison]::Ordinal)) { throw 'install_manifest.json hash does not match its sidecar.' }
    $manifest = Read-JsonUtf8 $manifestPath
    if ([int]$manifest.schema_version -ne 1) { throw 'Unsupported install manifest schema.' }
    if (-not [regex]::IsMatch([string]$manifest.patch_id, $script:PatchIdPattern)) { throw 'Invalid patch_id in manifest.' }
    $payload = @($manifest.payload)
    $packageFiles = @($manifest.package_files)
    $anchors = @($manifest.game.anchors)
    $profiles = @($manifest.supported_prestate_profiles)
    if ($payload.Count -eq 0 -or $packageFiles.Count -eq 0 -or $anchors.Count -eq 0 -or $profiles.Count -eq 0) { throw 'Manifest has an empty required list.' }

    $expected = @{}
    foreach ($record in $packageFiles) {
        $rel = [string]$record.path
        Assert-RelativePath $rel 'package_files.path' | Out-Null
        if ($expected.ContainsKey($rel.ToLowerInvariant())) { throw "Duplicate package path: $rel" }
        Assert-HashRecord $record "package file $rel"
        $expected[$rel.ToLowerInvariant()] = $rel
        $full = Join-SafeRelativePath $package $rel 'package file path'
        Assert-FileHash $full ([Int64]$record.size) ([string]$record.sha256) "package file $rel"
    }
    $expected['install_manifest.json'] = 'install_manifest.json'
    $expected['install_manifest.sha256'] = 'install_manifest.sha256'
    $actual = @{}
    $allItems = @(Get-ChildItem -LiteralPath $package -Recurse -Force)
    foreach ($item in $allItems) {
        if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Package reparse point rejected: $($item.FullName)" }
        if (-not $item.PSIsContainer) {
            $rel = Get-RelativeForwardPath $package $item.FullName
            $key = $rel.ToLowerInvariant()
            if ($actual.ContainsKey($key)) { throw "Package contains a case-colliding path: $rel" }
            $actual[$key] = $rel
        }
    }
    if ($actual.Count -ne $expected.Count) { throw "Package file count mismatch: expected $($expected.Count), found $($actual.Count)." }
    foreach ($key in $expected.Keys) { if (-not $actual.ContainsKey($key)) { throw "Package is missing or renamed: $($expected[$key])" } }

    $payloadPaths = @{}
    foreach ($entry in $payload) {
        $rel = [string]$entry.path
        Assert-RelativePath $rel 'payload.path' | Out-Null
        if (-not $rel.StartsWith('game/', [StringComparison]::Ordinal) -or -not $rel.EndsWith('.rpyc', [StringComparison]::OrdinalIgnoreCase)) { throw "Only compiled game/*.rpyc payload is accepted: $rel" }
        $key = $rel.ToLowerInvariant()
        if ($payloadPaths.ContainsKey($key)) { throw "Duplicate payload path: $rel" }
        $payloadPaths[$key] = $entry
        Assert-HashRecord $entry "payload $rel"
        $packageRel = 'payload/' + $rel
        if (-not $expected.ContainsKey($packageRel.ToLowerInvariant())) { throw "Payload is absent from package_files: $rel" }
        $pRecord = $null
        foreach ($candidate in $packageFiles) { if ([string]$candidate.path -eq $packageRel) { $pRecord = $candidate; break } }
        if ($null -eq $pRecord -or [Int64]$pRecord.size -ne [Int64]$entry.size -or [string]$pRecord.sha256 -ne [string]$entry.sha256) { throw "Payload/package hash records disagree: $rel" }
        $stateSignatures = @{}
        $stateIds = @{}
        foreach ($state in @($entry.pre_states)) {
            $sid = [string]$state.id
            if (-not [regex]::IsMatch($sid, $script:PatchIdPattern) -or $stateIds.ContainsKey($sid)) { throw "Invalid/duplicate pre-state id for $rel" }
            $stateIds[$sid] = $true
            if ([string]$state.kind -eq 'absent') { $signature = 'absent' }
            elseif ([string]$state.kind -eq 'file') { Assert-HashRecord $state "pre-state $rel/$sid"; $signature = "file:$($state.size):$($state.sha256)" }
            else { throw "Invalid pre-state kind for $rel/$sid" }
            if ($stateSignatures.ContainsKey($signature)) { throw "Duplicate pre-state signature for $rel" }
            $stateSignatures[$signature] = $true
        }
    }
    foreach ($anchor in $anchors) {
        $rel = [string]$anchor.path
        Assert-RelativePath $rel 'anchor.path' | Out-Null
        if ($payloadPaths.ContainsKey($rel.ToLowerInvariant())) { throw "Anchor and payload overlap: $rel" }
        if (@($anchor.accepted).Count -eq 0) { throw "Anchor has no accepted hashes: $rel" }
        foreach ($accepted in @($anchor.accepted)) { Assert-HashRecord $accepted "anchor $rel" }
    }
    foreach ($profile in $profiles) {
        $refs = @($profile.states)
        if ($refs.Count -ne $payload.Count) { throw "Profile does not cover every payload path: $($profile.id)" }
        $seen = @{}
        foreach ($ref in $refs) {
            $path = [string]$ref.path
            $key = $path.ToLowerInvariant()
            if (-not $payloadPaths.ContainsKey($key) -or $seen.ContainsKey($key)) { throw "Profile contains an unknown/duplicate path: $($profile.id)/$path" }
            $seen[$key] = $true
            $found = $false
            foreach ($state in @($payloadPaths[$key].pre_states)) { if ([string]$state.id -eq [string]$ref.state_id) { $found = $true; break } }
            if (-not $found) { throw "Profile references an unknown pre-state: $($profile.id)/$path" }
        }
    }
    return [PSCustomObject]@{ PackageRoot=$package; ManifestPath=$manifestPath; ManifestSha256=$manifestSha; Manifest=$manifest }
}

function Assert-TargetProcessStopped {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Manifest)
    $rel = [string]$Manifest.game.process_executable_relative_path
    $target = Join-SafeRelativePath $GameRoot $rel 'process executable path'
    $targetKey = Get-PathKey $target
    foreach ($process in @(Get-Process -ErrorAction SilentlyContinue)) {
        try { $running = [string]$process.MainModule.FileName } catch { continue }
        if (-not [string]::IsNullOrEmpty($running) -and (Get-PathKey $running) -eq $targetKey) {
            throw "The exact target game executable is running (PID $($process.Id)). Close it first."
        }
    }
}

function Assert-GameAnchors {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Manifest)
    foreach ($anchor in @($Manifest.game.anchors)) {
        $rel = [string]$anchor.path
        $path = Join-SafeRelativePath $GameRoot $rel 'anchor path'
        if (-not [System.IO.File]::Exists($path)) { throw "Trusted baseline anchor is missing: $rel" }
        $item = Get-Item -LiteralPath $path -Force
        if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Anchor reparse point rejected: $rel" }
        $digest = Get-FileSha256 $path
        $matched = $false
        foreach ($accepted in @($anchor.accepted)) {
            if ([Int64]$accepted.size -eq [Int64]$item.Length -and [string]$accepted.sha256 -eq $digest) { $matched = $true; break }
        }
        if (-not $matched) { throw "Trusted baseline anchor hash rejected: $rel" }
    }
}

function Get-PayloadEntryMap {
    param([Parameter(Mandatory=$true)]$Manifest)
    $map = @{}
    foreach ($entry in @($Manifest.payload)) { $map[[string]$entry.path] = $entry }
    return $map
}

function Get-CurrentPreState {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Entry)
    $rel = [string]$Entry.path
    $target = Join-SafeRelativePath $GameRoot $rel 'payload target path'
    if (-not (Test-Path -LiteralPath $target)) {
        foreach ($state in @($Entry.pre_states)) { if ([string]$state.kind -eq 'absent') { return $state } }
        throw "Target is absent but that state is not supported: $rel"
    }
    if (-not [System.IO.File]::Exists($target)) { throw "Payload target is not a regular file: $rel" }
    $item = Get-Item -LiteralPath $target -Force
    if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Payload target reparse point rejected: $rel" }
    $digest = Get-FileSha256 $target
    $matches = @()
    foreach ($state in @($Entry.pre_states)) {
        if ([string]$state.kind -eq 'file' -and [Int64]$state.size -eq [Int64]$item.Length -and [string]$state.sha256 -eq $digest) { $matches += $state }
    }
    if ($matches.Count -ne 1) { throw "Target hash is unknown or ambiguously declared: $rel" }
    return $matches[0]
}

function Get-SupportedCurrentProfile {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Manifest)
    $stateByPath = @{}
    foreach ($entry in @($Manifest.payload)) { $stateByPath[[string]$entry.path] = Get-CurrentPreState $GameRoot $entry }
    $matches = @()
    foreach ($profile in @($Manifest.supported_prestate_profiles)) {
        $ok = $true
        foreach ($ref in @($profile.states)) {
            if ([string]$stateByPath[[string]$ref.path].id -ne [string]$ref.state_id) { $ok = $false; break }
        }
        if ($ok) { $matches += $profile }
    }
    if ($matches.Count -ne 1) {
        $summary = @($stateByPath.Keys | Sort-Object | ForEach-Object { "$_=$([string]$stateByPath[$_].id)" }) -join '; '
        throw "The exact target mixture is not an approved pre-state profile: $summary"
    }
    return [PSCustomObject]@{ Profile=$matches[0]; StateByPath=$stateByPath }
}

function Test-AllTargetsPatched {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Manifest)
    foreach ($entry in @($Manifest.payload)) {
        $target = Join-SafeRelativePath $GameRoot ([string]$entry.path) 'payload target path'
        if (-not [System.IO.File]::Exists($target)) { return $false }
        $item = Get-Item -LiteralPath $target -Force
        if ([Int64]$item.Length -ne [Int64]$entry.size -or (Get-FileSha256 $target) -ne [string]$entry.sha256) { return $false }
    }
    return $true
}

function Assert-AllTargetsPatched {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Manifest)
    if (-not (Test-AllTargetsPatched $GameRoot $Manifest)) { throw 'Installed Korean payload hashes do not match the package.' }
}

function Copy-VerifiedFile {
    param([Parameter(Mandatory=$true)][string]$Source, [Parameter(Mandatory=$true)][string]$Destination,
          [Parameter(Mandatory=$true)][Int64]$Size, [Parameter(Mandatory=$true)][string]$Sha256,
          [Parameter(Mandatory=$true)][string]$Label)
    $parent = [System.IO.Path]::GetDirectoryName($Destination)
    if (-not [System.IO.Directory]::Exists($parent)) { [System.IO.Directory]::CreateDirectory($parent) | Out-Null }
    [System.IO.File]::Copy($Source, $Destination, $true)
    Assert-FileHash $Destination $Size $Sha256 $Label
}

function Replace-WithIncoming {
    param([Parameter(Mandatory=$true)][string]$Incoming, [Parameter(Mandatory=$true)][string]$Target,
          [Parameter(Mandatory=$true)][string]$ReplacementBackup)
    if ([System.IO.File]::Exists($ReplacementBackup)) { [System.IO.File]::Delete($ReplacementBackup) }
    if ([System.IO.File]::Exists($Target)) { [System.IO.File]::Replace($Incoming, $Target, $ReplacementBackup, $true) }
    else { [System.IO.File]::Move($Incoming, $Target) }
}

function Remove-EmptyPlannedDirectories {
    param($Directories)
    foreach ($dir in @($Directories | Sort-Object { ([string]$_).Length } -Descending)) {
        if ([System.IO.Directory]::Exists([string]$dir) -and (Get-ChildItem -LiteralPath ([string]$dir) -Force | Measure-Object).Count -eq 0) {
            [System.IO.Directory]::Delete([string]$dir)
        }
    }
}

function Remove-TransactionTemps {
    param([Parameter(Mandatory=$true)]$Journal)
    foreach ($entry in @($Journal.entries)) {
        foreach ($name in @('incoming_path','replacement_backup_path')) {
            $path = [string]$entry.$name
            if (-not [string]::IsNullOrEmpty($path) -and [System.IO.File]::Exists($path)) { [System.IO.File]::Delete($path) }
        }
    }
    Remove-EmptyPlannedDirectories @($Journal.planned_created_directories)
}

function Assert-TransactionEntrySet {
    param([Parameter(Mandatory=$true)]$Entries, [Parameter(Mandatory=$true)]$Context,
          [Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)][string]$BackupDirectory,
          [Parameter(Mandatory=$true)][string]$RecoveryDirectory, [Parameter(Mandatory=$true)][string]$TransactionId,
          [string]$ExpectedProfileId='')
    if (-not [regex]::IsMatch($TransactionId, '^\d{8}T\d{13}Z-[0-9a-f]{32}$')) { throw 'Transaction id is invalid.' }
    $entryMap = Get-PayloadEntryMap $Context.Manifest
    $items = @($Entries)
    if ($items.Count -ne $entryMap.Count) { throw 'Transaction entry count mismatch.' }
    $seen = @{}
    $stateByPath = @{}
    foreach ($entry in $items) {
        $rel = [string]$entry.path
        if (-not $entryMap.ContainsKey($rel) -or $seen.ContainsKey($rel)) { throw "Transaction contains an unknown/duplicate path: $rel" }
        $seen[$rel] = $true
        $payloadEntry = $entryMap[$rel]
        $declared = @($payloadEntry.pre_states | Where-Object { [string]$_.id -eq [string]$entry.pre_state_id })
        if ($declared.Count -ne 1) { throw "Transaction references an unknown pre-state: $rel/$($entry.pre_state_id)" }
        $pre = $declared[0]
        if ([string]$entry.pre_kind -ne [string]$pre.kind) { throw "Transaction pre-kind differs from manifest: $rel" }
        if ([string]$pre.kind -eq 'file') {
            if ([Int64]$entry.pre_size -ne [Int64]$pre.size -or [string]$entry.pre_sha256 -ne [string]$pre.sha256) { throw "Transaction pre-state hash differs from manifest: $rel" }
        }
        elseif (-not [string]::IsNullOrEmpty([string]$entry.backup_path)) { throw "Absent pre-state unexpectedly names a backup file: $rel" }
        $stateByPath[$rel] = [string]$pre.id

        $targetExpected = Join-SafeRelativePath $GameRoot $rel 'transaction target path'
        if ((Get-PathKey ([string]$entry.target_path)) -ne (Get-PathKey $targetExpected)) { throw "Transaction target path mismatch: $rel" }
        $backupExpected = Join-SafeRelativePath $BackupDirectory $rel 'transaction backup path'
        if ([string]$pre.kind -eq 'file' -and (Get-PathKey ([string]$entry.backup_path)) -ne (Get-PathKey $backupExpected)) { throw "Transaction backup path mismatch: $rel" }
        $recoveryExpected = Join-SafeRelativePath $RecoveryDirectory $rel 'transaction recovery path'
        if ((Get-PathKey ([string]$entry.recovery_path)) -ne (Get-PathKey $recoveryExpected)) { throw "Transaction recovery path mismatch: $rel" }
        $targetDir = [System.IO.Path]::GetDirectoryName($targetExpected)
        $leaf = [System.IO.Path]::GetFileName($targetExpected)
        $incomingExpected = Join-Path $targetDir ('.' + $leaf + '.fatal12ko-' + $TransactionId + '.incoming')
        $replacementExpected = Join-Path $targetDir ('.' + $leaf + '.fatal12ko-' + $TransactionId + '.replace-backup')
        if ((Get-PathKey ([string]$entry.incoming_path)) -ne (Get-PathKey $incomingExpected) -or
            (Get-PathKey ([string]$entry.replacement_backup_path)) -ne (Get-PathKey $replacementExpected)) {
            throw "Transaction temporary path mismatch: $rel"
        }
        Assert-FileHash ([string]$entry.recovery_path) ([Int64]$payloadEntry.size) ([string]$payloadEntry.sha256) "patched recovery copy $rel"
        if ([string]$pre.kind -eq 'file') { Assert-FileHash ([string]$entry.backup_path) ([Int64]$pre.size) ([string]$pre.sha256) "original backup $rel" }
    }
    $profileMatches = @()
    foreach ($profile in @($Context.Manifest.supported_prestate_profiles)) {
        $ok = $true
        foreach ($ref in @($profile.states)) {
            if ([string]$stateByPath[[string]$ref.path] -ne [string]$ref.state_id) { $ok = $false; break }
        }
        if ($ok) { $profileMatches += $profile }
    }
    if ($profileMatches.Count -ne 1) { throw 'Transaction entries do not form exactly one supported pre-state profile.' }
    $profileId = [string]$profileMatches[0].id
    if (-not [string]::IsNullOrEmpty($ExpectedProfileId) -and $profileId -ne $ExpectedProfileId) { throw 'Transaction profile id does not match its exact entry states.' }
    return $profileId
}

function Assert-JournalShapeAndSources {
    param([Parameter(Mandatory=$true)]$Journal, [Parameter(Mandatory=$true)]$Context,
          [Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)][string]$BackupRoot,
          [Parameter(Mandatory=$true)][string]$RecoveryRoot)
    if ([string]$Journal.patch_id -ne [string]$Context.Manifest.patch_id -or [string]$Journal.manifest_sha256 -ne $Context.ManifestSha256) { throw 'Transaction journal belongs to another package.' }
    if ([string]$Journal.operation -ne 'install' -and [string]$Journal.operation -ne 'restore') { throw 'Transaction journal operation is invalid.' }
    if ((Get-PathKey ([string]$Journal.game_root)) -ne (Get-PathKey $GameRoot)) { throw 'Transaction journal GameRoot mismatch.' }
    $txId = [string]$Journal.transaction_id
    $patchId = [string]$Context.Manifest.patch_id
    $expectedBackup = Join-Path (Join-Path $BackupRoot $patchId) $txId
    $expectedRecovery = Join-Path (Join-Path $RecoveryRoot $patchId) $txId
    if ((Get-PathKey ([string]$Journal.backup_directory)) -ne (Get-PathKey $expectedBackup)) { throw 'Transaction backup directory mismatch.' }
    if ((Get-PathKey ([string]$Journal.recovery_directory)) -ne (Get-PathKey $expectedRecovery)) { throw 'Transaction recovery directory mismatch.' }
    $null = Assert-TransactionEntrySet @($Journal.entries) $Context $GameRoot $expectedBackup $expectedRecovery $txId

    $allowedDirectories = @{}
    foreach ($payloadEntry in @($Context.Manifest.payload)) {
        $target = Join-SafeRelativePath $GameRoot ([string]$payloadEntry.path) 'payload target path'
        $dir = [System.IO.Path]::GetDirectoryName($target)
        while ((Test-PathWithinOrSame $dir $GameRoot) -and (Get-PathKey $dir) -ne (Get-PathKey $GameRoot)) {
            $allowedDirectories[(Get-PathKey $dir)] = $true
            $dir = [System.IO.Path]::GetDirectoryName($dir)
        }
    }
    foreach ($dir in @($Journal.planned_created_directories)) {
        if (-not $allowedDirectories.ContainsKey((Get-PathKey ([string]$dir)))) { throw "Journal cleanup directory is outside the payload ancestor set: $dir" }
    }
}

function Restore-DesiredStateFromJournal {
    param([Parameter(Mandatory=$true)]$Journal, [Parameter(Mandatory=$true)]$Context,
          [ValidateSet('pre','patched')][string]$Desired)
    foreach ($entry in @($Journal.entries)) {
        $target = [string]$entry.target_path
        $incoming = [string]$entry.incoming_path
        $replacement = [string]$entry.replacement_backup_path
        $parent = [System.IO.Path]::GetDirectoryName($target)
        if (-not [System.IO.Directory]::Exists($parent)) { [System.IO.Directory]::CreateDirectory($parent) | Out-Null }
        if ($Desired -eq 'pre') {
            if ([string]$entry.pre_kind -eq 'absent') {
                if ([System.IO.File]::Exists($target)) { [System.IO.File]::Delete($target) }
            }
            else {
                Copy-VerifiedFile ([string]$entry.backup_path) $incoming ([Int64]$entry.pre_size) ([string]$entry.pre_sha256) "rollback incoming $($entry.path)"
                Replace-WithIncoming $incoming $target $replacement
                Assert-FileHash $target ([Int64]$entry.pre_size) ([string]$entry.pre_sha256) "rolled-back target $($entry.path)"
            }
        }
        else {
            $payloadEntry = $null
            foreach ($candidate in @($Context.Manifest.payload)) { if ([string]$candidate.path -eq [string]$entry.path) { $payloadEntry = $candidate; break } }
            Copy-VerifiedFile ([string]$entry.recovery_path) $incoming ([Int64]$payloadEntry.size) ([string]$payloadEntry.sha256) "restore rollback incoming $($entry.path)"
            Replace-WithIncoming $incoming $target $replacement
            Assert-FileHash $target ([Int64]$payloadEntry.size) ([string]$payloadEntry.sha256) "restore rolled-back target $($entry.path)"
        }
    }
    Remove-TransactionTemps $Journal
}

function Test-ExactJournalPreState {
    param([Parameter(Mandatory=$true)]$Journal)
    foreach ($entry in @($Journal.entries)) {
        $target = [string]$entry.target_path
        if ([string]$entry.pre_kind -eq 'absent') { if (Test-Path -LiteralPath $target) { return $false } }
        else {
            if (-not [System.IO.File]::Exists($target)) { return $false }
            $item = Get-Item -LiteralPath $target -Force
            if ([Int64]$item.Length -ne [Int64]$entry.pre_size -or (Get-FileSha256 $target) -ne [string]$entry.pre_sha256) { return $false }
        }
    }
    return $true
}

function Recover-IncompleteTransaction {
    param([Parameter(Mandatory=$true)][string]$JournalPath, [Parameter(Mandatory=$true)][string]$InstalledStatePath,
          [Parameter(Mandatory=$true)]$Context, [Parameter(Mandatory=$true)][string]$GameRoot,
          [Parameter(Mandatory=$true)][string]$BackupRoot, [Parameter(Mandatory=$true)][string]$RecoveryRoot)
    if (-not [System.IO.File]::Exists($JournalPath)) { return }
    $journal = Read-JsonUtf8 $JournalPath
    Assert-JournalShapeAndSources $journal $Context $GameRoot $BackupRoot $RecoveryRoot
    if ([string]$journal.operation -eq 'install') {
        if ([System.IO.File]::Exists($InstalledStatePath)) {
            $state = Read-JsonUtf8 $InstalledStatePath
            if ([string]$state.transaction_id -eq [string]$journal.transaction_id -and (Test-AllTargetsPatched $GameRoot $Context.Manifest)) {
                Remove-TransactionTemps $journal
                [System.IO.File]::Delete($JournalPath)
                return
            }
        }
        Restore-DesiredStateFromJournal $journal $Context 'pre'
        if (-not (Test-ExactJournalPreState $journal)) { throw 'Interrupted install recovery could not verify the pre-install state.' }
        if ([System.IO.File]::Exists($InstalledStatePath)) { [System.IO.File]::Delete($InstalledStatePath) }
        [System.IO.File]::Delete($JournalPath)
    }
    else {
        if (-not [System.IO.File]::Exists($InstalledStatePath) -and (Test-ExactJournalPreState $journal)) {
            Remove-TransactionTemps $journal
            [System.IO.File]::Delete($JournalPath)
            return
        }
        Restore-DesiredStateFromJournal $journal $Context 'patched'
        Assert-AllTargetsPatched $GameRoot $Context.Manifest
        [System.IO.File]::Delete($JournalPath)
    }
}

function New-PlannedCreatedDirectories {
    param([Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Manifest)
    $dirs = @{}
    foreach ($entry in @($Manifest.payload)) {
        $target = Join-SafeRelativePath $GameRoot ([string]$entry.path) 'payload target path'
        $dir = [System.IO.Path]::GetDirectoryName($target)
        while (-not [System.IO.Directory]::Exists($dir) -and (Get-PathKey $dir) -ne (Get-PathKey $GameRoot)) {
            $dirs[(Get-PathKey $dir)] = $dir
            $dir = [System.IO.Path]::GetDirectoryName($dir)
        }
    }
    return @($dirs.Values | Sort-Object { ([string]$_).Length })
}

function New-TransactionArtifacts {
    param([Parameter(Mandatory=$true)]$Context, [Parameter(Mandatory=$true)][string]$GameRoot,
          [Parameter(Mandatory=$true)][string]$BackupRoot, [Parameter(Mandatory=$true)][string]$RecoveryRoot,
          [Parameter(Mandatory=$true)]$CurrentProfile)
    $txId = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssfffffffZ') + '-' + [Guid]::NewGuid().ToString('N')
    $patchId = [string]$Context.Manifest.patch_id
    $backupDir = Join-Path (Join-Path $BackupRoot $patchId) $txId
    $recoveryDir = Join-Path (Join-Path $RecoveryRoot $patchId) $txId
    [System.IO.Directory]::CreateDirectory($backupDir) | Out-Null
    [System.IO.Directory]::CreateDirectory($recoveryDir) | Out-Null
    $entries = @()
    foreach ($payloadEntry in @($Context.Manifest.payload)) {
        $rel = [string]$payloadEntry.path
        $pre = $CurrentProfile.StateByPath[$rel]
        $target = Join-SafeRelativePath $GameRoot $rel 'payload target path'
        $targetDir = [System.IO.Path]::GetDirectoryName($target)
        $leaf = [System.IO.Path]::GetFileName($target)
        $incoming = Join-Path $targetDir ('.' + $leaf + '.fatal12ko-' + $txId + '.incoming')
        $replacement = Join-Path $targetDir ('.' + $leaf + '.fatal12ko-' + $txId + '.replace-backup')
        $backupPath = $null
        if ([string]$pre.kind -eq 'file') {
            $backupPath = Join-SafeRelativePath $backupDir $rel 'backup path'
            Copy-VerifiedFile $target $backupPath ([Int64]$pre.size) ([string]$pre.sha256) "backup $rel"
        }
        $recoveryPath = Join-SafeRelativePath $recoveryDir $rel 'recovery path'
        $packagePath = Join-SafeRelativePath (Join-Path $Context.PackageRoot 'payload') $rel 'package payload path'
        Copy-VerifiedFile $packagePath $recoveryPath ([Int64]$payloadEntry.size) ([string]$payloadEntry.sha256) "recovery copy $rel"
        $entries += [PSCustomObject]@{
            path=$rel; target_path=$target; pre_state_id=[string]$pre.id; pre_kind=[string]$pre.kind;
            pre_size=$(if ([string]$pre.kind -eq 'file') { [Int64]$pre.size } else { $null });
            pre_sha256=$(if ([string]$pre.kind -eq 'file') { [string]$pre.sha256 } else { $null });
            backup_path=$backupPath; recovery_path=$recoveryPath; incoming_path=$incoming;
            replacement_backup_path=$replacement
        }
    }
    $backupManifest = [PSCustomObject]@{
        schema_version=1; patch_id=$patchId; transaction_id=$txId; pre_profile_id=[string]$CurrentProfile.Profile.id;
        files=@($entries | ForEach-Object { [PSCustomObject]@{ path=$_.path; kind=$_.pre_kind; size=$_.pre_size; sha256=$_.pre_sha256 } })
    }
    $backupManifestPath = Join-Path $backupDir 'backup_manifest.json'
    Write-JsonAtomic $backupManifest $backupManifestPath
    $recoveryManifest = [PSCustomObject]@{
        schema_version=1; patch_id=$patchId; transaction_id=$txId;
        files=@($Context.Manifest.payload | ForEach-Object { [PSCustomObject]@{ path=$_.path; size=[Int64]$_.size; sha256=[string]$_.sha256 } })
    }
    $recoveryManifestPath = Join-Path $recoveryDir 'recovery_manifest.json'
    Write-JsonAtomic $recoveryManifest $recoveryManifestPath
    return [PSCustomObject]@{
        TransactionId=$txId; BackupDirectory=$backupDir; RecoveryDirectory=$recoveryDir; Entries=@($entries);
        BackupManifestPath=$backupManifestPath; BackupManifestSha256=(Get-FileSha256 $backupManifestPath);
        RecoveryManifestPath=$recoveryManifestPath; RecoveryManifestSha256=(Get-FileSha256 $recoveryManifestPath)
    }
}

function Assert-InstalledState {
    param([Parameter(Mandatory=$true)]$State, [Parameter(Mandatory=$true)]$Context,
          [Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)][string]$BackupRoot,
          [Parameter(Mandatory=$true)][string]$RecoveryRoot)
    if ([string]$State.status -ne 'installed' -or [string]$State.patch_id -ne [string]$Context.Manifest.patch_id -or
        [string]$State.release_version -ne [string]$Context.Manifest.release_version -or
        [string]$State.manifest_sha256 -ne $Context.ManifestSha256) { throw 'Installed state belongs to another release manifest.' }
    if ((Get-PathKey ([string]$State.game_root)) -ne (Get-PathKey $GameRoot)) { throw 'Installed state GameRoot mismatch.' }
    $txId = [string]$State.transaction_id
    $patchId = [string]$Context.Manifest.patch_id
    $expectedBackup = Join-Path (Join-Path $BackupRoot $patchId) $txId
    $expectedRecovery = Join-Path (Join-Path $RecoveryRoot $patchId) $txId
    if ((Get-PathKey ([string]$State.backup_directory)) -ne (Get-PathKey $expectedBackup)) { throw 'Installed state backup directory mismatch.' }
    if ((Get-PathKey ([string]$State.recovery_directory)) -ne (Get-PathKey $expectedRecovery)) { throw 'Installed state recovery directory mismatch.' }
    $null = Assert-TransactionEntrySet @($State.entries) $Context $GameRoot $expectedBackup $expectedRecovery $txId ([string]$State.pre_profile_id)

    $backupManifestExpected = Join-Path $expectedBackup 'backup_manifest.json'
    $recoveryManifestExpected = Join-Path $expectedRecovery 'recovery_manifest.json'
    if ((Get-PathKey ([string]$State.backup_manifest_path)) -ne (Get-PathKey $backupManifestExpected) -or
        (Get-PathKey ([string]$State.recovery_manifest_path)) -ne (Get-PathKey $recoveryManifestExpected)) {
        throw 'Installed state manifest path mismatch.'
    }
    foreach ($record in @(
        [PSCustomObject]@{ Path=$backupManifestExpected; Hash=[string]$State.backup_manifest_sha256; Label='backup manifest' },
        [PSCustomObject]@{ Path=$recoveryManifestExpected; Hash=[string]$State.recovery_manifest_sha256; Label='recovery manifest' }
    )) {
        if (-not [regex]::IsMatch($record.Hash, $script:ShaPattern) -or -not [System.IO.File]::Exists($record.Path)) { throw "$($record.Label) is missing or has an invalid hash record." }
        $item = Get-Item -LiteralPath $record.Path -Force
        if (($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0 -or (Get-FileSha256 $record.Path) -ne $record.Hash) { throw "$($record.Label) integrity check failed." }
    }

    $backupManifest = Read-JsonUtf8 $backupManifestExpected
    if ([int]$backupManifest.schema_version -ne 1 -or [string]$backupManifest.patch_id -ne $patchId -or
        [string]$backupManifest.transaction_id -ne $txId -or [string]$backupManifest.pre_profile_id -ne [string]$State.pre_profile_id) {
        throw 'Backup manifest identity mismatch.'
    }
    $backupRecords = @{}
    foreach ($record in @($backupManifest.files)) {
        $rel = [string]$record.path
        if ($backupRecords.ContainsKey($rel)) { throw "Duplicate backup manifest path: $rel" }
        $backupRecords[$rel] = $record
    }
    if ($backupRecords.Count -ne @($State.entries).Count) { throw 'Backup manifest entry count mismatch.' }
    foreach ($entry in @($State.entries)) {
        $rel = [string]$entry.path
        if (-not $backupRecords.ContainsKey($rel)) { throw "Backup manifest path missing: $rel" }
        $record = $backupRecords[$rel]
        if ([string]$record.kind -ne [string]$entry.pre_kind -or [string]$record.sha256 -ne [string]$entry.pre_sha256) { throw "Backup manifest state mismatch: $rel" }
        if ([string]$entry.pre_kind -eq 'file' -and [Int64]$record.size -ne [Int64]$entry.pre_size) { throw "Backup manifest size mismatch: $rel" }
    }

    $recoveryManifest = Read-JsonUtf8 $recoveryManifestExpected
    if ([int]$recoveryManifest.schema_version -ne 1 -or [string]$recoveryManifest.patch_id -ne $patchId -or
        [string]$recoveryManifest.transaction_id -ne $txId) { throw 'Recovery manifest identity mismatch.' }
    $recoveryRecords = @{}
    foreach ($record in @($recoveryManifest.files)) {
        $rel = [string]$record.path
        if ($recoveryRecords.ContainsKey($rel)) { throw "Duplicate recovery manifest path: $rel" }
        $recoveryRecords[$rel] = $record
    }
    $payloadMap = Get-PayloadEntryMap $Context.Manifest
    if ($recoveryRecords.Count -ne $payloadMap.Count) { throw 'Recovery manifest entry count mismatch.' }
    foreach ($rel in $payloadMap.Keys) {
        if (-not $recoveryRecords.ContainsKey($rel)) { throw "Recovery manifest path missing: $rel" }
        $record = $recoveryRecords[$rel]
        $payloadEntry = $payloadMap[$rel]
        if ([Int64]$record.size -ne [Int64]$payloadEntry.size -or [string]$record.sha256 -ne [string]$payloadEntry.sha256) { throw "Recovery manifest hash mismatch: $rel" }
    }
}

function New-JournalObject {
    param([Parameter(Mandatory=$true)][string]$Operation, [Parameter(Mandatory=$true)]$Context,
          [Parameter(Mandatory=$true)][string]$GameRoot, [Parameter(Mandatory=$true)]$Artifacts,
          [Parameter(Mandatory=$true)][AllowEmptyCollection()]$CreatedDirectories)
    return [PSCustomObject]@{
        schema_version=1; operation=$Operation; phase='in_progress'; patch_id=[string]$Context.Manifest.patch_id;
        manifest_sha256=$Context.ManifestSha256; transaction_id=$Artifacts.TransactionId; game_root=$GameRoot;
        backup_directory=$Artifacts.BackupDirectory; recovery_directory=$Artifacts.RecoveryDirectory;
        planned_created_directories=@($CreatedDirectories); completed_count=0; entries=@($Artifacts.Entries)
    }
}

function Invoke-KoreanPatchInstall {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)][string]$GameRoot,
        [Parameter(Mandatory=$true)][string]$PackageRoot,
        [Parameter(Mandatory=$true)][string]$BackupRoot,
        [Parameter(Mandatory=$true)][string]$StateRoot,
        [Parameter(Mandatory=$true)][string]$RecoveryRoot,
        [int]$TestFailAfterReplacement=0,
        [int]$TestPauseAfterReplacement=0,
        [string]$TestPauseSignalPath=''
    )
    $ErrorActionPreference = 'Stop'
    $context = Get-PackageContext $PackageRoot
    $game = Get-CanonicalFullPath $GameRoot
    if (-not [System.IO.Directory]::Exists($game)) { throw 'GameRoot does not exist.' }
    Assert-ExternalRoots $game $context.PackageRoot $BackupRoot $StateRoot $RecoveryRoot | Out-Null
    Assert-TargetProcessStopped $game $context.Manifest
    $patchStateRoot = Join-Path (Get-CanonicalFullPath $StateRoot) ([string]$context.Manifest.patch_id)
    $installedPath = Join-Path $patchStateRoot 'installed.json'
    $journalPath = Join-Path $patchStateRoot 'in_progress.json'
    Recover-IncompleteTransaction $journalPath $installedPath $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot)
    Assert-GameAnchors $game $context.Manifest
    if ([System.IO.File]::Exists($installedPath)) {
        $state = Read-JsonUtf8 $installedPath
        Assert-InstalledState $state $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot)
        Assert-AllTargetsPatched $game $context.Manifest
        Write-Output 'INSTALL IDEMPOTENT: exact Korean payload is already installed.'
        return
    }
    $current = Get-SupportedCurrentProfile $game $context.Manifest
    $artifacts = New-TransactionArtifacts $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot) $current
    $createdDirs = @(New-PlannedCreatedDirectories $game $context.Manifest)
    [System.IO.Directory]::CreateDirectory($patchStateRoot) | Out-Null
    $journal = New-JournalObject 'install' $context $game $artifacts $createdDirs
    Write-JsonAtomic $journal $journalPath
    $committed = $false
    try {
        foreach ($dir in @($createdDirs)) { if (-not [System.IO.Directory]::Exists([string]$dir)) { [System.IO.Directory]::CreateDirectory([string]$dir) | Out-Null } }
        $payloadMap = Get-PayloadEntryMap $context.Manifest
        $needsWrite = @{}
        foreach ($entry in @($journal.entries)) {
            $payloadEntry = $payloadMap[[string]$entry.path]
            $targetAlreadyPatched = [System.IO.File]::Exists([string]$entry.target_path) -and
                [Int64](Get-Item -LiteralPath ([string]$entry.target_path)).Length -eq [Int64]$payloadEntry.size -and
                (Get-FileSha256 ([string]$entry.target_path)) -eq [string]$payloadEntry.sha256
            $needsWrite[[string]$entry.path] = (-not $targetAlreadyPatched)
            if (-not $targetAlreadyPatched) {
                $packageFile = Join-SafeRelativePath (Join-Path $context.PackageRoot 'payload') ([string]$entry.path) 'package payload path'
                Copy-VerifiedFile $packageFile ([string]$entry.incoming_path) ([Int64]$payloadEntry.size) ([string]$payloadEntry.sha256) "incoming $($entry.path)"
            }
        }
        $replacementCount = 0
        foreach ($entry in @($journal.entries)) {
            $payloadEntry = $payloadMap[[string]$entry.path]
            if ([bool]$needsWrite[[string]$entry.path]) {
                Replace-WithIncoming ([string]$entry.incoming_path) ([string]$entry.target_path) ([string]$entry.replacement_backup_path)
                Assert-FileHash ([string]$entry.target_path) ([Int64]$payloadEntry.size) ([string]$payloadEntry.sha256) "installed target $($entry.path)"
                $replacementCount++
            }
            $journal.completed_count = [int]$journal.completed_count + 1
            Write-JsonAtomic $journal $journalPath
            if ([bool]$needsWrite[[string]$entry.path] -and $TestPauseAfterReplacement -gt 0 -and $replacementCount -eq $TestPauseAfterReplacement) {
                if (-not [string]::IsNullOrEmpty($TestPauseSignalPath)) { [System.IO.File]::WriteAllText((Get-CanonicalFullPath $TestPauseSignalPath), 'paused', [System.Text.Encoding]::ASCII) }
                Start-Sleep -Seconds 120
            }
            if ([bool]$needsWrite[[string]$entry.path] -and $TestFailAfterReplacement -gt 0 -and $replacementCount -eq $TestFailAfterReplacement) { throw "Synthetic failure after replacement $TestFailAfterReplacement." }
        }
        Assert-AllTargetsPatched $game $context.Manifest
        $state = [PSCustomObject]@{
            schema_version=1; status='installed'; patch_id=[string]$context.Manifest.patch_id;
            release_version=[string]$context.Manifest.release_version; manifest_sha256=$context.ManifestSha256;
            transaction_id=$artifacts.TransactionId; game_root=$game; pre_profile_id=[string]$current.Profile.id;
            backup_directory=$artifacts.BackupDirectory; recovery_directory=$artifacts.RecoveryDirectory;
            backup_manifest_path=$artifacts.BackupManifestPath; backup_manifest_sha256=$artifacts.BackupManifestSha256;
            recovery_manifest_path=$artifacts.RecoveryManifestPath; recovery_manifest_sha256=$artifacts.RecoveryManifestSha256;
            entries=@($artifacts.Entries)
        }
        Write-JsonAtomic $state $installedPath
        $committed = $true
        try {
            Remove-TransactionTemps $journal
            if ([System.IO.File]::Exists($journalPath)) { [System.IO.File]::Delete($journalPath) }
        }
        catch { Write-Warning ("Install committed; non-destructive cleanup is deferred: " + $_.Exception.Message) }
        Write-Output "INSTALL PASS: $($context.Manifest.patch_id) $($context.Manifest.release_version)"
        Write-Output "Backup: $($artifacts.BackupDirectory)"
        Write-Output "Recovery: $($artifacts.RecoveryDirectory)"
    }
    catch {
        if (-not $committed) {
            try {
                Assert-JournalShapeAndSources $journal $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot)
                Restore-DesiredStateFromJournal $journal $context 'pre'
                if (-not (Test-ExactJournalPreState $journal)) { throw 'Rollback verification failed.' }
                if ([System.IO.File]::Exists($installedPath)) { [System.IO.File]::Delete($installedPath) }
                if ([System.IO.File]::Exists($journalPath)) { [System.IO.File]::Delete($journalPath) }
            }
            catch { throw "Install failed and rollback is incomplete; recovery evidence was preserved. Cause: $($_.Exception.Message)" }
        }
        throw
    }
}

function Invoke-KoreanPatchRestore {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)][string]$GameRoot,
        [Parameter(Mandatory=$true)][string]$PackageRoot,
        [Parameter(Mandatory=$true)][string]$BackupRoot,
        [Parameter(Mandatory=$true)][string]$StateRoot,
        [Parameter(Mandatory=$true)][string]$RecoveryRoot,
        [int]$TestFailAfterReplacement=0
    )
    $ErrorActionPreference = 'Stop'
    $context = Get-PackageContext $PackageRoot
    $game = Get-CanonicalFullPath $GameRoot
    if (-not [System.IO.Directory]::Exists($game)) { throw 'GameRoot does not exist.' }
    Assert-ExternalRoots $game $context.PackageRoot $BackupRoot $StateRoot $RecoveryRoot | Out-Null
    Assert-TargetProcessStopped $game $context.Manifest
    $patchStateRoot = Join-Path (Get-CanonicalFullPath $StateRoot) ([string]$context.Manifest.patch_id)
    $installedPath = Join-Path $patchStateRoot 'installed.json'
    $journalPath = Join-Path $patchStateRoot 'in_progress.json'
    Recover-IncompleteTransaction $journalPath $installedPath $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot)
    Assert-GameAnchors $game $context.Manifest
    if (-not [System.IO.File]::Exists($installedPath)) {
        if (Test-AllTargetsPatched $game $context.Manifest) { throw 'Exact patched files exist but no authoritative install state is available; restoration target is unknown.' }
        $null = Get-SupportedCurrentProfile $game $context.Manifest
        Write-Output 'RESTORE IDEMPOTENT: the game already matches an approved uninstalled profile.'
        return
    }
    $state = Read-JsonUtf8 $installedPath
    Assert-InstalledState $state $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot)
    Assert-AllTargetsPatched $game $context.Manifest
    $journal = [PSCustomObject]@{
        schema_version=1; operation='restore'; phase='in_progress'; patch_id=[string]$context.Manifest.patch_id;
        manifest_sha256=$context.ManifestSha256; transaction_id=[string]$state.transaction_id; game_root=$game;
        backup_directory=[string]$state.backup_directory; recovery_directory=[string]$state.recovery_directory;
        planned_created_directories=@(); completed_count=0; entries=@($state.entries)
    }
    Write-JsonAtomic $journal $journalPath
    $committed = $false
    try {
        foreach ($entry in @($journal.entries)) {
            if ([string]$entry.pre_kind -eq 'file') {
                Copy-VerifiedFile ([string]$entry.backup_path) ([string]$entry.incoming_path) ([Int64]$entry.pre_size) ([string]$entry.pre_sha256) "restore incoming $($entry.path)"
            }
        }
        $replacementCount = 0
        foreach ($entry in @($journal.entries)) {
            $target = [string]$entry.target_path
            if ([string]$entry.pre_kind -eq 'absent') {
                if (-not [System.IO.File]::Exists($target)) { throw "Installed target disappeared before restore: $($entry.path)" }
                if ([System.IO.File]::Exists([string]$entry.replacement_backup_path)) { [System.IO.File]::Delete([string]$entry.replacement_backup_path) }
                [System.IO.File]::Move($target, [string]$entry.replacement_backup_path)
            }
            else {
                Replace-WithIncoming ([string]$entry.incoming_path) $target ([string]$entry.replacement_backup_path)
            }
            $replacementCount++
            $journal.completed_count = [int]$journal.completed_count + 1
            Write-JsonAtomic $journal $journalPath
            if ($TestFailAfterReplacement -gt 0 -and $replacementCount -eq $TestFailAfterReplacement) { throw "Synthetic restore failure after replacement $TestFailAfterReplacement." }
        }
        if (-not (Test-ExactJournalPreState $journal)) { throw 'Restored files do not match the exact saved pre-install state.' }
        $historyRoot = Join-Path $patchStateRoot 'history'
        [System.IO.Directory]::CreateDirectory($historyRoot) | Out-Null
        $history = Join-Path $historyRoot (([string]$state.transaction_id) + '.restored.json')
        if ([System.IO.File]::Exists($history)) { [System.IO.File]::Delete($history) }
        [System.IO.File]::Move($installedPath, $history)
        $committed = $true
        try {
            Remove-TransactionTemps $journal
            if ([System.IO.File]::Exists($journalPath)) { [System.IO.File]::Delete($journalPath) }
        }
        catch { Write-Warning ("Restore committed; non-destructive cleanup is deferred: " + $_.Exception.Message) }
        Write-Output "RESTORE PASS: exact pre-install profile '$($state.pre_profile_id)' restored."
    }
    catch {
        if (-not $committed) {
            try {
                Assert-JournalShapeAndSources $journal $context $game (Get-CanonicalFullPath $BackupRoot) (Get-CanonicalFullPath $RecoveryRoot)
                Restore-DesiredStateFromJournal $journal $context 'patched'
                Assert-AllTargetsPatched $game $context.Manifest
                if ([System.IO.File]::Exists($journalPath)) { [System.IO.File]::Delete($journalPath) }
            }
            catch { throw "Restore failed and rollback is incomplete; installed state and recovery evidence were preserved. Cause: $($_.Exception.Message)" }
        }
        throw
    }
}

Export-ModuleMember -Function Get-FileSha256, Invoke-KoreanPatchInstall, Invoke-KoreanPatchRestore
