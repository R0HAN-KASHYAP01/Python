with open("emp.txt","r") as f:
   line = f.readline()
   search_id = input("Enter the id: ")
   while line != "":
        if line[0] == search_id:
           print(line)
        line = f.readline()

   
   

   
   
   
    # while True:
    #     Id = int(input("Enter the Id: "))
    #     Name = input("Enter the Name: ")
    #     Salary = int(input("Enter the salary: "))
    #     f.write(f"{[Id,Name,Salary]}\n")
    #     choice = input("To add more 'y' and 'N' for exit: ")
    #     if choice == "N":
    #         break
