words = input("Enter the words seperated by comman: ")
unique = words.split(",")
s = set(unique)

print(",".join(sorted(s)))
