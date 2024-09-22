def Count_H_T():
    with open("Poem1.txt", "r") as f:
        count = 0
        line = f.readline()
        while line != "":
            if line[0] == "H" or line[0] == "T":
                count += 1
            
         
            line = f.readline()
            
        print(count)
        
Count_H_T()

















#     f.write('''Here we go round the mulberry bust,\n

# Thmulberry bush,\n
# The mulberry bust.\n
# Here we go round the mulberry bush\n
# On a cold and frosty morning.''')