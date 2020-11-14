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
    pwdfile=input("Enter your wordlist: ")
    zfile=input("Enter your zip file: ")
    
	#Check the file
    test=testZip(pwdfile, zfile)

    if test:
        zip=zipfile.ZipFile(zfile)
        pwd=open(pwdfile,"r")
        pwdlist=[]
        for line in pwd:
            passwd = line.strip() #Strip each line for password only
            try: #Test each line of the file 
                zip.setpassword(bytes(passwd,"utf-8"))#Convert character to bytes and test password
                zip.testzip()
                pwdlist= pwdlist+[passwd]
            except:
                continue 

    else:
        print("The zip file or wordlist entered does not exist")
    return pwdlist

#Execute the function to test password
result=getPwd()
if result:
    for item in result:
        print ("The password is: %s"%item)
else:
    print("Password not found in list")
    
