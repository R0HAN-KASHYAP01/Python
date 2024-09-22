import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(host="localhost",user = "root", passwd = "#Shooting")
        return connection
    except mysql.connector.Error as error:
        print(f"ERROR: {error}")
        return None
    

connection = connect_to_database()
mycursor = connection.cursor()

try:
    mycursor.execute("Use Schooool;")
    # mycursor.execute("CREATE TABLE STUDENT(RollNo int Primary key, Name varchar(20), Class int, Marks int);")
    while True:
        Roll_no = int(input("Enter the roll number: "))
        Name = input("Enter the name of the student: ")
        Class = int(input("Enter the class of the student: "))
        Marks = int(input("Enter the Marks of the student: "))
        mycursor.execute("INSERT INTO student (RollNO,Name,Class, Marks) VALUES(%s,%s,%s,%s)",(Roll_no,Name,Class,Marks))
        connection.commit()
        choice = input("To add more data 'Y' and 'N' for not: ")
        if choice == "N":
            break

except mysql.connector.Error as error:
    print(f"ERROR : {error}")

