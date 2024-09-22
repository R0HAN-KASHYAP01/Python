class Employee:
    no_of_leaves = 6
    pass

harry = Employee()
rohan= Employee()
harry.name = "Harry"
rohan.name = "Rohan"
Employee.no_of_leaves = 7
print(harry.no_of_leaves)