def A(size):
    for row in range(size):
        for col in range(size + 1):
            # Conditions for printing stars to form the "A"
            if (col == 0 or col == size) and row != 0:  # Left and right legs
                print("*", end=" ")
            elif row == 0 and (col != 0 and col != size):  # Top horizontal bar
                print("*", end=" ")
            elif row == size // 2:  # Middle horizontal bar
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  

A(7)