import csv
def ADD():
    with open("Resultss.csv","a",newline="") as f:
        mywriter = csv.writer(f,delimiter=",")
        while True:
            EmpID = int(input("Enter the ID: "))
            Name = input("Enter the Name: ")
            Mobileno = int(input("Enter the mobile NO: "))
            Salary = int(input("Enter the salary: "))
            mywriter.writerow([EmpID,Name,Mobileno,Salary])
            choice = input("To add more 'y' and 'n' for exit: ")
            if choice == "N":
                break

def countR():
    with open("Resultss.csv","r") as f:
        data = csv.reader(f)
        count = 0
        for row in data:
            count += 1
    
    print(f"Total number of records in the file are {count-1}")

        

# ADD()
countR()