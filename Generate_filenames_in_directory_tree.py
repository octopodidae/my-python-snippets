import os

path = input("Specify a folder to scan : ")

for root, dirs, files in os.walk(path):
    print ( root )
    print ( "---------------" )
    print ( dirs )
    print ( "---------------" )
    print ( files )
    print ( "---------------" )
