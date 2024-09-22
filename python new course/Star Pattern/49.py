old = input("Enter the changing word: ")
new = input("Enter the changed word: ")
with open("Biopic.txt", "r") as f:
    data = f.read()
    changed = data.replace(old, new)

    print(changed)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # line = f.readline()
    # while True:
    #     if line != "":
    #         words = line.split()
    #         for word in words:
    #             if word == "he":
    #                 word = "she"
    #                 print(word,end=" ")
    #             else:
    #                 print(word, end=' ')
    #     else:
    #         break 
    #     line = f.readline()
