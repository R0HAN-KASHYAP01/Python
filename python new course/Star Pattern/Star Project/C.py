def C(size):
    for row in range(size):
        for col in range(size//2+1):
            if (row == 0 or row== size-1) and col != 0:
                print("*",end=" ")
            elif (col == 0) and (row!=0 or row != size-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


C(7)