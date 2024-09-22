str1 = input("Enter the string: ")
string = str1.lower()
if string == string[::-1]:
    print(f"{string} is a Palidrome")
else:
    print(f"{string} is not a Palidrome")


