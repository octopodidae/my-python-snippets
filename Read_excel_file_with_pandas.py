import os
import pandas as pd

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print( cwd )

# Change directory
os.chdir(r"C:\BLA\dev\python\training\my-python-snippets\tmp")
print( os.getcwd() )

# List all files and directories in current directory
print( os.listdir(".") )

# Assign spreadsheet filename to `file`
file = "file.xlsx"

# Load spreadsheet
xl = pd.ExcelFile( file )

print( xl.sheet_names )

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse( "Feuille1" )
print( df1 )





