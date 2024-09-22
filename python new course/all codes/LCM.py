
def lst_maker():
    new_list = []
    lst_input = input("Enter the list and seperated by (,):\n")
    for i in lst_input.split(","):
        new_list.append(int(i))
    return new_list

# numbers = lst_maker()
# for i in range(numbers):
    