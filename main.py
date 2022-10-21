import Modules.truthTables as MT
import Modules.sets as MS
import sys

def printHelp():
    MT.cleanScreen()
    print('---------------------- Tablas de Verdad ------------------------ ')
    print('Uso: python main.py -t "[expresion]" ')
    print('Use unicamente estas variables: -  [p, q, r, s, t, u, w, x, y, z]')
    print('Conjuncion: ------------------------------------------------- "^"')
    print('Disyuncion: ------------------------------------------------- "v"')
    print('Negacion: --------------------------------------------------- "~"')
    print('Implicacion: ------------------------------------------------ ">"')
    print('Doble Implicacion: ------------------------------------------ "-"')
    print('-----------------------------------------------------------------')
    print('Nota: Es necesario escribir la expresion entre comillas ("")')
    print('Ejemplo: python main.py "p^qvr"')
    print('------------------ Operaciones de Conjuntos -------------------- ')
    print('Uso: python main.py -s [-A, -B or -C] [values]')
    print('Declara un conjunto -A, -B o -C, y a su derecha los valores')
    print('Ejemplo: python main.py -s -A 1,2,3 -C 2,3,4 -B 3,4,5')

#Main() function where all magic happen
def main():
    ARGS = sys.argv

    if ARGS[1] == '-t':
        MT.truthtable(ARGS[2])
    elif ARGS[1] == '-s':
        MS.sets(ARGS)
    else:
        printHelp()

#Simple try and except, if fails prints the help info 
#about usage and syntax using printHelp(), if not 
#main() worked

#"""
try:
    main()
except:
    printHelp()
#"""

#main()