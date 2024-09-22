def count_And():
    with open("para.txt", "r") as f:
        count = 0
        line = f.readline()
        while line != "":
            words = line.split()
            for word in words:
                if word.lower() == "and":
                    count += 1
            line = f.readline()
    print(f"The numbers of line stating with 'And','and' is {count}")

count_And()
