
def calcUnion(setA=None, setB=None, setC=None):

    if(setA is None and setB is None and setC is None):               return None
    elif(setA is None and setB is None and setC is not None):         return setC
    elif(setA is None and setB is not None and setC is None):         return setB
    elif(setA is None and setB is not None and setC is not None):     return setB | setC
    elif(setA is not None and setB is None and setC is None):         return setA
    elif(setA is not None and setB is None and setC is not None):     return setA | setC
    elif(setA is not None and setB is not None and setC is None):     return setA | setB
    elif(setA is not None and setB is not None and setC is not None): return setA | setB | setC

def calcIntersection(setA=None, setB=None, setC=None):

    if(setA is None and setB is None and setC is None):               return None
    elif(setA is None and setB is None and setC is not None):         return setC
    elif(setA is None and setB is not None and setC is None):         return setB
    elif(setA is None and setB is not None and setC is not None):     return setB & setC
    elif(setA is not None and setB is None and setC is None):         return setA
    elif(setA is not None and setB is None and setC is not None):     return setA & setC
    elif(setA is not None and setB is not None and setC is None):     return setA & setB
    elif(setA is not None and setB is not None and setC is not None): return setA & setB & setC

def calcDifference(setA=None, setB=None, setC=None):

    if(setA is None and setB is None and setC is None):               return None
    elif(setA is None and setB is None and setC is not None):         return setC
    elif(setA is None and setB is not None and setC is None):         return setB
    elif(setA is None and setB is not None and setC is not None):     return setB - setC
    elif(setA is not None and setB is None and setC is None):         return setA
    elif(setA is not None and setB is None and setC is not None):     return setA - setC
    elif(setA is not None and setB is not None and setC is None):     return setA - setB
    elif(setA is not None and setB is not None and setC is not None): return setA - setB - setC

def calcSymetricDifference(setA=None, setB=None, setC=None):

    if(setA is None and setB is None and setC is None):               return None
    elif(setA is None and setB is None and setC is not None):         return setC
    elif(setA is None and setB is not None and setC is None):         return setB
    elif(setA is None and setB is not None and setC is not None):     return setB ^ setC
    elif(setA is not None and setB is None and setC is None):         return setA
    elif(setA is not None and setB is None and setC is not None):     return setA ^ setC
    elif(setA is not None and setB is not None and setC is None):     return setA ^ setB
    elif(setA is not None and setB is not None and setC is not None): return setA ^ setB ^ setC

def setEmpty(SET):
    if(len(SET)==0):
        return True
    else:
        return False

def defSets(sets):
    A = set()
    B = set()
    C = set()
    tempSet = ""
    for i in range(len(sets)):
        if sets[i] == '-A':
            tempSet = sets[i+1]
            A.update(tempSet.split(','))
        elif sets[i] == '-B':
            tempSet = sets[i+1]
            B.update(tempSet.split(','))
        elif sets[i] == '-C':
            tempSet = sets[i+1]
            C.update(tempSet.split(','))

    return checkSets(A, B, C)

def checkSets(setA=None, setB=None, setC=None):
    if(setEmpty(setA) and setEmpty(setB) and setEmpty(setC)):               return None, None, None
    elif(setEmpty(setA) and setEmpty(setB) and not setEmpty(setC)):         return None, None, setC
    elif(setEmpty(setA) and not setEmpty(setB) and setEmpty(setC)):         return None, setB, None
    elif(setEmpty(setA) and not setEmpty(setB) and not setEmpty(setC)):     return None, setB, setC
    elif(not setEmpty(setA) and setEmpty(setB) and setEmpty(setC)):         return setA, None, None
    elif(not setEmpty(setA) and setEmpty(setB) and not setEmpty(setC)):     return setA, None, setC
    elif(not setEmpty(setA) and not setEmpty(setB) and setEmpty(setC)):     return setA, setB, None
    elif(not setEmpty(setA) and not setEmpty(setB) and not setEmpty(setC)): return setA, setB, setC


def sets(sets):
    setA, setB, setC = defSets(sets)
    print("UNION", calcUnion(setA, setB, setC))
    print("INTERSECTION", calcIntersection(setA, setB, setC))
    print("DIFFERENCE", calcDifference(setA, setB, setC))
    print("SYMETRIC DIFFERENCE", calcSymetricDifference(setA, setB, setC))
