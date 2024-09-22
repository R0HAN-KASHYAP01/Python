Ditem = {"Pen": 106,"Pencil": 59,"Notebook":80,"Eraser":25}
stack = []
def Push():
    count = 0
    for key,value in Ditem.items():
        if value >= 75:
            stack.append(key)
            count +=1
    print(stack)
    print(f"The count of elements in the stack is {count}")

    
Push()
