# python3
# SelectiveCopy.py

import shutil, os, sys
        
def findAndMoveFiles(folderpath, extension, newfolderpath):
    for folderName, subfolders, filenames in os.walk(folderpath):
        path = ""
        for filepath in filenames:
            file_name, file_extension = os.path.splitext(filepath)
            if file_extension == extension:
                path = folderName + "/" + filepath
                shutil.move(path, newfolderpath)

def enterFolderPath(commandLineFlag, prompt):
    invalidFolderPath = True
    folderPath = ""
    while (invalidFolderPath):
        print(prompt)
        if (commandLineFlag):
            folderPath = sys.argv[1]
            if (os.path.exists(folderPath)):
                invalidFolderPath = False
            else:
                print("Invalid folder path!")
        else:
            folderPath = input()
            if os.path.exists(folderPath):
                invalidFolderPath = False
            else:
                print("Invalid folder path!")
    return folderPath

def enterExtension(commandLineFlag):
    invalidExtension = True
    extension = ""
    while (invalidExtension):
        print("Enter an extension: ")
        if (commandLineFlag):
            extension = sys.argv[2]
            if (extension[0] == '.' and len(extension) > 1):
                invalidExtension = False
            else:
                print("Invalid extension!")
        else:
            extension = input()
            if (extension[0] == '.' and len(extension) > 1):
                invalidExtension = False
            else:
                print("Invalid extension!")
    return extension

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True
    folderPath = enterFolderPath(useCommandLine, "Enter a folder to search through: ")
    extension = enterExtension(useCommandLine)
    newFolderPath = enterFolderPath(useCommandLine, "Enter a folder to move to: ")
    findAndMoveFiles(folderPath, extension, newFolderPath)

main()
    
    
    


                
                
        
