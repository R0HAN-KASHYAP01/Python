with open("statusss.txt","r") as f:
   line = f.readline()
   count = 0
   while line != "":
        words = line.split()
        if words[0].lower() == "open":
           print(line)
           count += 1 # count = count + 1
        line = f.readline()
    

print(f"Total number of lines start with Open is {count}")
           
   
   
   
   
   
   
   
   
   
   
   
    # f.write("Get the data value to be deleted.\nOpen the file for reading from it.\nRead the complete file into a list.\nDelete the data from the list\nOpen the file.\nOpen same file for writing into it.\nClose the file.\nThe method should display.")