stack = []
no_ele = int(input("Enter the number of elements yo want: "))

for i in range(1, no_ele+1):
    a = int(input(f"Enter the element{i}: "))
    stack.append(a)

stack.sort(reverse= True)
print(f'The largest number of the stack is {stack[0]}')
