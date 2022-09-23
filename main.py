import sys
from prettytable import PrettyTable

def printHelp():
    print('Usage: python main.py "[expression]" ')

def getVars(exp):
    vars = ['p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
    listVars = []
    for letra in exp:
        if letra in vars:
            listVars.append(str(letra))
    listVars =  list(dict.fromkeys(listVars))

    return listVars

def assignValues(nvars):
    matrix = []
    posibilidades = 2**nvars
    hNumber = len(str(bin(posibilidades)[2:]))-1
    
    for i in range(posibilidades):
        current_number = bin(i)[2:].zfill(hNumber)
        tempMatrix = [] 
        for digit in str(current_number):
            if digit == '1':
                tempMatrix.append('1')
            elif digit == '0':
                tempMatrix.append('0')
        #tempMatrix.append(eval(f"{tempMatrix[0]} and {tempMatrix[1]} and {tempMatrix[2]}"))
        matrix.append(tempMatrix)

    matrix = list(reversed(matrix))

    return matrix

def evalExp(exp, arr, vars):
    expTemp = exp
    for i in range(len(arr)):
        j=0
        for var in vars:
            expTemp = expTemp.replace(var, arr[i][j])
            if 'o1' in expTemp:
                expTemp = expTemp.replace('o1','or')
            if 'o0' in expTemp:
                expTemp = expTemp.replace('o0','or')
            if 'nor' in expTemp:
                expTemp = expTemp.replace('nor','not')
            j+=1
        
        #print(expTemp)
        arr[i].append(eval(expTemp))
        expTemp = exp

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '1' or arr[i][j] == 1 or arr[i][j] == True:
                arr[i][j]='T'
            elif arr[i][j] == '0' or arr[i][j] == 0 or arr[i][j] == False:
                arr[i][j]='F'

    return arr

def arrayToTable(arr, fieldNames):
    table = PrettyTable()
    table.add_rows(arr)
    table.field_names = fieldNames

    return table

def fieldNames(listVars, exp):
    fields = []
    for var in listVars:
        fields.append(var)
    fields.append(exp)
    
    return fields

def implication(partOne, partTwo):
    imp = ['(', '~', 'v', ')']

    for i in range(len(partTwo)):
        imp.insert(3+i, partTwo[i])
    for i in range(len(partOne)):
        imp.insert(2+i, partOne[i])

    return imp

def doubleImplication(partOne, partTwo):
    dimp = ["(","~","v",")","^","(","~","v",")"]

    for i in range(len(partOne)):
        dimp.insert(8+i, partOne[i])
    for i in range(len(partTwo)):
        dimp.insert(7+i, partTwo[i])
    for i in range(len(partTwo)):
        dimp.insert(3+i, partTwo[i])
    for i in range(len(partOne)):
        dimp.insert(2+i, partOne[i])
    
    return dimp

def listExpression(exp):
    exp = exp.replace(" ", "")
    listExp = list(exp)
    
    return listExp

def lookForSimpleOperators(listExp):

    while(('^' in listExp) or ('v' in listExp) or ('~' in listExp)):
        if '^' in listExp:
            listExp.insert(listExp.index('^'), 'and')
            listExp.remove('^')
        elif 'v' in listExp:
            listExp.insert(listExp.index('v'), 'or')
            listExp.remove('v')
        elif '~' in listExp:
            listExp.insert(listExp.index('~'), 'not')
            listExp.remove('~')

    return listExp

def lookForComplexOperators(listExp):
    j=1

    while j<len(listExp):
        if listExp[j] == '>':
            partOne, partTwo, lenExp, posDif = separator(listExp, '>')

            product = implication(partOne, partTwo)

            posOp = listExp.index('>')
            posOp -= posDif
            for i in range(lenExp):
                listExp.__delitem__(posOp)
            
            for k in range(len(product)):
                listExp.insert(posOp+k, product[k])
            
            j -= posDif
        elif listExp[j] == '-':
            partOne, partTwo, lenExp, posDif = separator(listExp, '-')

            product = doubleImplication(partOne, partTwo)

            posOp = listExp.index('-')
            posOp -= posDif

            for i in range(lenExp):
                listExp.__delitem__(posOp)
            
            for k in range(len(product)):
                listExp.insert(posOp+k, product[k])
            
            j -= posDif
        else:
            j+=1

    return listExp

def spacer(listExp):
    for i in range(1, (len(listExp)*2)-1, 2):
        listExp.insert(i, " ")

    return listExp

def listToString(listExp):
    expStr = ""

    for element in listExp:
        expStr+=element

    return expStr

def separator(exp, operator):
    vars = ['p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

    partOne = []
    OneFlag = True
    partTwo = []
    TwoFlag = True

    pos = exp.index(operator)

    # Part One
    while(OneFlag):
        if exp[pos-1] in vars:
            if exp[pos-2] == '~':
                partOne.insert(0, exp[pos-1])
                partOne.insert(0, exp[pos-2])
                OneFlag = False
            else:
                partOne.insert(0, exp[pos-1])
                OneFlag = False
        elif exp[pos-1] == ')':
            chPos = 2
            partOne.insert(0, ')')
            parentCounter = 1

            while(parentCounter!=0):
                if exp[pos-chPos] == ')':
                    partOne.insert(0, exp[pos-chPos])
                    chPos+=1
                    parentCounter+=1
                elif exp[pos-chPos] == '(':
                    partOne.insert(0, exp[pos-chPos])
                    chPos+=1
                    parentCounter-=1
                else:
                    partOne.insert(0, exp[pos-chPos])
                    chPos+=1

            if exp[pos-chPos] == '~':
                partOne.insert(0, exp[pos-chPos])
                OneFlag = False
            else:
                OneFlag = False

    # Part two
    while(TwoFlag):
        if exp[pos+1] in vars:
            partTwo.append(exp[pos+1])
            TwoFlag = False
        elif exp[pos+1] == '~':
            partTwo.append(exp[pos+1])
            if exp[pos+2] in vars:
                partTwo.append(exp[pos+2])
                TwoFlag = False
            elif exp[pos+1] == '(':
                parentCounter = 1
                chPos = 2
                partTwo.append(exp[pos+1])

                while(parentCounter!=0):
                    if exp[pos+chPos] == '(':
                        partTwo.append(exp[pos+chPos])
                        chPos+=1
                        parentCounter+=1
                    elif exp[pos+chPos] == ')':
                        partTwo.append(exp[pos+chPos])
                        chPos+=1
                        parentCounter-=1
                    else:
                        partTwo.append(exp[pos+chPos])
                        chPos+=1

                TwoFlag = False
        elif exp[pos+1] == '(':
            partTwo.append(exp[pos+1])
            parentCounter = 1
            chPos = 2

            while(parentCounter!=0):
                if exp[pos+chPos] == '(':
                    partTwo.append(exp[pos+chPos])
                    chPos+=1
                    parentCounter+=1
                elif exp[pos+chPos] == ')':
                    partTwo.append(exp[pos+chPos])
                    chPos+=1
                    parentCounter-=1
                else:
                    partTwo.append(exp[pos+chPos])
                    chPos+=1

                TwoFlag = False
    lenExp = len(partOne) + len(partTwo) + 1
    posDif = len(partOne)
    return partOne, partTwo, lenExp, posDif


def main():
    args = sys.argv

    if len(args) == 2:

        exp = args[1]

        vars = getVars(exp)

        matrix = assignValues(len(vars))

        expTemp = listExpression(exp)
        #print('listExpression', expTemp)
        expTemp = lookForComplexOperators(expTemp)
        #print('lookForComplexOperators', expTemp)
        expTemp = lookForSimpleOperators(expTemp)
        #print('lookForSimpleOperators', expTemp)
        expTemp = spacer(expTemp)
        #print('spacer', expTemp)
        expTemp = listToString(expTemp)
        #print('listToString', expTemp)

        evalExpression = evalExp(expTemp, matrix, vars)

        tableFields = fieldNames(vars, exp)
        table = arrayToTable(evalExpression, tableFields)

        print(table)

    else:
        printHelp()

try:
    main()
except:
    printHelp()
