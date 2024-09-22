class School:
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
        return cls(*string.split("-"))
    @staticmethod
    def printmoring(string):
        print("Good morning, " + string)
class Programmer(School):
    def __int__(self, name, standard, lang, rollno ):
        self.name = name
        self.standard = standard
        self.lang = lang
        self.rollno = rollno


    def Introduction1(self):
        return f"The name of the student is {self.name}. The class of the student {self.standard} and the roll no. is {self.rollno}. The programmering language you know{self.lang}"


harry = School("Harry", "XI - B", "1")
rohan = Programmer("Rohan", "XI-B", "2",["python"])
atul = School ("Atul","XI_B","3")
print(rohan.Introduction1())




