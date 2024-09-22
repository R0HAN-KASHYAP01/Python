import pickle
def creatfile(BookNO , BookName, Author, Price):
    with open("book.dat", "ab") as f:
        pickle.dump([BookNO, BookName, Author, Price],f)
        print("Data added successfully!")


def countRec(Author):
    with open("Book.dat", "rb") as f:
        count = 0
        books = []
        try:
            while True:
                line = pickle.load(f)
                if line[2] == Author:
                    count += 1
                    books.append(line[1])
        except EOFError:
            pass


        
        print(f"The number of books writen by {Author} are {count}")
        print(f"Books written by the author are:-\n{books}")

while True:
    choice = int(input('''Choose the option given below:-
1. Add data in the file.
2. Search book of an author.
3. Save and quit.\n'''))

    if choice == 1:
        book_no = int(input("Enter the book number: "))
        book_name = input("Enter the book name: ")
        author = input("Enter the name of author: ")
        price = int(input("Enter the price of book: "))
        creatfile(book_no,book_name,author,price)
    
    elif choice == 2: 
        author = input("Enter the name of author: ")
        countRec(author)

    else:
        print("Thanks for using!")
        break


