t = tuple()
n = int(input("Enter the times of counting no. "))
for i in range(0,n):
    num = int(input())

    t = num + t
print("\nThe no. of in tuple are : ")
print(t)

print("\n The maximum no is :")
print(max(t))

print("the minimum no is: ")
print(min(t))