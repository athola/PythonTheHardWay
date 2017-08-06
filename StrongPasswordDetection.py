import re

def getPassword():
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
    print("A strong password has at least eight characters,")
    print("contains both uppercase and lowercase characters,")
    print("and has at least one digit.")
    passwordValidated = False
    while (not passwordValidated):
        thePw = getPassword()
        if (validatePassword(thePw)):
            passwordValidated = True
            print("Valid password!")
        else:
            print("Password invalid! Please try again.")
            print("")

main()
