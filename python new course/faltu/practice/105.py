string = input("Enter the line: ")
words = string.split()
for word in words:
    if word.islower():
        print(word.upper(),end=" ")

