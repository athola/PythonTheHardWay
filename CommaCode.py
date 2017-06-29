def separateWithComma(listItem):
    newStr = ''
    for item in listItem:
        if item == listItem[-1]:
            newStr += ('and ' + str(item))
        else:
            newStr += (str(item) + ', ')
    return newStr

def main():
    theList = [2, '4', 6, 8, 10, True]
    theStr = separateWithComma(theList)
    print(theStr)

main()
