list = eval(input("Enter a list: "))

print("Original list: ", list)
list = list*2
print("Replicated list: ", list)
list.sort()
print("Sort in ascending order: ", list)
list.sort(reverse = True)
print("Sort in descending order: ", list)

