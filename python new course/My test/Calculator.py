
list = []
operation = input("Enter the operation: ")
if operation == "+":
    while operation == "+":
        operation = input("Enter the operation: ")
        if operation == "+":
            ele = int(input("Enter the number: "))
        elif operation == "=":
            break

        list.append(ele)
    total = 0
    for number in list:
        total += number
    print(f"the number you added are {list}")
    print(f"The sum of the digit is {total}")
elif operation == "-":
    num = int(input("Enter the number: "))
    list = []
    operation = input("Enter the operation: ")
    if operation == "+":
        while operation == "+":
            operation = input("Enter the operation: ")
            if operation == "+":
                ele = int(input("Enter the number: "))
            elif operation == "=":
                break

            list.append(ele)
        total = 0
        for number in list:
            total += number
    list.extend([num])
    total = 0
    for number in list:
        print(f"the number you subtracted are {list}")
        print(f"The difference of the digit is {total}")
elif operation == "*":
    while operation == "*":
        operation = input("Enter the operation: ")
        if operation == "*":
            ele = int(input("Enter the number: "))
        elif operation == "=":
            break

        list.append(ele)
    total = 1
    for number in list:
        total = number * total
    print(f"the number you multiplied are {list}")
    print(f"The multiplication of the digit is {total}")
else:
    print("Please! Enter a valid operation")








