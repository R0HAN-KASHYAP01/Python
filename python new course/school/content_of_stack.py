def display(stack):
    x = len(stack)
    print("The current element of the stack are:-")
    for i in range(x-1,-1,-1):
        print(stack[i])

stack = [1,24,3]
display(stack)