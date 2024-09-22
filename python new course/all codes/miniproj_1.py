class Libary:
    def __init__(self, Booklst, name):
        self.Booklst = Booklst
        self.name = name
        self.LendDict = {}

    def displayBook(self):
        print(f"The Book in the Libary are:-")
        for book in self.Booklst:
            print(book)
        print("\n")

    
    def LendBook(self, book, name):
        if book not in self.LendDict.keys():
            self.LendDict.update({book:name})
            print("Book have been lend succesfully.")
            print("\n")

        else:
            print(f"Book already had been taken by {self.LendDict[book]}")
            print("\n")

    def AddBook(self, book):
        self.Booklst.append(book)
        print("Book added succesfully. Thanks to giving the book.")
        print("\n")

    def Returnbook(self, book):
        self.LendDict.pop(book)
        print("Book return succesfully.")
        print("\n")


if __name__ == '__main__':
    start = Libary(['Python', 'C++', 'Java', 'Javascript'], "R0#@n's Libary")
    while(True):
        print(f"Welcome to the {start.name}. Choose any of the option.")
        print("1. Display name")
        print("2. Lend a book")
        print("3. Add a book.")
        print("4. Return a book")
        user_choice = input()
        
        if user_choice == "1":
            start.displayBook() 

        elif user_choice == "2":
            book = input("Enter the name of the book. You want: ")
            name = input("Enter your name: ")
            start.LendBook(book, name)
        
        elif user_choice == "3":
            book = input("Enter the name of the book you want to add: ")
            start.AddBook(book)
        
        elif user_choice == "4":
            book = input("Enter the name of the book you want to return: ")
            start.Returnbook(book)

        else:
            print("Chose a valid option")

        print("Enter the q for quit and c for continue: ")
        user_choice2 = " "
        while (user_choice2 != "q" and user_choice2 != "c"):
            # print("Enter the q for quit and c for continue: ")
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue    


