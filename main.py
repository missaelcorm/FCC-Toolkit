import sys
import numpy as np

def getVars(exp):
    nvars = []
    for letra in exp:
        if letra in vars:
            nvars.append(str(letra))
    nvars =  list(dict.fromkeys(nvars))
    nvars = len(nvars)

    return nvars
#Holaaaa
def formatExp(exp):
    for letra in exp:
        if '^' in exp:
            exp = exp.replace('^', ' and ')
        if 'v' in exp:
            exp = exp.replace('v', ' or ')
        if '~' in exp:
            exp = exp.replace('~', ' not ')
    
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

    return arr


args = sys.argv
vars = ['p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
exp = args[1]


p=1
q=1

exp = formatExp(exp)
nvars = getVars(exp)
#arr = assignValues(nvars)

print(nvars)

print(exp)

print(eval(exp))

#print(arr)