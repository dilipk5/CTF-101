# HTB-tips

## Windows Privilege Escalation - Registry Autologon
Sometimes windows stores credentials in plaintext (DefaultDomainName, DefaultUserName,DefaultPassword)

EXAMPLE USAGE:
```bash
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```


## Windows Privilege Escalation - Powershell history file
Windows stores the powershell history in a file named psreadline(just like linux stores it under the .bash_history).
```
more C:\users\adam\appdata\roaming\microsoft\windows\powershell\psreadline.txt
```
