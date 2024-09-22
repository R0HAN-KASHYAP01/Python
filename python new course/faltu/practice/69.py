with open("MYFile.txt","r") as f:
    content = f.read()
    ncontent=content.replace(" ", "-")
    print(ncontent)

