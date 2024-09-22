def lst_maker():
    new_list = []
    lst_input = input("Enter the list and seperated by (,):\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

list1 = lst_maker()
a = sorted(list1)
place = int(input("Enter the which greater number you want: "))

print(f"The {place} greater number is {a[-place]}")