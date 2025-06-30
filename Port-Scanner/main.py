import sys
import socket
import time
import threading

usage = "python portscanner.py target_ip_address start_port end_port"

if (len(sys.argv )!= 4):
    print(f"[+] Usage: {usage}")
    sys.exit()
try:
    target = socket.gethostbyname(sys.argv[1])
    print(target)
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("*"*50)
print("SCANNING")
print("*"*50)

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = s.connect_ex((target, port))
    if (not con):
        print("Port is open", port)
    s.close()


for port in range(start_port, end_port):
    thread = threading.Thread(target= port_scan, args=(port,))
    thread.start()
