def listchange(lst):
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            lst[i] = 10
        else:
            lst[i] = lst[i]*5
        
    print(lst)

lst = [10,20,23,45]
listchange(lst)
