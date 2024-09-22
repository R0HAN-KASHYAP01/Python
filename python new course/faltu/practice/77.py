with open("Myfiless.txt","a+") as f:
    print("Enter the sentences and to end type 'END':")
    while True:
        sentence = input()
        if sentence != "END":
            f.write(f"{sentence}\n")
        else:
            break

    f.seek(0)
    line = f.readline()
    while line != "":
        if line[0].isupper():
            print(line,end="")
            
        line = f.readline()
