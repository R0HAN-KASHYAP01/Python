import pickle


# with open("shoes.dat", "wb") as f:
#     heading = ["s_id", "name", "brand", "type", "price"]
#     pickle.dump(heading, f)
# Above lines only run once to create file only

def add_record(file_name,content):
    with open(file_name, "ab") as f:
        pickle.dump(content, f)
        print("Data added Successfully!")

def display_record(file_name):
    try:
        with open(file_name, "rb") as f:
            while True:
                data1 = pickle.load(f)
                print(data1)
    except EOFError:
        pass
    
def search(file_name,id):
    found = False
    try:
        with open(file_name, "rb") as f:
            while True:
                data1 = pickle.load(f)
                if data1[0] == id:
                    print(data1)
                    found = True     
                    break
    except EOFError:
        if not found:
            print("No data Founded!")

def Menu():                
    print("\nMenu")
    print('''1.) Add record
2.) Display record
3.) Search Record
4.) Exit''')

    choice = int(input("Choose from the option: "))
    if choice == 1:
        s_id = int(input("Enter the Shoe id: "))
        name = input("Enter the Shoe name: ")
        brand = input("Enter the brand of the shoes: ")
        type = input("Enter the type of the shoe: ")
        price = int(input("Enter the price of the shoe: "))
        new_data = [s_id, name, brand, type, price]
        add_record("shoes.dat",new_data)
        
    elif choice == 2: 
        display_record("shoes.dat")
        
    elif choice == 3:
        id = int(input("Enter the s_id to search data: "))
        search("shoes.dat", id)

    elif choice == 4:
        exit()

    else:
        print("Choose a valid option!")

Menu()        

while True:
    print("To reapeat press Y if not press N")
    choice = input()
    if choice == "Y":
        Menu()
    elif choice == "N":
        exit()
    else:
        print("Choose a valid option!")
