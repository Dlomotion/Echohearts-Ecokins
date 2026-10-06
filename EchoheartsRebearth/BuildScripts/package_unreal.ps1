param(
    [Parameter(Mandatory = $true)][string]$EngineRoot,
    [string]$Configuration = "Development",
    [string]$Output = "$PSScriptRoot/../Packaged"
)
$project = Resolve-Path "$PSScriptRoot/../EchoheartsRebearth.uproject"
& "$EngineRoot/Engine/Build/BatchFiles/RunUAT.bat" BuildCookRun `
    -project="$project" -noP4 -platform=Win64 -clientconfig=$Configuration `
    -build -cook -stage -pak -archive -archivedirectory="$Output"
exit $LASTEXITCODE
