stack = []
def Push(contents):
    stack.append(contents)

def Pop():
    if len(stack) != 0:
        stack.pop()
        print(stack)
    else:
        print("Stack is Empty! Underflow")

    

Push(34)
Push(5454)
Push(6454)
Push(36453)
Push(35453)
Push(876757)
Push(367531)
print(stack)
Pop()

