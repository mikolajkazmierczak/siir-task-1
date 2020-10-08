<#
  Script for activating python virtual enviroments without the folder hassle.
#>

# absolute location of the venv folder
$venv_location = ''

$location = Get-Location
Set-Location $venv_location
.\venv\Scripts\activate.ps1
Set-Location $location