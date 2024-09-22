#  Ques: Updating Marks of student using MySQL.connector

import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

cursor = connection.cursor()

cursor.execute("USE CS")

Student_name = input("Enter the Student:\n")

New_marks = int(input("Enter the new marks of the student:\n"))

cursor.execute('UPDATE Class_XII SET Marks = %s WHERE Name = %s',(New_marks, Student_name))
connection.commit()
print("Marks Update Succesfully!")
