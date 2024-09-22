import csv
with open("employee.csv", "r",newline="") as f:
    data = csv.reader(f)
    first_line = next(data)

    for row in data:
        if int(row[2]) >= 5000:
            print(row)


















    # writer = csv.writer(f, delimiter=",")



    # # heading = writer.writerow(["EMPno", "EMPname", "Salary"])
    # while True:
    #         empno = int(input("Enter the emp no. of the Employee: "))
    #         empname = input("Enter the name of the Employee: ")
    #         salary = input("Enter the Salary of the Employee: ")
    #         writer.writerow([empno,empname,salary])
    #         Choice = input("Y/N: ")
            
    #         if Choice.lower() == "n":
    #             break
    