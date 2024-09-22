import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Shooting",
    database="airlines"
)

cursor = db.cursor()

def display_flights():
    query = "SELECT * FROM flights"
    cursor.execute(query)
    flights = cursor.fetchall()

    print("\nAvailable Flights:")
    for flight in flights:
        print(f"Flight ID: {flight[0]}, From: {flight[1]}, To: {flight[2]}, Departure Time: {flight[3]}")

def book_flight():
    display_flights()
    flight_id = input("Enter the Flight ID you want to book: ")

    cursor.execute("SELECT * FROM flights WHERE id = %s", (flight_id,))
    flight = cursor.fetchone()

    if flight:
        passenger_name = input("Enter your name: ")
        seat_class = input("Enter seat class (Economy/Business): ")

        cursor.execute("UPDATE flights SET seats_available = seats_available - 1 WHERE id = %s", (flight_id,))
        db.commit()

        cursor.execute("INSERT INTO bookings (flight_id, passenger_name, seat_class) VALUES (%s, %s, %s)",
                       (flight_id, passenger_name, seat_class))
        db.commit()

        print(f"Booking successful! Thank you, {passenger_name}.")
    else:
        print("Invalid Flight ID. Please try again.")

while True:
    print("\nAirline Booking System:")
    print("1. Display Available Flights")
    print("2. Book a Flight")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_flights()
    elif choice == "2":
        book_flight()
    elif choice == "3":
        print("Exiting the booking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
