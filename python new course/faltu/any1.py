s = "Python is fun"
x = s.split()
s_new = "_".join([word[0].upper() + word[1:].capitalize() for word in x])
print(s_new)
