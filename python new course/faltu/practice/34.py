Text1 = "IND-23"
Text2 = ""
I = 0
while I < len(Text1):
    if Text1[I] >="0" and Text1[I] <="9":
        Val = int(Text1[I])
        Val = Val +1
        Text2 = Text2 + str(Val)
    elif Text1[I] >= "A" and Text1[I] <="Z":
        Text2 = Text2 + Text1[I +1]

    else:
        Text2 = Text2 + "*"
    
    I += 1
print(Text2)