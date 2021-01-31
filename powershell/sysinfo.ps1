$Hello = "Hello,powersell!"
write-Host($Hello)
function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}
Write-Host(getIP)


$IP = getIP
$Date = ""
$Host1 = $Host.Version.Major
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $. PowerShell version $Host1. Today's Date is $Date"

Write-Host($Body)

#Send-MailMessage -To "wenhanja@mail.uc.edu" -From "wenhanja@mail.uc.edu" -Subject "IT3038c windows SysInfo" -Body $Body -smtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)