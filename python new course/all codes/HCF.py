
def lst_maker():
    new_list = []
    lst_input = input("Enter the list and seperated by (,):\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

numbers = lst_maker() 
numbers.sort()
numbers.reverse()
print(numbers)

largest_number = 0
remainder = 0
divisor = 0

for i in range(0, len(numbers)):
    while largest_number % divisor != 0:
        largest_number = numbers[i]
        divisor = numbers[i+1]
        print(divisor)
        
# factors = []
# for num in numbers:
#     fac = []
#     for i in range(2, num+1):    
#         while num % i == 0:
#             num = num // i
#             fac.append(i)
#     factors.append(fac)

        
# print(factors)

# for i in factors:
#     for j in i:
#         if i[j] == 