def N(size):
    for row in range(size):
        for col in range(size):
            if col == 0 or col == size-1 or col == row:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

N(7)
