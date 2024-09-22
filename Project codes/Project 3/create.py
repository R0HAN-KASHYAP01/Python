import mysql.connector

# Connect to MySQL server (assuming MySQL server is already installed and running)
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# # Create the database
cursor.execute("CREATE DATABASE Hotel_Management")
cursor.execute("USE hotel_management")

# Create the 'rooms' table
cursor.execute("""
    CREATE TABLE rooms (
        room_no INT Primary key ,
        room_type VARCHAR(50),
        location VARCHAR(100),
        max_guests INT,
        per_day_charge INT,
        status VARCHAR(20)
    )
""")

# Insert sample data into the 'rooms' table
cursor.execute("""
    INSERT INTO rooms (room_no, room_type, location, max_guests, per_day_charge, status)
    VALUES
        (101, 'Single', 'Tower A, Floor 1', 1, 100, 'Vacant'),
        (102, 'Double', 'Tower A, Floor 2', 2, 150, 'Vacant'),
        (201, 'Suite', 'Tower B, Floor 1', 3, 200, 'Vacant')
""")

# Create the 'bookings' table
cursor.execute("""
    CREATE TABLE bookings (
        booking_id INT AUTO_INCREMENT PRIMARY KEY,
        room_no INT,
        customer_name VARCHAR(100),
        id_number VARCHAR(20),
        address VARCHAR(200),
        phone_number VARCHAR(15),
        gender VARCHAR(10),
        checkin_date DATE,
        FOREIGN KEY (room_no) REFERENCES rooms(room_no)
    )
""")

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database, tables, and initial data created successfully.")
