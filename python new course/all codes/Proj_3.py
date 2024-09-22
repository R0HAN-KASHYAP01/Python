input_list = input("Enter the list seperated by space: ")
lst = input_list.split()
lst1 = [x for x in lst]

lst1 = sorted(lst1)
print(f"The original list is {lst1}")
print("Method 1:-", list(reversed(lst1)),"\n")
print("Method 2:-", lst1[::-1],"\n")
lst3 = []
b = lst1[::-1]

for i in range(0 , len(lst1)):
    x = lst1[i]
    y = b[i]
    x,y = y,x
    a = x
    lst3.append(a)

print("Method 3:-",lst3)