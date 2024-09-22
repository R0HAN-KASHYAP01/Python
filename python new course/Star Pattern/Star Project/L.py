def L(size):
    for row in range(size):
        for col in range(size):
            if col == 0:
                print("*",end=" ")
            elif row == size -1 and col <= size//2+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

L(7)