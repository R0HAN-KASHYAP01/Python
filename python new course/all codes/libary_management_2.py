book_lst = ["Python", "CSS", "HTML", "JAVA"]
lend_book = []
def Display_book():
    print("The books in the libary are:-")
    print(book_lst)
    print("\n")


def Lend_book(book, name):
    if book not in lend_book:
        lend_book.append(book)
        print("The book have been lended succesfully!\n")
    else:
        print("Sorry! book already had been taken by someone else.\n")

def Add_book(book):
    book_lst.append(book)
    print("Book added successfully! Thanks for the contribution.\n")

def Return_book(book):
    lend_book.remove(book)
    print("Book return successfully!\n")



while(True):
        print(f"Welcome to the R0#@n's Libary. Choose any of the option.")
        print("1. Display name")
        print("2. Lend a book")
        print("3. Add a book.")
        print("4. Return a book")
        user_choice = input()
        
        if user_choice == "1":
            Display_book()
        elif user_choice == "2":
            book = input("Enter the name of the book. You want: ")   
            name = input("Enter your name: ")
            Lend_book(book, name)        
        elif user_choice == "3":
            book = input("Enter the name of the book you want to add: ")
            Add_book(book)        
        elif user_choice == "4":
            book = input("Enter the name of the book you want to return: ")
            Return_book(book)

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


