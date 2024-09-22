with open("Input.txt","r") as f:
    line = f.readline()
    while True:
        if line != "":
            words = line.split()
            for word in words:
                if word[0] == "O":
                    rev = word[::-1]
                    print(rev,end=" ")
                else:
                    print(word,end=" ")
        else:
            break 
        line = f.readline()