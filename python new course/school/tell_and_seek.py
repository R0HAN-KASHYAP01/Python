# Use of tell and seek function
with open("1.txt", "r") as f:
    print(f"What is the current location of cursor:- {f.tell()}")
    print(f.read())
    print(f"Now move the cursor from beginning:- {f.seek(6)}")
    print(f"What is the current location of cursor:- {f.tell()}")
    print(f.read())
    print(f"What is the current location of cursor:- {f.tell()}")
