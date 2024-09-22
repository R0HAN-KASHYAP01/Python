def U(size):
    for row in range(size):
        for col in range(size):
            if (col == 0 or col == size-1 ) and row != size-1:
                print("*",end=" ")
            elif (col >0 and col <size-1) and row == size-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

U(7)
