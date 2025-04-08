import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '7015743950'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE webdb")

print("All Done")