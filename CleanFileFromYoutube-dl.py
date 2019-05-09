#!/usr/bin/env python3

import os
import sys

# Getting the current work directory (cwd)
path = os.getcwd()
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(path)

p=12

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:        
        print(file)
        
        filename, file_extension = os.path.splitext(file)
        
        if filename[len(filename)-p]=="-":
            if file_extension == ".mkv":
                Newfile_extension=".mp4"
            else:
                Newfile_extension=file_extension

            newFileName = filename[:-p]+Newfile_extension
            filename = filename+file_extension

            # print(filename)
            # print(newFileName)
            # print(path+"/"+filename)
            # print(path+"/"+newFileName)

            fullPath = path+"/"+filename
            fullNewPath=path+"/"+newFileName
            
            os.rename(fullPath, fullNewPath)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")