import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE CS")

cursor.execute("USE CS")

cursor.execute('''CREATE TABLE Class_XII(
    Rollno int(3) PRIMARY key,
    Name varchar(20),
    Marks integer)''')

print("Database and table created successfully! ")