import csv
with open("myfile.csv", "a") as f:
    writer = csv.writer(f, delimiter=",")
    while True:
        employee_number = int(input("Enter the employee number: "))

        employee_name = input("Enter the employee name: ")
        employee_salary = int(input("Enter the employee salary: "))
        writer.writerow([employee_number, employee_name, employee_salary])
        choice = input("Do you want to add more record? <Y/N>: ")
        if choice.lower() == "y":
            continue
        else:
            print("Data submitted successfully!")
            break



