param(
    [Parameter(Mandatory = $true)]
    [string]$ReviewRoot,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-fA-F]{64}$')]
    [string]$ExpectedExeSha256,

    [Parameter(Mandatory = $true)]
    [string]$PayloadManifestPath,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-fA-F]{64}$')]
    [string]$ExpectedPayloadManifestSha256,

    [string]$EvidencePath = (Join-Path $PSScriptRoot 'visible_user_review.session.json')
)

$ErrorActionPreference = 'Stop'
$workspace = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..\..')).Path
$projectReviewBase = [IO.Path]::GetFullPath('P:\AI\Codex\projects\fatal-twelve-ko')
$review = (Resolve-Path -LiteralPath $ReviewRoot).Path
$exe = (Resolve-Path -LiteralPath (Join-Path $review 'fatal.exe')).Path
$manifest = (Resolve-Path -LiteralPath $PayloadManifestPath).Path
$liveRoot = 'F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve'

$allowedReviewBases = @($workspace, $projectReviewBase)
$reviewIsAllowed = $false
foreach ($allowedBase in $allowedReviewBases) {
    if ($review.StartsWith($allowedBase + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        $reviewIsAllowed = $true
        break
    }
}
if (-not $reviewIsAllowed) {
    throw "Review root is outside approved isolated roots: $review"
}
if ($review.StartsWith($liveRoot, [StringComparison]::OrdinalIgnoreCase) -or
    $exe.StartsWith($liveRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Live F: game execution is forbidden: $exe"
}
if (-not $exe.Equals((Join-Path $review 'fatal.exe'), [StringComparison]::OrdinalIgnoreCase)) {
    throw "Unexpected executable path: $exe"
}

$actualExeSha256 = (Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actualExeSha256 -ne $ExpectedExeSha256.ToLowerInvariant()) {
    throw "Review fatal.exe SHA-256 mismatch: $actualExeSha256"
}
$actualManifestSha256 = (Get-FileHash -LiteralPath $manifest -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actualManifestSha256 -ne $ExpectedPayloadManifestSha256.ToLowerInvariant()) {
    throw "Payload manifest SHA-256 mismatch: $actualManifestSha256"
}

$muteSource = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot 'f12_user_review_mute.rpy')).Path
$muteInstalled = (Resolve-Path -LiteralPath (Join-Path $review 'game\f12_user_review_mute.rpy')).Path
$muteSourceSha256 = (Get-FileHash -LiteralPath $muteSource -Algorithm SHA256).Hash.ToLowerInvariant()
$muteInstalledSha256 = (Get-FileHash -LiteralPath $muteInstalled -Algorithm SHA256).Hash.ToLowerInvariant()
if ($muteSourceSha256 -ne $muteInstalledSha256) {
    throw "Review mute overlay differs from approved source"
}

$reviewPrefix = $review.TrimEnd([IO.Path]::DirectorySeparatorChar) + [IO.Path]::DirectorySeparatorChar
$alreadyRunning = Get-CimInstance Win32_Process -Filter "Name='fatal.exe'" | Where-Object {
    $_.ExecutablePath -and $_.ExecutablePath.StartsWith($reviewPrefix, [StringComparison]::OrdinalIgnoreCase)
}
if ($alreadyRunning) {
    throw "Review executable tree is already running: $($alreadyRunning.ProcessId -join ', ')"
}

$evidence = [IO.Path]::GetFullPath($EvidencePath)
$evidenceDirectory = Split-Path -Parent $evidence
New-Item -ItemType Directory -Force -Path $evidenceDirectory | Out-Null
$stdout = Join-Path $evidenceDirectory 'visible_user_review.stdout.log'
$stderr = Join-Path $evidenceDirectory 'visible_user_review.stderr.log'

# Child-process-only environment. The visible game keeps the normal video
# driver, while audio is forced to SDL's dummy backend.
$env:SDL_AUDIODRIVER = 'dummy'
$env:RENPY_DISABLE_JOYSTICK = '1'
$env:APPDATA = Join-Path $review 'review_appdata'
$env:LOCALAPPDATA = Join-Path $review 'review_localappdata'
New-Item -ItemType Directory -Force -Path $env:APPDATA, $env:LOCALAPPDATA | Out-Null

