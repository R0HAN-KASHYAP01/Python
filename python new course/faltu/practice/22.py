import csv 
# file = open("contacts.csv", "a",newline="")
# Name = input("Please enter name: ")
# phno = input("Please enter phone number: ")
# data = [Name,phno]
# writer = csv.writer(file,delimiter=",")
# writer.writerow(data)
# file.close()

with open("contacts.csv", "r") as f:
    reader = csv.reader(f)
    print(reader)
    for row in reader:
        print(f"Name: {row[0]}        Phone: {row[1]}")


