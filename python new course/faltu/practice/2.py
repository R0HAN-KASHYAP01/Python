# THIS THE MAIN FUNCTION. WHICH IS USED TO REMOVE THE LOWER CASE LINE FROM Ist FILE AND ADD TO IInd FILE. 
def remove_lowercase(file1, file2):
    with open(file1, "r") as f1:
        new_data1 = [] # DATA SUBMIT IN THE FIRST FILE
        new_data2 = []  #DATA SUBMIT IN THE SECOND FILE
        line = f1.readline()
        while line != "":
            if line[0].islower():
                new_data2.append(line)
            else:
                new_data1.append(line)
            line = f1.readline()
                
    with open(file1, "a") as f1:
        f1.truncate(0) # DELETE ALL THE DATA FROM THE FILE
        f1.seek(0)  # PUT THE CURSOR AT THE STARTING OF THE FILE
        f1.writelines(new_data1)
    
    with open(file2, "a") as f2:
        f2.writelines(new_data2)

remove_lowercase("File1.txt", "File2.txt")

with open("File1.txt", "r") as f1:
    print(f1.read()) # SHOWING THE CONTENT OF THE  FIRST FILE
with open("File2.txt", "r") as f2:
    print(f2.read())  # SHOWING THE CONTENT OF THE  SECOND FILE



# THIS IS USE FOR THE ENTERING SAMPLE DATA IN THE FILE.
# with open("File1.txt", "+a") as f1:
#     f1.write("Hello world\n")
#     f1.write("how are you\n")
#     f1.write("what are you doing\n")
#     f1.write("I am fine\n")
#     f1.write("what about you\n")
#     f1.write("I am also fine.\n")
    
# with open("File2.txt", "+a") as f2:
#     f2.write("THis is second file.\n")