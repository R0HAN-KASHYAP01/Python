import mysql.connector
from datetime import date

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting",
    database="Employee_Management"
)

cursor = db.cursor()

def mark_attendance(employee_id, status):
    today = date.today()
    attendance_date = today.strftime("%Y-%m-%d")

    cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
    employee = cursor.fetchone()

    if employee:
        cursor.execute("INSERT INTO attendance (employee_id, attendance_date, status) VALUES (%s, %s, %s)",
                       (employee_id, attendance_date, status))
        db.commit()
        print(f"Attendance marked for {employee[1]} ({status}) on {attendance_date}.")
    else:
        print(f"Employee with ID {employee_id} not found.")

def view_attendance(employee_id):
    cursor.execute("SELECT * FROM attendance WHERE employee_id = %s", (employee_id,))
    attendance_records = cursor.fetchall()

    print(f"\nAttendance records for Employee ID {employee_id}:")
    for record in attendance_records:
        print(f"Date: {record[2]}, Status: {record[3]}")

while True:
    print("\nEmployee Attendance System:")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        employee_id = int(input("Enter Employee ID: "))
        status = input("Enter Attendance Status (Present/Absent): ").capitalize()
        mark_attendance(employee_id, status)
    elif choice == "2":
        employee_id = int(input("Enter Employee ID: "))
        view_attendance(employee_id)
    elif choice == "3":
        print("Exiting the Employee Attendance System. Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

db.close()
