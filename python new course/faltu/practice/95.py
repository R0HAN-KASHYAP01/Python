import pickle
with open("Student.dat","rb") as f:
    search_sno = int(input("Enter the searched SNO: "))
    line = pickle.load(f)
    try:
        while True:
            if line[0] == search_sno:
                print(line)
                
            elif line[0] != search_sno:
                print("Sno not found in the file. Give the valid SNO!")
                break
            
            
            line = pickle.load(f)
    except EOFError:
        pass

            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # while True:
    #     Sno = int(input("Enter the Sno: "))
    #     Name = input("Enter the name: ")
    #     marks = int(input("Enter the marks: "))
    #     pickle.dump([Sno,Name,marks],f)
    #     choice = input("TO add more 'Y' and 'N' for exit: ")
    #     if choice == "N":
    #         break