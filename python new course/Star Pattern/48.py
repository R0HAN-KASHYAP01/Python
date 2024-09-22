with open("Details.txt", "r") as f:
    line = f.readline()
    count = 0
    while True:
        if line != "":
            words = line.split()
            for word in words:
                if word[-1].isnumeric():
                    count += 1
        else:
            break 
        line = f.readline()

print(count)
