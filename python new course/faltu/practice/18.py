import os
def add_line(main_file,Sentence,postion):
    f_old = open(main_file,"r")
    f_new = open("new_file.txt","a")
    for i in range(postion):
        line = f_old.readline()
        f_new.write(line)

    f_new.write(Sentence)
    
    while True:
        line = f_old.readline()
        if not line:
            break
        f_new.write(line + "\n")

main_file = "accept.txt"
sentence = input("Enter the sentence:\n")
add_line(main_file,sentence,3)
os.replace("new_file.txt",main_file)