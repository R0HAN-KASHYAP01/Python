def Fibonacoi(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f =  Fibonacoi(n-1) + Fibonacoi(n-2)
        yield f

number = int(input("Enter a number: "))
v = Fibonacoi(number)
print(v.__next__())
