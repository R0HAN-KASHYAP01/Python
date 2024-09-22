def filedel(word):
    with open("Python.txt","r+") as f:
        data = f.readlines()
        with open("algo1.txt","a") as f1:
            for line in data:
                if word not in line:
                    print(line)
                    f1.write(line)
       

filedel("how")

                