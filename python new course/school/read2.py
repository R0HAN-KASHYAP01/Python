# Reading on binary file

# By using normal method
import pickle
f = open("1.bin" , "rb")
a = pickle.load(f)
print(a)
f.close()

# By using clause method
with open("1.bin", "rb") as f:
    print(pickle.load(f))
    