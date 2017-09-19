import sys

useCommandLine = False
if (len(sys.argv) > 1):
    useCommandLine = True

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
if (useCommandLine):
    name = sys.argv[1]
else:
    name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
