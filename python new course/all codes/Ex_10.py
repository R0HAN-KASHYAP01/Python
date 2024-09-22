import pickle
f = open("iris.txt", "w+")
v = f.read()
ls = v.split("\n", maxsplit=" ")
print(type(v))
# f.write(ls)


f.close