age = int(input("Enter your age: "))

if age>18:
    if age>100:
        print("Please! Enter a valid age")
    else:
         print("You are eligble for driving.")
elif age== 18:
    print("You are eligble for driving but first we have to check your physical condition before to get driving license.")
else:
    print("SORRY! but you are not eligble for driving"
          "licence.")
