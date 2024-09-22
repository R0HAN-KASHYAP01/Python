def I(size):
    for row in range(size):
        for col in range(size//2):
            if row == 0 or row == size-1:
                print("*",end=" ")
            elif col == (size //2)//2:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()

I(7)
