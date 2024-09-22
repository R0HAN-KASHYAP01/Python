apples = int(input("Enter the number of get: "))
mn = int(input("Enter the minimum value of the range: "))
mx = int(input("Enter the maximum value of the range "))
for i in range (mn , mx+1):
    if (apples% i) == 0 :
        print(f"{apples} is divisble by {i}")
    else: 
        print(f"{apples} is not divisible by {i}")
        