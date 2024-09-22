# Writing on csv(Comma-seperated-value) file

# By using normal method
import csv
heading = ["Roll no","Name"]
data = [["1", "Rohan"], ["2", "Deepash"]]
f = open("1.csv", "w", newline='')
a = csv.writer(f, delimiter=",")
a.writerow(heading)
for i in data:
    a.writerow(i)
f.close()

# By using clause method
heading = ["Roll no","Name"]
data = [["100", "Rohan"],["101", "Deepash"]]
with open("1.csv", "w", newline='') as f:
    a = csv.writer(f, delimiter=",")
    a.writerow(heading)
    for i in data:
        a.writerow(i)