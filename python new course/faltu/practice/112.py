numbers = input("Enter the numbers seperated by ',' : ")
lst = numbers.split(",")
print(lst)
suum  = 0
for num in lst:
    suum += int(num)

length = len(lst)
mean = suum / length

print(suum)
print(mean)

    