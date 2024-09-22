line = input("Enter the line\n")
digitcount = totalcount = symcount = lowercount = uppercount = alphacount = 0
for i in line:
    if i.islower():
        lowercount += 1
    elif i.isupper():
        uppercount += 1
    elif i.isdigit():
        digitcount += 1
    elif i.isalpha():
        alphacount += 1
    elif i.isalnum() != True and i != ' ':
        symcount += 1

print(f"Number of uppercase letter is {uppercount}")
print(f"Number of lowercase letter is {lowercount}")
print(f"Number of alphabets letter is {alphacount}")
print(f"Number of digit letter is {digitcount}")
print(f"Number of symbols letter is {symcount}")
