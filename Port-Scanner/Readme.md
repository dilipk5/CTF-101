# Python Port Scanner

**Overview**
This is a simple yet efficient port scanner written in Python. It utilizes multi-threading to scan a range of ports on a specified target IP address, making it faster than a single-threaded scanner.

**Features**
Multi-threaded: Uses Python's threading library to scan multiple ports simultaneously.
Efficient: Designed to quickly determine which ports are open on a given target.

**Code Explanation**
1. Imports:

sys: For command-line arguments and exiting the program.
socket: For network connections and port checking.
time: (Unused in the current implementation but typically used for time-related operations).
threading: For creating multiple threads to speed up the scanning process.

2. Usage Check:

The script checks if exactly three command-line arguments are provided: the target IP, start port, and end port.
Target Resolution:

Converts the target hostname to an IP address.

3. Port Scanning:

A function port_scan(port) is defined to create a socket connection to the target IP on the specified port. If the connection is successful (i.e., the port is open), it prints a message.

4.Multi-threading:

For each port in the specified range, a new thread is started to perform the port scan, allowing multiple ports to be checked simultaneously.
