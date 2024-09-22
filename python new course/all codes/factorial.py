number = int(input("Enter a number: "))
factorial = 1
if number >1:
    for i in range(1, number+1):
        factorial = factorial*i

    print(f"The factorial of {number} is {factorial}")
elif number ==0 or 1:
    print(f"The factorial of {number} is 1")