num = float(input("Enter the number: "))
str = str(num)
for i in range(len(str)):
    if str[i] == ".":
        print(str[:i])
        
