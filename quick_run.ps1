<#
  Shortcut script for running all three python apps.
#>


invoke-expression 'cmd /c start powershell -Command {
  .\venv\Scripts\activate.ps1;
  Set-Location "app1";
  py app.py;
}'

start-sleep -s 2

invoke-expression 'cmd /c start powershell -Command {
  .\venv\Scripts\activate.ps1;
  Set-Location "app2";
  py app.py;
}'

start-sleep -s 2

invoke-expression 'cmd /c start powershell -Command {
  .\venv\Scripts\activate.ps1;
  Set-Location "app3";
  py app.py;
}'