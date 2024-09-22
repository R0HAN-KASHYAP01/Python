import pickle

student_lst = [['1', 'Rohan'], ['2', 'Deepash'], ['3', 'Uday'], ['4', 'Atul'], ['5', 'Aditya']]

# Save data to binary file
with open("Sample.bin", "wb") as f:
    pickle.dump(student_lst, f)

# Load data from binary file
with open("Sample.bin", "rb") as f:
    a = pickle.load(f)

# Search for a student based on the roll number
search = input("Enter the Roll no.:\n")
found = False

for i in range(len(a)):
    if a[i][0] == search:
        print(f"Student with Roll no. {search} found: {a[i][1]}")
        found = True
        break

if not found:
    print("Student not found. Enter a valid roll no.")
