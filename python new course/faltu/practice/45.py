with open("Bookname.txt","r") as f:
    line = f.readline()
    while True:
        if line != "":
            if "y" in line.lower():
                print(line)
        else:
            break 
        line = f.readline()