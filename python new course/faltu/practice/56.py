def search_replace(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            lst[i] = 0
        
    print(lst)

L = [10,20,30,40,10,4]
search_replace(L,10)
        