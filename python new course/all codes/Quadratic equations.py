a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
print(f"The quardratic equation is {a}x² + {b}x + {c}")
x =  '%.2f' % (((-b) + (((b**2) - 4*a*c)**0.5))/(2*a))
x1 =  '%.2f' % (((-b) - (((b**2) - 4*a*c)**0.5))/(2*a))
print(f"The value of x are {x} and {x1}")