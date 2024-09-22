lst = []
with open("Hello.txt","r") as f:
    for line in f:
        if "a" not in line.lower():
            lst.append(line)

with open("Another.txt" , 'w') as f:
    f.writelines(lst)
