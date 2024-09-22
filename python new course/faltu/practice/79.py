staff = [["Deepak",9999999999,"Delhi"],["Rajat",88888888888,"Mumbai"],["Murugan",777777777777,"Cochin"],["Ashmit",66666666666,"Delhi"]]

def push_element(stack):
    for person in staff:
        if person[-1] ==  "Delhi":
            stack.append(person)

def Pop_element(stack):
    while True:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print("Stack is empty")
            break

stacks = []
a = push_element(stacks)

Pop_element(stacks)


