class Employee:
    no_of_leaves = 6
    _math = "Mathematics"
    __CS = "Computer Science"


harry = Employee()
rohan= Employee()
harry.name = "Harry"
rohan.name = "Rohan"
Employee.no_of_leaves = 7
print(harry._Employee__CS)
print(harry._math)