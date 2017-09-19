import sys

useCommandLine = False
if (len(sys.argv) > 1):
    useCommandLine = True

print('Hello world!')
print('What is your name?')
if (useCommandLine):
    myName = sys.argv[1]
else:
    myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
if (useCommandLine):
    myName = sys.argv[2]
else:
    myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

