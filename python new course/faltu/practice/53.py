import pickle
with open("Patients.dat", "ab+") as f:
    f.seek(0)
    line = pickle.load(f)
    no_patient = 0
    try:
        while line != "":
            if (line[-1]) == "COVID-19":
                print(line)
                no_patient += 1 
            line = pickle.load(f)
    except :
        pass
    
    print(no_patient)

    
    # while True:
    #     PId = int(input("Enter the ID: "))
    #     name = input("Enter the name: ")
    #     Disease = input("Enter the Dosease name: ")
    #     pickle.dump([PId,name,Disease],f)
    #     choice = input("To add more Press 'Y' OR to exit Press 'N': ")
        
    #     if choice == "N":
    
    #         break
