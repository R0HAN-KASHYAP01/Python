import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE Employee_Management")
cursor.execute("USE Employee_Management")

cursor.execute("""
    CREATE TABLE employees ( 
        Employee_id INT PRIMARY KEY AUTO_INCREMENT,
        Employee_name VARCHAR(100) NOT NULL,
        Designation VARCHAR(50) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE attendance (
        Attendance_id INT PRIMARY KEY AUTO_INCREMENT,
        Employee_id INT,
        Attendance_Date DATE,
        Status VARCHAR(10),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
""")

db.close()

print("Database and tables created successfully.")
