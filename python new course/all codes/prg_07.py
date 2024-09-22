# i = int(input("Enter a number: "))

while (True) :
    num = int(input("Enter a number: "))
    if num<=100:
        print("Sorry! Try again")
        continue
    if num>100:
        print("Congrats! You entered a greater number than 100")
        break
