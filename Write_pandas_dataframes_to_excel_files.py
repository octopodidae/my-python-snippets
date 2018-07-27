# Install `XlsxWriter`
# pip install

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
file = "file2.xlsx"

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Specify a writer
writer = pd.ExcelWriter( file, engine="xlsxwriter" )

# Write your DataFrame to a file
df.to_excel( writer, "Sheet1" )

# Save the result
writer.save()