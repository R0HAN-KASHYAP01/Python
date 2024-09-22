Books = {"Python":560,"Java":450,"MySQL":330,"Web Development":725}
book_stack = []
def push_element():
    count = 0
    for k,v in Books.items():
        if v > 500:
            book_stack.append([k,v])
            count += 1
    return count

num = push_element()
print(book_stack)
print(f"The element in the stack is {num}")

