# # For 1 answer: 
with open("data.txt", "w") as f:
    f.write("Python file handling is very interesting")


# # For 2 answer: 
import csv

# First make the file and add some record 

with open("College.csv","a", newline="") as f:
    writer = csv.writer(f,delimiter=",")
    heading = ["SrNo", "Studname", "City", "Percentage"]
    writer.writerow(heading) # Adding Heading the file

    data = [[1,"Rohan", "Meerut", "91%"],[2,"Uday", "Meerut", "95%"],[3, "atul", "Uganda", "10001%"],[4,"Aditya", "Tillu","99999%"]]

    # To add nested(list ka ander list at a single time) use writerows function 
    writer.writerows(data)
    
    ''' To add nested(list ka list) one by one  use writerow function
    for record in data:
        writer.writerow(record)
    '''


    
def removeRow():
    with open("College.csv", "r") as f:
        remove = input("Enter the SrNo fo the data to remove that record: ")
        data = csv.reader(f)
        rows = list(data)
        for row in rows:
            if row[0] == remove:
                rows.remove(row)

    
    with open("College.csv", "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(rows)
            
            
def getCollege():
    with open("College.csv","r") as f:
        data = csv.reader(f)
        rows = list(data)
        for row in rows:
            if row[1][0] in "aeiou":
                print(row)



removeRow()  
getCollege()   
                