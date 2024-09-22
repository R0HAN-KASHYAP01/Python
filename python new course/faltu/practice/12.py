import csv
with open("Student.csv", "a",newline='') as f:
        writer = csv.writer(f, delimiter=",")
        lines = []
        while True:
            rollno = int(input("Enter the roll no. of the student: "))
            name = input("Enter the name of the student: ")
            stream = input("Enter the stream of the student: ")
            Marks = input("Enter the marks of the student: ")
            Choice = input("Y/N")
            lines.append([rollno,name,stream,Marks])
            if Choice.lower() == "n":
                break
        
        writer.writerows(lines)

                