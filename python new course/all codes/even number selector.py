a = input("Enter the list and seperated by (,):\n")
lst = []
for i in a.split(","):
    lst.append(int(i))
even_lst = []
odd_lst = []
for num in lst:
    if num % 2 == 0:
        even_lst.append(num)
    else:
        odd_lst.append(num)

print(f"Original list:\n {lst}")
print(f"Even number list:\n {even_lst}")
# print(f"The sum of even number is {sum(even_lst)}")
print(f"Odd number list:\n {odd_lst}")
# print(f"The sum of odd number is {sum(odd_lst)}")


# One liner coding
# a = input("Enter the list of integers separated by commas:\n")
# lst = [int(i) for i in a.split(",")]
# even_lst = [num for num in lst if num % 2 == 0]
# odd_lst = [num for num in lst if num % 2 != 0]

# print(f"Original list:\n {lst}")
# print(f"Even number list:\n {even_lst}")
# print(f"The sum of even numbers is {sum(even_lst)}")
# print(f"Odd number list:\n {odd_lst}")
# print(f"The sum of odd numbers is {sum(odd_lst)}")

