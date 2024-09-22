def add(*args):
    sum = 0
    for num in args:
        sum += num
    return (sum)


def difference(*args):
    difference = args[0]
    for num in args[1:]:
        difference -= num
    return (difference)


def multiply(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return (multiply)


def divide(*args):
    divide = args[0]
    for num in args[1:]:
        divide /= num
    return (divide)


print("Choose the operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Choose (1/2/3/4):\n")

numbers = []
num = float(input("Enter the first number: "))
numbers.append(num)

while True:
    another_num = input("Enter the another number(TO stop press Enter): ")
    if another_num == "":
        break
    numbers.append(float(another_num))

if choice == "1":
    print("Result: ", add(*numbers))
elif choice == "2":
    print("Result: ", add(*numbers))

elif choice == "3":
    print("Result: ", add(*numbers))

elif choice == "4":
    print("Result: ", add(*numbers))
