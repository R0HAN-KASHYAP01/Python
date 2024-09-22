with open("Hello.txt", "r") as f:
    line = f.readline()
    num_line = 0
    while True:
        if line != "":
            num_line += 1
        else:
            break 
        line = f.readline()

print(num_line)
