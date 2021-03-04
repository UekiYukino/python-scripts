#!/usr/bin/env python3
from PIL import Image
import PIL
import os
import sys
import argparse

def receive_input():
    parser=argparse.ArgumentParser()
    parser.add_argument("-s", "--source", dest="sourceDirectory", help="Specify the name of the directory contains the images")
    parser.add_argument("-d", "--dest", dest="destinationDirectory", help="Specify the name of the destination directory to store the new images")
    parser.add_argument("-i", "--input", dest="inputImage", help="Name of the image to process")
    parser.add_argument("-o","--output", dest="outputImage", help="Name of the output image")
    parser.add_argument("-W", "--width", dest="width", help="Specify the width of the new image")
    parser.add_argument("-H", "--height", dest="height", help="Specify the height of the new image")
    parser.add_argument("-x", "--extension", dest="extension", help="The new image extension, can skip if you only process 1 specific picture")
    
    options=parser.parse_args()
    #Message the user if the input/output is missing
    if not (options.sourceDirectory or options.inputImage):
        parser.error("[-] Input file or directory is missing, use --help for more information")
    elif not (options.destinationDirectory or options.outputImage):
        parser.error("[-] Output file or directory is missing, use --help for more information")
    
    #Message the user if they want to resize image and only add width or height
    if options.width or options.height:
        if not options.width:
            parser.error("[-] Width is missing, use --help for more information")
        elif not options.height:
            parser.error("[-] Height is missing, use --help for more information")
        else:
            size=(int(options.width),int(options.height))
    else:
        size=None #Return None if neither width or height is specify
    
    #Message the user if they use -o or --output without specify an extension for the output file
    if "." not in options.outputImage and not options.extension:
        parser.error("[-] Extension is missing from output file")

    return options.sourceDirectory, options.destinationDirectory, options.inputImage, options.outputImage, size, options.extension


def edit_image(old_pic,new_pic,size):
    """Edit/modify image according to the input parameter"""
    try:
        #Convert the image to RGB and edit the image
        pic = Image.open(old_pic)
        if pic.mode == "RGB":
            rbg_pic=pic
        else:
            rbg_pic=pic.convert("RGB")
        
        #If no size is specify -> Do not resize the image
        if not size:
            rbg_pic.save(new_pic)
        else:
            rbg_pic.resize(size).save(new_pic)
    
    #Capture the error if the file is not an image
    except PIL.UnidentifiedImageError:
        print("[-] {} might not be an image file! Skipping".format(old_pic))
    except IsADirectoryError:
        print("[-] {} is a directory! Please try again".format(old_pic))


def change_extension(old_name,new_ext):
    """Changing the extension of a given file to a new one"""
    #If the file does not have an extension -> Add the new extension to it
    if "." not in old_name:
        #If the new extension is not specify for a file without extention -> message the user to specify an extension
        if not new_ext:
            print("[-] The current input file does not have an extension, use -x to specify one or --help for more information")
            sys.exit(1)
        else:
            new_name= "{}.{}".format(old_name,new_ext)
    
    #If the extension is not specify -> use the old file name 
    elif not new_ext:
        new_name=old_name

    #Extract the old extension
    else:
        old_ext=old_name.split(".")[-1]
        #Replace the extension
        new_name=old_name.replace(old_ext,new_ext)
    return new_name


def dest_check(dest):
    """Cheking if the destination directory exist or not. If not, create that directory"""
    if not os.path.exists(dest):
        os.mkdir(dest)


def process_image(path,dest,size,new_ext):
    
    #Check if the source directory exist, escape the program if source is not found on system
    if not os.path.exists(path):
        print("[-] Source directory \"{}\" not found".format(path))
        sys.exit(1)
    if not os.path.isdir(path):
        print("[-] \"{}\" is not a directory! Please try again".format(path))
        sys.exit(1)

    #Check destination directory and create if does not exist yet
    for root,_,pictures in os.walk(path):
        #Replace the old path with the destination path for the current root directory
        new_path=root.replace(path,dest)
        dest_check(new_path)
        for pic in pictures:
            old_pic=os.path.join(root,pic)
            
            #Run the change_extension function to check and add extension to the output files
            new_name=change_extension(pic,new_ext)

            #Join the path and file name together then save the new image to the destination
            new_pic=os.path.join(new_path,new_name)
            edit_image(old_pic,new_pic,size)

def main():
    #Except user input
    source,dest,inFile,outFile,size,ext=receive_input()
    
    #Call process_image function when a source and destination directory is specify
    if all((source,dest)):
        process_image(source,dest,size,ext)

    #If the entered input parameter is a file, check for the ouput type
    elif inFile:
        if outFile:
            new_name=change_extension(outFile,ext)
            edit_image(inFile,new_name,size)
        elif dest:
            #Call destination check function to check and create destination directory when needed
            dest_check(dest)
            new_name=change_extension(inFile,ext)#Check and change extension when needed
            new_pic=os.path.join(dest,new_name)
            edit_image(inFile,new_pic,size)
    else:
        print("[-] Invalid input, output parameters! Please try again")

if __name__=="__main__":
    main()
