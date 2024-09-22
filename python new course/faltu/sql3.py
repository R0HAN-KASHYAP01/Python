import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

cursor = connection.cursor()

cursor.execute("USE CS")
cursor.execute("SELECT * FROM CLASS_XII")
record = cursor.fetchall()
no_rec = cursor.rowcount
print("Total no. of records found are:", no_rec)
for row in record:
    print(f"{row[0]}:{row[1]}:{row[2]};")
    