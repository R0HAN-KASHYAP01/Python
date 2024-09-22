# Write on  text file

# By noraml method
f = open("1.txt", "w")
f.write("kuch bhi")
f.close()

# By using clause method
with open("1.txt", "w") as f:
    f.write("koi sa bhi use kar lo")
    