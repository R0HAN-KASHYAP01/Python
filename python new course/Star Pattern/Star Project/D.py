def D(size):
    for row in range(size):
        for col in range(size//2+1):
            if col == 0:
                print("*",end=" ")
            elif (row == 0 or row == size - 1) and col != size // 2:
                print("*",end=" ")
            elif col == size // 2 and (row != 0 and row != size -1):
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()

D(7)