x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))
z = int(input("Enter the number 3: "))
print("Oringnal numbers: ",x,y,z)
x,y,z = y,z,x
print("After swapping: ",x,y,z)
