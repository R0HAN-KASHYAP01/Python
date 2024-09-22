def poping(stack):
    if len(stack) == 0:
        print("underflow") # Underflow means there is no element in stack
    else: 
        return stack.pop()

stack = [1,24,3]
poping(stack)
print(stack)