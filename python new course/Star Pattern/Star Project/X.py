def X(size):
    for row in range(size):
        for col in range(size):
            if col == row or col == size - row-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

X(7)
