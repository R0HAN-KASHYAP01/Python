


def lst_maker():
    new_list = []
    lst_input = input("Enter the list separated by commas:\n")
    for i in lst_input.split(","):
        new_list.append(str(i))
    return new_list


def lst_changer(lst):
    for i in lst:
        return i


Item_no = lst_maker()
Item_name = lst_maker()
Qty = lst_maker()
price = lst_maker()
print(Item_name)

with open("ncert.txt", "a") as f:
    f.write(f"{lst_changer(Item_no)}\n")
    f.write(f"{lst_changer(Item_name)}\n")
    f.write(f"{lst_changer(Qty)}\n")
    f.write(f"{lst_changer(price)}\n")

# with open("ncert.txt", "r") as f:
#     a = f.read()
#     print(a)
#     i = 0
#     while i<= len(Qty):
#         a = int(Qty[i]) * float(price[i])
#         print(a, end=" ")
#         i+= 1

