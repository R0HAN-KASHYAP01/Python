list1 = []
no_ele = int(input("Enter the number of elements yo want: "))

for i in range(1, no_ele+1):
    a = int(input(f"Enter the element{i}: "))
    list1.append(a)


v = int(input("Enter the which place of the larger number you want: "))
list1.sort()
print(list1)
print(f"The {v} largest number of the list is {list1[-v]}")