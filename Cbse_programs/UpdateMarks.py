import pickle
student_lst = [['1', 'Rohan',334], ['2', 'Deepash',769], ['3', 'Uday',875], ['4', 'Atul',785], ['5', 'Aditya',987]]
with open("Sample.bin", "wb") as f:
    pickle.dump(student_lst, f)
with open("Sample.bin", "rb") as f:
    a = pickle.load(f)
    search = input("Enter the ROll no. :-\n")
    for student in a:
        if student[0] == search:
            update = int(input("Enter the new marks:-\n"))
            student[2] = update
            print("Marks update successfully!")

print("Do you want to check the new list with updated marks?")
user_choice = input("Select q for quit and c for continue:- ")
if user_choice == "q":
    print("Thanks Bye!")
    exit()
elif user_choice == "c":
    print(a)