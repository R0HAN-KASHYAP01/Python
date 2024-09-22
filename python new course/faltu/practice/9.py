import csv 
def writecsv(Roll_no, Name, Stream, Marks):
    with open("Student.csv", "a",newline='') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow([Roll_no , Name, Stream , Marks])

def readcsv():
    with open("Student.csv", "r") as f:
        data = csv.reader(f)
        for row in data:
            print(row)


while True:
    choice = int(input('''Choose the option given below:-
1. Add data in file.
2. Read data from file.
3. Save and quit.\n'''))

    if choice == 1:
        rollno = int(input("Enter the roll no. of the student: "))
        name = input("Enter the name of the student: ")
        stream = input("Enter the stream of the student: ")
        Marks = input("Enter the marks of the student: ")
        writecsv(rollno, name, stream, Marks)
    elif choice == 2: 
        readcsv()
    else:
        print("Thanks for using!")
        break
