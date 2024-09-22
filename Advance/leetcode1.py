l1 = [2,4,3]
l2 = [5,6,4]
num1 = "0"
for num in l1[::-1]:
    num1 = num1+str(num)

print(num1)
num2 = "0"
for num in l2[::-1]:
    num2 = num2+str(num)

print(num2)

sum = int(num1) + int(num2)
print(sum)

# sum_ls = list(str(sum))
# print(sum_ls)
