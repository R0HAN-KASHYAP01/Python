num = int(input("Enter the number: "))
answer = num
operation = "+"
while(operation != "="):
    operation = input("Enter the operation (+, -, *, /): ")
    if operation == "+":
        num = int(input("Enter the number: "))
        answer = answer + num
    elif operation == "-":
        num = int(input("Enter the number: "))
        answer = answer - num
    elif operation == "*":
        num = int(input("Enter the number: "))
        answer = answer * num
    elif operation == "/":
        num = int(input("Enter then number: "))
        answer  = answer /num

    else:
        break

print(f"The answer is {answer}")