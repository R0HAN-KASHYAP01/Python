from operator import length_hint


list = eval(input("Enter a list: "))
length = len(list)
mean = sum = 0
for i in range(0, length):
    sum += list[i]
mean = sum/length
print("The mean of the given list is: ", mean)



