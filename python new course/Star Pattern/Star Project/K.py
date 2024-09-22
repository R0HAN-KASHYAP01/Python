def K(size):
    for row in range(size):
        for col in range(size):
            if col == 0:
                print("*",end=" ")
            elif row <= size//2 and col == (size//2+1 - row):
                print("*",end=" ")

            elif row > size//2 and col == (row - size//2+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

K(7)
