import sys

print('Please enter a value for spam: ')

useCommandLine = False
if (len(sys.argv) > 1):
    useCommandLine = True

if (useCommandLine):
    spam = sys.argv[1]
else:
    spam = input()
    
if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings!')
