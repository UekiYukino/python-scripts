#!/usr/bin/env python3
#--------------------------------------------------------
# Description: This program accept a directory and print
#	       out the contents
#--------------------------------------------------------

# Import Library
import os 
import argparse

def receiveInput():
    """This function accept input and return help menu when needed"""
    parser=argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", dest="directory", help="Specify the directory to scan")
    options=parser.parse_args()
    if not options.directory:
        parser.error("[-] Specify a directory, use --help for more information")
    return options.directory


def getDir():
    """Use the os.walk module of python to travel the directory and generate directory tree report"""
    path=receiveInput()
	# Test if the path to the directory exist or not
	# Run the FileInfo function if there exist the path 
    if os.path.isdir(path)== True: 
	
		# Initial counter for the file size and number of files 
        TotalSize=0
        TotalFile=0

		# Walk through the directory 
        for current, dirs, files in os.walk(path):
            DirSize=0
			# Indent if the current directory is not the input directory
            if current !=path:
                #Indent according to the amount of depth in relative to the os path
	            spaces= 2*(1+ current.count(os.sep)-path.count(os.sep))
            else:
	            spaces=0
            indent= " "*spaces
            
            #If the current directory is not the entered directory -> Only print out the relative path coresponding to the entered path
            if current!=path:
                break_dir=current.split(os.sep)
                print("{}/{}/".format(indent,break_dir[len(break_dir)-1]))
            else:
                print(path)

							
			# Running through the file lists
            for file in files:

				# Join the file path and get file size
                FileItem=os.path.join(current,file)
                try:
                    size=os.path.getsize(FileItem)
                except:
                    continue
				# Adding up the total files and total size 
                TotalFile+=1
                TotalSize+=size 
                DirSize+=size
				# Print out the indented string 
                print ("{}|-{}\t{:,} bytes".format(indent,file,size)) 
			
				
        print ("[+] The total files are: {}".format(TotalFile))
        print ("[+] The total file size is: {:,} bytes ({:,.2f} MB)".format(TotalSize,TotalSize/1048576))
    # Return no directory if there is no such path 
    else:
        print ("[-] Directory does not exist")

# Execute the function		
getDir()
	
