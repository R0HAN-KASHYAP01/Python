def change(lst):
    list2 = []
    for i in range(len(lst)):
        factorial = 1
        if lst[i] >1:
            n = lst[i]
            for i in range(1, n+1):
                factorial = factorial*i
            list2.append(factorial)

        elif lst[i] ==0 or 1:
            list2.append(1)
    
    return list2

            
list1 = [3,7,4,8,10,5]
list1 = change(list1)
print(list1)

