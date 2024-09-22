def Top(stack):
    if len(stack) == 0:
        print("Stack is empty!!")
    else:
        x = len(stack)
        print(stack[x-1])

stack = []
Top(stack)