
def lst_maker():
    new_list = []
    lst_input = input("Enter the list and seperated by (,):\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

def digit(lst):
    new_lst = []
    for i in lst:
        suum = 0
        num = str(i)
        b = list(num)
        for a in b:
            suum += int(a)
        new_lst.append(suum)

    print(new_lst)

lst1 = [12,43,756,78,354]
print(lst1)
digit(lst1)
