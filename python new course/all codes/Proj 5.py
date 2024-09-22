# Making the panidrom number.
def next_panidrom(n):
    if n >=10:
        n =  n+1
        while not is_panidrom(n):
            n += 1
        return n
    else: # This is for the number less than 10
        return n

# Taking the number and comparing with it recipocal
def is_panidrom(n):
    return str(n) == str(n)[::-1]

# Taking the how many number you want to check
n = int(input("Enter the number you want to insert: "))

# Instalizing a empty list
numbers = []

# Add the number in the numbers list.
for i in range(n):
    number = int(input("Enter the number that you want the next paridonal: "))
    numbers.append(number)

# Instalizing the another empty list
palandoiramal_lst = []

# Add the number in Palandorimal_list.
for i in range(n):
    new_number = next_panidrom(numbers[i])
    palandoiramal_lst.append(new_number)

# OUTPUT:-
print(f"The original list is:-\n{numbers}")
print(f"The palandorify list is:-\n{palandoiramal_lst}")



