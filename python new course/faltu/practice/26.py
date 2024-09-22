def push(Arr):
    stack = []
    for i in range(0, len(Arr)):
        if Arr[i] % 5 == 0:
            stack.append(Arr[i])
    
    if len(stack) == 0:
        print("The stack is empty!")
    else:
        print(stack)
        

    
push([2,4,5,10,15,20,445])
