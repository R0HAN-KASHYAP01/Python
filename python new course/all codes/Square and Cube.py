power = input("Choose what you want (s)Square and (c)Cube: ")
if power == "s":
    num = int(input("Enter the number: "))
    print(f"The value of {num}² is  {num**2}")
elif power == "c":
    num = int(input("Enter the number: "))
    print(f"The value of {num}³ is {num**3}")

