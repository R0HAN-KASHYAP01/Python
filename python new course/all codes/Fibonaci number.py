def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

number = int(input("Enter the 'n'th term of the Fibonacci series: "))
print(f"The {number}th term of the Fibonacci series is {Fibonacci(number)}")
