#From ARGS returns a list of tuples
def getPairs(ARGS):
    pairs = ARGS[2]
    pairs = list(pairs) #Convert from str to a list
    pairsParsed = list()
    for i in range(len(pairs)):
        if(pairs[i]=='('):  #If an element is '(' the next character sould be 'x' then the comma and finally the 'y' value
            pairsParsed.append(tuple([int(pairs[i+1]), int(pairs[i+3])]))  #Append as a tuple x and y to the final list
    pairsParsed.sort()  #Sort the list by tuple values
    return pairsParsed

#Checks if is reflective
def isReflexive(PAIRS):
    found = True
    for i in range(len(PAIRS)):  # For every element in the array
        actualX = PAIRS[i][0]  # Actual x is found
        if found == False:  # If reflexivity was not found, cycle ends and reurns false
            return False
        found = False  # Found value restarted
        for j in range(len(PAIRS)):
            if PAIRS[j][0] == actualX and PAIRS[j][1] == actualX:  # If x = actualX and y = actualX
                found = True  # Reflexivity was found
    return True

#Checks if is symmetric
def isSymmetric(PAIRS):
    found = True
    for i in range(len(PAIRS)):  # For every element in the array
        actualX = PAIRS[i][0]
        actualY = PAIRS[i][1]
        if found == False:
            return False
        found = False
        for j in range(len(PAIRS)):
            if PAIRS[j][0] == actualY and PAIRS[j][1] == actualX:  # If symmetry is found, we set found as true
                found = True
    return True


#Checks if is transitive
def isTransitive(PAIRS):
    transitive = True  # Transitivity assumed as true
    for i in range(len(PAIRS)):  # For every element in the array
        actualX = PAIRS[i][0]
        actualY = PAIRS[i][1]
        if transitive == False:
            break
        for j in range(len(PAIRS)):  # For every element in the array
            if PAIRS[j][0] == actualY:  # If an x equals actualY
                newActualY = PAIRS[j][1]
                for k in range(len(PAIRS)):  # For every element in the array
                    if PAIRS[k][0] == actualX and PAIRS[k][1] == newActualY:  # If (actualX, newActualY) is found, it's True
                        transitive = True
                        break
                    else:
                        transitive = False
    return transitive

#Returns 'x' and 'y' domains
def getCoDomain(PAIRS):
    #We defines 'x' and 'y' sets, this to just have unique values
    xDomain = set()
    yDomain = set()
    
    for i in range(len(PAIRS)):
        xDomain.add(PAIRS[i][0]) #For every set, the first value is added to 'x' set
        yDomain.add(PAIRS[i][1]) #For every set, the second value is added to 'y' set
        
    return xDomain, yDomain

#Returns if the pairs can be a function
def isFunction(PAIRS):
    for i in range(len(PAIRS)):
        if(i!=len(PAIRS)-1):  #This evaluate if i+1 exist
            if(PAIRS[i][0] == PAIRS[i+1][0]):  #If 2 'x' values has 2 or more 'y' values return false
                return False

    return True

#Receives arguments from main, and then do the calculations
def relationsAndFunctions(ARGS):
    pairs = getPairs(ARGS)

    Reflexive = isReflexive(pairs)
    Symmetric = isSymmetric(pairs)
    Transitive = isTransitive(pairs)
    
    xDomain, yDomain = getCoDomain(pairs)
    
    isFunc = isFunction(pairs)
         
    print("Reflexividad:", Reflexive)
    print("Simetría:", Symmetric)
    print("Transitividad:", Transitive)
    
    print("Dominio X =", xDomain)
    print("Dominio Y =", yDomain)
    
    print("Funcion:", isFunc)
    