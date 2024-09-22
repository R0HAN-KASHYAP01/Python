# Reading of text file

# By using normal method
f = open("1.txt", "r")
a = f.read()
print(a)
f.close()

# By using clause method
with open("1.txt", "r") as f:
    print(f.read())