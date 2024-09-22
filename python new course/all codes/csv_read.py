import csv
with open("Student.csv", "r")as f:
    a = csv.reader(f)

    for row in a:
        print(row)