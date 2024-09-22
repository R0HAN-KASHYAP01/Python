def J(size):
    for row in range(size):
        for col in range(size):
            if col == size//2 and row != size -1:
                print("*",end=" ")
            elif row == 0:
                print("*",end=" ")
            
            elif row == size -1 and col < row//2 and col !=0:
                print("*",end=" ")
            elif row == size -2 and col == 0:
                print("*",end=" ")

            
            else:
                print(" ",end=" ")
        print()

J(7)