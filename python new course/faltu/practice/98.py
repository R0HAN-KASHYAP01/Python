stack = []
def Push(sta):
    name = input("Enter the name: ")
    if name.isalpha():
        sta.append(name)

Push(stack)
print(stack)
