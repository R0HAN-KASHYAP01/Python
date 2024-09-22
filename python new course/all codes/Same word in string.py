str1 = input("Enter the string: ")
str2 = input("Enter the string: ")
a = []
for word in str1:
    if word in str2:
        a.append(word)
    else:
        pass

# for w in a:
#     print(w, end=" ")

w = "".join(a)
print(w)