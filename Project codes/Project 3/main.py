import mysql.connector
from datetime import datetime, timedelta

def display_available_rooms():
    query = "SELECT * FROM rooms WHERE status = 'Vacant'"
    cursor.execute(query)
    available_rooms = cursor.fetchall()

    print("\nAvailable Rooms:")
    for room in available_rooms:
        print(f"Room Number: {room[0]}, Type: {room[1]}, Location: {room[2]}, Max Guests: {room[3]}, Per Day Charge: {room[4]}")

def book_room():
    display_available_rooms()
    room_no = input("Enter the Room Number you want to book: ")

    cursor.execute("SELECT * FROM rooms WHERE room_no = %s AND status = 'Vacant'", (room_no,))
    room = cursor.fetchone()

    if room:
        customer_name = input("Enter your name: ")
        id_number = input("Enter your ID number: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        gender = input("Enter your gender: ")

        # Get check-in date and set check-out date (assuming a 3-day stay for simplicity)
        checkin_date = datetime.now().date()
        checkout_date = checkin_date + timedelta(days=3)

        # Update room status to 'Occupied'
        cursor.execute("UPDATE rooms SET status = 'Occupied' WHERE room_no = %s", (room_no,))
        db.commit()

        # Insert booking details into bookings table
        cursor.execute("""
            INSERT INTO bookings (room_no, customer_name, id_number, address, phone_number, gender, checkin_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (room_no, customer_name, id_number, address, phone_number, gender, checkin_date))
        db.commit()

        print(f"Room booking successful! Check-in Date: {checkin_date}, Check-out Date: {checkout_date}.")
    else:
        print("Invalid Room Number or the room is not vacant. Please try again.")

# Connect to MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting",
    database="hotel_management"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Main loop for the Hotel Management System
while True:
    print("\nHotel Management System:")
    print("1. Display Available Rooms")
    print("2. Book a Room")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_available_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        print("Exiting the Hotel Management System. Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Close the connection to the MySQL server
db.close()
