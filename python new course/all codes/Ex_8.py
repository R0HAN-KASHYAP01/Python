import os
def Changer(path, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)

    for file in files:
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i+=1
path = input("Enter the path:\n")
# file = input("Enter the file:\n")
format = input("Enter the fileformat:\n")
Changer(path,  format)