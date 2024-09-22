def Y(size):
    for row in range(size):
        for col in range(size):
            if (col == row or col == size - row -1) and row <=size//2:
                print("*",end=" ")
            elif col == size//2 and row > size//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

Y(7)
