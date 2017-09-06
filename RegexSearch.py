import os, re

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
    print(searchPhrase + ' found!')
    return len(contentList)

def main():
    useDefaultValid = False
    while (not useDefaultValid):
        useDefault = input('Use default filepath? (y/n): \n')
        if (useDefault.lower() == 'y'):
            folderPath = str(os.path.expanduser('~/Documents'))
            useDefaultValid = True
        elif (useDefault.lower() == 'n'):
            useDefaultValid = True
        else:
            print('Could not recognize input. Please enter \neither y for yes, or n for no\n')
    if (useDefaultValid):
        folderPathValid = True
    else:
        folderPathValid = False
    while (not folderPathValid):        
        folderPath = input('Please enter valid folder path: \n')
        folderPathValid = checkFolderPath(folderPath)
        if (not folderPathValid):
            print('Folder path invalid!\n')
    phrase = input('Enter a phrase to search text files for: \n')
    for file in os.listdir(folderPath):
        if (checkIfTxt(file)):
            fullPath = folderPath + '/' + file
            content = searchFile(fullPath)
            searchContentOccurences = findNumberOf(phrase, content)
            print(str(searchContentOccurences) + ' occurences in ' + file)

main()
