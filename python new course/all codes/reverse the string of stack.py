def reverse_string(input_string):
    stack = []
    reversed_string = ""

    # Push each character onto the stack
    for char in input_string:
        stack.append(char)

    # Pop characters from the stack to build the reversed string
    while len(stack) > 0:
        reversed_string += stack.pop()

    return reversed_string

# Example usage:
input_string = "Hello, World!"
reversed = reverse_string(input_string)
print(reversed)
