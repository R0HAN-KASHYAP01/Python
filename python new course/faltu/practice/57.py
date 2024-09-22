def sum3(L):
    Sum_lst = []
    for num in L:
        if str(num)[-1] == "3":
            Sum_lst.append(num)
    print(sum(Sum_lst))

lst = [123,10,13,15,23]
sum3(lst)
