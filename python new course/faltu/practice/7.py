with open("Filename.txt", "r+") as f:
    print(f.tell())
    a = f.seek(4,0)
    print(a)
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print(f.seek(7,0))
    print(f.read(10))
    
