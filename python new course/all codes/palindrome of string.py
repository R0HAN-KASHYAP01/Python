def push(stack, element):
    stack.append(element)

def pop(stack):
    if len(stack) == 0:
        return None
    return stack.pop()

def compare(stack, string):
    for char in string:
        if char != pop(stack):
            return False
    return len(stack) == 0

stack = []
string = input("Enter the string: ").replace(" ", "")  # Remove spaces

for char in string:
    push(stack, char)

is_palindrome = compare(stack, string)

if is_palindrome:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
