def Login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # def log(username, password):
    if (username == "Admin" and password == "Kuch bhi"):
        print("Login Successfully")
    else:
        print("Check your username or password and try again")
        Login()
start = Login()