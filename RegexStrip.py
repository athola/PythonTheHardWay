import re

def stripString(string, char=""):
    newStr = ""
    if (char==""):
        frontStrippedStr = ""
        stripFrontSpaceRegex = re.compile(r'^\s+')
        frontStrippedStr = stripFrontSpaceRegex.sub('', string)
        stripEndSpaceRegex = re.compile(r'\s+$')
        newStr = stripEndSpaceRegex.sub('', frontStrippedStr)
    else:
        stripCharRegex = re.compile(char)
        newStr = stripCharRegex.sub('', string)
    return newStr

def main():
    string = input("Please enter a string: ")
    char = input("Please enter a character to strip from the string: ")
    newString = stripString(string, char)
    print(newString)

main()
                                    
        
