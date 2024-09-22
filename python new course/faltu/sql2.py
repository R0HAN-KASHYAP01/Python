import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

cursor = connection.cursor()

cursor.execute("USE CS")
cursor.execute("""INSERT INTO CLASS_XII(ROLLNO,NAME,MARKS)
               VALUES(1,'Rohan',67),
               (2,'Atul',62),
               (3,'Uday',69),
               (4,'Aditya',62)""")
connection.commit()

print("All the data Inserted Succesfully!")