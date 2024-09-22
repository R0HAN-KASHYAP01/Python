username = input("Enter your username:\n")
words = list(username)
words = len(username)
if words<=10:
    print("Username is valid")
else:
    print("Usename is not valid")