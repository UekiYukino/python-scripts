# Backdoor
This is a directory contains 2 files "server.py" and "client.py" with functionality similar to `netcat` that can be used as a backdoor to a system

### Files
`server.py` : Run on the target system to perform a reverse connection to our machine
`client.py` : Run on the host machine to connect to the server open port

### Functions
#### 1. Perform execution of commands
Using the subprocess module of Python to perform command execution on the target machine
#### 2. Directory listing
Utilize the os module to perform directory listing

### Usage
##### server.py
`python server.py <[server_ip]> <[server_port]>`
  + `<[server_ip]>`: The IP you want server to be listen on (Eg: 127.0.0.1)
  + `<[server_port]>`: The port you want the server to be listen on (Eg: 8080)

##### client.py
`python client.py <[server_ip]> <[server_ip]>`
  + `<[server_ip]>`: The IP of the server you want to connect to (Eg: 192.168.3.6)
  + `<[server_ip]>`: The port number that is open on the server 
