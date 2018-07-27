################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------

import os
import os.path
from datetime import datetime

#----------------------------------------------------
#		Zone de déclaration des variables globales
#----------------------------------------------------

#-------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

def add_line( file, line ):
    f = open( file, "a+")
    f.write( line )
    f.close()

def read_file( file ):
    f = open(file, "r")
    print( f.read() )
    # for line in f.readlines():
    #     print( line )
    f.close()

def get_properties( file ):
    f = open(file, "r")
    lines = f.readlines()
    print("Number of line(s) : ", len(lines))
    sizeFile = os.path.getsize(file)
    print("Size of file : ", sizeFile, " octet(s)")
    time = datetime.fromtimestamp(os.path.getctime(file)).strftime('%m/%d/%Y %H:%M:%S')
    print("Creation time : ", time )
    f.close()

#-------------------------------------------------------
#						PROGRAMME
#-------------------------------------------------------

print( "\nCurrent directory before chdir ", os.getcwd() )
os.chdir( os.getcwd() + r"\tmp" )
print( "Current directory after chdir ", os.getcwd() )

print( "\nWriting into new.txt file\n" )

newline = "Python is wonderfull !!\n"

add_line( "test.txt", newline )

print( "\nReading file", "new.txt\n" )

read_file( "test.txt" )

get_properties( "test.txt" )

