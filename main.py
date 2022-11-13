import Modules.truthTables as MT
import Modules.sets as MS
import Modules.successions as MK
import sys
import os

# Evaluate the OS where are running the file
# then clean the screen
def cleanScreen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def printHelp():
    cleanScreen()
    print('''Uso: python main.py [Modulo] [Opciones]>
TABLAS DE VERDAD:
    Use unicamente estas variables: [p, q, r, s, t, u, w, x, y, z]
    -t <"expresion">: tablas de verdad
        ^: Conjuncion
        v: Disyuncion
        ~: Negacion
        >: Implicacion
        -: Doble Implicacion
    Nota: Es necesario escribir la expresion entre comillas ("")
    Ejemplo: python main.py -t "p^qvr"
CONJUNTOS:
    Declara un conjunto -A, -B o -C, y a su derecha los valores
    -s: Operaciones de Conjuntos
    -A <VALORES>: Declara un conjunto A y sus valores separados por comas
    -B <VALORES>: Declara un conjunto B y sus valores separados por comas
    -C <VALORES>: Declara un conjunto C y sus valores separados por comas
    Ejemplo: python main.py -s -A 1,2,3 -C 2,3,4 -B 3,4,5
SUCESIONES:
    Ingresa una sucesion usando "k" como variable.
    -k: Sucesiones
    --expression <"expression">: La expresion a calcular, usando "k" como variable.
        +: Suma
        -: Resta
        /: Division
        *: Multiplicacion
        ^: Potencia
    --limInf <numero>: Limite Inferior
    --limSup <numero>: Limite Superior
    Opcionales:
    --decimals <numero de decimales>: Ingresa el numero de decimales deseado (2 por default).
    Ejemplo: python main.py -k --expression "1/k^2" --limInf 10 --limSup 30 --decimals 6''')

#Main() function where all magic happen
def main():
    ARGS = sys.argv

    if ARGS[1] == '-t':
        MT.truthtable(ARGS[2])
    elif ARGS[1] == '-s':
        MS.sets(ARGS)
    elif ARGS[1] == '-k':
        MK.successions(ARGS)
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