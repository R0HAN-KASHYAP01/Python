text = "LearningCS"
L = len(text)
ntext = ""
for i in range(0,L):
    if text[i].islower():
        ntext = ntext+text[i].upper()
    elif text[i].isalnum():
        ntext = ntext + text[i-1]
        print(text[i])
    else:
        ntext = ntext + "&&"

print(ntext)
