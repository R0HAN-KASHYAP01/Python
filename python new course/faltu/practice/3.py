def countH():
    with open("para.txt", "r") as f:
        count = 0
        line = f.readline()
        while line != "":
            if line[0] == "H":
                count += 1
                print(line)
            line = f.readline()
    print(f"The numbers of line stating with 'H' is {count}")

countH()
