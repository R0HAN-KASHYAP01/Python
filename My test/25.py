
text = input("Enter your text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False

if spam == True:
    print("This text is a spam.")
else:
    print("Thsi text is not a spam.")


