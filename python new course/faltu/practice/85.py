stack = []
def Push(content):
    stack.append(content)
    print(f"Stack after Push is {stack}")

def Pop():
    if len(stack) == 0:
        print("Stack Underflow")  # Stack is empty
        
    else:
        print(stack.pop())
        