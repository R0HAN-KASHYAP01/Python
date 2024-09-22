import random
# Takes the range of the number to be Guess
a = int(input("Enter the minimum value of the range: "))
b = int(input("Enter the maximum value of the range: "))

# Taking the players name
player1 = input("Name of player1 is: ")
player2 = input("Name of player2 is: ")

# Inistial Guesses of the player
Guess_taken1 = 0
Guess_taken2 = 0

# Make a room for players
lst = [[player1, Guess_taken1], [player2, Guess_taken2]]

# Game starts!
for i in range(len(lst)):
    randoom = random.randrange(a,b) # Produce the random number
    name = lst[i][0]
    print(f"{name}'s Turn:-\n")
    print(f"The number lie between {a} to {b}")
    for j in range(1, 11):
        guess = int(input("Guess the number: "))
        if guess == randoom:
            print(f"{player1}, Your guess is correct")
            lst[i][1] = j # Update the no. guess taken by the user
            print(f"No. of Guess you taken are:- {lst[i][1]}\n")
            break
        elif guess < randoom:
            print("Your guess is too small")
            print("Guess a greater number.\n")
        elif guess > randoom:
            print("Your guess is too big")
            print("Guess a smaller number\n")
        else: # if rather than int any other type data is entered or Handling the eror 
            print("Guess the valid \n")

# Declare the winner!
if lst[0][1] > lst[1][1]:
    print(f"No. of guess taken by {player1} is {lst[0][1]}")
    print(f"No. of guess taken by {player2} is {lst[1][1]}")
    print(f"{player2} wins!")
if lst[0][1] < lst[1][1]:
    print(f"No. of guess taken by {player1} is {lst[0][1]}")
    print(f"No. of guess taken by {player2} is {lst[1][1]}")
    print(f"{player1} wins!")
if lst[0][1] == lst[1][1]:
    print(f"No. of guess taken by {player1} is {lst[0][1]}")
    print(f"No. of guess taken by {player2} is {lst[1][1]}")
    print("NO one wins! Both takes same number of guesses.")
