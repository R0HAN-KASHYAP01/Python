import random
comp = [ "S", "R", "P"]
player_win =0
comp_win = 0
Ties = 0
wrong_type = 0
for i in range(1, 6):
    computer = random.choice(comp)

    player = input("Enter 'S' for Scissor , 'R' for Rock  and 'P' for Paper\n")
    if player == "S":
        if computer == "R":
            print("Computer wins! Your choice S and Computer choice R")
            comp_win = comp_win + 1
        elif computer == "P":
            print("You win! Your choice  S and computer choice P")
            player_win = player_win + 1
        elif computer == "S":
            print("Tie! Your choice S and computer choice S")
            Ties = Ties + 1
    elif player == "R":
        if computer == "P":
            print("Computer wins! Your choice R and Computer choice P")
            comp_win = comp_win + 1
        elif computer == "S":
            print("You win! Your choice  R and computer choice S")
            player_win = player_win + 1
        elif computer == "R":
            print("Tie! Your choice R and computer choice R")
            Ties = Ties + 1
    elif player == "P":
        if computer == "S":
            print("Computer wins! Your choice P and Computer choice S")
            comp_win = comp_win + 1
        elif computer == "R":
            print("You win! Your choice  P and computer choice R")
            player_win = player_win + 1
        elif computer == "P":
            print("Tie! Your choice P and computer choice P")
            Ties = Ties + 1
    else:
        print("Chose any Valid!")
        wrong_type = wrong_type + 1

print("No. of times computer wins",comp_win)
print("No. of times player wins", player_win)
print("No. of times game ties", Ties)
print("NO. of times you type wrong",wrong_type)





