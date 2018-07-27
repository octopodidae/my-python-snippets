# pip install mysql-connector-python

import mysql.connector

user = "root"
password=""
host="127.0.0.1"
database_name= "pachadataformation"

connection = mysql.connector.connect( user=user, password=password, host=host, database=database_name )

print( "========================================")
print( "Host : {0}\nPort : {1}".format( connection.server_host, connection.server_port ) )
print( "========================================")

cur = connection.cursor()

cur.execute( "SELECT * FROM pays" )

result_set = cur.fetchall()

for row in result_set:
    print( row[2] )

print( "========================================")

cur.close()

connection.close()
