num = int(input("Enter the number of lines you want: "))

for i in range(num, 0, -1):
    # Print leading spaces
    for j in range(num - i):
        print(" ", end="")
    
    # Print asterisks
    for j in range(2 * i - 1):
        print("*", end="")
    
    print()
