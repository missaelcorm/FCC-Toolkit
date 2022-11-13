from prettytable import PrettyTable as PT

RES = []
SUM = 0
MULT = 1
COUNTER = 0
DECIMALS = 2


def setARGS(ARGS):
    global DECIMALS
    lim_sup = None
    lim_inf = None
    expression = ''
    for i in range(1, len(ARGS)):
        if ARGS[i] == '--limSup':
            lim_sup = int(ARGS[i+1])
        elif ARGS[i] == '--limInf':
            lim_inf = int(ARGS[i+1])
        elif ARGS[i] == '--expression':
            expression = ARGS[i+1]
        elif ARGS[i] == '--decimals':
            DECIMALS = int(ARGS[i+1])

    if lim_inf is None or lim_sup is None or expression == '':
        print('Error')

    return expression, lim_inf, lim_sup


def formatSuccession(succession):
    return succession.replace('^', '**')


def calcSucc(ak, lim_inf, lim_sup):
    global SUM, MULT
    if lim_inf <= lim_sup:
        k = lim_sup
        R = eval(ak)
        SUM += float(R)
        MULT *= float(R)
        RES.append(R)

        calcSucc(ak, lim_inf, lim_sup - 1)

    return SUM, MULT


def def_ak(ak, lim_inf, lim_sup):
    listTerms = []
    listkn = []
    count = 0
    for k in range(lim_inf, lim_sup + 1):
        listkn.append(f"k({lim_sup}-{count})")
        count += 1

    for k in range(lim_sup, lim_inf-2, -1):
        listTerms.append(ak.replace('k', str(k)).replace('**', '^'))

    return listTerms, listkn


def listsToMatrix(listTerms, listkn, RES):
    Matrix = []
    tempMatrix = []
    for i in range(len(RES)):
        tempMatrix.append(listTerms[i])
        tempMatrix.append(listkn[i])
        tempMatrix.append(format(round(RES[i], DECIMALS), f'.{DECIMALS}f'))
        Matrix.append(tempMatrix)
        tempMatrix = []

    return Matrix


def makeTable(matrix, succession, SUM_RES, MULT_RES):
    table = PT()
    table.field_names = [succession.replace('**', '^'), 'k(n-C)', "Result"]
    table.align["Result"] = 'r'
    table.add_rows(matrix)
    table.add_row(['---', '---', '---'])
    table.add_row(['', 'SUMA:', format(round(SUM_RES, DECIMALS), f'.{DECIMALS}f')])
    table.add_row(['', 'MULT:', f'{{:.{DECIMALS}e}}'.format(MULT_RES)])

    return table


def successions(ARGS):
    expression, lim_inf, lim_sup = setARGS(ARGS)
    expression = formatSuccession(expression)

    SUM_RES, MULT_RES = calcSucc(expression, lim_inf, lim_sup)

    listTerms, listkn = def_ak(expression, lim_inf, lim_sup)

    matrix = listsToMatrix(listTerms, listkn, RES)

    Table = makeTable(matrix, expression, SUM_RES, MULT_RES)
    print(Table)
