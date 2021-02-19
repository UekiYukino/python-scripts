#!/usr/bin/env python3
#--------------------------------------------------------
# Description: This program crack password of zip files 
#			   using a wordlist 
#
#
#---------------------------------------------------------

# Import the important library
import zipfile
import argparse
import sys
from tqdm import tqdm

def receiveInput():
    """Process the input"""
    parser=argparse.ArgumentParser()
    parser.add_argument('-w','--wordlist', dest='wordList', help='Specify the wordlist to use')
    parser.add_argument('-z','--zipfile', dest='zipFile', help='Specify the zip file name')
    options=parser.parse_args()
    if not options.wordList:
        parser.error('[-] Specify a wordlist to use, use --help for more information')
    elif not options.zipFile:
        parser.error('[-] Specify zip file, use --help for more information')

    return options.wordList,options.zipFile
    

#Test password against the encrypted zipfile
def passwordTest(passwd,zfile):
    """Set password to the zip file and try to process it with testzip then output possible password for the zip file"""
    try:
        z=zipfile.ZipFile(zfile)
        #Encode the password to bytes then use it to test the encrypted zip
        z.setpassword(bytes(passwd,"utf-8"))
        z.testzip()
        print("\n[+] Possible password found: {}".format(passwd))
    except FileNotFoundError: #If zip file does not exist -> Print the message then escape the program
        print("[-] {} does not exist on the system".format(zfile))
        sys.exit(1)
    except NotImplementedError:
        print("[-] Compression method for {} is not supported".format(zfile))
        sys.exit(1)
    except: #Pass other error message
        pass

#This function iterate through the wordlist and test each password
def getPwd():
    """Iterate through the wordlist and test each password"""
    pwdfile, zfile=receiveInput()
    #Open and process through the wordlist
    try:   
        with open(pwdfile,"r") as pwd:
            for line in tqdm(pwd,desc="Processing",leave=False,unit=" passwords"):
                passwd = line.strip() #Strip each line for password only
                #Test each line of the file 
                passwordTest(passwd,zfile)
            print("[+] Reaching the end of wordlist")
    except FileNotFoundError:
        print("[-] Wordlist not found on system")

#Execute the function
getPwd()
