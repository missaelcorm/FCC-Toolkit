
def getPairs(ARGS):
    pairs = ARGS[2]
    pairs = list(pairs)
    pairsParsed = list()
    for i in range(len(pairs)):
        if(pairs[i]=='('):
            pairsParsed.append(tuple([int(pairs[i+1]), int(pairs[i+3])]))
    pairsParsed.sort()
    return pairsParsed
    

def isReflexive(PAIRS):
    reflexivity = True  # Assuming reflexivity from the start
    found = True
    for i in range(len(PAIRS)):  # For every element in the array
        current_x = PAIRS[i][0]  # Current x is found
        if found == False:  # If not found for reflexivity, cycle ends and reflexivity is false
            reflexivity = False
            break
        found = False  # Found value restarted
        for j in range(len(PAIRS)):
            if PAIRS[j][0] == current_x and PAIRS[j][1] == current_x:  # If x = c_x and y = c_x
                found = True  # Reflexivity is achieved
    return reflexivity


def isSymmetric(PAIRS):
    symmetry = True  # Symmetry assumed as true
    found = True
    for i in range(len(PAIRS)):  # For every element in the array
        current_x = PAIRS[i][0]
        current_y = PAIRS[i][1]
        if found == False:
            symmetry = False
            break
        found = False
        for j in range(len(PAIRS)):
            if PAIRS[j][0] == current_y and PAIRS[j][1] == current_x:  # If symmetry is found...
                found = True
    return symmetry


def isTransitive(PAIRS):
    transitivity = True  # Transitivity assumed as true
    for i in range(len(PAIRS)):  # For every element in the array
        current_x = PAIRS[i][0]
        current_y = PAIRS[i][1]
        if transitivity == False:
            break
        for j in range(len(PAIRS)):  # For every element in the array
            if PAIRS[j][0] == current_y:  # If an x equals current_y
                current_z = PAIRS[j][1]
                for k in range(len(PAIRS)):  # For every element in the array
                    if PAIRS[k][0] == current_x and PAIRS[k][1] == current_z:  # If (current_x, current_z) is found...
                        transitivity = True
                        break
                    else:
                        transitivity = False
    return transitivity

def getCoDomain(PAIRS):
    xDomain = set()
    yDomain = set()
    
    for i in range(len(PAIRS)):
        xDomain.add(PAIRS[i][0])
        yDomain.add(PAIRS[i][1])
        
    return xDomain, yDomain

def isFunction(PAIRS):
    for i in range(len(PAIRS)):
        if(i!=len(PAIRS)-1):
            if(PAIRS[i][0] == PAIRS[i+1][0]):
                return False
        
    return True

def relationsAndFunctions(ARGS):
    pairs = getPairs(ARGS)

    Reflexive = isReflexive(pairs)
    Symmetric = isSymmetric(pairs)
    Transitive = isTransitive(pairs)
    
    xDomain, yDomain = getCoDomain(pairs)
    
    isFunc = isFunction(pairs)
         
    print("Reflectividad:", Reflexive)
    print("Simetría:", Symmetric)
    print("Transitividad:", Transitive)
    
    print("Dominio X =", xDomain)
    print("Dominio Y =", yDomain)
    
    print("Funcion:", isFunc)
    