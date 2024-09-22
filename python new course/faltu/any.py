import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

cursor = connection.cursor()




cursor.execute("Drop database CS")