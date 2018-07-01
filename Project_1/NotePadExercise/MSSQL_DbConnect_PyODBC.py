import pyodbc
from os import getenv
# import pymssql
# import sys
# print(sys.version)
# import pymssql

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MANI;"
                      "Database=Bhagavan;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()
var='SELECT * FROM EmpDetails'
cursor.execute(var)
print(cursor.execute(var))

for row in cursor:
    print('row = %r' % row)
    # print('row = %r' % (row,))
