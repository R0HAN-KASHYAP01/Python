def countmy():
    with open("Data.txt", "r") as f:
        count = 0
        line = f.readline()
        while line != "":
            for i in line.split():
                if i == "my":
                    
                    count += 1
            line = f.readline()
    print(f"The numbers of line stating with 'my' is {count}")

countmy()