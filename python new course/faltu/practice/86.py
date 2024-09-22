import csv
# This is used to create file and adding heading the file.
# with open("Record.csv","a",newline="") as f:
#     writer = csv.writer(f,delimiter=",")
#     writer.writerow(["BookID", "AuthorName", "Price"])

# Main program
def Insert():
    with open("Record.csv", "a", newline="") as f:
        writer = csv.writer(f,delimiter=",")
        while True:
            Id = int(input("Enter the Book id: "))
            Author_name = input("Enter the Author name: ")
            Price = int(input("Enter the price of the book: "))
            writer.writerow([Id,Author_name,Price])
            choice = input("To add more 'Y' or 'N' for Not: ")
            if choice.upper() == "N":
                break
            
def Total():
    with open("Record.csv", "r") as f:
        data = csv.reader(f)            
        count = len(list(data)) # you can use this to do work in one line 
        
        ''' You can use this also this also give the same answer
        for i in data:
            print(i)
            count += 1
        '''
    print(f"Total number of Books in the file is {count-1}")
Insert()
Total()