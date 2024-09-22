def M(size):
    for row in range(size):
        for col in range(size):
            if col == 0 or col == size-1:
                print("*",end=" ")

            elif row <= size//2 and (col == row or col == size -row-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

M(7)
