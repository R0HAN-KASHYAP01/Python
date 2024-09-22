def lst_maker():
    new_list = []
    lst_input = input("Enter the list separated by commas:\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

list1 = lst_maker()
result = []
for num in list1:
    if is_prime(num):
        result.append(num)

print(result)