$started = (Get-Date).ToUniversalTime()
$launcherProcess = Start-Process -FilePath $exe -WorkingDirectory $review -PassThru `
    -RedirectStandardOutput $stdout -RedirectStandardError $stderr

# The shipped root fatal.exe is a short-lived architecture selector. Track the
# actual GUI child (normally lib\windows-i686\fatal.exe) by isolated-tree path.
$deadline = (Get-Date).AddSeconds(60)
$windowHandle = [IntPtr]::Zero
$runtimeProcess = $null
$runtimeProcessInfo = $null
while ((Get-Date) -lt $deadline) {
    Start-Sleep -Milliseconds 250
    $runtimeCandidates = Get-CimInstance Win32_Process -Filter "Name='fatal.exe'" | Where-Object {
        $_.ExecutablePath -and $_.ExecutablePath.StartsWith($reviewPrefix, [StringComparison]::OrdinalIgnoreCase)
    }
    foreach ($candidate in $runtimeCandidates) {
        $candidateProcess = Get-Process -Id $candidate.ProcessId -ErrorAction SilentlyContinue
        if ($candidateProcess -and $candidateProcess.MainWindowHandle -ne 0) {
            $runtimeProcess = $candidateProcess
            $runtimeProcessInfo = $candidate
            $windowHandle = [IntPtr]$candidateProcess.MainWindowHandle
            break
        }
    }
    if ($windowHandle -ne [IntPtr]::Zero) {
        break
    }
}
if ($windowHandle -eq [IntPtr]::Zero) {
    $launcherProcess.Refresh()
    $launcherState = if ($launcherProcess.HasExited) {
        "stub exit $($launcherProcess.ExitCode)"
    } else {
        "stub PID $($launcherProcess.Id) still running"
    }
    throw "Visible review GUI child did not appear within 60 seconds ($launcherState); see $stderr"
}
$runtimeExe = (Resolve-Path -LiteralPath $runtimeProcessInfo.ExecutablePath).Path
if (-not $runtimeExe.StartsWith($reviewPrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Runtime child escaped isolated review tree: $runtimeExe"
}
$runtimeExeSha256 = (Get-FileHash -LiteralPath $runtimeExe -Algorithm SHA256).Hash.ToLowerInvariant()
$launcherProcess.Refresh()
$launcherExitCode = if ($launcherProcess.HasExited) { $launcherProcess.ExitCode } else { $null }

if (-not ('F12ReviewWindow' -as [type])) {
    Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
public static class F12ReviewWindow {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
    [DllImport("user32.dll")]
    public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")]
    public static extern bool GetClientRect(IntPtr hWnd, out RECT rect);
}
'@
}
$windowRect = New-Object F12ReviewWindow+RECT
$clientRect = New-Object F12ReviewWindow+RECT
[void][F12ReviewWindow]::GetWindowRect($windowHandle, [ref]$windowRect)
[void][F12ReviewWindow]::GetClientRect($windowHandle, [ref]$clientRect)
$runtimeProcess.Refresh()

$session = [ordered]@{
    schema_version = 'fatal-twelve-visible-user-review-session-v2'
    status = 'AWAITING_USER_REVIEW'
    started_at_utc = $started.ToString('o')
    review_root = $review
    launcher_stub_path = $exe
    launcher_stub_sha256 = $actualExeSha256
    launcher_stub_pid = $launcherProcess.Id
    launcher_stub_exited = $launcherProcess.HasExited
    launcher_stub_exit_code = $launcherExitCode
    runtime_executable_path = $runtimeExe
    runtime_executable_sha256 = $runtimeExeSha256
    payload_manifest_path = $manifest
    payload_manifest_sha256 = $actualManifestSha256
    mute_overlay_path = $muteInstalled
    mute_overlay_sha256 = $muteInstalledSha256
    live_executable_invoked = $false
    process_environment = [ordered]@{
        SDL_AUDIODRIVER = $env:SDL_AUDIODRIVER
        RENPY_DISABLE_JOYSTICK = $env:RENPY_DISABLE_JOYSTICK
        APPDATA = $env:APPDATA
        LOCALAPPDATA = $env:LOCALAPPDATA
    }
    mute_contract = [ordered]@{
        config_sound = $false
        config_audio_periodic_thread = $false
        music_volume = 0.0
        sfx_volume = 0.0
        voice_volume = 0.0
        music_muted = $true
        sfx_muted = $true
        voice_muted = $true
    }
    pid = $runtimeProcess.Id
    window_handle = $windowHandle.ToInt64()
    window_title = $runtimeProcess.MainWindowTitle
    window_rect = [ordered]@{
        left = $windowRect.Left; top = $windowRect.Top
        right = $windowRect.Right; bottom = $windowRect.Bottom
    }
    client_bounds = [ordered]@{
        left = $clientRect.Left; top = $clientRect.Top
        right = $clientRect.Right; bottom = $clientRect.Bottom
        width = $clientRect.Right - $clientRect.Left
        height = $clientRect.Bottom - $clientRect.Top
    }
    stdout_log = $stdout
    stderr_log = $stderr
    checklist = (Join-Path $PSScriptRoot 'MANUAL_RUNTIME_REVIEW_CHECKLIST.md')
}
$session | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $evidence -Encoding UTF8
Write-Output ($session | ConvertTo-Json -Depth 8)

