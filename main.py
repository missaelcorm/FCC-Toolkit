import sys
import numpy as np
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
    #a^bva^cv~c
    #[a, b, a, c, c]
    #[a,b,c]
    nvars = len(listVars)

    return listVars

def formatExp(exp):
    for letra in exp:
        if '^' in exp:
            exp = exp.replace('^', ' and ')
        if 'v' in exp:
            exp = exp.replace('v', ' or ')
            
        if '~' in exp:
            exp = exp.replace('~', ' not ')
        if '->' in exp:
            index = exp.find('->')
            exp = exp.replace('->', ') or ')
            
            exp = exp[:index-1] + ' (not ' + exp[index-1:]
    print(exp)
    return exp

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

    arr = np.array(matrix)

    return matrix

def setVars(vars, arr):

    for j in range(len(arr)):
        arr[j].append(eval(f"{arr[j][0]} or not {arr[j][1]}"))
    print(np.array(arr))
    return arr

def evalExp(exp, arr, vars):
    expTemp = exp
    for i in range(len(arr)):
        j=0
        for var in vars:
            expTemp = expTemp.replace(var, arr[i][j])
            j+=1

        expTemp = formatExp(expTemp)

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


args = sys.argv
exp = args[1]

#exp = "~((p->q)^(rvs)^((~s->~t)^(~qvs)^(~s)^((~p^r->u)^(wvt)->u^w"#args[1]


p=0
q=1

varse = getVars(exp)
#exp = formatExp(exp)
arr = assignValues(len(varse))
#dictVars = setVars(varse, arr)
evExp = evalExp(exp, arr, varse)

fields = fieldNames(varse, exp)
table = arrayToTable(evExp, fields)

print(table)
#print(np.array(evExp))

#print(varse)
#print(dictVars)
#print(arr)
#print(exp)

#print(eval(exp))

#print(arr)