def printTable(table):
    longestStringInRow = []
    longestStringLen = 0
    for row in table:
        for item in row:
            if (len(item) > longestStringLen):
                longestStringLen = len(item)
        longestStringInRow.append(longestStringLen)
        longestStringLen = 0
    rowIndex = 0
    itemIndex = 0
    countedItems = 0
    totalItems = len(table) * len(table[0])
    while (countedItems < totalItems):
        if (rowIndex < len(table) - 1):
            justifyLen = longestStringInRow[rowIndex] - len(table[rowIndex][itemIndex])
            print((" " * justifyLen) + table[rowIndex][itemIndex].rjust(justifyLen) + " ", end="")
            rowIndex += 1
        else:
            justifyLen = longestStringInRow[rowIndex] - len(table[rowIndex][itemIndex])
            print((" " * justifyLen) + table[rowIndex][itemIndex].rjust(justifyLen))
            rowIndex = 0
            itemIndex += 1
        countedItems += 1

def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)

main()
