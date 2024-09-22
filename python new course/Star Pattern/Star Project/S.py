def S(size):
    for row in range(size):
        for col in range(size):
           
            if (row == 0 or row == size - 1):
                print("*", end=" ")
           
            elif row == size // 2:
                print("*", end=" ")
           
            elif row < size // 2 and col == 0:
                print("*", end=" ")
            
            elif row > size // 2 and col == size - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Set the size for the letter S
S(7)
