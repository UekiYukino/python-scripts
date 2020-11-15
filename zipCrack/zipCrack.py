#--------------------------------------------------------
# Description: This program crack password of zip files 
#			   using a wordlist 
#
#
# History:
# Date			Author			        Description
# 2018/25/05	TUAN KHANH VU			Initial Creation
# 2020/13/11    TUAN KHANH VU           Edit Code
#--------------------------------------------------------

# Import the important library
import zipfile
import argparse

def receiveInput():
    parser=argparse.ArgumentParser()

    parser.add_argument('-w','--wordlist', dest='wordList', help='Specify the wordlist to use')
    parser.add_argument('-z','--zipfile', dest='zipFile', help='Specify the zip file name')
    options=parser.parse_args()
    if not options.wordList:
        parser.error('[-] Specify an interface, use --help for more information')
    elif not options.zipFile:
        parser.error('[-] Specify the number of packets to capture, use --help for more information')

    return options.wordList,options.zipFile
    


def testZip(wlist,file):
    try:
        pwd=open(wlist,"r")
        zip= zipfile.ZipFile(file)
        answer= True 
    except:
        answer= False
    return answer

#Create function that test password of a zip file and add to a list 
def getPwd():	
    pwdfile, zfile=receiveInput()
    
	#Check the file
    test=testZip(pwdfile, zfile)
    pwdlist=[]
    if test:
        zip=zipfile.ZipFile(zfile)
        pwd=open(pwdfile,"r")

        for line in pwd:
            passwd = line.strip() #Strip each line for password only
            try: #Test each line of the file 
                zip.setpassword(bytes(passwd,"utf-8"))#Convert character to bytes and test password
                zip.testzip()
                pwdlist= pwdlist+[passwd]
            except:
                continue 

    else:
        pwdlist=[1] #return 1 if the file is invalid
    return pwdlist

#Execute the function to test password
result=getPwd()
if result:
    for item in result:
        if item != 1:
            print("[+] Password found: %s"%result)
        else:
            print("[-] Wordlist or zip file not found")
else:
<<<<<<< HEAD
    print("[-] Password not found, try another wordlist")
        
    
=======
    print("Password not found in list")
    
>>>>>>> 3d5b6a953addde6c4234c7714c77823d8ca5385e
