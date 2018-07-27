import os
import xml.etree.ElementTree as ET

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print("==========================")
print( cwd )
print("==========================")
# Change directory
os.chdir(r"C:\BLA\dev\python\training\my-python-snippets\tmp")
print( os.getcwd() )
print("==========================")
# List all files and directories in current directory
print( os.listdir(".") )
print("==========================")
# Assign spreadsheet filename to `file`
file = "movies.xml"

tree = ET.parse("./movies.xml")

root = tree.getroot()

print("==========================")

print( "root.tag :", root.tag )

print("==========================")

for child in root:
    print( child.tag, child.attrib )

tags = [elem.tag for elem in root.iter()]

print("==========================")

for tag in tags:
    print (tag )

print("==========================")

for movie in root.iter( "movie" ):
    print( movie.attrib["title"] )

print("==========================")