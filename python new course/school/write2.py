# Writing on binary file

# By using normal method
import pickle
f = open("1.bin" , "wb")
pickle.dump("kuch bhi",f)
f.close()

# By using clause method
with open("1.bin", "wb") as f:
    pickle.dump("koi sa bhi use kar la", f)
    