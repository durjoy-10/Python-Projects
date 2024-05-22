import os
import shutil #for move file

path=input("Enter your path: ")

files=os.listdir(path) #get the file

for file in files:
    filename,extension=os.path.splitext(file) #splitext() function split filename and extension
    extension_1=extension[1:] #extension name without .
    
    folder_path=path+"\\"+extension_1
    
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+file,path+"\\"+extension_1+"\\"+file)
        
    else:
        os.makedirs(folder_path) #creating a folder
        shutil.move(path+"\\"+file,path+"\\"+extension_1+"\\"+file)