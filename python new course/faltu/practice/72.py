import csv
def AddRecord():
    with open("Mobile_Phones.csv","a",newline="") as f:
        writer = csv.writer(f,delimiter=",")
        Model_number = int(input("Enter the model: "))
        Mobile_name = input("Enter the mobile name: ")
        Manufacturer = input("Enter the manufacturer: ")
        price = int(input("Enter the price: "))
        writer.writerow([Model_number,Mobile_name,Manufacturer,price])

def Find():
    with open("Mobile_Phones.csv","r") as f:
        data = csv.reader(f)
        count = 0
        for i in data:
            count += 1
            if i[2] == "Apple":
                print(i)
    print(count)        
    
# AddRecord()
Find()

