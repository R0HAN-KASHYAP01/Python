import random
def dice():
    return(random.randint(1,6))

while True:
    roll = input("Press Enter to roll the dice or 'q' for quit:- ")
    if roll == "q":
        exit()
    result = dice()
    print(f"The result is {result}.\n")


