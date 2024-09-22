filename = "Student.txt"
def student_record(filename):

    choice = "y"
    while choice.lower() == "y":
        roll_no = int(input("Enter the roll no: "))
        student_name = input("Enter the name of the student: ")
        address = input("Enter the address of the student: ")
        choice = input("Do you want to add more records? <y,n>: ")
        with open(filename, "+a") as f:
            f.write(f"{roll_no},{student_name},{address}\n")

        if choice.lower() == "y":
            continue
        else:
            print("All data submit successfully!\n")
            break
        
def student_readdata(filename):
    with open(filename, "r") as f:
        print("Student Information")
        print("-"*35)
        for student in f:
            print(student,end="")
        print("-"*35)
def student_search(filename):
    with open(filename, "r") as f:
        search = input("Enter the roll no. to be searched: ")
        for student in f:
            if student[0] == search:
                print(student)
            else:
                print(f"There is no student record of the {search} roll no.")

while True:
    print('''Choose any of the option given below:
1. Add record
2. See all student record
3. Search student
4. Save and Quit''')

    choice = input()
    if choice == "1":
        student_record(filename)
    elif choice == "2":
        student_readdata(filename)
    elif choice == "3":
        student_search(filename)

    elif choice == "4":
        print("Thanks for using Bye!")
        break

            