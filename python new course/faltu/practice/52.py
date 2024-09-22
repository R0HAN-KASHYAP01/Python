import pickle
with open("Plants.dat", "rb+") as f:
    line = pickle.load(f)
    try:
        while line != "":
            if int(line[-1]) >= 500:
                print(line) 
            line = pickle.load(f)
    except :
        pass

    
    # while True:
    #     Id = int(input("Enter the ID: "))
    #     name = input("Enter the name: ")
    #     Price = input("Enter the price: ")
    #     pickle.dump([Id,name,Price],f)
    #     choice = input("To add more Press 'Y' OR to exit Press 'N': ")
        
    #     if choice == "N":
    
    #         break
