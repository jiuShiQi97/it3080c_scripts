$RANDO = 0
$Logfile = "C:\Users\JSQ97\Script\it3080c_scripts\powershell\logs\rando.log"
for($i = 0; $i -lt 5; $i++){
    $RANDO = Get-Random -Maximum 1000 -Minimum 1
    Write-Host($RANDO)
    Add-Content $Logfile "INFO: Random number is ${RANDO}"
}