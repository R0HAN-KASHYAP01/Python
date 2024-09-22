import csv
with open("Groceries.csv", "a+",newline="") as f:
    while True:
        item_no = input("Enter the item number: ")
        item_name = input("Enter the name of the item: ")
        Qty = int(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item: "))
        writer = csv.writer(f,delimiter=",")
        writer.writerow([item_no,item_name,Qty,price])
        choice = input("To submit more data <Y/N>: ")
        if choice.upper() == "Y":
            pass
        else:
            break
       
    f.seek(0) 
    print("\nThe list of Items is:")
    reader = csv.reader(f)
    for line in reader:
        print(f"Item No: {line[0]} \nItem Name: {line[1]} \nQuantity: {line[2]} \nPrice per item: {line[3]} \nAmount: {int(line[2])*float(line[3])} \n {"-"*35}")
