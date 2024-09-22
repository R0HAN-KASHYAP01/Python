with open("statusss.txt","r") as f:
    search = input("Enter the word to be searched: ")
    line_no = 1
    line = f.readline()
    while line != "":
        count = 0
        words = line.split()
        for word in words:
            if word.lower() == search:
                count += 1
        print(f"Line{line_no} : {count}")
        
        line_no += 1
        line = f.readline()
