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

# Create a function to indent
def indent(string,space):
	result="  "*(space-1) +string 
	return result 

# The main function 	
def getDir():
	path=receiveInput()
	# Test if the path to the directory exist or not
	# Run the FileInfo function if there exist the path 
	if os.path.isdir(path)== True: 
		# Create File list, dictionary
		FileList=[]
		FileDict={}
	
		# Initial counter for the file size and number of files 
		TotalSize=0
		TotalFile=0
	
		# Walk through the directory 
		for root, dirs, files in os.walk(path):
			# Indent the root according to how deep it is
			print (indent(root,root.count(os.sep)))
			# Link the file and its path and add them to the file list 
			for file in files:
				FileItem=os.path.join(root,file)
				
				# Get the size of the file 
				size=os.path.getsize(FileItem)
				
				
				# Adding up the total files and total size 
				TotalFile+=1
				TotalSize+=size 
				
				# Print out the indented string 
				print ("%s\t%s bytes"%(indent("|-%s"%file,root.count(os.sep)), "{:,}".format(size))) 
		print ("[+] The total files are: %s"%TotalFile)
		print ("[+] The total file size is: %s bytes (%s MB)"%("{:,}".format(TotalSize),"{:,}".format(round(TotalSize/1048576,2))))
    # Return no directory if there is no such path 
	else:
		print ("[-] Directory does not exist")

		
getDir()
	
