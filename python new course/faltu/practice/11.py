import csv
with open("Student.csv", "r") as f:
        data = csv.reader(f)
        column = input("Which column data you want: ")
        first_line = next(data)
        for i in range(0, len(first_line)):
            if first_line[i] == column:
                a = i
        try:      
            for row in data:
                print(row[a])
        except:
             print(f"Column name {column} not founded!") 