with open("Hello.txt", "r") as f:
    line = f.readline()
    while True:
        if line != "":
            words = line.split()
            if words[0] == "You":
                print(line)
        
        else:
            break
        line = f.readline()
    