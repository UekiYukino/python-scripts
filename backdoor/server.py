#!/usr/bin/env python3

import socket 
import subprocess
import sys 
import os

def check_input():
    """Validate user input and display help"""
    #Display usage if user don't know the parameters
    if len(sys.argv) < 3:
        print("[+] Usage: python server.py <[server_ip]> <[server_port]>")
        sys.exit(1)
    srv_add = sys.argv[1]
    if len(srv_add.split(".")) != 4:
        print("[-] Invalid IPv4 address")
        sys.exit(1)
    #Check to see if any octet of the IPv4 is not valid
    for octet in srv_add.split("."):
        if  not 0 <= int(octet) <= 255:
            print("[-] Invalid IPv4 address")
            sys.exit(1)
    try:
        srv_port = int(sys.argv[2])
    except:
        print("[-] Invalid port format")
        sys.exit(1)

check_input()



srv_add = sys.argv[1]
srv_port = int(sys.argv[2])

#Create a TCP socket on server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((srv_add, srv_port))
server.listen(4)
print("*" * 50)
print("[+] Server started! Accepting connection from port {}".format(srv_port))

def new_connection():
    """Establish new connection with client"""
    try:    
        client_socket,address = server.accept()
        print("[+] Incoming traffic from {}:{}".format(address[0],address[1]))
    #Capture KeyboardInterrupt and close the server connection
    except KeyboardInterrupt:
        print("\n[-] Terminate server!")
        server.close()
        sys.exit(1)
    return client_socket

def get_dir_content(directory):
    """Retrieve the content of a directory"""
    if os.path.isdir(directory):   
        content = os.listdir(directory)
        payload=""
        for item in content:
            item_path=os.path.join(directory,item)
            #Identify if the item is a file or a directory
            if os.path.isdir(item_path):
                payload+="{}/,".format(item)
            else:
                payload+="{},".format(item)
        client_socket.sendall(payload.encode("utf-8"))
    else:
        client_socket.sendall(b"NoDir")

def exec_command(command):
    """Execute command and send the output to client"""
    try:
        #Run the command and send the output to client
        output=subprocess.check_output(command.decode().split(" "))
        client_socket.sendall(b"[+] Command received\n")
        client_socket.sendall(output)
    #If the command could not be execute -> Send message to client
    except:
        client_socket.sendall(b"[-] Command not found\n")

#Initial connection
client_socket=new_connection()
while True:
    try:
        option = client_socket.recv(1024)
    #Capture when keyboard interrupt the process and close the connection
    except KeyboardInterrupt:
        print("\n[-] Terminate server!")
        server.close()
        break
    #Skip other error and continue
    except:
        continue
    #Restart the socket to allow new client to connect
    if option.decode() == "0":
        client_socket.close()
        client_socket = new_connection()

    elif option.decode() == "1":
        #Get the command from client
        command = client_socket.recv(1024)
        #Execute the command and send result to client
        exec_command(command)
    
    elif option.decode() == "2":
        #Get directory from client
        directory = client_socket.recv(1024)
        #Run the function to get directory content
        get_dir_content(directory.decode())
