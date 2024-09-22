import csv

def addcsv():
    with open("old.csv","r") as f1:
        with open("updated.csv","a",newline="") as f:
            writer = csv.writer(f,delimiter=",")
            data = csv.reader(f1)
            next(data)
            for row in data:
                writer.writerow(row)


# addcsv()

def convertcsv():
    with open("old.csv","r") as f1:
        with open("converted.csv","a",newline="") as f:
            writer = csv.writer(f,delimiter=",")
            data = csv.reader(f1)
            for row in data:
                a = row[0].split(":")
                writer.writerow(a)

convertcsv()
        

