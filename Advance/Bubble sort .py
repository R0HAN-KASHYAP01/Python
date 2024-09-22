def lst_maker():
    lst = []
    numbers = input("Enter the numbers seperated by ',':  ")
    num = numbers.split(",")
    # print(num)

    for n in num:
        lst.append(int(n))
    
    return lst

lst1 = lst_maker()

def ascending():
    for i in range(len(lst1) - 1 ):
        for j in range(len(lst1)-i-1):
            if lst1[j] > lst1[j+1]:
                lst1[j],lst1[j+1] = lst1[j+1] , lst1[j]

def descending():
    for i in range(len(lst1)-1):
        for j in range(len(lst1)-i-1):
            if lst1[j] < lst1[j+1]:
                lst1[j],lst1[j+1] = lst1[j+1], lst1[j]




ascending()
print(f"The ascending order of the list is : {lst1}")

descending()
print(f"The descending order of the list is : {lst1}")


            

            
