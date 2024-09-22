class Client:
    bname = "pnb"
    def __init__(self, name , acno, balance):
        self.name = name
        self.acno = acno
        self.balance = balance
    def getdetails(self):
        return (f"The name of the client = {self.name}\n"
        f"The account no.  of the client = {self.acno}\n"
        f"The balance of the client = {self.balance}\n")

c1 = Client("amit", 100, 34567890)
print(c1.getdetails())