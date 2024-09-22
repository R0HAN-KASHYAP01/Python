def P(size):
    for row in range(size):
        for col in range(size):
            if col == 0:
                print("*",end=" ")
            elif (row == 0 or row == size//2) and col <= size//2:
                print("*",end=" ")
            elif (row >0 and row < size//2) and col == size//2 +1:
                print("*",end=" ")
                
            else:
                print(" ",end=" ")
        print()

P(7)
