import pickle
student_lst = [['1', 'Rohan'], ['2', 'Deepash'], ['3', 'Uday'], ['4', 'Atul'], ['5', 'Aditya']]
with open("Sample.bin", "wb") as f:
    pickle.dump(student_lst, f)
with open("Sample.bin", "rb") as f:
    a = pickle.load(f)
    search = input("Enter the Roll no. :-\n")
    for i in range(0,len(student_lst)):
        if student_lst[i][0] == search:
            print(student_lst[i][1])
        else:
            print("Enter a valid roll no.!")
            exit()
