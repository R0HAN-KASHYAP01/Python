import csv
heading = ["Username", "Password"]
lst = [["Hello@gmail.com", "Helloworld"], ["World@gmail.com", "WorldHello"]]
with open("lst.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(heading)
    for i in lst:
        writer.writerow(i)

with open("lst.csv", 'r') as f:
    reader = csv.DictReader(f)
    search = input("Enter the username:- \n")
    for rows in reader:
        if rows['Username'] == search:
            print(f"The password of the {search} is {rows['Password']}.")



    