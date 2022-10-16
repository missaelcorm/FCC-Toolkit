import Modules.truthTables as MT
import Modules.sets as MS
import sys

#Main() function where all magic happen
def main():
    ARGS = sys.argv

    if ARGS[1] == '-t':
        MT.truthtable(ARGS[2])
    elif ARGS[1] == '-s':
        MS.sets(ARGS)
    else:
        MT.printHelp()

#Simple try and except, if fails prints the help info 
#about usage and syntax using printHelp(), if not 
#main() worked

"""
"""
try:
    main()
except:
    MT.printHelp()
"""
"""

#main()