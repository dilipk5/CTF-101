# HTB-tips

## Windows Privilege Escalation - Registry Autologon
Sometimes windows stores credentials in plaintext (DefaultDomainName, DefaultUserName,DefaultPassword)

EXAMPLE USAGE:
```bash
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```


## Windows Privilege Escalation - Powershell history file
Windows stores the powershell history in a file in the psreadlinefolder.(just like linux stores it under the .bash_history).
```
more C:\users\adam\appdata\roaming\microsoft\windows\powershell\psreadline\*.txt
```

## Linux Privilege Escalation - Dcoker Container Mounted files
A docker conatiner is mounted to a home directory. The docker connects the containers file system to the hosts file system -- live. So any changes in the host file system also affects in the docker and vice versa.If the we get root on the docker conatiner(by default we are root inside the docker) this can result in easy priv esc by setting up the setuid to a any binary.
