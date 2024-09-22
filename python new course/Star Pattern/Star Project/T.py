def T(size):
    for row in range(size):
        for col in range(size):
            if row == 0:
                print("*",end=" ")
            elif col == size//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

T(7)
