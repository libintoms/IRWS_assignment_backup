from genericpath import exists
import sys
import os
import glob

folder_loc=input("Enter the folder path: ")
assert os.path.exists(folder_loc), "Following file location does not exist: "+str(folder_loc)
for filename in glob.glob(os.path.join(folder_loc, '*.txt')):
    with open(filename,'r+') as f:
        text=f.read()
        print(filename)
        print(len(text))