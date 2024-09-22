n = int(input("Enter a number: "))
mn, mx = n, n 
for i in range(4):
    n = int(input("Enter a number: "))
    if mx< n:
        mx = n
    if mn> n :
        mn = n 
print("Maximum of number entered: ", mx)
print("Minimum of number entered: ", mn)

