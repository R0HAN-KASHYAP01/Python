def file_long(File_name):
    with open(File_name, "r") as f:
        content = f.readlines()
        longest = ""
        for line in content:
            if len(line) > len(longest):
                longest = line
        print(f"Longest line in the file is:\n{longest}")

file_long("Filename.txt")




