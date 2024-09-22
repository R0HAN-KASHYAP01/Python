import csv
def searcher():
    with open("Student.csv", "r")as f:
        data = csv.reader(f)
        name = input("Enter the name you want to search:-\n")
        for row in data:
            if row[0] == name:
                print(row)
            else:
                print("Name not found")
                pass

def changer():
    with open("Student.csv", "r")as f:
        data = csv.reader(f)
    name = input("Enter the name you want to search:-\n")
    for row in data:
        if row[0] == name:
            print("What you want to change")
            print("1. Name")
            print("2. class")
            reponse = input()
            if reponse == "1":
                name_change = input("Enter the name:-\n")
                row[0] = name_change
            elif reponse == "2":
                class_change = input("Enter the class: ")
                row[1] = class_change

        else:
            print("Name not found")
            pass
            

def remover():
    with open("Student.csv", "r")as f:
        data = csv.reader(f)
    name = input("Enter the name you want to delete:-\n")
    for row in data:
        if row[0]== name:
            del row

        else:
            print("Name not found")
            pass
            




    
    while True:
        to_repete = input("To repeat enter --> Y & To exit enter --> N: ")
        if to_repete.lower()== "y":
            print(''' What you want to do 
            1. Search
            2. Change
            3. Delete
            ''')
            reponse = input()
            if reponse == "1":
                a = searcher()
            elif reponse == "2":
                a = changer()
            elif reponse == "3":
                a = remover()            
            else:
                pass
        elif to_repete.lower() == "n":
            break
        else:
            pass

