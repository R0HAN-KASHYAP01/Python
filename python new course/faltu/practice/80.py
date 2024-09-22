student = {"Ponam":89,"Ramit":59,"Ankit":80,"Deep":25}
def push():
    stack = []
    count = 0
    for k,v in student.items():
        if v >= 75:
            stack.append(k)
            count += 1
    print(stack)
    print(count)



push()


