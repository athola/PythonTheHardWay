import shutil, os, sys

def findAndDeleteFiles(folderpath, size):
    for folderName, subfolders, filenames in os.walk(folderpath):
        path = ""
        for filepath in filenames:
            path = folderName + "/" + filepath
            if (os.path.getsize(path) > size):
                print(path)
                #os.unlink(path)

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

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True
    folderPath = enterFolderPath(useCommandLine, "Enter a folder to search through: ")
    findAndDeleteFiles(folderPath, 1000000)

main()
