power = input("Choose what you want (s)Square root and (c)Cube root: ")
if power == "s":
    num = int(input("Enter the number: "))
    print(f"The square root of {num} is {num**0.5}")
elif power == "c":
    num = int(input("Enter the number: "))
    print(f"The cube root of {num} is {num**(1/3)}")
else:
    print("Sorry! but you choose wrong.")
