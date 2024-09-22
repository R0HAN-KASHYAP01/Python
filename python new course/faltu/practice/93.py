with open("status.txt","r") as f:
    line = f.readline()
    no_line = 0
    no_space = 0
    while line !="":
        no_line += 1
        for ch in line:
            if ch == " ":
                no_space += 1
                
        line = f.readline() 
    print(f"Total lines in file are: {no_line}")
    print(f"Total spaces in file are: {no_space}")


