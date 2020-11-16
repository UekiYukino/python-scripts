#!/usr/bin/env python3
#--------------------------------------------------------
# Description: This program accept a directory and print
#	       out the contents
#
#
#
# History:
# Date		Author			Description
# 2018/07/06	TUAN KHANH VU		Initial Creation
#--------------------------------------------------------

# Import Library
import os 
import argparse

def receiveInput():
	parser=argparse.ArgumentParser()
	parser.add_argument("-d", "--directory", dest="directory", help="Specify the directory to scan")
	options=parser.parse_args()
	if not options.directory:
		parser.error("[-] Specify a directory, use --help for more information")
	return options.directory

	
def getDir():
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
				spaces= 2*(1+ current.count(os.sep)-path.count(os.sep))
			else:
				spaces=0
			indent= " "*spaces
			print ("%s%s"%(indent,current))
							
			
			# Running through the file lists
			for file in files:

				# Join the file path and get file size
				FileItem=os.path.join(current,file)
				size=os.path.getsize(FileItem)
								
				# Adding up the total files and total size 
				TotalFile+=1
				TotalSize+=size 
				DirSize+=size
				# Print out the indented string 
				print ("%s|-%s\t%s bytes"%(indent,file,"{:,}".format(size))) 
			
			# Return directory size if it's not the entered path
			if current != path:
				print ("%s[+] Directory size: %s bytes"%(indent,"{:,}".format(DirSize)))
			else: 
				continue
				
		print ("[+] The total files are: %s"%TotalFile)
		print ("[+] The total file size is: %s bytes (%s MB)"%("{:,}".format(TotalSize),"{:,}".format(round(TotalSize/1048576,2))))
    # Return no directory if there is no such path 
	else:
		print ("[-] Directory does not exist")

# Execute the function		
getDir()
	
