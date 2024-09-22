customer = [["Gudas",999999999,"Goa"],["Julee",888888888888,"Mumbai"],["Murugan",777777777777,"Cochin"],["Ashmit",101010101010,"Goa"]]

stack = []
def Push_element():
    for cus in customer:
        if cus[2] == "Goa":
            stack.append([cus[0],cus[1]])

def Pop_element():
    for i in range(len(stack)):
        if len(stack) != 0:
            print(stack.pop())
        else:
            print("Underflow")

Push_element()
print(stack)
Pop_element()