Stack = []
def push(stack,value):
    stack.append(value)

def pop(stack):
    if len(Stack) != 0:
        stack.pop()
        print("element is pop out successfully!\n")
    else:
        print("Underflow")
        print("Stack is empty\n")

def peek(stack):
    if len(stack) != 0:
        print(f"The element at the top of the stack is {stack[-1]}\n")
    else:
        print("Underflow")
        print("Stack is empty\n")

def is_empty(stack):
    if len(stack) == 0:
        print("True")
    else: 
        print("False")

def size(stack):
    print(f"The number of element in the stack is {len(stack)}\n")

while(True):
        print("1. Push")
        print("2. Pop")
        print("3. Peek.")
        print("4. Is_Empty")
        print("5. Size")
        print("6. To See the Stack")
        user_choice = input()
        
        if user_choice == "1":
            value = input("Enter the value you want to add:- ")
            push(Stack,value)
            print("Stack is updated!\n")
        elif user_choice == "2":
            pop(Stack)
        elif user_choice == "3":
            peek(Stack)    
        elif user_choice == "4":
               is_empty(Stack)
        elif user_choice == "5":
            size(Stack)
        elif user_choice == "6": 
            print(Stack)

        else:
            print("Chose a valid option")

        print("Enter the q for quit and c for continue: ")
        user_choice2 = " "
        while (user_choice2 != "q" and user_choice2 != "c"):
            # print("Enter the q for quit and c for continue: ")
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue    



