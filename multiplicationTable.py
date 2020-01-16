import sys, openpyxl

def getInteger():
    if (len(sys.argv) > 1):
        tableSize = sys.argv[1]
    else:
        print('Please enter a positive integer!')
        tableSize = input()
    while not (tableSize.isdigit):
        print('Please enter a positive integer!')
        tableSize = input()
    print(tableSize)
    return int(tableSize)

def createWorkbook():
    multiplicationWorkbook = openpyxl.Workbook()
    activeSheet = multiplicationWorkbook.active
    activeSheet.title = 'Multiplication Table'
    return multiplicationWorkbook

def addValuesToSheet(workbook, tableSize):
    sheet = workbook['Multiplication Table']
    for i in range(2, tableSize + 2):
        sheet.cell(row=i, column=1).value = i-1
        sheet.cell(row=i, column=1).font = openpyxl.styles.Font(bold=True)
        sheet.cell(row=1, column=i).value = i-1
        sheet.cell(row=1, column=i).font = openpyxl.styles.Font(bold=True)
        for j in range(1, tableSize+1):
            sheet.cell(row=i, column=j+1).value = (i-1)*(j)
    workbook.save('multiplicationTableSize{}.xlsx'.format(tableSize))

multiSize = getInteger()
multiWB = createWorkbook()
addValuesToSheet(multiWB, multiSize)
