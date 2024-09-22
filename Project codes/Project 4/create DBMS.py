
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS airlines")
cursor.execute("USE airlines")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS flights (
        id INT AUTO_INCREMENT PRIMARY KEY,
        departure_location VARCHAR(50),
        destination VARCHAR(50),
        departure_time DATETIME,
        seats_available INT
    )
""")

cursor.execute("""
    INSERT INTO flights (departure_location, destination, departure_time, seats_available)
    VALUES
        ('New York', 'Los Angeles', '2023-01-01 12:00:00', 50),
        ('Chicago', 'Miami', '2023-01-02 14:00:00', 30),
        ('San Francisco', 'Seattle', '2023-01-03 16:00:00', 20)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        flight_id INT,
        passenger_name VARCHAR(100),
        seat_class VARCHAR(20),
        FOREIGN KEY (flight_id) REFERENCES flights(id)
    )
""")

connection.commit()
connection.close()

print("Database, tables, and initial data created successfully.")
