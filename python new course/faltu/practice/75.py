import csv
with open("Studentss.csv", "a",newline="") as f:
    stuwriter = csv.writer(f,delimiter=",")
    data = []
    header = ['ROLL_NO','Name',"Class","Section"]
    data.append(header)
    for i in range(2):
        roll_no = int(input("Enter Roll number: "))
        name = input("Enter Name: ")
        Class = input("Enter Class: ")
        section = input("Enter section: ")
        rec = [roll_no,name,Class,section]
        data.append(rec)
    stuwriter.writerow(data)

