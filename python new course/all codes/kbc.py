name = input("Enter you name: ")

question = [["Who created the python language?", "Tony Stark", "Guido van Rossum", "Charles Babage", "James Gosling", "2"],
            ["When was the world Programmer's day celebrated?",
                "12th sep", "15th sep", "30th feb", "15th Jan", "1"],
            ["Who is the best Youtuber of Computer's teacher on Youtube?",
                "CodewithHarry", "PhysicsWallah", "ApneCollage", "R2h", "1"],
            ["Who is first president of India?", "Jawarlal Nehru",
             "Narander Modi", "Dr. Rajendra Prashad", "Mahatam Gandi", "3"],
            ["Who is the 'ship of the desert'?", "Lion",
                "Kingkong", "Shark", "Camal", "4"],
            ["How many second in an hour?", "3678 sec",
             "360 sec", "3600 sec", "60 sec", "3"],
            ["Which is the largest state of India?",
             "Uttar Pradesh", "China", "Rajasthan", "Kerla", "3"],
            ["Who is known as Father of Indian Constitution?", "Dr.Bhemrao Ambedkar",
             "Steve Rogers", "Mahatma Gandhi", "Lione Messie", "1"],
            ["Agra is situated on which river bank?", "Ganga",
             "Yamuna", "Nile", "Indian Ocean", "2"],
            ["Which is the largest planet of the solar system?",
             "Sun", "Earth", " Pluto", "Jupiter", "4"],
            ["Which course is best for the learing Python language?", "100 Days sleeping", "1/0 days coding", "100 days coding", "Only coding", "3"]]

levels = [0, 1000, 2000, 3000, 5000, 10000, 20000,
          30000, 50000, 100000, 320000, 100000000]

money = 0

for i in range(0, len(question)):
    print(f"Your next question is for Rs.{levels[i+1]}")
    print(f"{i+1}. {question[i][0]}")
    print(f"a. {question[i][1]}                b. {question[i][2]}")
    print(f"c. {question[i][3]}                d. {question[i][4]}")
    answer = input("Select the answer by 1-4 and q for quit: ")
    if answer == question[i][-1]:
        print("Your answer is correct!\n")
        money = levels[i]
        if i == 4:
            money = 4000
        elif i == 10:
            money = 320000
        if i == 4:
            money = 4000
    elif answer == "q":
        money = levels[i]

        print(f"The money you won is Rs.{money}")
        break
    else:
        print("Your answer is wrong!")
        print(f"The correct answer is {question[i][-1]}")
        print(f"Money you take home is Rs.{money} ")
        break
