#Receives the sets, and then if any argument has -A, -B or -C the next argument should be
#the content of the sets. So if we declare -A 1,2,3 the set "A" is gonna have {1,2,3} as values
def defSets(sets):
    A = set()
    B = set()
    C = set()
    indexA = None
    indexB = None
    indexC = None
    tempSet = ""
    for i in range(len(sets)):
        if sets[i] == '-A':
            indexA = i
            tempSet = sets[i+1]
            A.update(tempSet.split(','))
        elif sets[i] == '-B':
            indexB = i
            tempSet = sets[i+1]
            B.update(tempSet.split(','))
        elif sets[i] == '-C':
            indexC = i
            tempSet = sets[i+1]
            C.update(tempSet.split(','))
    
    A, B, C = checkSets(A, B, C)

    return A, B, C, indexA, indexB, indexC

#Check if the sets A, B and C are empty or not, evaluates each possibilities if some sets are not declared
def checkSets(setA=None, setB=None, setC=None):
    if(setEmpty(setA) and setEmpty(setB) and setEmpty(setC)):               return None, None, None
    elif(setEmpty(setA) and setEmpty(setB) and not setEmpty(setC)):         return None, None, setC
    elif(setEmpty(setA) and not setEmpty(setB) and setEmpty(setC)):         return None, setB, None
    elif(setEmpty(setA) and not setEmpty(setB) and not setEmpty(setC)):     return None, setB, setC
    elif(not setEmpty(setA) and setEmpty(setB) and setEmpty(setC)):         return setA, None, None
    elif(not setEmpty(setA) and setEmpty(setB) and not setEmpty(setC)):     return setA, None, setC
    elif(not setEmpty(setA) and not setEmpty(setB) and setEmpty(setC)):     return setA, setB, None
    elif(not setEmpty(setA) and not setEmpty(setB) and not setEmpty(setC)): return setA, setB, setC

#This sort the Name set (A, B or C) in order to be evaluated correctly
def indexSets(indexA, indexB, indexC, setA, setB, setC):
    One, Two, Three = None, None, None
    setOne, setTwo, setThree = {}, {}, {}

    if indexA is None:
        indexA = 99
    if indexB is None:
        indexB = 99
    if indexC is None:
        indexC = 99

    if(indexA < indexB and indexA < indexC): 
        One = indexA
        setOne = setA
        if(indexB < indexC): 
            Two = indexB
            Three = indexC
            setTwo = setB
            setThree = setC
        else:
            Three = indexB
            Two = indexC
            setTwo = setC
            setThree = setB
    elif(indexB < indexA and indexB < indexC): 
        One = indexB
        setOne = setB
        if(indexA < indexC): 
            Two = indexA
            Three = indexC
            setTwo = setA
            setThree = setC
        else:
            Three = indexA
            Two = indexC
            setTwo = setC
            setThree = setA
    elif(indexC < indexB and indexC < indexA): 
        One = indexC
        setOne = setC
        if(indexB < indexA): 
            Two = indexB
            Three = indexA
            setTwo = setB
            setThree = setA
        else:
            Three = indexB
            Two = indexA
            setTwo = setA
            setThree = setB

    if One == 99:
        One = None
    if Two == 99:
        Two = None
    if Three == 99:
        Three = None

    return One, Two, Three, setOne, setTwo, setThree

#This gets the flags. Ex. -A -> "A"
def indexSetText(PositionOne, PositionTwo, PositionThree, ARGS):
    setA, setB, setC = PositionOne, PositionTwo, PositionThree
    if(setA is None and setB is None and setC is None):
        return None
    elif(setA is None and setB is None and setC is not None):
        return "", "", ARGS[PositionThree].replace("-", "")
    elif(setA is None and setB is not None and setC is None):
        return "", ARGS[PositionTwo].replace("-", ""), ""
    elif(setA is None and setB is not None and setC is not None):
        return "", ARGS[PositionTwo].replace("-", ""), ARGS[PositionThree].replace("-", "")
    elif(setA is not None and setB is None and setC is None):
        return ARGS[PositionOne].replace("-", ""), "", ""
    elif(setA is not None and setB is None and setC is not None):
        return ARGS[PositionOne].replace("-", ""), "", ARGS[PositionThree].replace("-", "")
    elif(setA is not None and setB is not None and setC is None):
        return ARGS[PositionOne].replace("-", ""), ARGS[PositionTwo].replace("-", ""), ""
    elif(setA is not None and setB is not None and setC is not None):
        return ARGS[PositionOne].replace("-", ""), ARGS[PositionTwo].replace("-", ""), ARGS[PositionThree].replace("-", "")

