with open("Lines.txt","r") as f:
    line = f.readline()
    while True:
        if line != "":
            words = line.split()
            if len(words) >= 10:
                print(line)
                
        else:
            break 
        line = f.readline()


