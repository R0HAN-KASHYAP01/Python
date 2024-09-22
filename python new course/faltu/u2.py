def chrcount(ch,st):
    count = 0
    for character in st:
        if character == ch:
            count =+ 1
    return count

st = input("Enter the line: ")
ch = input("Enter the character: ")
count = chrcount(ch,st)
print(count)
