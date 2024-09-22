with open("statusss.txt","r") as f:
    # search = input("Enter the word to be searched: ")
    count = 0
    line = f.readline()
    while line != "":
        words = line.split()
        for word in words:
            if word.lower() == "the":
                count += 1
        
        line = f.readline()
    
    print(count)
