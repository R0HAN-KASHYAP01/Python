line = int(input("Enter the number of lines\n"))
a = int(input("1 for True or 2 for False\n"))
a = bool(a)
if a == True:
    for i in range(1, line+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
elif a == False:
    for i in range(line,0, -1):
        for j in range(1, i+1):
            print("*", end="")
        print()

