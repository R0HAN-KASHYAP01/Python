with open("Another.txt", "r") as f:
        uppercase = 0
        lowercase = 0
        others = 0
        upper_letter = []
        lower_letter = []
        others_letter = []
        data = f.read()
        for word in data:
            if word.isupper():
                uppercase += 1
                upper_letter.append(word)
            elif word.islower():
                lowercase += 1
                lower_letter.append(word)
            elif word == " " or word == "\n":
                pass
            else:
                others += 1
                others_letter.append(word)

                
with open("UPPER.txt", "a") as f:
    f.writelines(upper_letter)
with open("lower.txt", "a") as f:
    f.writelines(lower_letter)
with open("others.txt", "a") as f:
    f.writelines(others_letter)
    
print(f"The number of times UPPER CASE letter present are {uppercase}")
print(f"The number of times lower CASE letter present are {lowercase}")
print(f"The number of times others letter present are {others}")