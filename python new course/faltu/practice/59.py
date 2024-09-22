def lshift(lst,n):
    for i in range(0,len(lst)):
        if i < n:
            a = lst.pop(0)            
            lst.append(a)
    
    print(lst)

lst = [10,20,30,40,12,11]
lshift(lst,2)
