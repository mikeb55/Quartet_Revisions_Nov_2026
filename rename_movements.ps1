# Script to rename directories and update file references for new movement order
# Air: Movement 4 → Movement 3
# Fire: Movement 3 → Movement 4 (already done)

Write-Host "Renaming Air/Movement-4 to Air/Movement-3..."
$airPath = "Air\Movement-4"
$airNewPath = "Air\Movement-3"

if (Test-Path $airPath) {
    # Try to rename
    try {
        Rename-Item -Path $airPath -NewName "Movement-3" -Force
        Write-Host "Successfully renamed Air/Movement-4 to Air/Movement-3"
    } catch {
        Write-Host "Error renaming Air directory: $_"
        Write-Host "Please close any files in Air/Movement-4 and try again"
    }
} else {
    Write-Host "Air/Movement-4 not found - may already be renamed"
}

Write-Host "`nChecking directory structure..."
Get-ChildItem -Directory | Where-Object { $_.Name -match "^(Air|Fire|Earth|Water)$" } | ForEach-Object {
    $movDirs = Get-ChildItem $_.FullName -Directory | Where-Object { $_.Name -match "Movement" }
    if ($movDirs) {
        Write-Host "$($_.Name): $($movDirs.Name -join ', ')"
    }
}

