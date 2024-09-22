import pickle
with open("Store.dat", "ab+") as f:
    while True:
        item_no = input("Enter the item number: ")
        item_name = input("Enter the name of the item: ")
        Qty = int(input("Enter the quantity of the item: "))
        price = float(input("Enter the price of the item: "))
        pickle.dump([item_no,item_name,Qty,price],f)
        choice = input("To submit more data <Y/N>: ")
        if choice.upper() == "Y":
            pass
        else:
            break
       
    f.seek(0) 
    print("\nThe list of Item is:")
    try:
        while True:
            line = pickle.load(f)
            print(f"Item No: {line[0]} \nItem Name: {line[1]} \nQuantity: {line[2]} \nPrice per item: {line[3]} \nAmount: {line[2]*line[3]} \n {"-"*35}")
            
    except:
        print("Data finished!")
