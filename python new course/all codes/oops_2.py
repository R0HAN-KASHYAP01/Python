class School():
    no_of_leaves = 3
    def __init__(self, name, standard, rollno):
        self.name = name
        self.standard = standard
        self.rollno = rollno


    def Introduction(self):
        return f"The name of the student is {self.name}. The class of the student {self.standard} and the roll no. is {self.rollno}"
    @classmethod
    def changeleaves(cls, newleaves):
        cls.newleaves = newleaves
    @classmethod
    def from_dash(cls, string):
        # prams = string.split("-")
        # print(prams)
        # return cls(prams[0], prams[1],prams[2])
        #Another way is:-
        return cls(*string.split("-"))
    @staticmethod
    def printmoring(string):
        print("Good morning, "+ string)

harry = School("Harry", "XI - B", "1")
rohan = School("Rohan", "XI-B", "2")
atul = School.from_dash("Atul-XI_B-3")

# print(atul.Introduction())
rohan.printmoring("Rohan")

# harry.changeleaves(4)
# print(rohan.newleaves)
