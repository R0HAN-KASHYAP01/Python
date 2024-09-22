def Z(size):
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size-1:
                print("*",end=" ")
            elif col == size -row -1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    
Z(7)  