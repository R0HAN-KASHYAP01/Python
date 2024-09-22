num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
Operation = input("Enter the operator: ")
if Operation == "+":
    if (num1 == 45) and (num2 == 56):
        print(77)
    else:
        print(num1 + num2)
elif Operation == "-":
    if (num1 == 36) and (num2 == 24):
        print(37)
    else:
        print(num1-num2)
elif Operation == "*":
    if (num1 == 36) and (num2 == 66):
        print(88)
    else:
        print(num1*num2)
elif Operation == "/":
    print(num1/num2)
else:
    print("You choose wrong operation.")
