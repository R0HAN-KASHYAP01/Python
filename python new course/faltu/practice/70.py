Hostel = []
def Pust_element():
    while True:
        hostel_no = int(input("Enter the hostel number: "))
        Total_stu = int(input("Enter the total number of student: "))
        Total_room = int(input("Enter the total numbers of rooms: "))
        Hostel.append([hostel_no,Total_stu,Total_room])
        choice = input("To add more Enter 'Y' and 'N' for Not: ")
        if choice == "N":
            break

def Pop_element():
    while len(Hostel) != 0:
        print(Hostel.pop())

    else:
        print("Stack Empty")

Pust_element()
Pop_element()