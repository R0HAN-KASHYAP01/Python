import csv
field = ["Name", "Class"]
rows = []
def input_row():
    lst = []
    name = input("Enter the name: ")
    Class = input("Enter the class: ")
    lst.append(name)    
    lst.append(Class) 
    return lst   


while True:
    repeat = input("Do you want to enter data --> Y/N: ")
    if repeat.lower() == "y":
        a = input_row()
        rows.append(a)

    elif repeat.lower() == "n":       
        break
    else:
        pass

with open("student.csv", "w+", newline= '') as f:
    a = csv.writer(f, delimiter=",")
    a.writerow(field)
    for i in rows:
        a.writerow(i)
        

