n = 10
j = 10
print("Are you ready to start the game!\n The number of guesses you have",j)
while(True):
    i = int(input("Guess the number: "))
    j = j-1
    if i>n:
        print("Guess a smaller number")
        print("Number of Guesses left", j)
    elif i<n:
        print("Guess a larger number")
        print("Number of Guesses left", j)

    elif i ==n:

        print("Congrats! You guessed the correct")
        print("Number of Guesses taken", j)
        break
    if j == 0:
        print("Game over")
        break

    # break
    # j =j- 15


