def next_panidrom(n):
    n =  n+1
    while not is_panidrom(n):
        n += 1
    return n

def is_panidrom(n):
    return str(n) == str(n)[::-1]


n = int(input("Enter the number you want to insert: "))
numbers = []
for i in range(n):
    number = int(input("Enter the number that you want the next paridonal: "))
    numbers.append(number)

for i in range(n):
    print(f"The panidrom of {numbers[i]} is {next_panidrom(numbers[i])}")

