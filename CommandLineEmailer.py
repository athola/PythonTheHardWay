import re, sys
from selenium import webdriver

def enterArgument(argument):
    while True:
        print(argument.txt)
        if (argument.flg):
            entry = sys.argv[argument.num]
            print(entry)
        else:
            entry = input()
        if re.match(argument.reg, entry):
            return (entry)
        else:
            argument.flg = False
            
class Argument:
    def __init__(self, text, flag, number, regex_string):
        self.txt = text
        self.flg = flag
        self.num = number
        self.reg = regex_string

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True

    email = enterArgument(Argument('Enter your email: ', useCommandLine, 1, '(.*)@(.*)'))
    searchText = enterArgument(Argument('Enter text to search for: ', useCommandLine, 1, '.*'))
    browser = webdriver.Chrome()
    broswer.get("http://gmail.com")
    print(type(browser))

main()
