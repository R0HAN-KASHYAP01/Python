# Reading from csv file

# By using the noraml method
import csv
f = open("1.csv", "r")
a = csv.reader(f)
for row in a:
    print(row)

f.close()

# By using the clause method
with open("1.csv", "r") as f:
    a = csv.reader(f)
    for row in a:
        print(row)

