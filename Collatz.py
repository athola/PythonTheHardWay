import sys

def main():
    useCommandLine = False
    if (len(sys.argv) > 1):
        useCommandLine = True
    startingNumber = enterNumber(useCommandLine)
    print()
    checkIfOne(startingNumber)
    

def collatz(number):
    if number % 2 == 0:
        expression = number // 2
        print(expression)
        return (expression)
    else:
        expression = 3 * number + 1
        print(expression)
        return (expression)

def enterNumber(commandLineFlag):
    while True:
        print('Enter a number: ')
        if (commandLineFlag):
            number = sys.argv[1]
            print(number)
        else:
            number = input()
        try:
            return (int(number))
        except ValueError:
            print('That is not a valid integer')

def checkIfOne(number):
    notOne = True
    value = number
    while notOne:
       value = collatz(value)
       if value == 1:
           notOne = False

main()
        
        
