# Difference between writerow and writerows
import csv
with open("1.csv", "w") as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(["Class", "name"])
    a.writerows(["Class", "name"])
    
