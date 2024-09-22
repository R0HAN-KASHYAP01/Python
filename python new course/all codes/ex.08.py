import os

def path():
    path = input("Enter the path:-\n")
    os.chdir(path)
def Change_File():
    DNT_file = input("Enter the file name that you don't want to change:-\n")
    DNT_format = input("Enter the file format that you don't want to change:-\n")
    file = input("Enter the file you want to change:-\n")
    for i in range(1):
        os.rename(file , i.png )






v = path()
v = Change_File()