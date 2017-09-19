import re, sys

def getPassword(commandLineFlag):
    if (commandLineFlag):
        password = sys.argv[1]
    else:
        password = input("Please enter a valid password: ")
    return password

def validatePassword(password):
    validPassword = False
    uppercasePasswordRegex = re.compile(r'[A-Z]')
    lowercasePasswordRegex = re.compile(r'[a-z]')
    digitPasswordRegex = re.compile(r'\d')
    eightCharsPasswordRegex = re.compile(r'(.*){8,}')
    if (uppercasePasswordRegex.search(password) != None and
        lowercasePasswordRegex.search(password) != None and
        digitPasswordRegex.search(password) != None and
        eightCharsPasswordRegex != None):

        validPassword = True
    return validPassword

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True
    print("A strong password has at least eight characters,")
    print("contains both uppercase and lowercase characters,")
    print("and has at least one digit.")
    passwordValidated = False
    while (not passwordValidated):
        thePw = getPassword(useCommandLine)
        if (validatePassword(thePw)):
            passwordValidated = True
            print("Valid password!")
        else:
            print("Password invalid! Please try again.")
            print("")
            useCommandLine = False

main()
