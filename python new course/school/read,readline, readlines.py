# Difference between read , readline and readlines
# you can not read that character again that already read above 

with open("1.txt", "r") as f:
    print(f"The result of read function is :- \n{f.read()}")
    limit = f.read(5)
    print(f"The result of read function with given a limit is :- \n{limit}")
    # you can not use read or readline function together for same file

    print(f"The result of readline function is:-\n{f.readline()}")
    print(f"The result of readlines function is:-\n{f.readlines()}")
    
    