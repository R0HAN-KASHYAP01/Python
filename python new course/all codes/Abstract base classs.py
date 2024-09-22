from abc import ABC,abstractmethod

class Shape(ABC):  # This is used to make the function compulsory
    @abstractmethod
    def printarea(self):
        return 0

class Rectangale:
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 4

    def printarea(self):
        return self.length * self.breadth

rec1 = Rectangale()
print(rec1.printarea())
