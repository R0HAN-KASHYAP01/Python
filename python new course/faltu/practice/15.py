with open("Another.txt", "r") as f:
        count_to = 0
        count_the = 0
        data = f.read()
        words = data.split(" ")
        for word in words:
            if word == "to":
                count_to += 1
            elif word == "the":
                count_the += 1
            else:
                pass
    
print(f"The number of times 'to' present in the file is {count_to}")
print(f"The number of times 'the' present in the file is {count_the}")