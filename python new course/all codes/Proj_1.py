initial_age = int(input("Enter you age or your year of birth: "))
x = int(input("Enter the year in which you want to find your age: "))
if initial_age <=100:
    print(f"Your age on {x} is {x -(2023-initial_age)}")
elif initial_age >=100:
    print(f"Your age on {x} is {x - initial_age}")

