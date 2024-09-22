
def lst_maker():
    new_list = []
    lst_input = input("Enter the list and seperated by (,):\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

list1 = lst_maker()

print(f"Original list:\n{list1}")
print(f"The maximum value in the list is {max(list1)}")
print(f"The minimum value in the list is {min(list1)}")
print(f"The minimum value in the list is {round(sum(list1)/len(list1))}")



