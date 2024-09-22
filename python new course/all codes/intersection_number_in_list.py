
def lst_maker():
    new_list = []
    lst_input = input("Enter the list and seperated by (,):\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list
    


list1 = lst_maker()
list2 = lst_maker()
intersection_list = []
for num in list1:
    if num in list2:
        intersection_list.append(num)
    else:
        pass
print(intersection_list)
