# with open("friends.txt","r") as f:
#     line_number = 1
#     line = f.readline()
#     while line != "":
#             if line_number %2 != 0:
#                 print(line,end="")

#             line = f.readline()
#             line_number += 1
            

            
#     print(f"Total number of line in the files are: {line_number-1}")

            
with open("friends.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        if line_number % 2 != 0:
            print(line, end="")

    total_lines = line_number  # line_number contains the last line number after the loop

print(f"Total number of lines in the file: {total_lines}")
