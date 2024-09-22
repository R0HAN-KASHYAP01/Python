with open("Another.txt","r") as f:
    size = 0
    for line in f:
        line = line.strip()
        for ch in line:
            size += 1
        
    print(size)

# with open("Another.txt", "r") as f:
#     size = 0
#     for line in f:
#         line = line.strip()
#         if line:  # Check if line is not empty after stripping
#             size += len(line.encode('utf-8'))  # Calculate size of line after encoding

# print(size)
