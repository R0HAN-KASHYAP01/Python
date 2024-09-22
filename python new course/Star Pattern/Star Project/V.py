def V(size):
    for row in range(size):
        for col in range(size * 2 - 1):
          
            if col == row:
                print("*", end=" ")
         
            elif col == (size * 2 - 2) - row:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

V(7)
