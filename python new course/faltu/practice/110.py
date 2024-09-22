list = [32,54,432,645,23]
new_lst = []
for i in list:
        suum = 0
        num = str(i)
        for n in num:
            suum += int(n)
        new_lst.append(suum)


print(new_lst)
