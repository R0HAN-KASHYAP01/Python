def H(size):
    for row in range(size):
        for col in range(size//2+2):
            if col == 0 or col == size//2+1 :
                print("*",end=" ")
            if row == size//2 and col <size//2+1:

                print("*",end=" ")
            else:
                print(' ',end=" ")
        print()
    

H(7)
