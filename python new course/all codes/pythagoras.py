print("Choose what you want to find")
print(" Perpendicular(P), Base(B) and Hypotenous(H)")
func = input()
if func == "H":
    P = int(input("Enter the perpendicular: "))
    B = int(input("Enter the base: "))
    H = ((P**2)+(B**2))**0.5
    print(f"The Hypotenous is {H}")
elif func == "P":
    B = int(input("Enter the base: "))
    H = int(input("Enter the Hypotenous: "))
    P = ((H**2)-(B**2))**0.5
    print(f"The Perpendicular is {P}")

elif func == "B":
    P = int(input("Enter the Perpendicular: "))
    H = int(input("Enter the Hypotenous: "))
    B = ((H**2)-(P**2))**0.5
    print(f"The base is {B}")

else:
    print("You may choose the wrong!")