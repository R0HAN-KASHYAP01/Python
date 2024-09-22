list1 = []
list2 = []
list3 = []
no_ele = int(input("Enter the number of elements yo want: "))

for i in range(1, no_ele+1):
    a = int(input(f"Enter the element{i}: "))
    list1.append(a)

print(list1)
for elements in list1:
    if elements >=1:
        list2.append(elements)
    else:
        list3.append(elements)

print(list2)
print(list3)
