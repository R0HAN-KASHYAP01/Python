s = "Python is fun"
l = s.split()
print(l)
# PYTHON-is-Fun 
s_new = "-".join([l[0].upper(),l[1],l[2].capitalize()])
print(s_new)