#Receives the Name of the sets (A, B or C), the operations and returns a string with the operation that's being evaluated
def printOP(setA, setB, setC, operation, textSet):
    if(setA is None and setB is None and setC is None):               return "No hay conjuntos"
    elif(setA is None and setB is None and setC is not None):         return f"{textSet[0]} {operation} 'N/A':"
    elif(setA is None and setB is not None and setC is None):         return f"{textSet[0]} {operation} 'N/A':"
    elif(setA is None and setB is not None and setC is not None):     return f"{textSet[0]} {operation} {textSet[1]}:"
    elif(setA is not None and setB is None and setC is None):         return f"{textSet[0]} {operation} 'N/A':"
    elif(setA is not None and setB is None and setC is not None):     return f"{textSet[0]} {operation} {textSet[1]}:"
    elif(setA is not None and setB is not None and setC is None):     return f"{textSet[0]} {operation} {textSet[1]}:"
    elif(setA is not None and setB is not None and setC is not None): return f"{textSet[0]} {operation} {textSet[1]} {operation} {textSet[2]}:"

#Gets 3 sets (does not matter if there are just 1, 2 or 3 sets) and then return the Operation from operation parameter
def calcOperation(setA=None, setB=None, setC=None, operation=None):

    if(setA is None and setB is None and setC is None):               return None
    elif(setA is None and setB is None and setC is not None):         return eval(f"{setC}")
    elif(setA is None and setB is not None and setC is None):         return eval(f"{setB}")
    elif(setA is None and setB is not None and setC is not None):     return eval(f"{setB} {operation} {setC}")
    elif(setA is not None and setB is None and setC is None):         return eval(f"{setA}")
    elif(setA is not None and setB is None and setC is not None):     return eval(f"{setA} {operation} {setC}")
    elif(setA is not None and setB is not None and setC is None):     return eval(f"{setA} {operation} {setB}")
    elif(setA is not None and setB is not None and setC is not None): return eval(f"{setA} {operation} {setB} {operation} {setC}")

#If a result of any operation is empty, returns 0, if not returns the content of the operation
def setResultEmpty(SET):
    if(setEmpty(SET)):
        return 0
    else:
        return SET

#If a set has a len of 0, then is empty and return True, if not return False
def setEmpty(SET):
    if(len(SET)==0):
        return True
    else:
        return False

#This receives the arguments or sets from main.py, then do the calculation and print it
def sets(sets):
    setA, setB, setC, indexA, indexB, indexC = defSets(sets)
    indexOne, indexTwo, indexThree, setA, setB, setC = indexSets(indexA, indexB, indexC, setA, setB, setC)
    indexText = indexSetText(indexOne, indexTwo, indexThree, sets)

    opUnion = printOP(setA, setB, setC, "∪", indexText)
    opInter = printOP(setA, setB, setC, "∩", indexText)
    opDiff = printOP(setA, setB, setC, "-", indexText)
    opSymDiff = printOP(setA, setB, setC, "△", indexText)


    print(opUnion, setResultEmpty(calcOperation(setA, setB, setC, '|')))
    print(opInter, setResultEmpty(calcOperation(setA, setB, setC, '&')))
    print(opDiff, setResultEmpty(calcOperation(setA, setB, setC, '-')))
    print(opSymDiff, setResultEmpty(calcOperation(setA, setB, setC, '^')))
