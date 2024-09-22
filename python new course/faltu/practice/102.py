with open("statusss.txt","r") as f:
   line = f.readline()
   while line != "":
        words = line.split()
        for word in words:
            if word[0].lower() == "u":
                print(word)
        line = f.readline()
    
