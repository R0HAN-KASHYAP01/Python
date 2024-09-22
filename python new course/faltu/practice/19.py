
with open("Another.txt","r") as f:
    content = f.readlines()
    reverse_data = content[::-1]
    for line in reverse_data:
        print(line,end="")
