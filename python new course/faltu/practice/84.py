import mysql.connector
def connect_to_database():
    try:
        connection = mysql.connector.connect(host="localhost",user = "root", password = "#Shooting")
        return connection
    except mysql.connector.Error as error:
        print(f"ERROR : {error}")
        return None

connection = connect_to_database()
if connection:
    mycursor = connection.cursor()
    

try:
    mycursor.execute("USE Schooool")
    mycursor.execute("SELECT * FROM student WHERE MARKS >= 75")
    data = mycursor.fetchmany(5)
    print(data, type(data))
    # data = mycursor.fetchmany(5)
    # print(data, type(data))
    # data = mycursor.fetchmany(3)
    # print(data, type(data))

except mysql.connector.Error as error:
    print(f"ERROR : {error}")
