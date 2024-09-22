def O(size):
    for row in range(size):
        for col in range(size):
            if (col == 0 or col == size-1) and (row > 0 and row<size-1):
                print("*",end=" ") 
            elif (row == 0 or row == size-1) and (col > 0 and col < size-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

O(7)