def F(size):
    for row in range(size):
        for col in range(size//2+2):
            if col == 0:
                print("*",end=" ")
            elif row == 0:
                print("*",end=" ")
            elif row == size //2 and col != size//2+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

F(12)