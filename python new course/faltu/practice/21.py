with open("Another.txt","r") as f:
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        i += 1
        print(f"Line Number {i}: {line.strip()}")

# def display_records_with_line_numbers(file_name):
#     with open(file_name, 'r') as file:
#         for line_number, line in enumerate(file, start=1):
#             print(f"Line {line_number}: {line.strip()}")

# # Example usage:
# file_name = 'Another.txt'
# display_records_with_line_numbers(file_name)
