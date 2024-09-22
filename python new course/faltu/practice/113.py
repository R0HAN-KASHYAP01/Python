stack = []
def Push(name):
    if name.isalpha():
        stack.append(name)
    else:
        print("Give a valid name!")

