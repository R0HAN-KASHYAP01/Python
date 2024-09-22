def Push(stack,item):
    stack.append(item)
    return stack
 
def display(stack):
    if stack == []:
        print("Stack is empty!")
        print(stack)

    print(stack[::-1])

Stack = []
while True:
    print('''Choose any of the following options:
1. Push
2.Display stack
3. Exit
''')
    choice = int(input())
    if choice == 1:
        Item = input("Enter the item to submit in the stack: ")
        Push(Stack,Item)
    elif choice == 2:
        display(Stack)
    elif choice == 3:
        print("Thanks for using!")
        break
    else:
        print("Choose a valid option!")
        pass


