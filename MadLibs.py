import os, re, string

def getFilePath():
    return str(os.path.expanduser('~/Documents/madlibs.txt'))

def stripChars(string, characters):
    exclude = set(characters)
    return ''.join(ch for ch in string if ch not in exclude)

def findWordTypes(content):
    acceptedTypes = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
    wordTypesList = []

    wordTypes = content.split()
    for wordType in wordTypes:
        wordType = wordType.upper()
        wordTypeStrip = string.punctuation + "\n"
        wordType = stripChars(wordType, wordTypeStrip)
        if (wordType in acceptedTypes):
            if (wordType in wordTypesList):
                count = 0
                for words in wordTypesList:
                    words = stripChars(words, string.digits)
                    if (wordType == words):
                        count+=1
                wordTypesList.append(wordType + str(count))
            else:
                wordTypesList.append(wordType)
    return wordTypesList            

def createWordDictionary(wordTypes, words):
    wordDictionary = dict(zip(wordTypes, words))
    return wordDictionary
    
def replaceWords(fileContent, wordDictionary):
    for wordType in wordDictionary.keys():
        strippedWordType = stripChars(wordType, string.digits)
        fileContentRegex = re.compile(strippedWordType)
        fileContent = fileContentRegex.sub(wordDictionary[wordType], fileContent, count=1)
    return fileContent 

def main():
    theFilePath = getFilePath()
    theFile = open(theFilePath, 'r')
    fileContent = theFile.read()
    wordTypesList = findWordTypes(fileContent)
    wordList = []
    word = ''
    for wordType in wordTypesList:
        wordType = stripChars(wordType, string.digits)
        if (wordType[0] == 'a'):
            word = input('Enter an %s:\n' % (wordType))
        else:
            word = input('Enter a %s:\n' % (wordType))
        wordList.append(word)
    wordDictionary = createWordDictionary(wordTypesList, wordList)
    newContent = replaceWords(fileContent, wordDictionary)
    theFile = open(theFilePath, 'w')
    theFile.write(newContent)
    theFile.close()
    print(newContent)
main()
    
    


