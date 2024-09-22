# Difference between wirte and writelines
with open("1.txt", "w") as f:
    f.write("Used for single string\n")
    list = ["12\n", "Hello world\n"]
    # It take anything as an argument except interger
    f.writelines(list)
    # f.write(list) this show error for write 
    