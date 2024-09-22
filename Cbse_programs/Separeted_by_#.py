with open("Sample.txt", "r") as f:
    
    for line in f:
        print("The original line of the file!")
        print(line)
        new_line = line.replace(" ","#")
        print("The changed line of the file!.")
        print(new_line)