def factors(num):
    fac = []
    for i in range(2, num+1):    
        while num % i == 0:
            num = num // i
            fac.append(i)
    
    print(fac)

def factorial(num):
    factorial = 1
    if num >1:
        for i in range(1, num+1):
            factorial = factorial*i

        print(f"The factorial of {num} is {factorial}")
    elif num ==0 or 1:
        print(f"The factorial of {num} is 1")
        
number = int(input("Ente the number: "))

factors(number)
factorial(number)