# HTB-tips

## Windows Privilege Escalation - Registry Autologon
Sometimes windows stores credentials in plaintext (DefaultDomainName, DefaultUserName,DefaultPassword)

EXAMPLE USAGE:
```bash
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```
