import os, re, sys

def checkFolderPath(folderPath):
    return (os.path.exists(folderPath))
    
def checkIfTxt(fileName):
    fileSplit = fileName.split('.')
    return (fileSplit[-1] == 'txt')

def searchFile(fullFilePath):
    fileContent = ''
    if (os.path.isfile(fullFilePath)):
        theFile = open(fullFilePath, 'r')
        fileContent = theFile.read()
    return fileContent

def findNumberOf(searchPhrase, fileContent):
    searchRegex = re.compile(searchPhrase, re.IGNORECASE)
    contentList = searchRegex.findall(fileContent)
    if (len(contentList) > 0):
        print(searchPhrase + ' found!')
        return len(contentList)
    else:
        return 0

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True
    useDefaultValid = False
    usedDefault = True
    while (not useDefaultValid):
        if (useCommandLine and usedDefault):
            useDefault = sys.argv[1]
        else:
            useDefault = input('Use default filepath? (y/n): \n')
        if (useDefault.lower() == 'y'):
            folderPath = str(os.path.expanduser('~/Documents'))
            useDefaultValid = True
        elif (useDefault.lower() == 'n'):
            useDefaultValid = True
        else:
            print('Could not recognize input. Please enter \neither y for yes, or n for no\n')
            usedDefault = False
    if (useDefaultValid):
        folderPathValid = True
    else:
        folderPathValid = False
    while (not folderPathValid):        
        folderPath = input('Please enter valid folder path: \n')
        folderPathValid = checkFolderPath(folderPath)
        if (not folderPathValid):
            print('Folder path invalid!\n')
    if (useCommandLine):
        phrase = sys.argv[2]
    else:
        phrase = input('Enter a phrase to search text files for: \n')
    for file in os.listdir(folderPath):
        if (checkIfTxt(file)):
            fullPath = folderPath + '/' + file
            content = searchFile(fullPath)
            searchContentOccurences = findNumberOf(phrase, content)
            print(str(searchContentOccurences) + ' occurences in ' + file)

main()
