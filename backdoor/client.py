#!/usr/bin/env python3
import sys
import socket

def check_input():
    """Validate user input and display help"""
    #Display usage if user don't know the parameters
    if len(sys.argv) < 3:
        print("[+] Usage: python client.py <[server_ip]> <[server_port]>")
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
        return srv_add,srv_port
    except:
        print("[-] Invalid port format")
        sys.exit(1)


#Create a Tcp socket on client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    srv_add,srv_port=check_input()
    client.connect((srv_add,srv_port))
    print("*" * 50)
    print("[+] Connected to {}:{}".format(srv_add,srv_port))
#If the server is not response -> Print error and exit
except ConnectionRefusedError:
    print("[-] Error! Cannot connect to {}:{}".format(srv_add,srv_port))
    sys.exit(1)

def display_menu():
    """Display options menu"""
    print("*" * 50)
    print("* 0. Close the connection")
    print("* 1. Execute commands")
    print("* 2. Directory listing")
    print("*" * 50)
    choice=input("Your choice: ").encode("utf-8")
    return choice


while True:
    try:
        #Display the menu and ask user for their action
        choice = display_menu()
        client.sendall(choice)
        if choice.decode() == "0":
            client.close()
            break
            sys.exit(1)

        elif choice.decode() == "1":
            command= input("Enter the command you want to execute: ")

            #Send the command to run on server
            client.sendall(command.encode("utf-8"))
            #Receive server answer
            ans=client.recv(4068)
            print(ans.decode())
        
        elif choice.decode() == "2":
            directory= input("Enter the directory you want to extract: ")

            #Send the directory information to the server
            client.sendall(directory.encode("utf-8"))

            #Receive output from server
            ans = client.recv(4068)
            #If the answer from the server indicate the directory does not exist
            if ans.decode() == "NoDir":
                print("[-] Directory does not exist")
            else:
                print("*" * 50)
                dir_item=ans.decode("utf-8").split(",")
                for item in dir_item:
                    print(item)

    #Capture Keyboard interruption then send sygnal for the server
    #And terminate the program
    except KeyboardInterrupt:
        print("\n[-] Keyboard Interrupt! Closing connection!")
        client.sendall(b"0")
        client.close()
        break
        sys.exit(1)

    except BrokenPipeError:
        print("[-] Server is closed!")
