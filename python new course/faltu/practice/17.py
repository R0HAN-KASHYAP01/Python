
with open("accept.txt","a+") as f:
    print("Enter data or stop Type 'END' ")
    while True:
        line = input()
        
        if line == "END":
            break
        else:
            f.write(f"{line}\n")
    f.seek(0)
    line = f.readline()
    print("\nThe lines started with uppercase are:")
    while True:
        if line != "":
            if line[0].isupper():
                print(line,end="")
        elif line == "":
            break
        line = f.readline()
        