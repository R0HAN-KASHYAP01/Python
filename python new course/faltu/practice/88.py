import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost",user = "root",password="#Shooting",database = "Schooool")

    mycursor = connection.cursor()

except mysql.connector.Error as Error:
    print(f"ERROR : {Error}")

# # mycursor.execute("Delete from student where marks < 95")
# connection.commit()
# print(mycursor.rowcount)

mycursor.execute("Select * from Student")
read = mycursor.fetchall()
print(read)
