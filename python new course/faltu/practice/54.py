import csv
with open("Result.csv", "r",newline="") as f:
    won_stu = 0
    content = csv.reader(f)
    for row in content:
        if row[-1] == "Won":
            print(row)
            won_stu += 1

print(won_stu)

    
    # writer = csv.writer(f,delimiter=",")
    # writer.writerow(["Student_Id","Student_name","Game_name","Result"])
    # while True:
    #     St_Id = int(input("Enter the ID: "))
    #     St_name = input("Enter the name: ")
    #     Game_name = input("Enter the Game name: ")
    #     Result = input("Enter the result of the game: ")
    #     writer.writerow([St_Id,St_name,Game_name,Result])
    #     choice = input("To add more Press 'Y' OR to exit Press 'N': ")
        
    #     if choice == "N":
    #         break
