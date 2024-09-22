
submiting_table = []
Checking_table = []
def input_table(lst):
    table = input("Enter the table Seperated by space:-\n")
    lst = table.split(" ")
    return lst
a = input_table(submiting_table)

def checking_table(lst):
    x = a[0]
    for i in range(1,11):
        table = int(x)*i
        lst.append(table)
    return lst

b  = checking_table(Checking_table)
print(f"Table submitted by user is:-\n{a}\n")
print(f"Correct table is:-\n{b}\n")
for i in range(0,10):
    if int(a[i]) == b[i]:
        pass
    elif int(a[i]) != b[i]:
        print(f"The submitted table is wrong at {i+1}\n")
        print(f"Wrong number is {a[i]}")
        print(f"The correct number is {b[i]}\n")
