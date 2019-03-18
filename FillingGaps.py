import shutil, os, sys

def findGap(folderpath, prefix):
    for folderName, subfolders, filenames in os.walk(folderpath):
        path = ""
        temp = 0
        prefixSize = len(prefix)
        for filepath in filenames:
            filename, file_extension = os.path.split(filepath)
            if len(filename) > prefixSize:
                if filename[0:prefixSize] == prefix:
                    path = folderName + "/" + filepath
                    if (filename[-1] > temp + 1):
                        addFile(filename[0:-1], file_extension, folderName, temp)
                    temp += 1

def addFile(fileprefix, extension, folder, number):
    filename = fileprefix + str(number) + extension
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    else:
        print("File not added! Please check for an issue.")
                    

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

def enterPrefix(commandLineFlag, prompt):
    prefix = ""
    print(prompt)
    if (commandLineFlag):
        prefix = sys.argv[2]
    else:
        prefix = input()
    return prefix
    

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True
    folderPath = enterFolderPath(useCommandLine, "Enter a folder to search through: ")
    thePrefix = enterFolderPath(useCommandLine, "Enter a file prefix for gap location: ")
    findGap(folderPath, thePrefix)

main()
