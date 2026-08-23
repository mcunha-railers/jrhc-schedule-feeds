# Daily E9 schedule sync: picks up the newest CSV export dropped in the OneDrive
# source folder, regenerates the per-team .ics feeds if it's new, and pushes to GitHub
# (which republishes via GitHub Pages). No-ops quietly if nothing has changed.

$RepoDir    = "C:\Users\mattj\jrhc-schedule-feeds"
$SourceDir  = "C:\Users\mattj\OneDrive - Junior Railers Hockey Club, Inc\Claude\E9 Schedule Sync\source"
$MarkerFile = Join-Path $RepoDir ".last_processed.txt"
$LogFile    = Join-Path $RepoDir "sync.log"
$Gh         = "C:\Program Files\GitHub CLI\gh.exe"

function Write-Log($msg) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $msg"
    Add-Content -Path $LogFile -Value $line
}

$latest = Get-ChildItem -Path $SourceDir -Filter "*.csv" -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending | Select-Object -First 1

if (-not $latest) {
    Write-Log "No CSV found in source folder."
    $lastGood = if (Test-Path $MarkerFile) { (Get-Content $MarkerFile | Select-Object -Last 1) } else { $null }
    exit 0
}

$marker = "$($latest.Name)|$($latest.LastWriteTimeUtc.Ticks)"
$previous = if (Test-Path $MarkerFile) { Get-Content $MarkerFile -Raw } else { "" }

if ($previous.Trim() -eq $marker) {
    Write-Log "No change: '$($latest.Name)' already processed."
    exit 0
}

Write-Log "New export detected: '$($latest.Name)' (modified $($latest.LastWriteTime)). Regenerating..."

Push-Location $RepoDir
try {
    python "scripts\csv_to_ics.py" "$($latest.FullName)" "docs" 2>&1 | Tee-Object -Variable convertOutput | Out-Null
    Write-Log "Converter output: $($convertOutput -join ' | ')"

    git add -A
    $changes = git status --porcelain
    if (-not $changes) {
        Write-Log "Converter ran but produced no diff (feeds already up to date)."
        Set-Content -Path $MarkerFile -Value $marker
        exit 0
    }

    git -c user.name="Junior Railers Automation" -c user.email="mcunha@juniorrailers.com" `
        commit -m "Sync E9 schedule from $($latest.Name) ($(Get-Date -Format 'yyyy-MM-dd'))" | Out-Null
    git push 2>&1 | Tee-Object -Variable pushOutput | Out-Null

    if ($LASTEXITCODE -ne 0) {
        Write-Log "ERROR: git push failed: $($pushOutput -join ' | ')"
        exit 1
    }

    Set-Content -Path $MarkerFile -Value $marker
    Write-Log "Success: pushed updated feeds from '$($latest.Name)'."
}
catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    exit 1
}
finally {
    Pop-Location
}

# Staleness check: warn in the log if nobody has re-exported in over 10 days.
$age = (Get-Date) - $latest.LastWriteTime
if ($age.TotalDays -gt 10) {
    Write-Log "WARNING: newest source export is $([int]$age.TotalDays) days old - E9 schedule may be going stale."
}
