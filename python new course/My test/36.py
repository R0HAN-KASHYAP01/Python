def maximum(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
m = maximum(a,b,c)
print("The grestest number " + str(m))
